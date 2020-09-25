from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    owner = models.CharField("ФИО владельца", max_length=200)
    owner_pure_phone = PhoneNumberField('Нормализованный номер владельца', blank=True, null=True)
    owners_phonenumber = models.CharField("Номер владельца", max_length=20)
    created_at = models.DateTimeField("Когда создано объявление", default=timezone.now, db_index=True)
    new_building  = models.NullBooleanField('Новостройка', null=True)

    description = models.TextField("Текст объявления", blank=True)
    price = models.IntegerField("Цена квартиры", db_index=True)

    town = models.CharField("Город, где находится квартира", max_length=50, db_index=True)
    town_district = models.CharField("Район города, где находится квартира", max_length=50, blank=True, help_text='Чертаново Южное')
    address = models.TextField("Адрес квартиры", help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField("Этаж", max_length=3, help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField("Количество комнат в квартире", db_index=True)
    living_area = models.IntegerField("количество жилых кв.метров", null=True, blank=True, db_index=True)

    has_balcony = models.NullBooleanField("Наличие балкона", db_index=True)
    active = models.BooleanField("Активно-ли объявление", db_index=True)
    who_liked = models.ManyToManyField(User, related_name='Who_liked_info', verbose_name='Кто лайкнул', blank=True)
    construction_year = models.IntegerField("Год постройки здания", null=True, blank=True, db_index=True)

class Appeal(models.Model):
    author = models.ForeignKey(User, related_name='author_info', verbose_name='Кто жаловался', on_delete=models.CASCADE)
    apartment = models.ForeignKey(Flat, related_name='apartment_info', verbose_name='Квартира, на которую пожаловались.', on_delete=models.CASCADE)
    complaint_text = models.TextField("Текст жалобы", max_length=2000)