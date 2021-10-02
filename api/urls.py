from rest_framework import routers

from api.views import TaskView, UserTaskView, ChatTypeView, ForeignChatView

router = routers.DefaultRouter()
router.register(r'tasks', TaskView)
router.register(r'user_tasks', UserTaskView)
router.register(r'chat_types', ChatTypeView)
router.register(r'foreign_chats', ForeignChatView)

urlpatterns = router.urls
