import os
import json
import shutil
import argparse
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked

def build_site(data_path, output_dir='docs'):
    with open(data_path, encoding='utf-8') as f:
        books = json.load(f)

    for book in books:
        txt_path = Path(book['book_path'])
        html_name = txt_path.with_suffix('.html').name
        book['book_html_path'] = f"books_html/{html_name}"

    books_per_page = 10
    pages = list(chunked(books, books_per_page))

    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    index_tpl = env.get_template('index.html')
    book_tpl = env.get_template('book.html')

    os.makedirs(output_dir, exist_ok=True)

    folders_to_copy = ['static', 'media/img']
    for folder in folders_to_copy:
        if os.path.exists(folder):
            dest = os.path.join(output_dir, folder)
            if os.path.exists(dest):
                shutil.rmtree(dest)
            shutil.copytree(folder, dest)

    for page_number, books_on_page in enumerate(pages, start=1):
        rendered = index_tpl.render(
            books=books_on_page,
            current_page=page_number,
            total_pages=len(pages),
            base_url="./"
        )
        with open(f'{output_dir}/index{page_number}.html', 'w', encoding='utf-8') as f:
            f.write(rendered)

    rendered_root = index_tpl.render(
        books=pages[0],
        current_page=1,
        total_pages=len(pages),
        base_url="./"
    )
    with open(f'{output_dir}/index.html', 'w', encoding='utf-8') as f:
        f.write(rendered_root)

    for book in books:
        with open(book['book_path'], encoding='utf-8') as rf:
            text = rf.read()
        rendered = book_tpl.render(
            book={**book, 'text': text},
            base_url="../"
        )
        out_path = Path(output_dir) / book['book_html_path']
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, 'w', encoding='utf-8') as wf:
            wf.write(rendered)

def main():
    parser = argparse.ArgumentParser(description='Генерация сайта библиотеки.')
    parser.add_argument(
        '--data',
        default=os.getenv('BOOKS_JSON', 'meta_data.json'),
        help='Путь к JSON с данными о книгах (по умолчанию: meta_data.json или переменная окружения BOOKS_JSON)'
    )
    args = parser.parse_args()
    build_site(data_path=args.data)

if __name__ == '__main__':
    main()