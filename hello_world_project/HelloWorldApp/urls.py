from django.urls import path
from .views import HelloWorldAppView

urlpatterns = [
    path('HelloWorldApp/', HelloWorldAppView)
]
