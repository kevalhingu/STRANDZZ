# Generated by Django 4.1.1 on 2022-10-27 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_category_options_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Trending',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
