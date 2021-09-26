from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Q, F

User = get_user_model()


class Group(models.Model):
    title = models.CharField(verbose_name='title',
                             max_length=200)
    slug = models.SlugField(verbose_name='slug',
                            unique=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Группы'
        ordering = ('title',)

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(verbose_name='text')
    pub_date = models.DateTimeField(verbose_name='date published',
                                    auto_now_add=True,
                                    db_index=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='posts',
                               verbose_name='author name')
    group = models.ForeignKey(Group,
                              on_delete=models.SET_NULL,
                              blank=True, null=True,
                              related_name='groups',
                              verbose_name='group name')
    image = models.ImageField(upload_to='posts/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Записи'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             blank=True,
                             null=True,
                             related_name='comments', )
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments', )
    text = models.TextField(verbose_name='text',
                            help_text='Leave your comment here')
    created = models.DateTimeField(verbose_name='date published',
                                   auto_now_add=True,
                                   db_index=True)

    class Meta:
        verbose_name_plural = 'Комментарии'
        ordering = ('-created',)

    def __str__(self):
        return self.text


class Follow(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='follower')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='following')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'author'],
                                    name='uniq_follow'),
            models.CheckConstraint(check=~Q(user=F('author')),
                                   name='self_following'),
        ]
