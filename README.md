# LitHub — Онлайн библиотека

LitHub — это сайт для чтения книг онлайн. Каждая книга представлена с обложкой, описанием, жанрами и кнопкой для чтения.

Сайт доступен по адресу:  
https://tikhovskoy.github.io/LitHub/

## Возможности

- Каталог книг с пагинацией
- Отображение до 10 книг на странице
- Чтение книги в отдельной вкладке
- Чистый адаптивный интерфейс на Bootstrap
- У каждой книги отображаются:
  - обложка (если есть)
  - название и автор
  - жанры
  - ссылка на чтение

## Пример

Скриншот сайта:

![Скриншот сайта](screenshot/screenshot.png)

## Как собрать сайт вручную

Установите зависимости:

```bash
pip install -r requirements.txt
```

Сгенерируйте сайт:

```bash
python render_website.py
```

Собранный сайт будет находиться в папке `docs/`. Эту папку можно размещать на GitHub Pages.

## Структура проекта

```
LitHub/
├── docs/               # Сгенерированный сайт
├── static/             # Стили, скрипты, favicon
├── img/                # Обложки книг
├── templates/          # Jinja2-шаблоны
├── books_html/         # HTML-версии книг
├── render_website.py   # Скрипт генерации
├── requirements.txt
├── .gitignore
└── README.md
```