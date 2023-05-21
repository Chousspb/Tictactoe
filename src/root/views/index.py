from django.http import HttpRequest
from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request: HttpRequest):

        return render(request, "root/templates/layout.html", {})
