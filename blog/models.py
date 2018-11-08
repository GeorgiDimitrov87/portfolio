from django.db import models

# Create your models here.
#title
# publication date
#body
#image

from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')


# Adding the Blog app to the settings
# Create migration
# migrate
# add to the admin
