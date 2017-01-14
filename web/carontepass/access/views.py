from django.shortcuts import render
from rest_framework import generics
from .models import Device, Log, SecurityNode
from .serializers import DeviceResultSerializer
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from graphos.renderers import flot, gchart
from graphos.sources.simple import SimpleDataSource

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


# Create your views here.

class DeviceIDList(generics.ListAPIView):

    serializer_class = DeviceResultSerializer

    def get_queryset(self, **kwargs):

        code_id = self.kwargs['code']
        Device.check_exists_device(code_id)
        
        return Device.objects.filter(code=code_id)

    def get_serializer_context(self):
        return {'node_id': self.kwargs['node']}
        
@login_required(login_url='/')
def homepage(request):
    users_count = User.objects.count()
    users_in_count = Log.listUsersCount()
    return render(request, 'access/index.html', {'users_count': users_count, 'users_in_count': users_in_count})


@login_required(login_url='/')
def personal_info(request):
    return render(request, 'access/info.html')


@login_required(login_url='/')
def device_info(request):
    device_list_user = Device.objects.filter(user=User).all()
    return render(request, 'access/devicelist.html', {'device_list_user': device_list_user})
    

@login_required(login_url='/')
def global_charts(request):
    
    qs = Log.objects.all()
    week = [qs.filter(ts_input__week_day=i).count() for i in range(7)]
    
    data =  [
        ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        week
    ]

    #data_source = ModelDataSource(queryset, fields=['year', 'sales'])

    chart = gchart.ColumnChart(SimpleDataSource(data=data), html_id="line_chart")
    
    return render(request, 'access/global_charts.html', {'chart': chart } )
    
            
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })
    
    
    
    
    