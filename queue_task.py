from queue import Queue
import time
import random
import threading

# Створюємо чергу заявок
request_queue = Queue(maxsize=random.randint(10, 200))

# Ініціалізуємо ідентифікатор заявки
request_counter = 0

# Створюємо подію зупинки генерації (забезпечення виходу)
stop_event = threading.Event()


# Створюємо базовий клас заявки
class Request:
    def __init__(self, name):
        self.name = name


# Функція створення заявки та додавання її до черги
def generate_request():
    if request_queue.full():
        print("Заявка не створена, черга заповнена")
    else:
        global request_counter
        request_counter += 1
        request_name = f"Заявка-#{request_counter:06d}"
        current_request = Request(request_name)
        request_queue.put(current_request)
        print(
            f"Заявка '{request_name}' створена та додана до черги. Розмір черги: {request_queue.qsize()}"
        )


# Функція опрацювання заявки та видалення її з черги
def process_request():
    if request_queue.empty():
        print("Черга порожня.")
    else:
        request_name = request_queue.get_nowait().name
        print(f"Обробка заявки '{request_name}'.")
        time.sleep(random.uniform(0.2, 1.0))
        print(
            f"Заявка '{request_name}' оброблена. Розмір черги: {request_queue.qsize()}"
        )
        request_queue.task_done()


# Створюємо потік для генерації заявок.
def request_generator_thread():
    while not stop_event.is_set():
        generate_request()
        time.sleep(random.uniform(0.5, 2.0))


# Створюємо потік для оброблення заявок.
def request_processor_thread():
    while not stop_event.is_set():
        process_request()
        time.sleep(random.uniform(0.5, 2.0))


if __name__ == "__main__":
    print("Роботу розпочато. Для зупинки натисніть Ctrl+C.")
    generator = threading.Thread(target=request_generator_thread)
    processor = threading.Thread(target=request_processor_thread)
    generator.start()
    processor.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        stop_event.set()
        generator.join()
        processor.join()
        print("Роботу зупинено")
