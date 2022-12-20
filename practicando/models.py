from tortoise.models import Model
from tortoise import fields

class Todo(Model):
    id = fields.IntField(pk = True)
    name  = fields.CharField(100)
    age = fields.IntField()
    date_created = fields.DatetimeField(auto_now_add = True)
    last_update =  fields.DatetimeField(auto_now = True)

    class Meta:
        ordering = ['date_created']