from django.db import models


class Product(models.Model):
    name = models.CharField(verbose_name='Название', max_length=30)
    price = models.FloatField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    image = models.ImageField(verbose_name='Фото', upload_to='product_image')
    size = models.IntegerField(verbose_name='Размер')

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
