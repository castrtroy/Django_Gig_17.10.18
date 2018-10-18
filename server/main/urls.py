from django.urls import path

from main.views import (
    main, contact, about, fashion, model, blogsingle, travel
)


urlpatterns = [
    path('contact/', contact),
    path('about/', about),
    path('blogsingle/', blogsingle),
    path('fashion/', fashion),
    path('model/', model),
    path('travel/', travel),
    path('', main),
    
]
