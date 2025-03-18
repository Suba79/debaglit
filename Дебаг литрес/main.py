from books_sdk import get_book_by_id, get_author

print(get_author(get_book_by_id('AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM', 3)))

# Гипотеза 1: Неправильные скобки
# Способ проверки: методом клика пройтись по какой скобке
# Установленный факт: Все скобки на месте 
# Вывод: дело не в скобках

# Гипотеза 2: Ошибка во вложенной функции
# Способ проверки: Запустить вложенную функцию отдельно от внешней
# Код для проверки: print(get_author(get_book_by_id('1', 'AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM')))
# Установленный факт: Код не выдает ошибки, но ничего не происходит
# Вывод: Проблема с выводом данных

# Гипотеза 3: Проблема в типе данных, '1' должно быть числом
# Способ проверки: Убрал кавычки с 1
# Код для проверки: print(get_author(get_book_by_id(1, 'AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM')))
# Установленный факт: не работал print из за того что 1 было str
# Вывод: был не правльный тип данных

# Гипотеза 4: Нерпавильный токен
# Способ проверки: Поменять 1 и 'AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM' местами
# Код для проверки: print(get_author(get_book_by_id('AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM', 1)))
# Установленный факт: 
# Вывод: ...

# Гипотеза 5: ...
# Способ проверки: ...
# Код для проверки: ...
# Установленный факт: ...
# Вывод: ...