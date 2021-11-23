from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list_create),
    path('<int:article_pk>/', views.article_detail_update_delete),
    path('<int:article_pk>/comment/', views.comment_list_create),
    path('<int:article_pk>/comment/<int:comment_pk>/', views.comment_delete),
    path('<int:article_pk>/likes/', views.article_likes),
    path('<int:article_pk>/comment/<int:comment_pk>/likes/', views.comment_likes),
    path('search/<keyword>/', views.search)

]
