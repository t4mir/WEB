from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer, CompanyModelSerializer, VacancyModelSerializer

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
def CompanyDetailsView(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = CompanyModelSerializer(company)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        company.delete()
        return Response({'deleted': True})

@api_view(['GET'])
def VacanciesListByCompany(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return Response({'error': str(e)})
    vacancies = Vacancy.objects.filter(company=company)
    serializer = VacancySerializer(vacancies, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def VacanciesListView(request):
    if request.method == 'GET':
        serializer = VacancyModelSerializer(Vacancy.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'POST':
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response({"error": serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)


def VacancyDetailsView(request, id):
    try:
        this_vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist as e:
        return Response({'error': str(e)})
    if request.method == 'GET':
        serializer = VacancyModelSerializer(this_vacancy)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        # request_body = json.loads(request.body)
        serializer = VacancySerializer(instance=this_vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response({"error": serializer.errors})
    elif request.method == 'DELETE':
        this_vacancy.delete()
        return Response("Deleted", status=status.HTTP_202_ACCEPTED)
    else:
        return Response("error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def TopTenVacanciesView(request):
    if request.method == 'GET':
        serializer = VacancySerializer(Vacancy.objects.all().order_by('-salary')[:10], many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)