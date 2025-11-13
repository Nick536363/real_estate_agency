from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.BooleanField('Наличие балкона', null=True, blank=True, db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)

    new_building = models.BooleanField(
        verbose_name="Являеться ли новостройкой", 
        null=True, 
        db_index=True)
    liked_by = models.ManyToManyField(
        User, 
        related_name="liked_flats", 
        verbose_name="Кто лайкнул", 
        blank=True)

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'

    
class Complaint(models.Model):
    flat = models.ForeignKey(
        Flat, 
        verbose_name="Место жительства", 
        related_name="complaints", 
        on_delete=models.CASCADE)
    author = models.ForeignKey(
        User, 
        verbose_name="Автор жалобы", 
        related_name="complaints", 
        on_delete=models.CASCADE, 
        null=True)
    text = models.TextField("Текст жалобы")

    def __str__(self):
        return f"{self.flat.adress}, {self.user}"


class Owner(models.Model):
    name = models.CharField('ФИО владельца', max_length=200)
    pure_phone = PhoneNumberField(
        region="RU", 
        null=True, 
        verbose_name="Нормализированный номер владельца")
    flats = models.ManyToManyField(
        Flat, 
        related_name="owners", 
        verbose_name="Квартиры в собственности", 
        blank=True)
    def __str__(self):
        return f"{self.name}"