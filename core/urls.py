from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    filtros,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    posts,
    post_id,
    comentario_id,
    eliminarComentarios
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('filtros/', filtros, name='filtros'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('comment/', posts, name='posts'),
    path('post_id/<int:pk>/', post_id, name='post_id'),
    path('comentario_id/<int:pk>/', comentario_id, name='comentario_id'),
    path('delete/<int:id>/', eliminarComentarios, name='eliminar_Comentarios')
]
