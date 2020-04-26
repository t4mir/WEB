# from api.models import Category, Vacancy
# from django.http import JsonResponse
#
#
# def categories_lst(request):
#     categories = Category.objects.all()
#     json_categories = [i.to_json() for i in categories]
#     return JsonResponse(json_categories, safe=False)
#
# def getOneCategory(request, company_id):
#     try:
#         company = Company.objects.get(id=company_id)
#     except Company.DoesNotExist as e:
#         return JsonResponse({'error': str(e)})
#     return JsonResponse(company.to_json())
#
# def vacanciesByCompany(request, company_id):
#     try:
#         company = Company.objects.get(id=company_id)
#     except  Company.DoesNotExist as e:
#         return JsonResponse({'error': str(e)})
#     vacancies = Vacancy.object.filter(companies = company)
#     json_vacancies = [i.to_json() for i in vacancies]
#     return JsonResponse(json_vacancies, safe=False)
#
# def vacancies_lst(request):
#     vacancies = Vacancy.objects.all()
#     json_vacancies = [i.to_json() for i in vacancies]
#     return JsonResponse(json_vacancies, safe=False)
#
# def getOneVacancy(request, vacancy_id):
#     try:
#         vacancy = Vacancy.objects.get(id=vacancy_id)
#     except  Company.DoesNotExist as e:
#         return JsonResponse({'error': str(e)})
#     return JsonResponse(vacancy.to_json())
#
#
#
#
#
