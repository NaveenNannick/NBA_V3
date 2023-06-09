from django.db import models

class CAY(models.Model):
    year = models.DateField(null=True,blank=True)
    STR = models.FloatField(null=True,blank=True,default=0.0)
    FCR = models.FloatField(null=True,blank=True)
    FQ = models.FloatField(null=True,blank=True)
    FR = models.FloatField(null=True,blank=True)
    FP = models.FloatField(null=True,blank=True)
    IWO = models.FloatField(null=True,blank=True)
    FRP = models.FloatField(null=True,blank=True)
    TOTAL = models.FloatField(null=True,blank=True)

    @property
    def year_value(self):
        if self.year:
            return self.year.year
        else:
            return None
    
    