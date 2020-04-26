from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.models import Game, Category
from api.serializers import GameSerializer, CategorySerializer


class CategoryListView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        ser = CategorySerializer(categories, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = CategorySerializer(request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CategoryDetailsView(APIView):
    def get_object(self, id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, id):
        company = self.get_object(id)
        ser = CategorySerializer(company)
        return Response(ser.data)

    def put(self, request, id):
        serializer = CategorySerializer(instance=self.get_object(id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"error": serializer.errors})

    def delete(self, request, id):
        category = self.get_object(id)
        category.delete()
        return Response({"Deleted": True})


class GamesListView(APIView):
    def get(self, request):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GameDetailsView(APIView):
    def get_object(self, id):
        try:
            return Game.objects.get(id=id)
        except Game.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, game_id):
        game = self.get_object(game_id)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def put(self, request, vacancy_id):
        game = self.get_object(vacancy_id)
        serializer = GameSerializer(instance=game, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, game_id):
        game = self.get_object(game_id)
        game.delete()
        return Response({'deleted': True})

