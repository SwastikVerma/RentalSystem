from django.contrib import admin

# from django.contrib import admin
from api.models import CarModel,Rent_history
# Register your models here..

class CarAdmin(admin.ModelAdmin):
    list_display=('Category','number_plate','current_city')
    
class Rent_historyAdmin(admin.ModelAdmin):
    list_display=('origin','destination','amount')

admin.site.register(CarModel,CarAdmin)
admin.site.register(Rent_history,Rent_historyAdmin)
