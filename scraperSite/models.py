from django.db import models


# Create your models here.
class Link(models.Model):
    address = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    # When we refer to this object we get the name of the link, instead of the object of the Link
    def __str__(self):
        # Use self.name if it's not None, otherwise return a default string. Or if the link doesn't have a name
        return self.name or "Unnamed Link"