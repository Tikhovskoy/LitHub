# LitHub

**LitHub** проект, демонстрирующий принципы статической генерации контента на Python. Основная идея состоит в трансформации структурированного набора метаданных (JSON) и текстовых файлов книг в готовый к деплою статический веб‑сайт, обеспечивающий офлайн‑ и онлайн‑доступ.

---

## 1. Обзор проекта

LitHub реализует архитектуру «генерации за один проход» с использованием:

- **Jinja2** в качестве движка шаблонизации для разделения логики представления и данных;  
- **JSON** для хранения семантически аннотированных метаданных о книгах (название, автор, жанры, путь к тексту и обложке);  
- **livereload** для поддержания интерактивной среды разработки при изменении шаблонов и исходных данных.

Результатом работы является набор HTML‑страниц в каталоге `docs/`, готовых к хостингу на GitHub Pages или к локальному просмотру без необходимости установки серверного ПО.

---

## 2. Применение:

### 2.1. Конечный пользователь

Пользователь скачивает готовый архив и начинает чтение без предварительной установки инструментов.

1. **Скачать архив**: получить `LitHub.zip`.  
2. **Распаковать**: извлечь содержимое в произвольную директорию.  
3. **Запустить просмотр**: открыть файл `docs/index.html` в любом современном браузере.  
4. **Навигация и чтение**: перелистывание страниц каталога — стрелками или вводом номера; чтение текста — по клику «Читать», открытие в новой вкладке.

### 2.2. Разработчик

Для оценки применимости к исследовательским или учебным задачам достаточно ознакомиться с архитектурными и технологическими решениями.

- **Цель**: демонстрация методологии преобразования JSON‑данных в HTML через шаблоны.  
- **Данные**: метаданные в `meta_data.json` содержат всю необходимую семантику для генерации страниц.  
- **Онлайн‑демо**: полнофункциональная версия доступна по адресу   https://tikhovskoy.github.io/LitHub/.  

Для глубокого понимания кода и работы в живой среде разработчику рекомендуется следующее.

#### 2.2.1. Клонирование и настройка виртуального окружения

```bash
git clone https://github.com/Tikhovskoy/LitHub.git
cd LitHub
# Создание виртуального окружения
touch venv && python3 -m venv venv
# Активация окружения
source venv/bin/activate    # Linux/MacOS
.\venv\Scripts\Activate.ps1 # Для Windows PowerShell
# Установка зависимостей
pip install -r requirements.txt
```  

#### 2.2.2. Локальный сервер с автоматическим перезапуском

```bash
python serve.py
```  

Сайт станет доступен по адресу http://127.0.0.1:5500/ и будет автоматически обновляться при изменении шаблонов (`templates/`), JSON‑файла (`meta_data.json`) или ассетов (`static/`, `img/`).

#### 2.2.3. Структура репозитория
```
LitHub/
├── docs/                  # Готовый к публикации сайт
│   ├── index.html         # Главная страница каталога
│   ├── index*.html        # Остальные страницы
│   ├── books_html/        # HTML-страницы отдельных книг
│   ├── media/img/         # Обложки книг
│   └── static/            # Стили, скрипты, favicon
│
├── media/                 # Исходные данные
│   ├── books/             # Тексты книг
│   ├── img/               # Обложки книг
│   └── screenshot/        # Скриншоты проекта
│
├── static/                # Исходные стили, скрипты, favicon
├── templates/             # Шаблоны Jinja2: index.html, book.html
├── meta_data.json         # Метаданные книг
├── render_website.py      # Генератор HTML-страниц
├── serve.py               # Локальный сервер с livereload
├── requirements.txt       # Зависимости проекта
├── README.md              # Документация
└── .gitignore             # Исключения для git
```

#### 2.2.4. Расширение функциональности

1. **Добавление новой книги**: помещаете текстовый файл в директорию (например, `books/`), вносите запись в `meta_data.json` с полями `title`, `author`, `genres`, `book_path`, `img_src`.  
2. **Запуск генерации**: `python render_website.py`.  

## 3. Конфигурация пути к данным:

По умолчанию сайт генерируется на основе файла `meta_data.json`, находящегося в корне проекта. Но вы можете использовать **свои данные**, указав путь одним из следующих способов:

### 1. Через аргумент командной строки

```bash
python render_website.py --data путь/к/файлу.json
```

Пример:

```bash
python render_website.py --data test_data/scifi_books.json
```

---

### 2. Через переменную окружения `BOOKS_JSON`

```bash
export BOOKS_JSON=путь/к/файлу.json
python render_website.py
```

На Windows:

```powershell
$env:BOOKS_JSON = "test_data/scifi_books.json"
python render_website.py
```

---

### Приоритет

Если указать **и переменную окружения**, и `--data`, то приоритет будет у **аргумента командной строки**.