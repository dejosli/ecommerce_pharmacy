from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView
from core.models import Item

# Create your views here.
class SearchView(ListView):
    template_name = "layout/search.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        if query is not None:
            lookup = (Q(book_title__icontains=query) |
                      Q(author__icontains=query) |
                      Q(publication__icontains=query) |
                      Q(subject__icontains=query))
            return Book.objects.filter(lookup)
        return Book.objects.none()