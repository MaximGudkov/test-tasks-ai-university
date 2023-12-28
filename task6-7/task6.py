import re
from task7 import timeit

input_file_name = "random_emails.txt"
output_file_name = "output_emails.txt"

# @timeit(0.1) # throws error (because function is generator and we can't check its runtime with simple decorator logic)
def find_emails(file_name):
    email_pattern = re.compile(r"\b[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file:
                for match in email_pattern.finditer(line):
                    yield match.group()
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


find_emails(input_file_name)

# --------------------


@timeit(0.1)
def copy_emails_to_file(input_file, output_file):
    with open(output_file, "w", encoding="utf-8") as output:
        for email in find_emails(input_file):
            output.write(email + "\n")


copy_emails_to_file(input_file_name, output_file_name)
