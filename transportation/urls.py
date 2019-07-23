from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from transportation.views import ProviderCreateView, ProviderDetailsView
from transportation.views import ServiceAreaCreateView, ServiceAreaDetailsView, ServiceAreaQueryView

urlpatterns = {
    url(r'^providers/$', ProviderCreateView.as_view(), name="provider_create"),
    url(r'^providers/(?P<pk>[0-9]+)/$', ProviderDetailsView.as_view(), name="provider_details"),
    url(r'^service_area/$', ServiceAreaCreateView.as_view(), name="service_area_create"),
    url(r'^service_area/(?P<pk>[0-9]+)/$', ServiceAreaDetailsView.as_view(), name="service_area_details"),
    url(r'^service_area_query/$', ServiceAreaQueryView.as_view(), name="service_area_query"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
