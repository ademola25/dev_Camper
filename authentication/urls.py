from django.urls import path
from .views import RegisterView, VerifyEmail, LoginAPIView
#from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    #path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    #path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
]
