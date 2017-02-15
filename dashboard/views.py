from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from models import fitdata
from datetime import date
import json

# Create your views here.


def dashboard(request):
    return HttpResponse('Hello')


    
class dataTrack(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(dataTrack, self).dispatch(request, *args, **kwargs)
    
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
