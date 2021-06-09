from django.urls import path
from . import views
from .views import ContactCreateView

urlpatterns = [
    path('', views.home, name='web_app-home'),
    path('<str:pk>/', views.project_detail, name='project-details'),
    path('contact/', ContactCreateView.as_view(), name='web_app-contact'),
    # path('<str:pk>/', ProjectDetailView.as_view(), name='project-details'),
]
