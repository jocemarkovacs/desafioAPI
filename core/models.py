from django.db import models

# Create your models here.

class Workspaces(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    kind = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    

    class Meta:        
        verbose_name = 'workspace'
        verbose_name_plural = 'workspaces'
        ordering = ['id']

    def __str__(self):
        return self.name

class Visits(models.Model):    
    id 
    dataField = models.DateField(auto_now_add=True)
    yearField = models.CharField(max_length=4)
    monthField = models.CharField(max_length=2)
    dayOfMonth = models.CharField(max_length=2)
    dayOfWeek = models.CharField(max_length=1)
    workspace = models.ForeignKey(
        Workspaces,
        on_delete=models.CASCADE,        
        related_name='workspace_id')
    

    class Meta:        
        verbose_name = 'visits'
        ordering = ['-id']
        
    def __date__(self):
        return self.dataField
