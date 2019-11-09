from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    stock_names = ['REL','HDFC','TCS']
    context = {'stock_names':stock_names}
    return render(request, "stock/home.html", context)


def analysis(request, name):
    stock_detilas = {'REL':{'buy':['DEC'], 'sell':['JAN'],'hold':['June']},
                     'HDFC': {'buy': ['JAN'], 'sell': ['DEC'], 'hold': ['July']},
                     'TCS': {'buy': ['Nov'], 'sell': ['May'], 'hold': ['Aug']}}
    context = {'data':stock_detilas[name]}
    return render(request, "stock/stock_analysis.html", context)