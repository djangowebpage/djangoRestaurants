from django.contrib import admin

from .models import Pizza
from .models import Burger

# Register your models here.
class PizzaAdmin(admin.ModelAdmin):
    list_display =('name','priceM','priceL')
class BurguerAdmin(admin.ModelAdmin):
    list_display =('name','priceM','priceL')
admin.site.register(Pizza,PizzaAdmin)
admin.site.register(Burger,BurguerAdmin)