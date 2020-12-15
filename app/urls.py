from django.urls import path

from app.views import index
from app.views.animals import add_animal, edit_animal, delete_animal, details_animal, cure_animal

urlpatterns = [
    # Index page
    path('', index.index, name='index'),

    # Animals pages
    path('create/', add_animal, name='add-animal'),
    path('edit/<int:pk>', edit_animal, name='edit-animal'),
    path('delete/<int:pk>', delete_animal, name='delete-animal'),
    path('details/<int:pk>', details_animal, name='details-animal'),
    path('cure/<int:pk>', cure_animal, name='cure-animal'),
]
