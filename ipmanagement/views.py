# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template.context_processors import csrf

from common.mymako import render_mako_context
from netaddr import  *

from ipmanagement.models import IP_Address,IP_Range


# Create your views here.




class Index(View):

    def get(self, request, *args, **kwargs):
        return render_mako_context(request, '/ip_management/index.html')

class Ip_range(View):
    def get(self, request, *args, **kwargs):

        path =  request.path
        if path == '/ip_range_list/':
            ip_range_all = IP_Range.objects.all()
            print ip_range_all[0].start_ip
            return render_mako_context(request, '/ip_management/ip_range_list.html',{"ip_range_all":ip_range_all})
        elif path == '/ip_range_add/':
            return render_mako_context(request, '/ip_management/ip_range_add.html')

    def post(self,request, *args, **kwargs):
        start_ip = request.POST.get("start_ip")
        end_ip = request.POST.get("end_ip")
        des = request.POST.get("des")
        network = request.POST.get("network")
        netmask = request.POST.get("netmask")
        print start_ip,end_ip,des,network,netmask
        ip_list = list(iter_iprange(start_ip, end_ip))
        print len(ip_list)
        obj = IP_Range(start_ip=start_ip,end_ip=end_ip,des=des,network=network,netmask=netmask,use_ip=0,left_ip=len(ip_list))
        obj.save()
        for ip in ip_list:
            print ip
            ip_obj = IP_Address(ip=str(ip),gateway=str(ip_list[1]),network=network,netmask=netmask,state=u"未分配",)
            ip_obj.save()
        return render_mako_context(request, '/ip_management/ip_range_add.html')





def all_ip_list(request):
    ip_list = IP_Address.objects.all()
    len_list = range(0,len(ip_list))
    return render_mako_context(request, '/ip_management/all_ip_list.html', {"ip_list":ip_list,"len_list":len_list})

def ip_use_list(request):
    return render_mako_context(request, '/ip_management/ip_use_list.html')

def ip_unuse_list(request):
    return render_mako_context(request, '/ip_management/ip_unuse_list.html')

def ip_range_list(request):
    return render_mako_context(request, '/ip_management/ip_range_list.html')

def ip_range_add(request):
    return render_mako_context(request, '/ip_management/ip_range_add.html')