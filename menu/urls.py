from . import views
from django.urls import path

urlpatterns = [
  path('', views.MenuList.as_view(), name='menu'),
  path('<slug:slug>/', views.menu_detail, name='menu_detail'),
  path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
  path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete')
]