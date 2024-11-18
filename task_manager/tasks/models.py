from django.db import models

# Create your models here.

class Task(models.Model):
    tache = models.CharField(max_length=200)
    
    description = models.CharField(max_length=200 , blank=True)

    datedecreation = models.DateTimeField(auto_now_add= True)

    date_echeance = models.DateTimeField(null=True, blank=True)

    STATUT_CHOICES = [
                    
                    ('to do' , 'A faire'),
                    ('in progress' , 'en cours'),
                    ('done' , 'terminer'),
                    
                    ]
    
    status = models.CharField(choices=STATUT_CHOICES , max_length=200)

    def __str__(self):
        return f"{self.tache} - {self.get_status_display()}" 