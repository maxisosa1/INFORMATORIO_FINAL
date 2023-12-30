from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Noticia, Categoria, Comentario

from django.urls import reverse_lazy


def Listar_Noticias(request):
    contexto = {}

    id_categoria = request.GET.get('id', None)
    filtro = request.GET.get('filtro', None)

    if id_categoria:
        n = Noticia.objects.filter(categoria_noticia=id_categoria)
    else:
        n = Noticia.objects.all()  # RETORNA UNA LISTA DE OBJETOS

    if filtro:
        if filtro == 'antiguedad_asc':
            n = n.order_by('fecha')
        elif filtro == 'antiguedad_desc':
            n = n.order_by('-fecha')
        elif filtro == 'alfabetico_asc':
            n = n.order_by('titulo')
        elif filtro == 'alfabetico_desc':
            n = n.order_by('-titulo')

    contexto['noticias'] = n

    cat = Categoria.objects.all().order_by('nombre')
    contexto['categorias'] = cat

    return render(request, 'noticias/listar.html', contexto)


def Detalle_Noticias(request, pk):
	contexto = {}

	n = Noticia.objects.get(pk = pk) #RETORNA SOLO UN OBEJTO
	contexto['noticia'] = n

	c = Comentario.objects.filter(noticia = n)
	contexto['comentarios'] = c

	return render(request, 'noticias/detalle.html',contexto)


@login_required
def Comentar_Noticia(request):

	com = request.POST.get('comentario',None)
	usu = request.user
	noti = request.POST.get('id_noticia', None)# OBTENGO LA PK
	noticia = Noticia.objects.get(pk = noti) #BUSCO LA NOTICIA CON ESA PK
	coment = Comentario.objects.create(usuario = usu, noticia = noticia, texto = com)

	return redirect(reverse_lazy('noticias:detalle', kwargs={'pk': noti}))




@login_required
def borrar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, pk=comentario_id)
    
    if request.user == comentario.usuario or request.user.groups.filter(name='Colaborador').exists():
        comentario.delete()
        return redirect('noticias:detalle', pk=comentario.noticia.pk)
    else:
        return render(request, "usuarios/login.html")