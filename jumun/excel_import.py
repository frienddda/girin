import openpyxl
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","config.settings")
django.setup()

from .models import jumun_T


wb = openpyxl.load_workbook('jumun.xlsx')
sheet1 = wb['Sheet1']
rows = sheet1['A1':'R15814']


for row in rows:

    dict = {}
    dict['eng_flag']=row[0].value
    dict['jumun_date']=row[1].value
    dict['jumun_id']=row[2].value
    dict['jumun_name']=row[3].value
    dict['jumun_con']=row[4].value
    dict['brand']=row[5].value
    dict['prd_name']=row[6].value
    dict['prd_color']=row[7].value
    dict['quantity']=row[8].value
    dict['wholesale']=row[9].value
    dict['whole_pr']=row[10].value
    dict['note']=row[11].value
    dict['sup_pr']=row[12].value
    dict['name']=row[13].value
    dict['phone']=row[14].value
    dict['address']=row[15].value
    dict['jumun_id2']=row[16].value
    dict['date2']=row[17].value

    jumun_T(**dict).save()
