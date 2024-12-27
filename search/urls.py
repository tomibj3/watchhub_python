from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.home_view, name='home'),

    # Detalles de una serie/película
    path('<int:series_movie_id>/', views.search_detail, name='search_detail'),

    # Agregar una nueva serie/película
    path('add/', views.add_series_movie, name='add_series_movie'),

    # Eliminar una serie/película existente
    path('<int:series_movie_id>/delete/', views.delete_series_movie, name='delete_series_movie'),

    # Página "Acerca de"
    path('about/', views.about, name='about'),

    # Lista de series/películas
    path('list/', views.search_list, name='search_list'),
]