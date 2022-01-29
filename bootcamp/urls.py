from django.urls import path
#from django.views.decorators.csrf import csrf_exempt
from . import views


app_name = 'bootcamp'

urlpatterns = [
    path('', views.BootcampList.as_view(), name='bootcamp'),
    path('<int:id>', views.BootcampDetails.as_view(), name='get-bootcamp'),
    #path('addbootcamp/', views.ManageUserView.as_view(), name='add-bootcamp'),
    #path('updatebootcamp/', views.CreateUserView.as_view(), name='update-bootcamp'),
    #path('deletebootcamp/', views.CreateTokenView.as_view(), name='delete-bootcamp'),
]