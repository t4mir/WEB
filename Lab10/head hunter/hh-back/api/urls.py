from django.urls import path
from .views import views
from api.views import viewsCBV, viewsFBV
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    # url('companies/', views.companies_lst),
    # url('companies/<int:company_id>/', views.getOneCompany),
    # url('companies/<int:company_id>/vacancies/', views.vacanciesByCompany),
    # url('vacancies/', views.vacancies_lst),
    # url('vacancies/<int:vacancy_id>/', views.getOneVacancy),
    # url('vacancies/top_ten/', views.decSortedVacancies)

    path('login/', obtain_jwt_token),
    path('companies/', viewsFBV.CompanyListView),
    path('companies/<int:company_id>/', viewsFBV.CompanyDetailsView),
    path('companies/<int:company_id>/vacancies/', viewsFBV.VacanciesListByCompany),
    path('vacancies/', viewsFBV.VacanciesListView),
    path('vacancies/<int:vacancy_id>/', viewsCBV.VacancyDetailsView.as_view())
]