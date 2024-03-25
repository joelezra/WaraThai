from . import views
from django.urls import path

urlpatterns = [
  path('', views.MenuList.as_view(), name='menu'),
  path('<int:pk>/', views.menu_detail, name='menu_detail'),
  path('<int:pk>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
  path('<int:pk>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete')
]