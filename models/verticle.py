from tortoise.models import Model
from tortoise import fields

class Verticle(Model):
    verticalID = fields.IntField(primary_key=True)
    verticalName = fields.CharField(255, null=True)
    status = fields.CharField(255, null=True)
    groupID = fields.CharField(255, null=True)
    createdOn = fields.CharField(255, null=True)
    groupName = fields.CharField(255, null=True)
    totalOffers = fields.CharField(255, null=True)
