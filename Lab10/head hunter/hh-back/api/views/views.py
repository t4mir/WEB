from api.models import Company, Vacancy
from django.http import JsonResponse


def companies_lst(request):
    companies = Company.objects.all()
    json_companies = [i.to_json() for i in companies]
    return JsonResponse(json_companies, safe=False)

def getOneCompany(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(company.to_json())

def vacanciesByCompany(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except  Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    vacancies = Vacancy.object.filter(companies = company)
    json_vacancies = [i.to_json() for i in vacancies]
    return JsonResponse(json_vacancies, safe=False)

def vacancies_lst(request):
    vacancies = Vacancy.objects.all()
    json_vacancies = [i.to_json() for i in vacancies]
    return JsonResponse(json_vacancies, safe=False)

def getOneVacancy(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except  Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(vacancy.to_json())


def decSortedVacancies(request):
    vacancies = Vacancy.objects.order_by('salary')[:10]
    json_vacancies = [v.to_json() for v in vacancies]
    return JsonResponse(json_vacancies, safe=False)












