import json
from jinja2 import Environment, FileSystemLoader, select_autoescape

with open('meta_data.json', encoding='utf-8') as f:
    books = json.load(f)

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('index.html')

rendered_page = template.render(books=books)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(rendered_page)
