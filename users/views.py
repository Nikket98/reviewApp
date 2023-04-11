from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .forms import ForgotPasswordForm
from django.contrib.auth.forms import SetPasswordForm
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            profile = user.profile
            profile.security_question = form.cleaned_data['security_question']
            profile.security_answer = form.cleaned_data['security_answer']
            profile.save()
            messages.success(
                request, f'Your account has been created! Now you can login!')

            return redirect('login')
        else:
            messages.warning(request, f'Invalid input: {form.errors}')

            return redirect('reviewApp-home')
    else:
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form, 'title': 'Register'})


def reset_password(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your password has been reset. You can now log in.')
            return redirect('login')
    else:
        form = SetPasswordForm(user)
    return render(request, 'users/reset_password.html', {'form': form})


def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                profile = user.profile
                security_question = profile.security_question
                return render(request, 'users/answer_security_question.html', {
                    'user_id': user.id,
                    'security_question': security_question,
                })
            except User.DoesNotExist:
                messages.error(request, 'Email not found.')
        else:
            messages.error(request, 'Invalid input.')
    else:
        form = ForgotPasswordForm()
    return render(request, 'users/forgot_password.html', {'form': form})


def check_security_answer(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        profile = user.profile
        answer = request.POST['security_answer']
        if profile.security_answer.lower() == answer.lower():
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            return redirect(reverse('users:password_reset_confirm', kwargs={'uidb64': uid, 'token': token}))





        else:
            messages.error(request, 'Incorrect answer. Please try again.')
            return redirect(reverse('users:forgot_password'))
    else:
        return HttpResponseNotAllowed(['POST'])
   


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
