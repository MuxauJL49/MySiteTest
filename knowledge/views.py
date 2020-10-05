from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def knowledgeHome(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'knowledge/knowledgeHome.html', {'news' : news})


class NewDetailView(DetailView):
    model = Articles
    template_name = 'knowledge/details_view.html'
    context_object_name = 'article'

class NewUpadetView(UpdateView):
    model = Articles
    template_name = 'knowledge/create.html'

    form_class = ArticlesForm

class NewDeleteView(DeleteView):
    model = Articles
    success_url = "/knowledge/"
    template_name = 'knowledge/delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверная форма'
    form = ArticlesForm()

    data = {
        'form' : form,
        'error' : error
    }
    return render(request, 'knowledge/create.html', data)