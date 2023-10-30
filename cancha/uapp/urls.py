from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', HomeView.as_view(), name="home"),
    path('about/', AboutView.as_view(), name="about"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

# from django.urls import path
# from .views import HomeView, SignUpView, AboutView, ProfileView, ProfileEditView, CartView, OrdersView, MyLoginView, LogoutView

# urlpatterns = [
#     

#     path('signup/', SignUpView.as_view(), name='signup'),
#   path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
#     path('profile/edit/', ProfileEditView.as_view(), name='edit_profile'),
    
#     path('cart/', CartView.as_view(), name='cart'),
#     path('orders/', OrdersView.as_view(), name='orders'),
    
from django.urls.conf import include
#from registration.views import HomeView, MyLoginView , LogoutView, ProfileView
# from .views import CustomLoginView, CustomRegisterView
# urlpatterns = [
    # path('home/', include(HomeView.as_view()), name="home"),
    # path('login/',  MyLoginView.as_view(), name="login"),
    # path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    # path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    # path('login/', CustomLoginView.as_view(), name='login'),
    # path('register/', CustomRegisterView.as_view(), name='register'),
#]
