from django.conf.urls import url, include
from django.views.static import serve

from . import views
from card_db.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^catalog$', views.CatalogView.as_view(), name='catalog'),
    url(r'^summary$', views.SummaryView.as_view(), name='summary'),
    url(r'^testers$', views.TestersView.as_view(), name='testers'),
    url(r'^stats$', views.StatsView.as_view(), name='stats'),
    url(r'^setup$', views.SetupView.as_view(), name='setup'),
    url(r'^(?P<card>[0-9]{7})/$', views.detail, name='detail'),
    url(r'^media/(?P<path>.*)$',serve, {'document_root':MEDIA_ROOT}),
]
