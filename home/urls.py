
from django.urls import path, include
from .views import formularz


from .views import Home, Polityka, Regulamin
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('polityka/', Polityka.as_view(), name='polityka'),
    path('regulamin/', Regulamin.as_view(), name='regulamin'),
    path('formularz/', formularz, name='formularz'),

]
