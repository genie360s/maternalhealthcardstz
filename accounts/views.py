from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from accounts.models import User
from django.contrib import messages
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str
from django.contrib.auth import authenticate, login, logout
from accounts.forms import (
    HospitalRegistrationForm,
    ResearcherRegistrationForm,
    RegulatorRegistrationForm,
)
from .models import Hospital, Regulator, Researcher, Patient
from .forms import LoginForm, CustomPasswordResetForm, CustomSetPasswordForm


# Create your views here.


# stakeholders views
def stakeholders(request):
    return render(request, "accounts/stakeholders.html")


# patient views
def login_patient(request):
    return render(request, "accounts/login_patient.html")


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


def login_regulator(request):
    return render(request, "accounts/login_regulator.html")


# researcher views
def login_researcher(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, "accounts/login_researcher.html")


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
        return redirect("regs:research_dashboard")
    else:
        form = ResearcherRegistrationForm()
    return render(request, "accounts/register_researcher.html", {"form": form})


# hospital views
def login_hospital(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None and user.is_hospital:
                login(request, user)
                return redirect("hospital_dashboard")
            else:
                form.add_error(None, "Invalid email or password")
    else:
        form = LoginForm()

    return render(request, "hospital_login.html", {"form": form})


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


# password reset views
def password_reset(request):
    if request.method == "POST":
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            user = User.objects.filter(email=email).first()
            print(user)

            # Generate a password reset token
            token_generator = default_token_generator
            uid = urlsafe_base64_encode(user.pk.to_bytes(4, "big"))
            token = token_generator.make_token(user)
            print(token)

            # Store the reset token in the session
            request.session["reset_token"] = token
            request.session["reset_uid"] = uid
            print(uid)

            messages.success(
                request,
                "A password reset link has been generated. Please proceed to reset your password.",
            )
        #return redirect("accounts:password_update")
         # Render the password update form
            return render(request, "accounts/password_set.html", {"form": CustomSetPasswordForm(user)})
    else:
        form = CustomPasswordResetForm()
    return render(request, "accounts/password_reset.html", {"form": form})


def password_update(request):
    token = request.session.get("reset_token")
    uid = request.session.get("reset_uid")

    try:
        uid = urlsafe_base64_decode(uid).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is None:
        messages.error(request, "Invalid password reset link.")
        return redirect("accounts:password_reset")

    # Verify the reset token
    if (
        token is None
        or uid is None
        or not default_token_generator.check_token(user, token)
    ):
        messages.error(request, "Invalid password reset link.")
        print("invalid")
        return redirect("accounts:password_reset")

    if request.method == "POST":
        form = CustomSetPasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()

            # Clear the reset token and UID from the session
            del request.session["reset_token"]
            del request.session["reset_uid"]

            messages.success(request, "Your password has been updated.")
            return redirect("accounts:succesful_reset")
        print("success")
    else:
        form = CustomSetPasswordForm(request.user)
    return render(request, "accounts/password_set.html", {"form": form})
