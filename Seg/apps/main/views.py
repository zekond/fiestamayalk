from django.template import RequestContext
from django.shortcuts import render_to_response
from Seg.apps.main.models import Mattress, Youth, Diningroom, Bedroom, Livingroom, Category

def index_view(request):

    template = "home.html"
    return render_to_response(template, context_instance=RequestContext(request, locals()))

def contact_view(request):

    template = "contact.html"
    return render_to_response(template, context_instance=RequestContext(request, locals()))

def specials_view(request):

    template = "bedroom.html"
    return render_to_response(template, context_instance=RequestContext(request, locals()))

