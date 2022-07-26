from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import ItemForm
from .models import Item
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


# Create your views here.
def index(request):
    item_list = Item.objects.all()
    context = {'item_list': item_list, }
    return render(request, 'food/index.html', context)


class IndexListView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'food/detail.html', context)


class ItemDetailView(DetailView):
    model = Item
    template_name = 'food/detail.html'


def add_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')

    context = {
        'form': form,
    }

    return render(request, 'food/item-form.html', context)


class ItemCreateView(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)

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
    context = {'item': item}
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request, 'food/delete.html', context)
