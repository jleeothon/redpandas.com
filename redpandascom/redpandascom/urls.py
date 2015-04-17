from django.conf.urls import include, url
from django.contrib import admin

import redpanda.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'redpandascom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^redpandas/new', redpanda.views.RedPandaCreate.as_view(), name='redpanda-new'),
    url(r'^redpandas/(?P<name>[\w-]+)', redpanda.views.RedPandaDetail.as_view(), name='redpanda-detail'),

    url(r'^admin/', include(admin.site.urls)),
]
