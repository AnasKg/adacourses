# 1)Создать новый пост.
new_post = Post.objects.create(title="Новый пост", content="Это содержание нового поста", author=user)

# 2) Получить все посты.
all_posts = Post.objects.all()


# 3) Получить пост с определенным идентификатором.
post = Post.objects.get(id=10)

# 4) Получить все комментарии для определенного поста.
comments = Comment.objects.filter(post_id=post_id)

# 5) Создать новый комментарий для определенного поста.
new_comment = Comment.objects.create(post_id=post_id, author=user, content="Это новый комментарий")

# 6) Получить все комментарии, оставленные определенным автором.
comments = Comment.objects.filter(author_id=author_id)

# 7) Получить все посты, опубликованные после определенной даты.
posts = Post.objects.filter(created_at__gt=date)

# 8) Получить все посты, содержащие определенное слово в заголовке.
posts = Post.objects.filter(title__icontains=word)

# 9) Получить все посты, отсортированные по дате создания (от новых к старым).
posts = Post.objects.order_by('-created_at')

# 10) Получить количество комментариев для каждого поста.
from django.db.models import Count

post_comments_count = Post.objects.annotate(comment_count=Count('comment'))

# 11) Получить список авторов, оставивших комментарии.
comment_authors = User.objects.filter(comment__isnull=False).distinct()

# 12) Изменить содержание определенного поста.
post = Post.objects.get(id=post_id)
post.content = "Новое содержание поста"
post.save()

# 13) Изменить автора определенного комментария.
comment = Comment.objects.get(id=comment_id)
comment.author_id = new_author_id
comment.save()

# 14) Удалить определенный пост.
post = Post.objects.get(id=post_id)
post.delete()

# 15) Удалить все комментарии для определенного поста.
Comment.objects.filter(post_id=post_id).delete()

# 16) Получить первые 5 постов.
first_five_posts = Post.objects.all()[:5]

# 17) Получить последние 3 поста.
last_three_posts = Post.objects.all().order_by('-created_at')[:3]

# 18) Получить суммарное количество комментариев для всех постов.
from django.db.models import Sum

total_comments = Post.objects.aggregate(total_comments=Sum('comment__id'))

# 19) Получить список постов, у которых количество комментариев больше 10.
posts_with_more_than_10_comments = Post.objects.annotate(comment_count=Count('comment')).filter(comment_count__gt=10)

# 20) Получить список постов, у которых количество слов в содержании больше 100.
posts_with_more_than_100_words = Post.objects.filter(content__icontains=' ').annotate(word_count=Count('content__word')).filter(word_count__gt=100)
