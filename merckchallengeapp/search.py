from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import Compound, Protein, ProteinCompound
from .mlmodels import randomForrestModel

def searchForm(request):
    return render_to_response('search_form.html')

def search(request):
    request.encoding = 'utf-8'
    if 'c' in request.GET and request.GET['c'] and \
       'p' in request.GET and request.GET['p']:
        # message = 'you are searching ' + request.GET['c']
        # message = 'You are searching compound {} and protein {}'.format(request.GET['c'], request.GET['p'])
        e = ProteinCompound.objects.get(protein_id=request.GET['p'], compound_id=request.GET['c'])
        message = '{:.5f}'.format(e.activity)
    else:
        message = 'Please provide valid input'
    return HttpResponse(message)

def inquiryForm(request):
    return render_to_response('inquiry_form.html')

def inquiry(request):
    request.encoding = 'utf-8'
    if 'p' in request.GET and request.GET['p'] and \
       'feature' in request.GET and request.GET['feature']:
       feature = request.GET['feature']
       Y = randomForrestModel(feature, 49)
       print("Y = ", Y)
       if Y == -1:
           message = "Please input 50 features!"
       else:
           message = 'You are inquiry protein {} and compound with feature {}, and the activity is {}'.format(request.GET['p'], request.GET['feature'], Y)

    else:
        message = 'Please provide valid input'
    return HttpResponse(message)

def postForm(request):
    return render_to_response('post_form.html')
