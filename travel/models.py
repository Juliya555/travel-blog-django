from django.db import models


class Place(models.Model):
    position_number = models.IntegerField(default=0)
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    why_go_description = models.CharField(max_length=256, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    fun_fact_description = models.CharField(max_length=128, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Place"
        verbose_name_plural = "Places"


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, blank=True, null=True, default=None, on_delete=models.SET_DEFAULT)  # link to place
    image = models.ImageField(upload_to="images/")  # download image

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"


class Subscriber(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    email = models.EmailField()

    def __str__(self):
        return "%s" % self.name
