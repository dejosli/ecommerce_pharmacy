from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views.generic import ListView
from core.models import Item, Category

# Create your views here.


class SearchProductView(ListView):
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(
            *args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        if query is not None:
            return Item.objects.search(query)
        return Item.objects.featured()


class SearchCategoryView(ListView):

    template_name = "home.html"

    def get_queryset(self):
        model = Item

        self.category = get_object_or_404(
            Category, name=self.kwargs['category'])
        return Item.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):

        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['category'] = self.category
        return context
