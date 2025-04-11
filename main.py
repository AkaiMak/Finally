from modules.music import get_music_recommendation, get_available_genres
from modules.jokes import get_random_joke

def print_commands():
    """Вывод доступных команд"""
    print("\nДоступные команды:")
    print("1 — Рекомендация музыки")
    print("2 — Анекдот")
    print("off — Выключить бота")

def main():
    print("\n=== Текстовый бот-помощник ===")
    print("Введите команду для взаимодействия с ботом")

    while True:
            print_commands()
            user_input = input("\nВведите команду: ").strip().lower()

            if user_input == "1":
                    print("\nДоступные жанры:", ", ".join(get_available_genres()))
                    genre = input("Введите жанр (необязательно, нажмите Enter для случайного выбора): ").strip().lower()
                    print("\nРекомендуем:", get_music_recommendation(genre if genre else None))
            elif user_input == "2":
                    print("\nАнекдот:", get_random_joke())
            elif user_input == "off":
                    print("\nДо свидания! Хорошего дня!")
                    break
            else:
                    print("\nНеизвестная команда. Попробуйте еще раз.")

if __name__ == "__main__":
    main()