# Generated by Django 4.2.7 on 2023-12-09 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0009_country_alter_address_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
        migrations.AddField(
            model_name='country',
            name='code',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
