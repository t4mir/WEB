from django.shortcuts import render

from api.models import Product, Category
from django.http.response import HttpResponse, JsonResponse
from django.http import Http404

# Create your views here.
def product_list(request):
    try:
        products = Product.objects.all()
        products_json = [product.to_json() for product in products]
        return JsonResponse(products_json, safe=False)
    except:
        return JsonResponse({"error": "no product"})
def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(product.to_json())

def category(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(category.to_json())

def category_list(request):
    categories = Category.objects.all()
    json_categories = [c.to_json() for c in categories]
    return JsonResponse(json_categories, safe=False)

def products_category(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    products = category.product_set.all()
    json_products = [p.to_json() for p in products]
    return JsonResponse(json_products, safe=False)
