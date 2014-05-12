from django.shortcuts import render
from django.template import Context

from ads.models import Elemento
# Create your views here.


def index(request):
    """ Construivr un metodo que sea la vista principal de la aplicacion
    ads, el objetivo del metodo es mostrar todos los item de elementos."""

    elementos = Elemento.objects.all()
    context = Contex({'titulo': 'ADS site', 'elementos': elementos})
    return render_to_response('ads/index.html', context,
            context_instance=RequestContext(request))



