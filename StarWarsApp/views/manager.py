from django.shortcuts import render
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "manager/index.html"
    login_url = "accounts/login"
    raise_exception = False
