# Generated by Django 5.0.7 on 2024-07-31 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_reservation_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(default='images/default.png', upload_to='images/'),
        ),
    ]