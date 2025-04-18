from livereload import Server
import render_website

def build():
    render_website.build_site()

if __name__ == '__main__':
    build()

    server = Server()
    server.watch('templates/*.html', build)
    server.watch('render_website.py',   build)
    server.watch('meta_data.json',      build)
    server.watch('static/**/*.*',       build)
    server.watch('img/**/*.*',          build)
    server.serve(root='docs', host='127.0.0.1', port=5500)
