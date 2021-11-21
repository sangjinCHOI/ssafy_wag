from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('page/<int:page>/', views.index),
    path('<int:movie_pk>/', views.movie_detail),
    # path('recommended/', views.recommended, name='recommended'),
]