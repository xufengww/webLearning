from django.conf.urls import url
from jobs import views

urlpatterns = [
    # 职位列表
    url('^joblist/', view=views.joblist,name='joblist'),

    url(r'^job/(?P<job_id>\d+)/$',view=views.detail,name='job'),
]
