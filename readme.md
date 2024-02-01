## TODO
    + Добавить статистике функцию вывода в Excel
    +- Протестировать
    + Добавить остальные категории
    + Исправить остальные обязательные параметры

    + Исправить условия
        + Внешний вид на Форму
    + Добавить новые условия "Форма"
        
    - Прорефакторить
    - Создать .exe файл

## ИСПРАВИТЬ
    - Помнять способ определения условия для параметров через паттерн "Стратегия" (?)

## ДОБАВИТЬ
    - Список, куда будут добавляться категории, которые не были определены (?)
    - Класс для Result
    - Определение подкатегории "Профили" и "Блоки питания"

## ТЕСТИРОВАНИЕ
    + Условные параметры
        + Оформление OR Форма OR Форма плафона
        + Диаметр OR (Длина AND Ширина)
        + IF Цоколь == LED: Цветовая температура
                            AND Суммарная мощность LED
                            AND Цвет свечения
                            AND Световой поток, Lm
    + Заливка
        + Только необходимых для заполнения
        + Цвет
            + Неусловные — красным
            + Условные — оранджевым
    + Вывод статистики
        + Общее количество товаров
        + Количество незаполненных товаров
            + Наличие всех параметров
            + Наличие верного количества
        + Статистика параметров
    - Совпадение выполнения алгоритма с нужной категорией
    - Правильность обработки подкатегорий "Профили" и "Блоки питания"