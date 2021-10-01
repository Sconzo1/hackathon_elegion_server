from rest_framework import routers

from api.views import TaskView, UserTaskView

router = routers.DefaultRouter()
router.register(r'tasks', TaskView)
router.register(r'user_tasks', UserTaskView)

urlpatterns = router.urls
