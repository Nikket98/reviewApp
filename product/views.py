from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Review
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, DeleteView
from .forms import ReviewForm, ReviewUpdateForm
from django.urls import reverse_lazy

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.product = product
            review.save()
            return redirect('product-detail', pk=product.pk)
    else:
        form = ReviewForm()

    return render(request, 'product/product_detail.html', {'product': product, 'reviews': reviews, 'form': form})


def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'product/review_detail.html', {'review': review})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})



class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewUpdateForm
    template_name = 'product/review_update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.author

    def get_success_url(self):
        return reverse_lazy('product-detail', kwargs={'pk': self.object.product.pk})


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = 'product/review_confirm_delete.html'
    
    

    def get_success_url(self):
        return reverse_lazy('product-detail', kwargs={'pk': self.object.product.pk})

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.author