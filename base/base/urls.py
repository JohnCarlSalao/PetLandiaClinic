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
from core.features.versions.v1p0.display_parents.views.display_parents_views import DisplayParentViews, DisplayParentDetailViews
from core.features.versions.v1p0.display_pets.views.display_pets_views import DisplayPetViews, DisplayPetDetailViews
from core.features.versions.v1p0.edit_parents.views.edit_parent_details_views import EditParentViews
from core.features.versions.v1p0.edit_pets.views.edit_pets_details_views import EditPetsDetailsViews
from core.features.versions.v1p0.delete_parents.views.delete_parents_views import DeleteParentsViews
from core.features.versions.v1p0.delete_pets.views.delete_pets_views import DeletePetsViews
from core.features.versions.v1p0.create_medical_history.views.create_medical_history_views import CreateMedicalHistoryViews
from core.features.versions.v1p0.display_medical_history.views.display_medical_records import DisplayMedicalRecordsIndivViews, DisplayMedicalRecordsViews
from core.features.versions.v1p0.delete_medical_history.views.delete_medical_history import DeleteMedicalRecordsViews
from core.features.versions.v1p0.edit_medical_history.views.edit_medical_history_views import EditMedicalRecordViews
from core.features.versions.v1p0.display_pet_with_their_medical_history.views.display_pet_with_their_medical_history_views import MedicalHistoryByPetIDView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1p0/create_pets/', CreatePetsViews.as_view(), name ='create_pets_view'),
    path('v1p0/create_parents/', CreateParentViews.as_view(), name ='create_pets_view'),
    path('v1p0/display_parent/', DisplayParentViews.as_view(), name = 'display_parent'),
    path ('v1p0/display_parent/<pk>/', DisplayParentDetailViews.as_view(), name = 'display_parent_by_id'),
    path ('v1p0/display_pet/<pk>/', DisplayPetDetailViews.as_view(), name = 'display_pet_by_id'),
    path ('v1p0/display_pet/', DisplayPetViews.as_view(), name = 'display_pet'),
    path ('v1p0/edit_parent/<pk>/', EditParentViews.as_view(), name = 'edit_parent_view'),
    path ('v1p0/edit_pet/<pk>/',EditPetsDetailsViews.as_view(), name = 'edit_pets_view'),
    path ('v1p0/delete_parent/<pk>/', DeleteParentsViews.as_view(), name = 'delete_parent_view'),
    path ('v1p0/delete_pet/<pk>/',DeletePetsViews.as_view(), name = 'delete_pets_view'),
    path ('v1p0/create_medical_history/', CreateMedicalHistoryViews.as_view(), name = 'create_medical_history_views'),
    path ('v1p0/display_medical_history/', DisplayMedicalRecordsViews.as_view(), name = 'display_medical_history'),
    path ('v1p0/display_medical_history/<pk>/', DisplayMedicalRecordsIndivViews.as_view(),  name = 'display_medical_history_indiv'),
    path ('v1p0/delete_medical_history/<pk>/', DeleteMedicalRecordsViews.as_view(),  name = 'display_medical_history_indiv'),
    path ('v1p0/edit_medical_history/<pk>/', EditMedicalRecordViews.as_view(),  name = 'edit_medical_history_indiv'),
    path ('v1p0/display_medical_history/pet/<pet_id>/', MedicalHistoryByPetIDView.as_view(),  name = 'display_medical_history_pet'),
]


