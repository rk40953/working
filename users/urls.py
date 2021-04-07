from django.conf.urls import url
from rest_framework_simplejwt import views as jwt_views
from django.urls import path
from users import views

urlpatterns = [
    url(r'^login/', views.Login.as_view(),name='login_user'),
    url(r'^emp/',views.Emps.as_view(),name='to make operations'),
    url(r'^register/',views.Register.as_view(),name='Register'),
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]