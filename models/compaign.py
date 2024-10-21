from tortoise.models import Model
from tortoise import fields

class Compaign(Model):
    campaignID = fields.IntField(primary_key=True)
    campaignName = fields.CharField(255, null=True)
    payout = fields.CharField(255, null=True)
    status = fields.CharField(255, null=True)
    isDefault = fields.CharField(255, null=True)
    createdOn = fields.CharField(255, null=True)
    revenueModel = fields.CharField(255, null=True)
    payoutModel = fields.CharField(255, null=True)
    affiliateID = fields.CharField(255, null=True)
    affiliateName = fields.CharField(255, null=True)
    offerID = fields.CharField(255, null=True)
    offerName = fields.CharField(255, null=True)
    verticalID = fields.CharField(255, null=True)
    verticalName = fields.CharField(255, null=True)
    mediaType = fields.CharField(255, null=True)
    payoutType = fields.CharField(255, null=True)
    revenueType = fields.CharField(255, null=True)
    revenue = fields.CharField(255, null=True)
