# Generated by Django 2.2.4 on 2020-09-25 18:27

from django.db import migrations

def swap_owner(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(
            owner=flat.owner, owners_phonenumber=flat.owners_phonenumber,
            owner_pure_phone=flat.owner_pure_phone,)

   

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20200925_2157'),
    ]

    operations = [
            migrations.RunPython(swap_owner),
        ]
