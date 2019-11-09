from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    stock_names = ['REL,''HDFC', 'TCS']
    context = {'stock_names':stock_names}
    return render(request, "stock/home.html", context)