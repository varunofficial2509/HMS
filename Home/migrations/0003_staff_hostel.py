# Generated by Django 3.0.8 on 2020-07-21 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20200721_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='hostel',
            field=models.CharField(choices=[('Godavari', 'Godavari Boys Hostel'), ('krishna', 'Krishna Boys Hostel'), ('sharadha', 'Sharadha Girls Hostel'), ('saraswathi', 'Saraswathi Girls Hostel')], max_length=200, null=True),
        ),
    ]