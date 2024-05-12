from django.shortcuts import render

def pesquisar(request):
    print('porra')
    return render(request,'loja/pesquisar.html',{})


def home(request):
    return render(request,'loja/home.html',{})