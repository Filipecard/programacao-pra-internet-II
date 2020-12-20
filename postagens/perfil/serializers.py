from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import *

class PerfilSerializer(serializers.ModelSerializer):
	class Meta:
		model = Perfil
		fields = ('id','name', 'email')

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ('id','title', 'body','userId')

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ('id','name', 'email','body','postId')

class PostPerfilSerializer(serializers.HyperlinkedModelSerializer):
	userId = serializers.SlugRelatedField(queryset=Perfil.objects.all(),slug_field='name')
	class Meta:
		model = Post
		fields = ('id','title', 'body','userId')


class PostCommentSerializer(serializers.HyperlinkedModelSerializer):
	postId = serializers.SlugRelatedField(queryset=Post.objects.all(),slug_field='title')
	class Meta:
		model = Comment
		fields = ('id','name', 'email','body','postId')