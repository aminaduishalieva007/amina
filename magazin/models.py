from django.db import models

class Shop(models.Model):
    name = models.CharField(verbose_name='Название', max_length=25)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    logo = models.ImageField(verbose_name='logotiv', upload_to='product_image')


    class Meta:
        db_table = 'shop'
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

