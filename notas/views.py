from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
from django.views.generic.create_update import create_object
from django.views.generic.create_update import update_object
from django.views.generic.create_update import delete_object
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse

from models import Nota


def lista_de_notas(request):
    dato = {}
    dato['notas']=Nota.objects.all().order_by('-ultima_modificacion')[:5]
    return render_to_response('lista.html',dato,context_instance=RequestContext(request))


def detalle_de_nota(request, id):
    dato = {}
    dato['nota'] = get_object_or_404(Nota, pk=id)
    return render_to_response('detalle.html',dato, context_instance=RequestContext(request))   


def crear_nota(request):
    
    return create_object(request,
        model=Nota,
        template_name='crear.html',
        post_save_redirect=reverse("lista_de_notas")
    )           

def borrar_nota(request, id):

    dato = {}
    dato['nota'] = get_object_or_404(Nota, pk=id)
    if request.method =='POST':
        dato['nota'].delete()
        return HttpResponseRedirect('/lista/')
    # else
    context = {'nota': dato}
    return render_to_response('borrar.html',context,context_instance=RequestContext(request))


def modificar_nota(request, id):
    
    return update_object(request,
        model=Nota,
        object_id=id,
        template_name='modificar.html',
        post_save_redirect=reverse("lista_de_notas")
    )         
