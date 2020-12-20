from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .models import *
from .serializers import *


@api_view(['GET','POST'])
def perfil_list(request):
	if request.method == 'GET':
		perfis = Perfil.objects.all()
		perfil_serializer = PerfilSerializer(perfis, many=True)
		return Response(perfil_serializer.data)
	elif request.method == 'POST':
		perfil_serializer = PerfilSerializer(data=request.data)
		if perfil_serializer.is_valid():
			perfil_serializer.save()
			return Response(perfil_serializer.data, status=status.HTTP_201_CREATED)
		return Response(perfil_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'POST', 'DELETE'])
def perfil_detail(request, pk):
	try:
		perfil = Perfil.objects.get(pk=pk)
	except Perfil.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		perfil_serializer = PerfilSerializer(perfil)
		return Response(perfil_serializer.data)

	elif request.method == 'PUT':
		perfil_serializer = PerfilSerializer(perfil, data=request.data)		
		if perfil_serializer.is_valid():
			perfil_serializer.save()
			return Response(perfil_serializer.data)
		return Response(perfil_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

	elif request.method == 'DELETE':
		perfil.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def loadperfil(request):
    arquivo = open('perfil\db.json')
    data = json.load(arquivo)
    perfis = data['users']

    perfil_serializer = PerfilSerializer(data= perfis,many=True)		
    if perfil_serializer.is_valid():
        perfil_serializer.save()
    return Response(perfil_serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','POST'])
def loadpost(request):
    arquivo = open('perfil\db.json')
    data = json.load(arquivo)
    posts = data['posts']
    
    post_serializer = PostSerializer(data= posts,many=True)		
    if post_serializer.is_valid():
        post_serializer.save()
    return Response(post_serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','POST'])
def loadcomment(request):
    arquivo = open('perfil\db.json')
    data = json.load(arquivo)
    comments = data['comments']
    
    comment_serializer = CommentSerializer(data= comments,many=True)		
    if comment_serializer.is_valid():
        comment_serializer.save()
    return Response(comment_serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def postperfil_list(request):
	if request.method == 'GET':
		post = Post.objects.all()
		postperfil_serializer = PostPerfilSerializer(post, many=True)
		return Response(postperfil_serializer.data)

@api_view(['GET'])
def postperfil_detail(request, pk):
	try:
		post = Post.objects.get(pk=pk)
	except Post.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		postperfil_serializer = PostPerfilSerializer(post)
		return Response(postperfil_serializer.data)

@api_view(['GET'])
def postcomment_list(request):
	if request.method == 'GET':
		comment = Comment.objects.all()
		postcomment_serializer = PostCommentSerializer(comment, many=True)
		return Response(postcomment_serializer.data)
@api_view(['GET'])
def postcomment_detail(request, pk):
	try:
		comment = Comment.objects.get(pk=pk)
	except Post.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		postcomment_serializer = PostCommentSerializer(comment)
		return Response(postcomment_serializer.data)