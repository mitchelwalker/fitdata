from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from models import fitdata, weightdata
from datetime import date
import json

# Create your views here.


def home(request):
    return HttpResponse('Hello')

@login_required
def dashboard(request):
    username = request.user.username
    user = User.objects.get(username=username)
    return HttpResponse('Hello %s!' % user.first_name)


    
class dataStepsTrack(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(dataStepsTrack, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, username):
        return HttpResponse('Method Not Supported', status=405)

    def post(self, request, username):
        try:
            data = request.body
            data = json.loads(data)
        except:
            return HttpResponse("Error Processing Data", status=500)

        try:
            user = User.objects.get(username=username)
        except Exception as e:
            return HttpResponse("Unable to pull user, Error: %s" % e, status=500)
        
        try:
            if len(data) != 0:
                steps = data['steps']
                distance = data['distance']
                q1 = fitdata(distance=distance, steps=steps)
                q1.user = user
                q1.save()
                return HttpResponse(status=200)
            else:
                return HttpResponse(status=500)
        except Exception as e:
            return HttpResponse("Error adding data to DB. Error: %s " % e, status=500)


class dataWeightTrack(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(dataWeightTrack, self).dispatch(request, *args, **kwargs)

    def get(self, request, username):
        return HttpResponse('Method Not Supported', status=405)

    def post(self, request, username):
        try:
            data = request.body
            data = json.loads(data)
        except:
            return HttpResponse("Error Processing Data", status=500)

        try:
            user = User.objects.get(username=username)
        except Exception as e:
            return HttpResponse("Unable to pull user, Error: %s" % e, status=500)

        try:
            if len(data) != 0:
                weight = data['weight']
                q1 = weightdata(weight=weight)
                q1.user = user
                q1.save()
                return HttpResponse(status=200)
            else:
                return HttpResponse(status=500)
        except Exception as e:
            return HttpResponse("Error adding data to DB. Error: %s " % e, status=500)
