from django.urls import path  
from .views import signup, activate, confirmation, create_region, create_miasto, profil, create_preferencje, ProfilUpdate, sukces
urlpatterns = [  

    path('register/', signup, name = 'reg'),  
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
        activate, name='activate'),  
    path('confirmation', confirmation, name='confirmation'),
    path('sukces/', sukces, name='sukces'),
    path('profil/<int:pk>', profil, name="profil"),
    path('profil/<int:pk>/create-region/', create_region.as_view(), name='create_region'),
    path('profil/<int:pk>/create-region/create-miasto/', create_miasto.as_view(), name='create_miasto'),
    path('profil/<int:pk>/create-region/create-miasto/create-preferencje', create_preferencje.as_view(), name='create_preferencje'),
    path('profil/<int:pk>/update', ProfilUpdate.as_view(), name='update_profil')


]  