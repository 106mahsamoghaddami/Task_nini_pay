from django.urls import path
from . import views
urlpatterns = [

    path('',views.Shampoolists.as_view(),name='detail' ),
    # path('<int:brand_id>/', views.detail_product, name='product-detail')



]