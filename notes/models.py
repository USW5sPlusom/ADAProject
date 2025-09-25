from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, default = '')
    created = models.DateField(auto_now_add=True)

    class Meta:
        pass
    
    def __str__():
        pass
