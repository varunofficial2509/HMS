# Generated by Django 3.0.8 on 2020-07-27 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0032_auto_20200727_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='appeal',
            name='hostel',
            field=models.CharField(max_length=500, null=True),
        ),
    ]