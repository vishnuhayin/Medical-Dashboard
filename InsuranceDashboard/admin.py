from django.contrib import admin
from .models import KaggleTestInsurance,KaggleTrainInsurance,KaggleRegionInsurance

# Register your models here.

admin.site.register(KaggleTrainInsurance)
admin.site.register(KaggleTestInsurance)
admin.site.register(KaggleRegionInsurance)