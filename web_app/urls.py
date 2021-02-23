from django.urls import path
from . import views
from .views import ProjectDetailView

urlpatterns = [
    path('', views.home, name='web_app-home'),
    path('about/', views.about, name='web_app-about'),
    path('<str:pk>/', ProjectDetailView.as_view(), name='project-details')
]
