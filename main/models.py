from django.db import models

# Create your models here.
class Diabetes (models.Model):
    Name = models.CharField(max_length=100)
    Pregnancies = models.IntegerField()
    Glucose = models.FloatField()
    BloodPressure = models.FloatField()
    SkinThickness = models.FloatField()
    Insulin = models.FloatField()
    Height = models.FloatField()
    Weight = models.FloatField()
    DiabetesPedigreeFunction = models.FloatField()
    Age = models.IntegerField()
    Percentage = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.Name