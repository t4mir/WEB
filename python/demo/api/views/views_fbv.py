
from rest_framework.decorators import api_view
from api.models import Category
from api.serializers import CategorySerializer2
from rest_framework.response import Response

from rest_framework import status


@api_view(['GET', 'POST'])
def categories_list(request):
    if request.method == 'GET':

        categories = Category.objects.all()
        serializers = CategorySerializer2(categories, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializer = CategorySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response({'error': serializer.errors},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return Response({'error': str(e)})
    if request.method == 'GET':
        serializer = CategorySerializer2(category)
        return Response(serializer.data)
    elif request.method == 'PUT':

        serializer = CategorySerializer2(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        category.delete()
        return Response({'deleted': 'Done'})

#
# def category_products(request, category_id):
#     try:
#         category = Category.objects.get(id=category_id)
#     except Category.DoesNotExist as e:
#         raise Http404
#     products = category.products.all()
#     product_json = []
#     for pro in products:
#         p = to_full(pro)
#         product_json.append(p)
#     return JsonResponse(product_json, safe=False)
