from django.db import models
from django.utils.translation import gettext as _

class Food(models.Model):
    name = models.CharField(_("نام غذا"), max_length=255)
    description = models.TextField(_("توضیحات"), max_length=50)
    rate = models.IntegerField(_("امتیاز"), default=0)
    price = models.IntegerField(_("قیمت"))
    time = models.IntegerField(_("زمان لازم"))
    pub_date = models.DateField(_("تاریخ انتشار" ), auto_now=False, auto_now_add = True)
    photo = models.ImageField(upload_to= 'foods/')

    def __str__(self):
        return str(self.price)
    