from django.http import HttpResponse
from MTV.models import Familia

# Create your views here.
def Mi_familia(request):
    Familiares= Familia.object.all()
    
    cadena_respuesta = ""
    for familiar in Familiares:
        cadena_respuesta += familiar.nombre + " / "
    
    return HttpResponse(cadena_respuesta)

