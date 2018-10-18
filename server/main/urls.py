from django.urls import path

from main.views import (
    main, contacts, about, page1
)


urlpatterns = [
    path('contacts/', contacts),
    path('about/', about),
    path('page1/', page1),
    path('', main),
    
]
