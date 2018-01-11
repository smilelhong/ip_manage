from django.shortcuts import render
from django.http import HttpResponse
from common.mymako import render_mako_context


# Create your views here.
def index(request):
    return render_mako_context(request, '/ip_management/index.html')


def all_ip_list(request):
    return render_mako_context(request, '/ip_management/all_ip_list.html')

