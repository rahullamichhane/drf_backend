from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from apiframe.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),  # Root URL serves url.html
    path('admin/', admin.site.urls), 
    path('students/',include(('students.urls', 'students'), namespace='students')),
    path('books/', include(('books.urls', 'books'), namespace='books')),
    path('registration/', include('registration.urls')),
    path("apiframe/user/register/", CreateUserView.as_view(), name="register"),
    path("apiframe/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("apiframe/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("apiframe-auth/", include("rest_framework.urls")),
    path("apiframe/", include("apiframe.urls")),
    
    

 

  

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

