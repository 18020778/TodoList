from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('add_todo',views.add_todo, name='add_todo'),
    path('delete', views.delete, name='delete'),
    path('sortData', views.sortData, name='sortData'),
    path('searchData', views.searchData, name='searchData'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update')
]