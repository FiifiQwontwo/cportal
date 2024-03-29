from django.contrib import messages, auth
from django.shortcuts import render, redirect, get_object_or_404
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
from django.contrib.auth import authenticate


# Create your views here.
@login_required(login_url='accounts:login_url')
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
            user = Account.objects.create_user(last_name=last_name,
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


# def login(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#
#         user = auth.authenticate(email=email, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('portal:home_page')
#         else:
#             messages.error(request, "Invalid Credentials")
#             return redirect('accounts:login_url')
#
#     return render(request, 'accounts/login.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('portal:home_page')

    return render(request, 'accounts/login.html')


@login_required(login_url='accounts:login_url')
def logout(request):
    auth.logout(request)
    messages.success(request, "You're logged out")
    return redirect('accounts:login_url')


@login_required(login_url='accounts:login_url')
def activate(request, uidb64, token):
    user = get_object_or_404(Account, pk=urlsafe_base64_decode(uidb64).decode())
    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated.')
        return redirect('accounts:login_url')
    else:
        messages.error(request, "Invalid activation link.")
        return redirect('register')
    # return HttpResponse('ok')


#
#
#
def forgetpassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)

            current_site = get_current_site(request)
            mail_subject = "Accounts Reset"
            message = render_to_string('accounts/reset_verification.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })

            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, "password reset email has been sent to your mail")
            return redirect('accounts:login_url')

        else:
            messages.error(request, 'Accounts Doesnot Exist')
            return redirect('accounts:forgotpassword_url')

    return render(request, 'accounts/forgetpasswords.html')


def resetpasswordValiate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesnotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please Reset Your Password')
        return redirect('accounts:resetpassword_url')

    else:
        messages.error(request, 'This link is expired')
        return redirect('accounts:login_url')


def resetpassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password Reset Was Successful')
            return redirect('accounts:login_url')
        else:
            messages.error(request, "passwords dont match")
            return redirect('accounts:resetpassword_url')
    else:
        return render(request, 'accounts/passreset.html')
