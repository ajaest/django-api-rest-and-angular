from django.conf.urls import include, url
from django.conf import settings
from django.template.exceptions import TemplateDoesNotExist

from django.views.generic import TemplateView

from django.http.response import Http404

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


class SimpleStaticView(TemplateView):
    def get_template_names(self):
        return [self.kwargs.get('template_name') + ".html"]

    def get(self, request, *args, **kwargs):
        from django.contrib.auth import authenticate, login
        if request.user.is_anonymous():
            # Auto-login the User for Demonstration Purposes
            user = authenticate()
            login(request, user)
        try:
            response = super(SimpleStaticView, self).get(request, *args, **kwargs)
            response.render()
            return response
        except TemplateDoesNotExist:
            raise Http404


urlpatterns = [
    url(r'^api/', include('example.api.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<template_name>\w+)$', SimpleStaticView.as_view(), name='example'),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
]

if settings.DEBUG or True:
    from django.views.static import serve
    urlpatterns += [
        url(r'^(?P<path>favicon\..*)$', serve, {'document_root': settings.STATIC_ROOT}),
        url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:] , serve, {'document_root': settings.MEDIA_ROOT}),
        url(r'^%s(?P<path>.*)$' % settings.STATIC_URL[1:], serve, {'document_root': settings.STATIC_ROOT}),
    ]
