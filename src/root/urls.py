
from django.contrib import admin
from django.urls import path, include
from tictactoe.urls import tic_tac_urlpatterns
import root.views.index

urlpatterns = [
    path("", root.views.index.IndexView.as_view()),
    path("admin/", admin.site.urls),
    # tic tac toe
    path("tic-tac/", include(tic_tac_urlpatterns))
    ]
