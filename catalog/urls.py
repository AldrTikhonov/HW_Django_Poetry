from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView, UnpublishedProductView, CategoryListView, ProductsByCategoryView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="products_list"),
    path("products/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="products_detail"),
    path("products/create/", ProductCreateView.as_view(), name="products_create"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="products_update"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="products_delete"),
    path(
        "product/un_published_product_views/<int:product_id>/",
        UnpublishedProductView.as_view(),
        name="un_published_product_view"
    ),
    path("category/", CategoryListView.as_view(), name="category_list"),
    path("category/<int:pk>/", ProductsByCategoryView.as_view(), name="products_by_category"),
]
