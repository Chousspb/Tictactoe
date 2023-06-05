from django.contrib import admin
from django.urls import path, include
from tictactoe.urls import tic_tac_urlpatterns
import root.views.index

from django.contrib.auth import views as auth_views
from accounts.views import register, user_login
logout = auth_views.LogoutView.as_view()
login = auth_views.LoginView.as_view()


urlpatterns = [
    path("", root.views.index.IndexView.as_view(), name='main'),
    path("admin/", admin.site.urls),
    path("tic-tac/", include(tic_tac_urlpatterns)),
    path('register/', register, name='register'),
    path('login/', user_login, name='login')
]
