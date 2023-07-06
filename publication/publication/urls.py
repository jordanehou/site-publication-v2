"""educa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
# detail view to display a single course
#from courses.views import CourseListView
from django.conf import Settings, settings
from django.conf.urls.static import static

from publication.settings import MEDIA_ROOT, MEDIA_URL
from django.views.generic import RedirectView
#from django.conf.urls import url
#from courses.views import ManageCourseListView


urlpatterns = [
    #path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    #path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('', include('students.urls')),
    path('cart/', include('carts.urls', namespace='cart')),
    path('course/', include('courses.urls')),
    path('orders/', include('orders.urls', namespace='orders')),
    #path('course/', ManageCourseListView.as_view(), name='subjectlist'),
    
    # Rest framework
    #path('api-auth/', include('rest_framework.urls')),
    #path('api/', include('courses.api.urls', namespace='api')),


    #url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)