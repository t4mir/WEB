from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from core.models import Product, to_json
from django.http import Http404


# def product_list(request):
#     return JsonResponse({})

def product_list(request):
    p = Product.objects.all()
    product_json = []
    for product in p:
        pro = to_json(product)
        product_json.append(pro)
    return JsonResponse(product_json, safe = False)


def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        raise Http404
    return JsonResponse(to_json(product),safe = False)