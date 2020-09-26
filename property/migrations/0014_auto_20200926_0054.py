from django.db import migrations


def swap_owned_apartments(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        owner = Owner.objects.get_or_create(
            owner=flat.owner, owners_phonenumber=flat.owners_phonenumber,
            owner_pure_phone=flat.owner_pure_phone,)
        owner[0].owned_apartments.set([flat])


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20200926_0054'),
    ]

    operations = [
            migrations.RunPython(swap_owned_apartments),
        ]
