# Generated by Django 4.1.1 on 2022-10-27 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_contactename_contact_contactname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='contactname',
            new_name='contname',
        ),
    ]
