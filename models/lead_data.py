from tortoise.models import Model
from tortoise import fields

class LeadData(Model):
    id = fields.IntField(primary_key=True)
    lead = fields.ForeignKeyField("models.Lead")
    leadID = fields.CharField(255, null=True)
    uniqueName = fields.CharField(255, null=True)
    fieldLabel = fields.CharField(255, null=True)
    value = fields.TextField(null=True)