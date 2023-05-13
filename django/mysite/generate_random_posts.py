import random
import string
from django.contrib.auth.models import User
from posts.models import Post, Comment

# Генерация случайного названия поста
def generate_post_title():
    prefix = ['Интересный', 'Полезный', 'Забавный', 'Важный', 'Удивительный']
    suffix = ['пост', 'статья', 'блог']
    return random.choice(prefix) + ' ' + random.choice(suffix)

# Генерация случайного содержания поста
def generate_post_content():
    lorem_ipsum = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce mollis posuere nibh. 
    Vestibulum nec aliquam lectus. Sed vestibulum gravida ante, eu sagittis nisl fermentum at. 
    Integer volutpat erat in urna finibus, sit amet vulputate lectus consequat. Donec gravida congue malesuada.'''
    return lorem_ipsum

# Генерация случайного комментария
def generate_comment():
    lorem_ipsum = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce mollis posuere nibh. 
    Vestibulum nec aliquam lectus.'''
    return lorem_ipsum

# Генерация случайного имени пользователя
def generate_username():
    return ''.join(random.choices(string.ascii_lowercase, k=8))


def run():
    # Создание случайных пользователей
    users = []
    for _ in range(10):
        username = generate_username()
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        email = f'{username}@example.com'
        user = User.objects.create_user(username=username, first_name=username, password=password, email=email)
        users.append(user)

    # Создание 20 постов
    for _ in range(20):
        title = generate_post_title()
        content = generate_post_content()
        
        # Создание поста в модели Post
        post = Post.objects.create(title=title, content=content, author=random.choice(users))
        
        print("Создан пост:", post)
        
        # Генерация случайного числа комментариев для каждого поста (от 1 до 5)
        num_comments = random.randint(1, 5)
        
        # Создание комментариев для текущего поста
        for _ in range(num_comments):
            comment_content = generate_comment()
            
            # Создание комментария в модели Comment
            comment = Comment.objects.create(post=post, author=random.choice(users), content=comment_content)

            
            print("Создан комментарий:", comment)
        
        print("----")  # Разделитель между постами
