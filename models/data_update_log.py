from tortoise.models import Model
from tortoise import fields


class DataUpdateLog(Model):
    id = fields.IntField(pk=True)
    model_name = fields.CharField(max_length=255)  # Name of the model that was updated
    updated_at = fields.DatetimeField(auto_now_add=True)  # Timestamp when the update happened
    status = fields.CharField(max_length=50, default='success')  # Status of the update (e.g., success, failed)
    records_updated = fields.IntField(null=True)  # Number of records updated (optional)
    error_message = fields.TextField(null=True)  # Error message if the update failed (optional)
