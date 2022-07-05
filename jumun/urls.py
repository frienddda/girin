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
    path('tdupdate/', views.jumun_td_update, name='jumun_td_update'),
##    path('upload/', views.uploadFile, name="uploadFile"),
    path('excelupload2/', views.excel_upload, name="excel_upload"),
    path('alldelete/', views.all_delete, name="alldelete"),
    path('order/', views.order_list, name="order"),
    path('order/delete/', views.order_delete, name="order_delete"),
    path('order/excel/', views.order_excel, name="order_excel"),
    path('order/excel2/', views.order_excel2, name="order_excel2"),
    path('order/alldelete/', views.order_all_delete, name="order_alldelete"),
    path('order_submit/', views.order_submit, name="order_submit"),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
