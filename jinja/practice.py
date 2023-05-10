from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader(
    '/Users/anas/Desktop/adacourses/jinja/'))

template = environment.get_template('index.html')

context = {
    'name': 'Python',
    'title': 'Мой сайт',
    'text': 'jinja',
    'number': 15,
    'numbers': [1, 10, 20, 543, 4]
}

content = template.render(**context)

with open('result.html', 'w') as file:
    file.write(content)
