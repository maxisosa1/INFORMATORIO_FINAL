from django.shortcuts import render
from apps.noticias.models import Noticia

#request 'es un diccionario que continuamente se va pasando entre el navegador y el servidor'

def Home(request):

	noticias = Noticia.objects.all().order_by("fecha")[:3]

	return render(request, 't_home.html', {"noticias" : noticias})


def Nosotros(request):

	return render(request, 't_nosotros.html')