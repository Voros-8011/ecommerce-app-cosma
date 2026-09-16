from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from products.models import Product
from .models import CartItem
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from accounts.customer import CustomerRequiredMixin
# Create your views here.


@login_required
def increase_quantity(request, item_id):

    if request.user.role != 'customer':
        return redirect('eccom_home:main')

    cart_item = get_object_or_404(
        CartItem,
        id=item_id,
        user=request.user
    )

    cart_item.quantity += 1
    cart_item.save()

    return redirect('cart:cart')


@login_required
def decrease_quantity(request, item_id):

    if request.user.role != 'customer':
        return redirect('eccom_home:main')

    cart_item = get_object_or_404(
        CartItem,
        id=item_id,
        user=request.user
    )

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart:cart')




@login_required
def add_to_cart(req,product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=req.user, product=product, defaults={'quantity': 1})
    if req.user.role != 'customer':
        return redirect('eccom_home:main')
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('eccom_home:main')



@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if request.user.role != 'customer':
     return redirect('eccom_home:main')
    return render(request, 'cart.html', {
        'cart_items': cart_items
    })


class RemoveFromCartView (CustomerRequiredMixin, DeleteView):
    model = CartItem
    template_name = 'remove_from_cart.html'
    success_url = reverse_lazy('cart:cart')

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)
