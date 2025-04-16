import json
from livereload import Server
from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked

def on_reload():
    with open('meta_data.json', encoding='utf-8') as f:
        books = json.load(f)

    books = books[:100]

    book_pairs = list(chunked(books, 2))

    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('index.html')

    rendered_page = template.render(book_pairs=book_pairs)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(rendered_page)

on_reload()

server = Server()
server.watch('templates/*.html', on_reload)
server.watch('meta_data.json', on_reload)
server.serve(root='.')
