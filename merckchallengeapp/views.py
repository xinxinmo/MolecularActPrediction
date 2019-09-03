from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from .forms import PollForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render_to_response('index.html')

def inquiry(request, protein_id='', compound_id='', features=''):
    # if request.method == 'POST'
    # if the user provides the compound id

    # if the user provides the compound features
    return HttpResponse("inquiry page!")
#
# @staff_member_required
# def import(request):
#     if request.method == "POST":
#         form = DataInput(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             success = True
#             context = {"form": form, "success": success}
#             return render_to_response("imported.html", context,
#             context_instance=RequestContext(request))
#         else:
#             form = DataInput()
#             context = {"form": form}
#             return render_to_response("imported.html", context,
#             context_instance=RequestContext(request))
