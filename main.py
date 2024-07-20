import json
from random import randint


class Library:
    def __init__(self) -> None:
        self.first_go: bool = True  # Атрибут, позволяющий определить первый запуск программы
        self.go()

    def try_input(self, input_data: str) -> str | None:  # Метод, проверяющий ввод на пустую строку
        if input_data == '':                             # и возвращающий пользователя в главное меню при её вводе
            print()
            print("Вы ввели пустую строку")
            print("Возвращаюсь в главное меню")
            self.go()
        else:
            return input_data         # Здесь возвращаются введенные данные, если не пустая строка

    def __read_json(self) -> dict[str, dict[str, str | int]]:
        with open('books.json', 'r', encoding='utf-8') as books:
            return json.load(books)

    def __write_json(self, new_books: dict[str, dict[str, str | int]]) -> None:
        with open('books.json', 'w', encoding='utf-8') as books:
            json.dump(new_books, books)

    def __generate_id(self) -> int:                  # При необходимости можно усовершенствовать эту функцию
        while True:
            id_book: int = randint(0, 100000)      # генерируем ID
            if id not in self.__read_json():  # Возвращаем его, если такого ещё нет в books.json
                return id_book

    def show_book(self, book: dict[str, str | int]) -> None:  # Метод для красивого вывода информации о книге
        print(f'ID {book["id"]}, Название "{book["title"]}", автор {book["author"]}, год издания {book["year"]}, '
              f'статус "{book["status"]}"')

    def add_book(self, title: str, author: str, year: int) -> None:    # Метод добавления книги
        books: dict[str, dict[str, str | int]] = self.__read_json()                                     # Считываем json - получаем словарь
        book_id: int = self.__generate_id()                                 # генерируем ID
        books[str(book_id)] = {                                             # Добавляем книгу в словарь
            'id': book_id,
            'title': title,
            'author': author,
            'year': year,
            'status': "в наличии"
        }
        self.__write_json(books)                # Вносим новые данные в json
        print()
        print("Книга добавлена")

    def del_book(self, id_book: str) -> None:            # Метод удаления книги
        try:
            int(id_book)                    # Проверка на то, что введены только цифры
            books: dict[str, dict[str, str | int]] = self.__read_json()
            del books[str(id_book)]
            self.__write_json(books)
            print()
            print("Книга удалена")
        except ValueError:                  # Обработка ошибок
            print("Некорректный ввод. Введите только цифры")
            id_book: str = self.try_input(input('Введите ID книги: '))
        except KeyError:
            print("Такой книги нет. Проверьте правильность ввода")
            id_book: str = self.try_input(input('Введите ID книги: '))
        except Exception as e:
            print(f'Ошибка: {e}')
            id_book: str = self.try_input(input('Введите ID книги: '))

    def book_search(self, user_choice: str, data_insearch: str | int) -> None:  # Метод поиска книг
        search_by: str = ('title', 'author', 'year')[int(user_choice) - 1]      # Настройка режима поиска книги
        books_insearch: list[dict[str, str | int]] = []                         # ^по выбору пользователя,
        for book in self.__read_json().values():                                # ^user_choice влияет на выбор значения из кортежа
            if book[search_by] == data_insearch:
                books_insearch.append(book)
        if len(books_insearch) > 0:  # Проверка нашлись книги или нет
            for i in range(len(books_insearch)):
                self.show_book(books_insearch[i])
        else:
            print('Книг с указанными параметрами не найдено')

    def show_all_books(self) -> None:  # Метод демонстрации всех книг
        for book in self.__read_json().values():
            self.show_book(book)

    def change_status_book(self) -> None:  # Метод изменения статуса книги
        while True:
            book_id = self.try_input(input('Введите ID книги: '))
            if book_id not in self.__read_json():
                print("Такой книги нет. Проверьте правильность ввода")
                book_id= ''
            if book_id != '':
                break

        while True:
            book_status: str = self.try_input(input('Введите статус книги\n1 - в наличии\n2 - выдана: '))
            if book_status in '12':
                books = self.__read_json()
                new_status: str = ('в наличии', 'выдана')[int(book_status)-1]  # Выбор нового статуса книги из множества
                if books[book_id]['status'] == new_status:                # Сверка старого и нового статуса
                    print(f'Книга уже в статусе "{new_status}"')
                else:
                    books[book_id]['status'] = ('в наличии', 'выдана')[int(book_status)-1]
                    print()
                    print('Статус книги изменён')
                    self.__write_json(books)
                    break
            else:
                print()
                print('Нет такого статуса')

    def go(self) -> None:  # Метод главного меню
        if self.first_go:  # Проверка первого запуска и изменение атрибута first_go
            print("Добро пожаловать в систему управления библиотекой")
            self.first_go = False
        print()
        user_choice: str = input('Выберите действие:\n1. Добавить книгу\n2. Удалить книгу\n3. Найти книгу\n'
                                 '4. Показать все книги\n5. Изменить статус книги\n')
        if user_choice != '' and user_choice in '12345':  # Проверка ввода на правильность
            if user_choice == '1':                        # и далее запуск соответствующего выбору метода
                title: str = self.try_input(input('Введите название: '))
                author: str = self.try_input(input('Введите автора: '))
                year: int = -1
                while year < 0:
                    try:
                        year = int(self.try_input(input('Введите год издания: ')))
                        if year < 0:
                            print('Год не может быть отрицательным')
                    except ValueError:
                        print("Некорректный ввод. Введите только цифры")
                    except Exception as e:
                        print(f'Ошибка: {e}')
                        print("Попробуйте ввести ещё раз")
                self.add_book(title, author, year)
            if user_choice == '2':
                id_book: str = self.try_input(input('Введите ID книги: '))
                self.del_book(id_book)
            if user_choice == '3':
                choice: str = self.try_input(input('Какой поиск вы хотите осуществить?\n1. По названию\n2. По автору\n'
                                                   '3. По году издания\n4. Показать все книги\nВведите число: '))

                if choice in '1234':
                    data_insearch: str | int = ''
                    if choice == '1':
                        data_insearch = self.try_input(input('Введите название книги: '))
                    if choice == '2':
                        data_insearch = self.try_input(input('Введите автора: '))
                    if choice == '3':
                        try:
                            data_insearch = int(self.try_input(input('Введите год издания: ')))
                        except ValueError:
                            print("Некорректный ввод. Введите только цифры")
                        except Exception as e:
                            print(f'Ошибка: {e}')
                            print("Попробуйте ввести ещё раз")
                    if choice == '4':
                        self.show_all_books()
                        self.go()

                    self.book_search(choice, data_insearch)
                else:
                    print('Неверный ввод')
            if user_choice == '4':
                self.show_all_books()
            if user_choice == '5':
                self.change_status_book()
        elif user_choice == '':  # Реакция на ввод пустой строки в главном меню
            print('Вы уже в главном меню')
        else:                    # Реакция на неверный ввод
            print('Неверный ввод')
        self.go()                # Зацикленность выполнения метода главного меню


if __name__ == '__main__':
    Library()
