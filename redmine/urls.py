from rest_framework import routers

from redmine.views import IssueView

router = routers.DefaultRouter()
router.register(r'issues', IssueView, basename='redmine-issues')

urlpatterns = router.urls
