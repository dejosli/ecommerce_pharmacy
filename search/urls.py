from django.urls import path
from search.views import (
    SearchProductView,
    SearchCategoryView,
)

app_name = 'search'

urlpatterns = [
    path('s/', SearchProductView.as_view(), name='query'),
    path('category/<category>/', SearchCategoryView.as_view(), name='item_list_by_category'),
]
