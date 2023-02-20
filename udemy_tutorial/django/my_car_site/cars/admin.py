from django.contrib import admin
from .models import Car


# Register your models here.

class CarAdmin(admin.ModelAdmin):
    # if you want to change the order of fields in a specific order
    fields = ['year', 'brand']

    # # if you want to set information for each field
    # field_sets = [
    #     ('TIME INFORMATION', {'fields': ['year']}),
    #     ('CAR INFORMATION', {'fields': ['brand']})
    # ]


admin.site.register(Car, CarAdmin)
