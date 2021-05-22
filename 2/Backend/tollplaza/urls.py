from django.contrib import admin
from django.urls import path, include
from receipt import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="Toll PLaza")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('receipt/', include('receipt.urls')),
    path('', schema_view),
    path('accounts/', include('rest_framework.urls')),
]
