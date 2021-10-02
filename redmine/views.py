from pprint import pprint

from django.http import JsonResponse
from redminelib import Redmine
from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin


class IssueView(viewsets.GenericViewSet, ListModelMixin):

    # def get_queryset(self):
    #     id_user = self.request.query_params.get('id_user')
    #     if validate_int(id_user, min_value=0, required=True):
    #         return User.objects.get(pk=id_user)

    def list(self, request, *args, **kwargs):
        redmine = Redmine('https://stud.redmine.tpu.ru', username='avk224',
                          password='9N9u9tT2')
        project = redmine.project.get('hghdfhfgd')
        issues = []
        priorities_to_num = {
            'Низкий': 1,
            'Нормальный': 3,
            'Высокий': 4,
            'Неотложный': 5,
        }
        for issue in project.issues:
            issues.append({
                'name': str(issue),
                'priority': priorities_to_num[str(issue.priority)],
                'date_expired': str(issue.start_date)
            })
        pprint(issues)
        return JsonResponse(issues, safe=False, json_dumps_params={'ensure_ascii': False})
