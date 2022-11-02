"""
model for kaggle test data and train data
"""

from django.db import models

# Create your models here.


class KaggleTestInsurance(models.Model):
    """model for kaggle test data"""
    kaggle_id = models.IntegerField()
    perc_premium_paid_by_cash_credit = models.FloatField()
    age_in_days = models.IntegerField()
    income = models.IntegerField()
    Count_3_to_6_months_late = models.SmallIntegerField()
    Count_6_to_12_months_late = models.SmallIntegerField()
    Count_more_than_12_months_late = models.SmallIntegerField()
    application_underwriting_score = models.FloatField()
    no_of_premiums_paid = models.SmallIntegerField()
    sourcing_channel = models.CharField(max_length=5)
    residence_area_type = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Test (Insurance) data from Kaggle'

    #function for string repreentation of data
    def __str__(self):
        return f'{self.kaggle_id}-{self.residence_area_type}'

class KaggleTrainInsurance(models.Model):
    '''model for kaggle terain data'''
    kaggle_id = models.IntegerField()
    perc_premium_paid_by_cash_credit = models.FloatField()
    age_in_days = models.IntegerField()
    income = models.IntegerField()
    Count_3_to_6_months_late = models.SmallIntegerField()
    Count_6_to_12_months_late = models.SmallIntegerField()
    Count_more_than_12_months_late = models.SmallIntegerField()
    application_underwriting_score = models.FloatField()
    no_of_premiums_paid = models.SmallIntegerField()
    sourcing_channel = models.CharField(max_length=5)
    residence_area_type = models.CharField(max_length=50)
    premium = models.FloatField()
    target = models.SmallIntegerField()

    class Meta:
        verbose_name_plural = 'Train (Insurance) data from Kaggle'

    #function for string repreentation of data
    def __str__(self):
        return f'{self.kaggle_id} ({self.residence_area_type}) - Premium = {self.premium}'
    

class KaggleRegionInsurance(models.Model):
    age = models.IntegerField()
    sex = models.CharField(max_length=15)
    bmi = models.FloatField()
    children = models.IntegerField()
    smoker = models.BooleanField()
    region = models.CharField(max_length=50)
    charges = models.FloatField()

    class Meta:
        verbose_name_plural = 'Region based (Insurance) data from Kaggle'

    #function for string repreentation of data
    def __str__(self):
        return f'{self.sex} ({self.region}) - Age = {self.age}'
    