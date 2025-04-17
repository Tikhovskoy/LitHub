import os
import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked
from pathlib import Path
import shutil

with open('meta_data.json', encoding='utf-8') as f:
    books = json.load(f)

for book in books:
    txt_path = Path(book["book_path"]) 
    html_name = txt_path.with_suffix('.html').name
    book["book_html_path"] = f"books_html/{html_name}"

books_per_page = 10
pages = list(chunked(books, books_per_page))

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

os.makedirs('pages', exist_ok=True)
index_tpl = env.get_template('index.html')

for page_number, books_on_page in enumerate(pages, start=1):
    rendered = index_tpl.render(
        books=books_on_page,
        current_page=page_number,
        total_pages=len(pages),
        base_url=""  
    )
    with open(f'pages/index{page_number}.html', 'w', encoding='utf-8') as f:
        f.write(rendered)

rendered_root = index_tpl.render(
    books=pages[0],
    current_page=1,
    total_pages=len(pages),
    base_url="pages/"
)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(rendered_root)

book_tpl = env.get_template('book.html')
os.makedirs('books_html', exist_ok=True)

for book in books:
    html_out = Path(book["book_html_path"])
    with open(book["book_path"], encoding='utf-8') as rf:
        txt = rf.read()
    book['text'] = txt
    rendered = book_tpl.render(book=book)
    with open(html_out, 'w', encoding='utf-8') as wf:
        wf.write(rendered)

shutil.copy('static/favicon.ico', 'pages/favicon.ico')
