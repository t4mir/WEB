from rest_framework.decorators import api_view
from api.models import Category
from api.serializers import CategorySerializer2
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status


@api_view(['GET', 'POST'])
class CategoryListAPIViews(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer2(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.error})


@api_view(['GET', 'PUT', 'DELETE'])
class CategoryDetailAPIViews(APIView):

    def get_object(self, id2):
        try:
            return Category.objects.get(id=id2)
        except Category.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, category_id):
        category = self.get_object(category_id)
        serializer = CategorySerializer2(category)
        return Response(serializer.data)

    def put(self, request, category_id):
        category = self.get_object(category_id)
        serializer = CategorySerializer2(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, category_id):
        category = self.get_object(category_id)
        category.delete()
        return Response({'deleted': 'Done'})
