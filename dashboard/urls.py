from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard_With_Pivot, name='dashboard_with_pivot'),
    path('data', views.Pivot_Data, name='pivot_data'),
]
