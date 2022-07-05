
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'jumun'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.jumun_create, name='jumun_create'),
    path('delete/', views.jumun_delete, name='jumun_delete'),
    path('excel/', views.jumun_excel, name='jumun_excel'),
    path('excel2/', views.jumun_excel2, name='jumun_excel2'),
##    path('upload/', views.uploadFile, name="uploadFile"),
    path('excelupload2/', views.excel_upload, name="excel_upload"),
    path('alldelete/', views.all_delete, name="alldelete"), 

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
