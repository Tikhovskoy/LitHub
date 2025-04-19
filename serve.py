from livereload import Server
import os
import render_website

def build():
    data_path = os.getenv('BOOKS_JSON', 'meta_data.json')
    render_website.build_site(data_path)

def main():
    build()
    server = Server()
    server.watch('templates/*.html', build)
    server.watch('render_website.py', build)
    server.watch('meta_data.json', build)
    server.watch('static/**/*.*', build)
    server.watch('media/img/**/*.*', build)
    server.watch('media/books/**/*.*', build)
    server.serve(root='docs', host='127.0.0.1', port=5500)

if __name__ == '__main__':
    main()