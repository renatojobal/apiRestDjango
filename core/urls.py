
# Django
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

# Rest framewkor imports
from rest_framework import routers

# Local project imports
from core import views


router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet)



urlpatterns = [
    # path('', include(router.urls)),  # Default views, but not used because the urls for some other methos are in singular, like 'stundet'
    path('students', views.list_students, name='list_students'),
    path('student/<int:id>', views.manage_student, name='manage_student'),
    path('students/filter', views.get_student_by_filter_query_paramans),
    path('student', views.create_student),


]
