from django.shortcuts import render,render_to_response, RequestContext, HttpResponseRedirect
#from django.template import RequestContext
from django.contrib import messages
from .forms import SignUpForm

def index(request):
   return render_to_response("index.html",
                             locals(),
                             context_instance=RequestContext(request)
                             )
def home(request):
   form =SignUpForm(request.POST or None)
   
   if form.is_valid():
      save_it =form.save(commit=False)
      save_it.save()
      messages.success(request,'Welcome to NSDI Ethiopia')
      return HttpResponseRedirect('/join/')
   return render_to_response("post_list.html",
                             locals(),
                             context_instance=RequestContext(request)
                             )
def join(request):
   return render_to_response("join.html",
                             locals(),
                             context_instance=RequestContext(request)
                             )
def layer(request):
   return render_to_response("layer.html",
                             locals(),
                             context_instance=RequestContext(request)
                             )



# Create your views here.
