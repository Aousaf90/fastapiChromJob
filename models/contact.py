from tortoise.models import Model
from tortoise import fields

class Contact(Model):
    contactID = fields.IntField(primary_key=True)
    type = fields.CharField(255, null=True)
    typeID = fields.CharField(255, null=True)
    firstName = fields.CharField(255, null=True)
    lastName = fields.CharField(255, null=True)
    jobTitle = fields.CharField(255, null=True)
    emailAddress = fields.CharField(255, null=True)
    officePhone = fields.CharField(255, null=True)
    portalAccess = fields.CharField(255, null=True)
    phoneNumber = fields.CharField(255, null=True)
    ext = fields.CharField(255, null=True)
    massEmail = fields.CharField(255, null=True)
    role = fields.CharField(255, null=True)
    isPrimary = fields.CharField(255, null=True)
    permission_account = fields.CharField(255, null=True)
    permission_users = fields.CharField(255, null=True)
    permission_billing = fields.CharField(255, null=True)
    permission_offers = fields.CharField(255, null=True)
    permission_reports = fields.CharField(255, null=True)
    unsubNotifications = fields.CharField(255, null=True)
    requirePasswordReset = fields.CharField(255, null=True)
    status = fields.CharField(255, null=True)
    createdOn = fields.CharField(255, null=True)
    fullName = fields.CharField(255, null=True)