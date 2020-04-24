# import json
#
# from django.http import Http404
# from django.http.response import JsonResponse
#
# from api.models import Category, to_js, to_full
#
# from django.views.decorators.csrf import csrf_exempt
#
#
# @csrf_exempt
# def categories_list(request):
#     if request.method == 'GET':
#
#         categories = Category.objects.all()
#         categories_json = []
#         for pro in categories:
#             p = to_js(pro)
#             categories_json.append(p)
#         return JsonResponse(categories_json, safe=False)
#     elif request.method == 'POST':
#         request_body = json.loads(request.body)
#         # category = Category.objects.create(name=request_body["name"])
#         category = Category.objects.create(name=request_body.get('name', 'default value'))
#         cat = to_js(category)
#         return JsonResponse(cat)
#
#
# @csrf_exempt
# def category_detail(request, category_id):
#     try:
#         category = Category.objects.get(id=category_id)
#     except Category.DoesNotExist as e:
#         raise Http404
#     if request.method == 'GET':
#         return JsonResponse(to_js(category), safe=False)
#     elif request.method == 'PUT':
#         request_body = json.loads(request.body)
#         category.name = request_body.get('name', category.name)
#         category.save()
#         return JsonResponse(to_js(category))
#     elif request.method == 'DELETE':
#         category.delete()
#         return JsonResponse({'deleted': 'Done'})
#
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
