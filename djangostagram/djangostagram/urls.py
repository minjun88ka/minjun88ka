"""djangostagram URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from user.views import RegisterView
from user.views import LoginView
from user.views import logout

from post.views import WriteView
from post.views import TimelineList
from post.views import PostDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/register/', RegisterView.as_view(), name='register'),
    path('user/login/', LoginView.as_view(), name='login'),
    path('user/logout/', logout, name='logout'),
    path('upload/', WriteView.as_view(), name='write'),
    path('', TimelineList.as_view(), name='timeline'),
    path('post/<int:pk>/', PostDetail.as_view(), name='detailview'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
