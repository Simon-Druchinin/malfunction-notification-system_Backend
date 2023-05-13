from django.db import models
from django.utils import timezone

from users.models import User

class ItemCategory(models.Model):
    name = models.CharField(max_length=127, unique=True, db_index=True)
    zIndex = models.IntegerField(default=1)
    help_text = models.CharField(max_length=127, blank=True, null=True)
    
class Item(models.Model):
    name = models.CharField(max_length=127, unique=True, db_index=True)
    characteristics = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=127, help_text="Тип элемента для отрисовки на сайте (lamp, table, ...)")
    category = models.ForeignKey(ItemCategory, on_delete=models.PROTECT)

class RoomSchema(models.Model):
    name = models.CharField(max_length=127, unique=True, db_index=True)
    width = models.IntegerField()
    length = models.IntegerField()

class RoomItem(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    room_schema = models.ForeignKey(RoomSchema, related_name='items', on_delete=models.CASCADE)

class MalfunctionReportStatus(models.Model):
    name = models.CharField(max_length=127)

class MalfunctionReport(models.Model):
    name = models.CharField(max_length=127)
    problem_text = models.TextField(blank=True, null=True, help_text="Общее описание неисправностей в комнате")
    room_schema = models.ForeignKey(RoomSchema, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, related_name='created_by', on_delete=models.CASCADE)
    taken_by = models.ForeignKey(User, related_name='taken_by', on_delete=models.CASCADE, blank=True, null=True)
    status = models.ForeignKey(MalfunctionReportStatus, on_delete=models.PROTECT)

class MalfunctionReportItem(models.Model):
    problem_text = models.TextField(blank=True, null=True, help_text="Описание неисправности элемента")
    malfunction_report = models.ForeignKey(MalfunctionReport, related_name='problem_elements', on_delete=models.CASCADE)
    room_element = models.ForeignKey(RoomItem, on_delete=models.CASCADE)
    