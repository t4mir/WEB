from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.models import Vacancy, Company
from api.serializers import VacancySerializer, CompanySerializer

class CompanyListView(APIView):

    def get(self, request):
        companies = Company.objects.all()
        ser = CompanySerializer(companies, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = CompanySerializer(request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VacanciesListView(APIView):
    def get (self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VacancyDetailsView(APIView):
    def get_object(self, id):
        try:
            return Vacancy.objects.get(id=id)
        except Vacancy.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, vacancy_id):
        vacancy = self.get_object(vacancy_id)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

    def put(self, request, vacancy_id):
        vacancy = self.get_object(vacancy_id)
        serializer = VacancySerializer(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, vacancy_id):
        vacancy = self.get_object(vacancy_id)
        vacancy.delete()
        return Response({'deleted': True})


class CompanyDetailsView(APIView):
    def get_object(self, id):
        try:
            return Company.objects.get(id=id)
        except Company.DoesNotExist as e:
            return Response({'error': str(e)})
    def get(self, request, id):
        company = self.get_object(id)
        ser = CompanySerializer(company)
        return Response(ser.data)
    def put(self, request, id):
        serializer = CompanySerializer(instance=self.get_object(id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"error": serializer.errors})
    def delete(self, request, id):
        company = self.get_object(id)
        company.delete()
        return Response({"Deleted": True})

class TopTenVacanciesView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.order_by('-salary')[:10]
    serializer_class = VacancySerializer
    permission_classes = (IsAuthenticated,)