# Generated by Django 4.2 on 2023-05-05 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_dropdownmenu_icon_alter_navigationmenu_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dropdownmenu',
            name='group_id',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='dropdownmenu',
            name='type',
            field=models.CharField(blank=True, default='', max_length=63, null=True),
        ),
    ]
