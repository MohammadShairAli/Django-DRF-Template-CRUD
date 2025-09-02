from django.db import models
class Colours(models.Model):
    choices = (
        ("green","green"),
        ("red","red"),
        ("pink","pink")
    )
    colourName = models.CharField(max_length=10,choices=choices, blank=False, null=False)

    def __str__(self):
        return self.colourName
