
from django.shortcuts import render,redirect
from accounts.models import CustomUser
from form.forms import CustomUserCreationForm, VendorRegistrationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from django.views import View
from form.forms import VendorLoginForm
# Create your views here.

class Sign_Up_View (CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name="registration/signup.html"


class VendorRegistrationView(CreateView):

    form_class = VendorRegistrationForm
    template_name = "registration/vendor_register.html"
    success_url = reverse_lazy("accounts:vendor_login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.role = CustomUser.Vendor  # Set the role to 'vendor'
        user.save()
        return super().form_valid(form)

class VendorLoginView(View):
    def get (self ,req):
        form = VendorLoginForm()
        return render(req, "registration/vendor_login.html", {"form": form})
    def post(self, req):
        form = VendorLoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(req, username=username, password=password)
            if user is not None and user.role == CustomUser.VENDOR:
                login(req, user)
                return redirect('vendor:all')  # Redirect to vendor dashboard or desired page
            else:
                form.add_error(None, "Invalid credentials or not a vendor.")

        return render(req, "registration/vendor_login.html", {"form": form})


