from django.db import models

class Todo(models.Model):
    # create model that have title, description, completed, and id auto increment

    def __str__(self):
        return self.title
    
