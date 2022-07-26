from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('<int:pk>/', views.ItemDetailView.as_view(), name='detail'),
    path("add/", views.ItemCreateView.as_view(), name="add_item"),
    path("edit/<int:item_id>/", views.edit_item, name="edit_item"),
    path("delete/<int:item_id>/", views.delete_item, name='delete_item')
]
