from django.contrib import admin
from django.urls import path, include
from .views import callHelloWorld, HelloWorldClass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('HelloWorld/', callHelloWorld),
    path('HelloWorldHtml/', HelloWorldClass.as_view()),
    path('App/', include('HelloWorldApp.urls'))
]
