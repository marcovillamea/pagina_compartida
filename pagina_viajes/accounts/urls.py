from django.urls import path
from accounts.views import login_request, register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/",login_request, name = "login"),
    path("signup/",register,name="signup"),
    path('logout/', LogoutView.as_view(template_name = 'accounts/logout.html'), name='logout'),
]