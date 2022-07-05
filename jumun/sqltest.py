##import pymysql
##pymysql.install_as_MySQLdb()

from django.conf import settings
from . import models


test = JumunT.objects.order_by('jumun_t_id')

print(test)

