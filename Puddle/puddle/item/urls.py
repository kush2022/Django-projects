from django.urls import path 
from . import views 

app_name = 'item'

urlpatterns = [
    path('', views.browse, name='browse'),
    path('detail<int:pk>/', views.detail, name='detail'),
    path('new-item/', views.new_item, name='new-item'),
    path('delete-item/<int:pk>/', views.delete_item, name='delete-item'),
    path('edit-item/<int:pk>/', views.edit_item, name='edit-item')

]