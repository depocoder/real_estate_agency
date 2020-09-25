# Generated by Django 2.2.4 on 2020-09-25 21:54

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20200925_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='owned_apartments',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='owned_apartments_info', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner',
            field=models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, null=True, region=None, verbose_name='Нормализованный номер владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owners_phonenumber',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Номер владельца'),
        ),
    ]
