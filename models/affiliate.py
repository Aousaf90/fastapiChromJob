from tortoise.models import Model
from tortoise import fields

class Affiliate(Model):
    affiliateID = fields.IntField(primary_key=True)
    payoutTierID = fields.CharField(255, null=True)
    affiliateName = fields.CharField(255, null=True)
    accountManagerID = fields.CharField(255, null=True)
    apiAccess = fields.CharField(255, null=True)
    portalAccess = fields.CharField(255, null=True)
    status = fields.CharField(255, null=True)
    createdOn = fields.CharField(255, null=True)
    payoutTier = fields.CharField(255, null=True)
    accountManagerName = fields.CharField(255, null=True)
