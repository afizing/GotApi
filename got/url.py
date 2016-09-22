from django.conf.urls import url, patterns, include
from rest_framework.urlpatterns import format_suffix_patterns
from got import views


urlpatterns = patterns('',
                       url(r'^api/$', views.BattleList.as_view()),
                       url(r'^api/(?P<pk>[0-9]+)/$', views.BattleDetail.as_view()),
                       url(r'^api/year/(?P<year>.+)/$', views.BattleListByYear.as_view(), name='battle-list-by-year'),
                      )

urlpatterns = format_suffix_patterns(urlpatterns)