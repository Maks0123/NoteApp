
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    url(r'^api/v1/', include('notes.urls')),
    path('admin/', admin.site.urls),

]
