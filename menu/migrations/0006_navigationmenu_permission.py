# Generated by Django 4.2 on 2023-05-13 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('menu', '0005_remove_dropdownmenu_group_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigationmenu',
            name='permission',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='auth.permission'),
        ),
    ]
