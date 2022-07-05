from django.db import models

# Create your models here.


##class jumun_T(models.Model):
##    eng_flag = models.CharField(verbose_name = "영문",max_length=10,blank =True, null = True )
##    jumun_date = models.CharField(verbose_name = "주문일",max_length=30, blank =True, null = True)
##    jumun_id = models.CharField(verbose_name = "주문ID",max_length=30, blank =True, null = True)
##    jumun_name = models.CharField(verbose_name = "주문자",max_length=30, blank =True, null = True)
##    jumun_con = models.CharField(verbose_name = "위탁자",max_length=30, blank =True, null = True)
##    brand = models.CharField(verbose_name = "브랜드",max_length=30, blank =True, null = True)
##    prd_name = models.TextField(verbose_name = "상품명", blank =True, null = True)
##    prd_color = models.TextField(verbose_name = "색상", blank =True, null = True)
##    quantity = models.SmallIntegerField(verbose_name="수량", blank = True, null = True)
##    wholesale = models.CharField(verbose_name = "중도매", max_length=30, blank =True, null = True)
##    whole_pr = models.CharField(verbose_name = "도매가", max_length=30, blank =True, null = True)
##    note = models.TextField(verbose_name = "비고", blank =True, null = True)
##    sup_pr = models.CharField(verbose_name = "공급가",max_length=30, blank =True, null = True)
##    name = models.CharField(verbose_name = "이름",max_length=30, blank =True, null = True)
##    phone = models.CharField(verbose_name = "전화번호",max_length=30, blank =True, null = True)
##    address = models.TextField(verbose_name = "주소", blank =True, null = True)
##    jumun_id2 =models.CharField(verbose_name = "ID",max_length=30, blank =True, null = True)
##    date2 = models.CharField(verbose_name = "나온날짜",max_length=30, blank =True, null = True)
##    

#파일업로드 test모
##class Document(models.Model):
##    title = models.CharField(max_length=200)
##    uploadedFile = models.FileField(upload_to="result/")
##    dateTimeOfUpload = models.DateTimeField(auto_now=True)



class JumunT(models.Model):
    jumun_t_id = models.AutoField(primary_key=True)
    영문 = models.CharField(max_length=12, blank=True, null=True)
    주문날짜 = models.CharField(max_length=45, blank=True, null=True)
    주문자id = models.CharField(db_column='주문자ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    주문자 = models.CharField(max_length=45, blank=True, null=True)
    위탁자 = models.CharField(max_length=45, blank=True, null=True)
    브랜드 = models.CharField(max_length=45, blank=True, null=True)
    상품명 = models.CharField(max_length=45, blank=True, null=True)
    색상 = models.CharField(max_length=255, blank=True, null=True)
    수량 = models.CharField(max_length=12, blank=True, null=True)
    중도매 = models.CharField(max_length=25, blank=True, null=True)
    도매가 = models.CharField(max_length=25, blank=True, null=True)
    비고 = models.CharField(max_length=255, blank=True, null=True)
    공급가 = models.CharField(max_length=25, blank=True, null=True)
    이름 = models.CharField(max_length=45, blank=True, null=True)
    전화번호 = models.CharField(max_length=45, blank=True, null=True)
    주소 = models.CharField(max_length=255, blank=True, null=True)
    아이디 = models.CharField(max_length=45, blank=True, null=True)
    나온날짜 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        verbose_name = '주문장'
        db_table = 'jumun_t'



class OrderT(models.Model):
    order_t_id = models.AutoField(primary_key=True)
    영문 = models.CharField(max_length=12, blank=True, null=True)
    주문날짜 = models.CharField(max_length=45, blank=True, null=True)
    주문자id = models.CharField(db_column='주문자ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    주문자 = models.CharField(max_length=45, blank=True, null=True)
    위탁자 = models.CharField(max_length=45, blank=True, null=True)
    브랜드 = models.CharField(max_length=45, blank=True, null=True)
    상품명 = models.CharField(max_length=45, blank=True, null=True)
    색상 = models.CharField(max_length=255, blank=True, null=True)
    수량 = models.CharField(max_length=12, blank=True, null=True)
    중도매 = models.CharField(max_length=25, blank=True, null=True)
    도매가 = models.CharField(max_length=25, blank=True, null=True)
    비고 = models.CharField(max_length=255, blank=True, null=True)
    공급가 = models.CharField(max_length=25, blank=True, null=True)
    이름 = models.CharField(max_length=45, blank=True, null=True)
    전화번호 = models.CharField(max_length=45, blank=True, null=True)
    주소 = models.CharField(max_length=255, blank=True, null=True)
    아이디 = models.CharField(max_length=45, blank=True, null=True)
    나온날짜 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        verbose_name = '발송요청'
        db_table = 'order_t'
