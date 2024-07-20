# library

Это проект системы управления библиотекой.
В приложении есть несколько функций.

После запуска открывается главное меню
(Для того чтоб в него попасть - достаточно ввести пустую строку на любом этапе работы с системой)

1. Добавить книгу
2. Удалить книгу
3. Найти книгу
4. Показать все книги
5. Изменить статус книги

Нужно ввести номер действия которое вы хотите совершить и нажать Enter

Если вы выбрали "Добавить книгу" необходимо:
- ввести название и нажать Enter
- ввести автора и нажать Enter
- ввести год издания и нажать Enter

После этого данные о книге будут внесены в books.json.
В этом файле хранится информация о книгах (ID, название, автор, год издания и статус книги)
ID книги генерируется автоматически, название, автор и год издания вносятся из введенных данных, статус книги автоматически выставляется как "в наличии"

Если вы выбрали "Удалить книгу" нужно будет ввести ID книги и нажать Enter
Данные о книге будут удалены из books.json

Если вы выбрали "Найти книгу", то откроется меню выбора режима поиска:
- По названию
- По автору
- По году издания
- Показать все книги

После этого нужно ввести данные в соответствии с выбранным режимом (название, автора или год издания книги) и нажать Enter
После этого отобразится список найденных книг или сообщение "Книг с указанными параметрами не найдено"

Если выбран режим "Показать все книги", то сразу отобразится список всех книг включающий ID, название, автора, год издания и статус книги

Если вы выбрали "Изменить статус книги" нужно будет ввести ID книги и нажать Enter
После этого выберите статус книги из предложенных вариантов (1 - в наличии, 2 - выдана)
Если введен статус соответствующий книге, то появится сообщение о том, что книга уже в этом статусе, например "Книга уже в статусе "в наличии""
Ессли введен статус изменяющий статус книги, то Данные о статусе книге будут изменены в books.json
