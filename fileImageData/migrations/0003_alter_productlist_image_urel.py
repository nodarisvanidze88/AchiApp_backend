# Generated by Django 4.2.4 on 2023-09-01 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileImageData', '0002_alter_productlist_image_urel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlist',
            name='image_urel',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
