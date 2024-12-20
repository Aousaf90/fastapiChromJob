from tortoise.models import Model
from tortoise import fields

class Offer(Model):
    offerID = fields.IntField(primary_key=True)
    offerName = fields.CharField(255, null=True)
    revenueModel = fields.CharField(255, null=True)
    payoutModel = fields.CharField(255, null=True)
    defaultPayout = fields.CharField(255, null=True)
    visibility = fields.CharField(255, null=True)
    status = fields.CharField(255, null=True)
    createdOn = fields.CharField(255, null=True)
    callTrackingEnabled = fields.CharField(255, null=True)
    mode = fields.CharField(255, null=True)
    previewURL = fields.CharField(255, null=True)
    featured = fields.CharField(255, null=True)
    enableRPS = fields.CharField(255, null=True)
    enablePPS = fields.CharField(255, null=True)
    paySalePercentage = fields.CharField(255, null=True)
    leadsPayoutMethod = fields.CharField(255, null=True)
    leadsPayoutAmount = fields.CharField(255, null=True)
    leadsPayoutPercentage = fields.CharField(255, null=True)
    callsPayoutMethod = fields.CharField(255, null=True)
    callsPayoutDuration = fields.CharField(255, null=True)
    buyerID = fields.CharField(255, null=True)
    buyerName = fields.CharField(255, null=True)
    verticalID = fields.CharField(255, null=True)
    verticalName = fields.CharField(255, null=True)
    defaultRevenue = fields.CharField(255, null=True)
