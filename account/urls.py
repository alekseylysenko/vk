from django.urls import path, include
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('/account', include('django.contrib.auth.urls'))
]