from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from models import fitdata

# Create your views here.


def dashboard(request):
    return HttpResponse('Hello')
    
class dataTrack(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(dataTrack, self).dispatch(request, *args, **kwargs)
    
    def get(self, request):
        return HttpResponse('Method Not Supported', status=405)

    def post(self, request):
        try:
            data = request.body
        except:
            return HttpResponse("Error Processing Data", status=500)
        
        try:
            if len(data) != 0:
                date = data['date']
                steps = data['steps']
                distance = data['distance']
                q1 = fitdata(distance=distance, steps=steps, date=date)
                q1.save()
                return HttpResponse(status=200)
            else:
                return HttpResponse(status=500)
        except Exception as e:
            return HttpResponse("Error adding data to DB. Error: %s " % e, status=500)
