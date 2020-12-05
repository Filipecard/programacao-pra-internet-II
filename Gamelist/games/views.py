"""
Book: Building RESTful Python Web Services
Chapter 2: Working with class based views and hyperlinked APIs in Django
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect
from datetime import datetime
from .models import Game
from .serializers import GameSerializer

def lista_names(objects):
	lista = []
	for dados in objects:
		lista += [dados['name']]
	return lista


@api_view(['GET','POST'])
def game_list(request):
	if request.method == 'GET':
		games = Game.objects.all()
		games_serializer = GameSerializer(games, many=True)
		return Response(games_serializer.data)
	elif request.method == 'POST':
		games = Game.objects.all()
		gameslist = lista_names(GameSerializer(games, many=True).data)
		
		games_serializer = GameSerializer(data=request.data)
		if games_serializer.is_valid():
			name = request.data['name']
			if name in gameslist:
				pass
			else:
				games_serializer.save()
				return Response(games_serializer.data, status=status.HTTP_201_CREATED)
		return Response(games_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'POST', 'DELETE'])
def game_detail(request, pk):
	try:
		game = Game.objects.get(pk=pk)
	except Game.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		games_serializer = GameSerializer(game)
		return Response(games_serializer.data)

	elif request.method == 'PUT':
		games_serializer = GameSerializer(game, data=request.data)		
		if games_serializer.is_valid():
			games_serializer.save()
			return Response(games_serializer.data)
		return Response(games_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		games_serializer = GameSerializer(game)
		data = str(games_serializer.data['release_date']) 
		ano = tratamento(data)
		if ano < 0:
			game.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
		else:
			pass
		return redirect('/games')
		

def tratamento(data):
	dat = ''

	hoje = str(datetime.now())
	dt = ''
	for i in range(len(data)):
		if data[i] == 'T':
			break
		dat += data[i]
		dt += hoje[i]

	
	day = int(dt[8]+dt[9]) - int(dat[8]+dat[9])
	month =  int(dt[5]+dt[6]) - int(dat[5]+dat[6])
	year =  int(dt[0]+dt[1]+dt[2]+dt[3]) - int(dat[0]+dat[1]+dat[2]+dat[3])

	if day < 0:
		month -=1
		day += 30
	if month < 0:
		year -= 1
		month += 12
	return year
	
	

