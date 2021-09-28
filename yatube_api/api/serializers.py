from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from posts.models import Group, Post, Comment, Follow, User


class CurrentUserDefaultId(object):
    requires_context = True

    def __call__(self, serializer_instance=None):
        if serializer_instance is not None:
            self.user_id = serializer_instance.context['request'].user.id
            return self.user_id


class PostSerializer(serializers.ModelSerializer):
    author_id = serializers.HiddenField(default=CurrentUserDefaultId())
    author = serializers.PrimaryKeyRelatedField(
        source='author.username', read_only=True)

    class Meta:
        fields = '__all__'
        read_only_fields = ('pub_date', 'author_id')
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'slug', 'description')
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.HiddenField(default=CurrentUserDefaultId())
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        fields = (
            'id',
            'author',
            'post',
            'text',
            'created',
            'author_id'
        )
        read_only_fields = ('author', 'author_id', 'created')
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.CharField(default=CurrentUserDefault(), read_only=True)
    following = serializers.SlugRelatedField(slug_field='username',
                                             queryset=User.objects.all())

    class Meta:
        fields = (
            'user',
            'following',
        )
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'user'),
                message=('following error')
            ),
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
            ),
        ]
        model = Follow
