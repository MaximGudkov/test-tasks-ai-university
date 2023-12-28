def count_words_in_each_line(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file:
                words = line.strip().split()
                word_count = len(words)
                print(word_count)
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Пример использования

name = "text.txt"
count_words_in_each_line(name)
