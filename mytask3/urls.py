"""mytask3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from polls.views import PersonListView,PersonDetailView,PersonUpdateView,PersonDeleteView,PersonCreateView,Registration
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', PersonListView.as_view(), name='list'),
    path('api/<int:person_id>/detail/', PersonDetailView.as_view(), name='api-detail'),
    path('api/<int:person_id>/update/', PersonUpdateView.as_view(), name='api-update'),
    path('api/<int:person_id>/delete/', PersonDeleteView.as_view(), name='api-delete'),
    path('api/create/', PersonCreateView.as_view(), name='api-create'),
    path('register/',Registration.as_view(),name='register'),
    path('login/',obtain_jwt_token,name="login"),



]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)