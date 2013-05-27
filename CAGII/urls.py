from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

#import CAGII.notas.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CAGII.views.home', name='home'),
    # url(r'^CAGII/', include('CAGII.foo.urls')),
    # url(r'^$', 'notas.views.lista_de_notas', name='lista_de_notas'),
    url(r'^$', RedirectView.as_view(url='/lista/')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^lista/$', 'notas.views.lista_de_notas', name='lista_de_notas'),  
    url(r'^detalle/(?P<id>\d+)/$', 'notas.views.detalle_de_nota', name='detalle_de_nota'),  
    url(r'^crear/$', 'notas.views.crear_nota', name='crear_nota'),  
    url(r'^modificar/(?P<id>\d+)/$', 'notas.views.modificar_nota', name='modificar_nota'),  
    url(r'^borrar/(?P<id>\d+)/$', 'notas.views.borrar_nota', name='borrar_nota'),  
)
