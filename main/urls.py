from django.urls import path, re_path
from main import views

urlpatterns = [

    # The home page
    path('', views.HomeView, name='home'),
    path('pets/', views.PetView, name='pets'),
    path('owners/', views.OwnerView, name='owners'),

    path('addPet/', views.PetAddView, name='pet-add'),
    path('addOwner/', views.OwnerAddView, name='owner-add'),

    path('petDetail/<int:pk>', views.PetDetailView, name='pet-detail'),
    path('petUpdate/<int:pk>', views.PetUpdateView, name='pet-update'),
    path('petDelete/<int:pk>', views.PetDeleteView, name='pet-delete'),

    path('ownerDetail/<int:pk>', views.OwnerDetailView, name='owner-detail'),
    path('ownerUpdate/<int:pk>', views.OwnerUpdateView, name='owner-update'),
    path('ownerDelete/<int:pk>', views.OwnerDeleteView, name='owner-delete'),

    path('search/', views.SearchView, name='search'),

]