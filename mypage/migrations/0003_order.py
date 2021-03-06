# Generated by Django 4.0.2 on 2022-03-15 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_alter_product_category_alter_product_market'),
        ('mypage', '0002_remove_cart_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='수량')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='주문 등록 날짜')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='수정 날짜')),
                ('product_real', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productreal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
