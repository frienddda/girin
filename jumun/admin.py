from django.contrib import admin
from .models import JumunT
## Register your models here.


##class JumunAdmin(admin.ModelAdmin):
##    list_display =('eng_flag','jumun_date','jumun_id','jumun_name','jumun_con','brand', 'prd_name','prd_color','quantity','wholesale','whole_pr','note','sup_pr','name','phone','address','jumun_id2','date2',)

class Jumunadmin(admin.ModelAdmin):
    list_display =('jumun_t_id','영문','주문날짜','주문자id','주문자','위탁자','브랜드','상품명','색상','수량','중도매','도매가','비고','공급가','이름','전화번호','주소','아이디','나온날짜')
    search_fields = ['주문자id']
admin.site.register(JumunT,Jumunadmin)
