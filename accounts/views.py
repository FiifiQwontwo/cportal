from django.contrib import messages, auth
from django.shortcuts import render, redirect
from .models import Account
from .forms import RegistrationForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url = 'accounts:login_url')
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']

            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name,
                                               phone=phone, email=email,
                                               username=username, password=password)
            user.save()
            current_site = get_current_site(request)
            mail_subject = "Accounts Activation"
            message = render_to_string('accounts/verification.html', {
                'user': user,
                'domian': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })

            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            messages.success(request, 'Sign up was successful, please complete your verification from your mail')
            return redirect('/accounts/login/?command=verification&email=' + email)
    else:
        form = RegistrationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('portal:home_page')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('accounts:login_url')

    return render(request, 'accounts/login.html')


@login_required(login_url = 'accounts:login_url')
def logout(request):
    auth.logout(request)
    messages.success(request, "You're logged out")
    return redirect('accounts:login_url')


@login_required(login_url = 'accounts:login_url')
def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesnotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'congratulation! your accounts is activated')
        return redirect('accounts:login_url')
    else:
        messages.error(request, "invalid activation link")
        return redirect('register')
    
