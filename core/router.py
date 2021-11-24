# Rest_framework imports
from django.db import router
from rest_framework import routers

from core.views import (StudentViewSet)


router = routers.DefaultRouter()

router.register('students/', StudentViewSet)