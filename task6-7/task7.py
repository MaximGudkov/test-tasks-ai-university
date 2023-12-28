import inspect
from faker import Faker

fake = Faker()


def generate_emails(file_name, num_emails):
    with open(file_name, "w", encoding="utf-8") as file:
        for _ in range(num_emails):
            email = fake.email()
            file.write(email + "\n")


generate_emails("random_emails.txt", 1000)

# --------------------

import time


def timeit(N):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)

            if inspect.isgeneratorfunction(func):
                raise RuntimeError("Передаваемая функция не может быть генератором")

            end_time = time.time()
            elapsed_time = end_time - start_time

            print(f"Время выполнения функции '{func.__name__}': {elapsed_time:06f}")

            if elapsed_time > N:
                print(
                    f"Внимание: Время выполнения превысило установленный порог ({N} секунд)"
                )

            return result

        return wrapper

    return decorator
