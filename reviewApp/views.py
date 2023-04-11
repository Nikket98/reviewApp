from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Issue,Contact

from django.conf import settings
from django.shortcuts import render
from django.shortcuts import render, redirect

from django.conf import settings


# Create your views here.
def home(request):
    return render(request, 'reviewApp/home.html', {'title': 'Welcome Page'})

def about(request):
    return render(request, 'reviewApp/about.html', {'title': 'About Us'})

def report(request):
    daily_report = {
        'issues': Issue.objects.all(),
        'title': 'Daily Reports'
    }

    return render(request, 'reviewApp/report.html', daily_report)

def contact(request):
    return render(request, 'reviewApp/contact.html', {'title': 'Contact Us'})

class PostListView(ListView):
    model = Issue
    template_name = 'reviewApp/report.html'
    context_object_name = 'issues'
    ordering = ['-date_submitted']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context.update({'title': 'List of Issues'})
        return context

class PostDetailView(DetailView):
    model = Issue

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    fields = ['type', 'room', 'details']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Issue
    fields = ['type', 'room', 'details']

    def test_func(self):
        issue = self.get_object()
        return self.request.user == issue.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Issue
    success_url = '/report'

    def test_func(self):
        issue = self.get_object()
        return self.request.user == issue.author

class UserPostListView(ListView):
    model = Issue
    template_name = 'reviewApp/user_issues.html'
    context_object_name = 'issues'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User,
        username = self.kwargs.get('username'))
        return Issue.objects.filter(author=user).order_by('-date_submitted')
    
    

def contact_view(request):
    if request.method == 'POST':
        print("Form submitted.")
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Save the submitted data as a Contact model instance
        contact = Contact(name=name, email=email, message=message)
        contact.save()

        return redirect('reviewApp-success') # Redirect to a success page
    return render(request, 'reviewApp/contact.html', {'title': 'Contact Us'})

def success_view(request):
    return render(request, 'reviewApp/success.html', {'title': 'Success'})



