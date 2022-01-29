from django.urls import path
#from django.views.decorators.csrf import csrf_exempt
from . import views


app_name = 'review'

urlpatterns = [
    path('', views.ReviewList.as_view(), name='review'),
    path('<int:id>', views.ReviewDetails.as_view(), name='get-review'),
    #path('addbootcamp/', views.ManageUserView.as_view(), name='add-bootcamp'),
    #path('updatebootcamp/', views.CreateUserView.as_view(), name='update-bootcamp'),
    #path('deletebootcamp/', views.CreateTokenView.as_view(), name='delete-bootcamp'),
]