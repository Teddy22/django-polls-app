from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns = [
	# ex: /polls/
	url(r'^$', views.index, name='index'),

	# ex: /polls/5
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='question_details_url'),

	# ex: /polls/5/results/
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='question_results_url'),

	# ex: /polls/5/vote
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
