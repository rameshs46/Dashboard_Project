from django.shortcuts import render
from django.http import JsonResponse
from .models import Order
from django.core import serializers


# Create your views here.
def Dashboard_With_Pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})


def Pivot_Data(request):
    dataset = Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)
