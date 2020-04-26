from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.models import Category, Game, Company
from api.serializers import CategorySerializer, GameSerializer, CategoryModelSerializer2, GameModelSerializer, \
    CompanySerializer


@api_view(['GET', 'POST'])
def CategoryListView(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'POST'])
def CompanyListView(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def CategoryDetailsView(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
        # Category.sorted_objects.sort_by_title(request).filter(name_id=name_id)
        # categroy = Category.sorted_objects.sort_by_id(request).filter(id_id=id_id)
    except Category.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = CategoryModelSerializer2(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        category.delete()
        return Response({'deleted': True})


@api_view(['GET'])
def GamesListByCategory(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return Response({'error': str(e)})
    games = Game.objects.filter(category=category)
    serializer = GameSerializer(games, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def GamesListView(request):
    if request.method == 'GET':
        serializer = GameModelSerializer(Game.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'POST':
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response({"error": serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)


def GameDetailsView(request, id2):
    try:
        this_game = Game.objects.get(id=id2)
    except Game.DoesNotExist as e:
        return Response({'error': str(e)})
    if request.method == 'GET':
        serializer = GameModelSerializer(this_game)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        # request_body = json.loads(request.body)
        serializer = GameSerializer(instance=this_game, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response({"error": serializer.errors})
    elif request.method == 'DELETE':
        this_game.delete()
        return Response("Deleted", status=status.HTTP_202_ACCEPTED)
    else:
        return Response("error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
