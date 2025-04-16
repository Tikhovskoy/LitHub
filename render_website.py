import os
import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked
from pathlib import Path

with open('meta_data.json', encoding='utf-8') as f:
    books = json.load(f)

for book in books:
    txt_path = Path(book["book_path"])
    html_path = f"books_html/{txt_path.with_suffix('.html').name}"
    book["book_html_path"] = html_path

books_per_page = 10
pages = list(chunked(books, books_per_page))

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml'])
)
template = env.get_template('index.html')

os.makedirs('pages', exist_ok=True)

for page_number, books_on_page in enumerate(pages, start=1):
    rendered_page = template.render(
        books=books_on_page,
        current_page=page_number,
        total_pages=len(pages),
        base_url=""
    )
    output_path = os.path.join('pages', f'index{page_number}.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(rendered_page)

rendered_root = template.render(
    books=pages[0],
    current_page=1,
    total_pages=len(pages),
    base_url="pages/"
)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(rendered_root)
