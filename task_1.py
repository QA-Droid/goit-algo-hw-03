import os
import shutil
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання та сортування файлів за розширеннями.")
    parser.add_argument('source_dir', help="Шлях до вихідної директорії")
    parser.add_argument('destination_dir', nargs='?', default='dist', help="Шлях до директорії призначення (за замовчуванням 'dist')")
    return parser.parse_args()

def copy_and_sort_files(source_dir, destination_dir):
    try:
        # Перевірка існування вихідної директорії
        if not os.path.exists(source_dir):
            print(f"Вихідна директорія '{source_dir}' не існує.")
            return

        # Створення директорії призначення, якщо вона не існує
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
            print(f"Створено директорію призначення '{destination_dir}'.")

        # Рекурсивне перебування файлів та директорій
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    # Отримання розширення файлу
                    _, extension = os.path.splitext(file)
                    extension = extension[1:].lower() if extension else 'no_extension'

                    # Шлях до піддиректорії за розширенням
                    dest_subdir = os.path.join(destination_dir, extension)
                    if not os.path.exists(dest_subdir):
                        os.makedirs(dest_subdir)
                        print(f"Створено піддиректорію '{dest_subdir}' для розширення '.{extension}'.")

                    # Копіювання файлу до призначеної директорії
                    shutil.copy2(file_path, dest_subdir)
                    print(f"Файл '{file_path}' скопійовано до '{dest_subdir}'.")
                except Exception as e:
                    print(f"Помилка при копіюванні файлу '{file_path}': {e}")
    except Exception as e:
        print(f"Помилка при обробці директорії '{source_dir}': {e}")

def main():
    args = parse_arguments()
    copy_and_sort_files(args.source_dir, args.destination_dir)

if __name__ == "__main__":
    main()