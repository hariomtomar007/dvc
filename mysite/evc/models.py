from django.db import models
from django.db import models
import uuid

# Create your models here.
class Model(models.Model):
    '''
    model defined to hold the information of aimodel
    '''
    id = models.UUIDField(primary_key=True,
                        default=uuid.uuid4,
                        editable=False,
                        db_index=True)
    name = models.CharField(max_length=1000, blank=True)
    commit_id = models.CharField(max_length=1000, blank=True)
    project_name = models.CharField(max_length=1000, blank=True)


    def __str__(self):
        return f"{self.name}"