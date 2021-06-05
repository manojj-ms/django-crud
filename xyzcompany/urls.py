"""XYZ company URL Configuration

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
from django.urls import include,path
from .views import HomePageView
from django.views.generic.base import TemplateView # new
from django.conf import settings 
from django.conf.urls.static import static 
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)




urlpatterns = [
    # A JSON view of your API specification at /swagger.json
    # A YAML view of your API specification at /swagger.yaml
    path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # A swagger-ui view of your API specification at /swagger/
    path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # A ReDoc view of your API specification at /redoc/
    path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # display Custom Admin Login  page
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(),name='home'), # display home page 
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),  # display about page
    path('services/', TemplateView.as_view(template_name='services.html'), name='services'),  # display services page
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),  # display contact page
    path('accounts/', include('accounts.urls'), name='accounts'),  # display Sign up page
    
]

if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


