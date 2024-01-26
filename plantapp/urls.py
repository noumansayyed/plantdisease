from django.urls import path
from . import views
from .views import GetUserInfo

urlpatterns = [
    # Other URL patterns
    path('api_create_leaf/', views.create_leaf, name='api_create_leaf'), 
    path('leaf_data/', views.leaf_data_view, name='leaf_data'),
    path('register_user/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login'),
    
    path('predict_disease/', views.predict_disease, name='predict_disease'),

    path('api/disease/<int:id>/', views.disease_detail),
    path('api/get_user_info/<str:unique_id>/', GetUserInfo.as_view(), name='get_user_info'),
    path('update_user_info/<str:unique_id>/', views.UpdateUserInfo.as_view(), name='update_user_info'),
]

