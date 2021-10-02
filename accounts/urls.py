from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('signup/', TemplateView.as_view(template_name='home.html'), 'signup')
]