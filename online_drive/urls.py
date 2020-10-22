from django.contrib import admin

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from upload import views


urlpatterns = [
    path('', views.file_list, name='home'),
    path('upload/', views.upload, name='upload'),
    path('files/', views.file_list, name='file_list'),
    path('files/upload/', views.upload_file, name='upload_file'),
    path('files/rename/<int:pk>/', views.RenameFileView.as_view(), name='rename_file'),
    path('files/<int:pk>/', views.delete_file, name='delete_file'),

    # path('class/files/upload/', views.UploadFileView.as_view(), name='class_upload_file'),

    # User management
    path('accounts/', include('django.contrib.auth.urls')), 
    path('accounts/', include('users.urls')),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
