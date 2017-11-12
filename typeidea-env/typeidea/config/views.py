from django.shortcuts import render
from django.views.generic import ListView
from .models import Link


class LinkView(ListView):
    queryset = Link.objects.filter(status=1)
    template_name = 'config/link.html'
    context_object_name = 'links'


    

