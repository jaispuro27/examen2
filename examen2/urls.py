from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/', include('apis.urls')),
    path('todos/', include('ToDoS.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]

