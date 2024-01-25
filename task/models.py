from django.db import models

# Create your models here
class CreateTask(models.Model):
    title=models.CharField(max_length=200)
    create_date=models.DateTimeField()
    user_name=models.CharField(max_length=200)
    options=(
        ("pending","pending"),
        ("inprogress","inprogress"),
        ("done","done")
    )
    status=models.CharField(max_length=200,choices=options,default="pending")
    def __str__(self):
        return self.title
        

