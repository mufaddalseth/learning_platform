"""
URL configuration for learning_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path , include
import debug_toolbar

# from courses_section import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Below path is for admin page
    path('admin/', admin.site.urls),
    # Below path is for toolbar
    path('__debug__/',include(debug_toolbar.urls)),
    path('', include("courses_section.urls")), 

    # Below path is for Application 1 - courses_section
    path('courses/', include("courses_section.urls")), 
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

