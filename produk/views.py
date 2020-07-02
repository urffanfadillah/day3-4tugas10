from django.shortcuts import render, redirect, get_object_or_404
from .models import Produk
from .forms import ProdukForm

# Create your views here.
def index(request):
    template    = 'index.html'
    context     = {
        'produk':Produk.objects.all(),
    }
    return render(request, template, context)

def tambah_produk(request):
    template    = 'tambah_produk.html'
    form        = ProdukForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        form    = ProdukForm()
    context     = {
        'form':form,
    }
    return render(request, template, context)

def update_produk(request, produk_id):
    template    = 'tambah_produk.html'
    obj         = get_object_or_404(Produk, id=produk_id)
    form        = ProdukForm(request.POST or None, instance=obj)
    context     = {
        'form': form,
    }
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        form    = ProdukForm()
    return render(request, template, context)

def delete_produk(request, produk_id):
    obj         = get_object_or_404(Produk, id=produk_id)
    obj.delete()
    return redirect('/')