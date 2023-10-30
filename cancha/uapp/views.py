from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView

# from cancha.uapp.models import CustomUser
# from .forms import CustomUserCreationForm, CustomAuthenticationForm

# class CustomLoginView(LoginView):
#     authentication_form = CustomAuthenticationForm
#     template_name = 'uapp/login.html'
#     success_url = '/capp/'  # Redirige a la vista 'cancha' después del inicio de sesión

# class CustomRegisterView(CreateView):
#     model = CustomUser
#     form_class = CustomUserCreationForm
#     template_name = 'uapp/registro.html'
#     success_url = '/capp/'  # Redirige a la vista 'cancha' después del registro