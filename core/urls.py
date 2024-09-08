from django.urls import path
from .views import UserCreateView, UserListView, UserUpdateView, UserDeleteView
from .views import ServiceCreateView, ServiceListView, ServiceUpdateView, ServiceDeleteView

urlpatterns = [
    # Rotas de Usuário
    path('users/', UserCreateView.as_view(), name='user_create'),
    path('users/list/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),

    # Rotas de Serviço
    path('services/', ServiceCreateView.as_view(), name='service_create'),
    path('services/list/', ServiceListView.as_view(), name='service_list'),
    path('services/<int:pk>/', ServiceUpdateView.as_view(), name='service_update'),
    path('services/<int:pk>/delete/', ServiceDeleteView.as_view(), name='service_delete'),
]
