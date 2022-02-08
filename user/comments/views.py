# from django.shortcuts import render
# from .forms import EmailPostForm
#
#
# def post_share(request, post_id):
#     post = get_object_or_404(Post, id=post_id, status='published')
#     if request.method == 'POST':
#         # Form was submitted
#         form = EmailPostForm(request.POST)
#         if form.is_valid():
#             # Form fields passed validation
#             cd = form.cleaned_data
#             # ... send email
#     else:
#         form = EmailPostForm()
#     return render(request, 'blog/post/share.html', {'post': post,
#     'form': form})


from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from ..cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                             product=item['product'],
                             price=item['price'],
                             quantity=item['quantity'])
            cart.clear()
            return render(request,
                          'diplom/autontification/../../templates/diplom/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'diplom/autontification/../../templates/diplom/order/create.html',
                  {'cart': cart, 'form': form})