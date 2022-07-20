from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import ItemForm
from .models import Item
from django.template import loader


# Create your views here.
def index(request):
    item_list = Item.objects.all()
    context = {'item_list': item_list, }
    return render(request, 'food/index.html', context)


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'food/detail.html', context)


def add_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')

    context = {
        'form': form,
    }

    return render(request, 'food/item-form.html', context)

def edit_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')

    context = {
        'form': form,
        'item': item
    }

    return render(request, 'food/item-form.html', context)

def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {'item':item}
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request, 'food/delete.html', context)
