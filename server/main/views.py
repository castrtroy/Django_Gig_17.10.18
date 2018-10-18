from django.shortcuts import render


def main(request):
    return render(request, 'main/index.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def about(request):
    return render(request, 'main/about.html')

def page1(request):
    return render(request, 'main/page1.html')
