from django.shortcuts import render
from .models import Register, Contact


def index(request):
    return render(request, 'intra/Home.html')


def about(request):
    return render(request, 'intra/about_us.html')


def faq(request):
    return render(request, 'intra/faq.html')


def training(request):
    return render(request, 'intra/training.html')


def register(request):
        if request.method == 'POST':
            if request.POST.get('name'):
                regist = Register()
                regist.name = request.POST.get('name')
                regist.number = request.POST.get('number')
                regist.email = request.POST.get('email')
                regist.program = request.POST.get('program')
                regist.company = request.POST.get('company')
                regist.location = request.POST.get('loc')
                regist.save()
                return render(request, 'intra/Home.html')

        else:
            return render(request, 'intra/Registration.html')


def cont(request):
    if request.method == 'POST':
        if request.POST.get('name'):
            con = Contact()
            con.name = request.POST.get('name')
            con.number = request.POST.get('number')
            con.email = request.POST.get('email')
            con.message = request.POST.get('message')
            con.save()
            return render(request, 'intra/Home.html')

    else:
        return render(request, 'intra/contact_us.html')