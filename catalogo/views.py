from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Jogo
from .forms import JogoForm, ReviewForm


# Create your views here.

def pagina_inicial(request):
    em_destaque = Jogo.objects.filter(
        destaque=True).first()  # em caso de teste que tinham varios em destauqem o que aparecia fiacva aleatorio
    jogos = Jogo.objects.all()
    if em_destaque:
        jogos = jogos.exclude(pk=em_destaque.pk)

    context = {'em_destaque': em_destaque, 'jogos': jogos}

    return render(request, 'catalogo/index.html', context)

def detalhes(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    reviews = jogo.review_set.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.jogo = jogo
            review.save()
            return redirect('catalogo:detalhe_jogo', pk=jogo.pk)
    else:
        form = ReviewForm()

    context = {'jogo': jogo, 'reviews': reviews, 'form': form}
    return render(request, 'catalogo/detalhe_jogo.html', context)

@login_required
def dashboard(request):
    jogos = Jogo.objects.all().order_by('nome')
    return render(request, 'catalogo/dashboard.html', {'jogos': jogos})

@login_required
def novo_jogo(request):
    if request.method == 'POST':
        form = JogoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('catalogo:home')
    else:
        form = JogoForm()

    return render(request, 'catalogo/jogo_form.html', {'form': form, 'titulo': 'Criar jogo'})

@login_required
def editar_jogo(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    if request.method == 'POST':
        form = JogoForm(request.POST, request.FILES, instance=jogo)
        if form.is_valid():
            form.save()
            return redirect('catalogo:home')
    else:
        form = JogoForm(instance=jogo)

    return render(request, 'catalogo/jogo_form.html', {'form': form, 'titulo': 'Editar jogo'})

@login_required
def eliminar_jogo(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    if request.method == 'POST':
        jogo.delete()
        return redirect('catalogo:home')
    return render(request, 'catalogo/jogo_confirmar_exclusao.html', {'jogo': jogo})
