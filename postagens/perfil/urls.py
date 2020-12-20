from django.urls import path
from perfil import views

urlpatterns = [
    path('perfil/', views.perfil_list),
    path('prefil/<int:pk>/', views.perfil_detail),
    path('loadperfil/', views.loadperfil),
    path('loadpost/', views.loadpost),
    path('loadcomment/', views.loadcomment),
    path('postperfil/',views.postperfil_list),
    path('postperfil/<int:pk>/', views.postperfil_detail),
    path('postcomment/',views.postcomment_list),
    path('postcomment/<int:pk>/', views.postcomment_detail),
]
