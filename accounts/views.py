from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from accounts.models import User
from django.contrib import messages
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordResetConfirmView
from accounts.forms import (
    HospitalRegistrationForm,
    ResearcherRegistrationForm,
    RegulatorRegistrationForm,
    PatientRegistrationForm,
)
from django.urls import reverse

from  api.views import get_user_data
from .models import Hospital, Regulator, Researcher, Patient
from .forms import LoginForm, CustomPasswordResetForm, CustomSetPasswordForm


# Create your views here.


# stakeholders views
def stakeholders(request):
    return render(request, "accounts/stakeholders.html")


# patient views


# regulator views
def register_regulator(request):
    if request.method == "POST":
        form = RegulatorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Creating a new Hospital instance and associating it with the user
            regulator = Regulator.objects.create(user=user)
            # Additional logic specific to hospitals

            login(request, user)
            return redirect("accounts/researchdashboard")
    else:
        form = RegulatorRegistrationForm()
    return render(request, "accounts/register_regulator.html", {"form": form})


# researcher views


def register_researcher(request):
    if request.method == "POST":
        form = ResearcherRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            # Creating a new researcher instance and associating it with the user
            researcher = Researcher.objects.create(
                user=user,
                institution_name=form.cleaned_data["institution_name"],
                institution_id=form.cleaned_data["institution_id"],
                phone_number=form.cleaned_data["phone_number"],
                national_id=form.cleaned_data["national_id"],
                email=form.cleaned_data["email"],
                # first_name=form.cleaned_data['first_name'],
                # last_name=form.cleaned_data['last_name'],
                password=user.password,
                agree_terms=form.cleaned_data["agree_terms"],
            )
            return redirect("accounts:successful_registered")
    else:
        form = ResearcherRegistrationForm()
    return render(request, "accounts/register_researcher.html", {"form": form})


# hospital views


def register_hospital(request):
    if request.method == "POST":
        form = HospitalRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Creating a new Hospital instance and associating it with the user
            hospital = Hospital.objects.create(user=user)
            # Additional logic specific to hospitals

            login(request, user)
            return redirect("hospital_dashboard")
    else:
        form = HospitalRegistrationForm()
    return render(request, "accounts/hospital_register.html", {"form": form})


def retrieve_user(request):
    if request.method == 'POST':
        file_path = 'staticfiles/citizens/citizen.json'  # Provide the correct file path
        national_id = request.POST.get('nida_no')
        user_detail = get_user_data(file_path, national_id)

        if user_detail is not None:
            request.session['user_detail'] = user_detail
            return redirect('accounts:hospital_registers_patient')

        return JsonResponse({'error': 'User not found.'}, status=404)
    else:
        return render(request, 'regs/hospitaldash_registerpatient.html')


def hospital_registers_patient(request):
    user_detail = request.session.get('user_detail')  # Retrieve user_detail from session
    form = PatientRegistrationForm(request.POST or None, initial=user_detail)

    if request.method == "POST":
        if form.is_valid():
            print('Form is valid')
            user = form.save(commit=False)
            user.save()
            # Creating a new patient instance and associating it with the user
            Patient.objects.create(
                user=user,
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                national_id=form.cleaned_data["national_id"],
                phone_number=form.cleaned_data["phone_number"],
                email=form.cleaned_data["email"],
                date_of_birth=form.cleaned_data["date_of_birth"],
            )
            return redirect("accounts:successful_patient_registered")
        else:
            print('Form is not valid')

    context = {
        'user_detail': user_detail,
        'form': form,
    }

    return render(request, 'regs/hospitaldash_registerpatient.html', context)



# forgot password
def forgot_password(request):
    return render(request, "regs/forgot_password.html")


# login view for all users


def login_view(request):
    print(request.POST)
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            print(form.cleaned_data)

            if user is not None:
                login(request, user)
                # request.session['user_type'] = user.user_type
                request.session["username"] = user.username
                request.session["user_id"] = user.id
                if user.is_patient:
                    return redirect("regs:research_dashboard")
                elif user.is_hospital:
                    return redirect("regs:hospital_dashboard")
                elif user.is_regulator:
                    return redirect("regs:regulator_dashboard")
                elif user.is_researcher:
                    return redirect("regs:research_dashboard")
        else:
            print("not valid")
            print(form.errors)
    form = LoginForm()  # Creating an instance of the form

    return render(request, "accounts/login.html", {"form": form})


# logout view for all users
def logout_view(request):
    if request.session.get("logout_on_browser_back"):
        if request.user.is_authenticated:
            logout(request)
        request.session.flush()
    return redirect("accounts:login")


# login required decorator
def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("accounts:login")
        return view_func(request, *args, **kwargs)

    return wrapper


# success views
def success_loader(request):
    return render(request, "accounts/success.html")


def successful_registered(request):
    return render(request, "accounts/register_success.html")


def successful_reset(request):
    return render(request, "accounts/reset_success.html")


def successful_patient_registered(request):
    return render(request, "accounts/patient_register_success.html")


# password reset views


def password_reset(request):
    if request.method == "POST":
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            user = User.objects.get(email=email)

            # Generate a password reset token
            token_generator = default_token_generator
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = token_generator.make_token(user)

            # Build the password reset URL
            current_site = "localhost:8000"
            reset_url = f"http://{current_site}/accounts/password_update/{uid}/{token}/"

            # Send password reset email
            mail_subject = "Reset your password"
            message = render_to_string(
                "accounts/password_reset_email.html",
                {
                    "user": user,
                    "reset_url": reset_url,
                },
            )
            send_mail(
                mail_subject,
                message,
                "alexgmkwizu@gmail.com",
                [email],
                html_message=message,
            )
            messages.success(
                request,
                "An email has been sent with instructions to reset your password.",
            )
            return redirect("accounts:password_reset")
        print("success")
    else:
        form = CustomPasswordResetForm()
    return render(request, "accounts/password_reset.html", {"form": form})


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    template_name = "accounts/password_set.html"
    success_url = "accounts:password_changed"

    def get(self, request, *args, **kwargs):
        self.uidb64 = kwargs["uidb64"]
        self.token = kwargs["token"]
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["uidb64"] = self.uidb64
        context["token"] = self.token
        return context

    def form_valid(self, form):
        uid = urlsafe_base64_decode(self.kwargs["uidb64"]).decode()
        messages.success(self.request, "Your password has been updated.")
        return super().form_valid(form)
