# Generated by Django 4.2 on 2023-05-10 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schemas', '0004_rename_item_section_item_item_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='item_type',
            new_name='type',
        ),
        migrations.AlterField(
            model_name='malfunctionreportitem',
            name='malfunction_report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problem_elements', to='schemas.roomschema'),
        ),
    ]