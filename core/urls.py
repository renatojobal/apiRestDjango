
# Django
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

# Rest framewkor imports
# ...

# Local project imports
from core.router import router
from core import views

app_name = 'core'

urlpatterns = [

    path('students', views.list_students, name='list_students'),
    path('student/<int:student_id>', views.get_student),
    path('students/filter', views.get_student_by_filter),
    path('student', views.create_student),
    path('student/<int:student_id>', views.update_student),
    path('student/<int:student_id>', views.delete_student),

]
