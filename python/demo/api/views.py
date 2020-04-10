from django.http.response import JsonResponse
from api.models import Category


def categories_list(request):
    categories = Category.objects.all()

    categories_json = []
    for pro in categories:
        categories_json.append(pro.to_catjson)

    return JsonResponse(categories_json, safe=False)
