"""neu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django import contrib
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from accounts import views as account_views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('account/', include('accounts.urls')),
    path('register/', account_views.register_view, name='register'),
    path('creator-register/', account_views.creator_register_view, name='register creator'),
    path('login/', account_views.login_view, name='login'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    #path('profile/', account_views.user_update_view, name='profile'),
#    path('game/', include('feed.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)