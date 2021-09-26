from rest_framework import serializers

from posts.models import Group, Post, Comment, Follow


class CurrentUserDefault(object):

    requires_context = True

    def __call__(self, serializer_instance=None):
        if serializer_instance is not None:
            self.user_id = serializer_instance.context['request'].user.id
            return self.user_id


class PostSerializer(serializers.ModelSerializer):
    author_id = serializers.HiddenField(default=CurrentUserDefault())
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
    author_id = serializers.HiddenField(default=CurrentUserDefault())
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
    user_id = serializers.HiddenField(default=CurrentUserDefault())
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        fields = '__all__'
        read_only_fields = ('user_id',)
        model = Follow
