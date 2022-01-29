from django.urls import path
#from django.views.decorators.csrf import csrf_exempt
from . import views


app_name = 'courses'

urlpatterns = [
    path('', views.CoursesList.as_view(), name='courses'),
    path('<int:id>', views.CoursesDetails.as_view(), name='get-courses'),
    #path('addbootcamp/', views.ManageUserView.as_view(), name='add-bootcamp'),
    #path('updatebootcamp/', views.CreateUserView.as_view(), name='update-bootcamp'),
    #path('deletebootcamp/', views.CreateTokenView.as_view(), name='delete-bootcamp'),
]