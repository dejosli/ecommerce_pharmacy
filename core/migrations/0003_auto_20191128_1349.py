# Generated by Django 2.2.5 on 2019-11-28 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191128_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Analgesics'), ('SW', 'Sport wear'), ('OW', 'Outwear')], max_length=2),
        ),
    ]