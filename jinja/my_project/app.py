from jinja2 import Environment, FileSystemLoader
from flask import Flask, render_template
import json

app = Flask(__name__)
app.config['DEBUG'] = True

# environment = Environment(loader=FileSystemLoader(
#     '/Users/anas/Desktop/adacourses/jinja/my_project/templates/'))


@app.route('/')
def index():
    # template = environment.get_template('index.html')
    # content = template.render(title='Сайт фильмов')
    content = render_template('index.html', title='Сайт фильмов')
    return content

@app.route('/movies/')
def get_movies():
    file = open('jinja/my_project/movies.json')
    data = json.load(file)

    movies = data.values()

    context = {
        'title': 'Фильмы',
        'movies': movies
    }

    template = environment.get_template('movies.html')
    content = template.render(**context)
    return content

@app.route('/movie/<int:id>/')
def movie_detail(id):
    file = open('jinja/my_project/movies.json')
    data = json.load(file)
    movie = data.get(str(id))
    if movie:
        template = environment.get_template('movie-detail.html')
        content = template.render(movie=movie)
        return content
    
    return '<h1>Такого фильма нет!</h1>'

if __name__ == '__main__':

    app.run()
