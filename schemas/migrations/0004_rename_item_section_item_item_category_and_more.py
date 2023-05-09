# Generated by Django 4.2 on 2023-05-09 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schemas', '0003_rename_room_schema_id_malfunctionreport_room_schema_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_section',
            new_name='item_category',
        ),
        migrations.AlterField(
            model_name='roomitem',
            name='room_schema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='schemas.roomschema'),
        ),
    ]