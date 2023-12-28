import threading
import time


def print_messages(thread_name, delay, n):
    for i in range(n):
        time.sleep(delay)
        print(f"{thread_name}: Сообщение {i + 1}")


thread1 = threading.Thread(target=print_messages, args=("Поток 1", 1, 5))
thread2 = threading.Thread(target=print_messages, args=("Поток 2", 2, 5))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
