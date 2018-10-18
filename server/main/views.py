from django.shortcuts import render


def main(request):
    return render(request, 'main/index.html')

def contact(request):
    return render(request, 'main/contact.html')

def about(request):
    return render(request, 'main/about.html')

def blogsingle(request):
    return render(request, 'main/blogsingle.html')

def fashion(request):
    return render(request, 'main/fashion.html')

def model(request):
    return render(request, 'main/model.html')

def travel(request):
    return render(request, 'main/travel.html')