# Generated by Django 4.2 on 2023-05-10 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schemas', '0007_remove_itemcategory_zindex'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcategory',
            name='zIndex',
            field=models.IntegerField(default=1),
        ),
    ]