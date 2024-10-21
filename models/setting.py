from tortoise.models import Model
from tortoise import fields

class Setting(Model):
    id = fields.IntField(primary_key=True)
    key = fields.CharField(255)
    value = fields.CharField(255)