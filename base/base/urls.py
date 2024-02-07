"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from core.features.versions.v1p0.create_parents.views.create_parents_views import CreateParentViews
from core.features.versions.v1p0.create_pets.views.create_pets_views import CreatePetsViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_pets/', CreatePetsViews.as_view(), name ='create_pets_view'),
    path('create_parents/', CreateParentViews.as_view(), name ='create_pets_view')
]
