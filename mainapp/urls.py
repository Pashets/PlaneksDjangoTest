from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='mainapp'),
    path('new', views.new_schema, name='new'),
    path('<int:schema_id>', views.data_sets_schema, name='detail'),
    path('download/<str:file_name>', views.download, name='download'),
]
