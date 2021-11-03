from tortoise import fields
from tortoise import models

from core.base.base_models import BaseCreatedUpdatedAtModel

class Information(BaseCreatedUpdatedAtModel, models.Model):

    id = fields.IntField(pk=True)
    state = fields.CharField(max_length=30, unique=True)
    cases = fields.IntField()
    deaths = fields.IntField()
    confirmed_cases = fields.IntField()
    confirmed_deaths = fields.IntField()

    class Meta:
        table = "information"

    def __str__(self):
        return self.id