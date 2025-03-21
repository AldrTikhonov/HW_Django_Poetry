# HW_Django_Poetry

В данной работе создается проект интернет-магазина, который будем дорабатывать на каждом уроке в течение всего курса.

В первом задании произведем следующие действия:

1. Настройка проекта

2. Создание и настройка приложения

3. Создание шаблонов

4. Реализация контроллеров

Во втором задании произведем следующие действия:

1. Подключение СУБД PostgreSQL для работы в проекте

2. В приложении каталога создадим модели Product и Category и опишем для них базовые настройки

3. Перенесем отображение модулей в базу данных с помощью инструмента миграций

4. Создадим суперпользователя и зарегистрируем модели Product и Category в админке, затем настроим отображение моделей

5. Через инструмент Django shell заполним список категорий и продуктов, а затем применив различные фильтры выполним запросы

6. Сформируем фикстуры для моделей Product и Category

7. Создадим кастомные команды для удаления старых данных и добавление новых данных в базу

В третьем задании выполним следующие действия:

1. Перевод имеющихся в проекте контроллеры с FBV на CBV

2. Создание нового приложения для блога и добавление его в файл settings.py.

   Создание новой модели блоговой записи с полями:

    - заголовок,

    - содержимое,

    - превью (изображение),

    - дата создания,

    - признак публикации (булевое значение),

    - количество просмотров

    Для работы с блогом реализуем полный CRUD для новой модели, используя CBV.

3. Модифицируем вывод и обработку запросов, добавив следующую логику на уровне контроллеров:

    1. Увеличение счетчика просмотров: при открытии отдельной статьи увеличивать счетчик просмотров

    2. Фильтрация опубликованных статей: выводить с список статей только те, которые имеют положительный признак 
       публикации

    3. Перенаправление после редактирования: после успешного редактирования записи необходимо перенаправлять 
       пользователя на просмотр этой статьи
