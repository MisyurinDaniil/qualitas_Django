from django.urls import path

from . import views


urlpatterns = [
    path('product/<slug:productItemSlug>', views.ProductDetail.as_view(), name='product'),
    path('category/<slug:productCategorySlug>', views.ProductsInCategoryList.as_view(), name='category'),
    path('product/addReview/<int:pk>', views.AddReview.as_view(), name='add_review'),
]
