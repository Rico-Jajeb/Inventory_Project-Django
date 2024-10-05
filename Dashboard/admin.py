from django.contrib import admin

#this is to import the items models to admin
from .models import cpu_items_db,gpu_items_db, mobo_items_db, ram_items_db, storage_items_db, keyboard_items_db, monitor_items_db, mouse_items_db, psu_items_db, cpu_fan_items_db, case_items_db, mousepad_items_db, headphone_items_db
#------this is for the transaction, defective, supplier models --
from .models import transactions, defective_items, all_supplier

# Register your models here.


#-- this is to display the all items_db into the django-admin
admin.site.register(cpu_items_db)  
admin.site.register(gpu_items_db)  
admin.site.register(mobo_items_db)  
admin.site.register(ram_items_db)  
admin.site.register(storage_items_db)  
admin.site.register(keyboard_items_db)  
admin.site.register(monitor_items_db)  
admin.site.register(mouse_items_db)  
admin.site.register(psu_items_db)  
admin.site.register(cpu_fan_items_db)  
admin.site.register(case_items_db)  
admin.site.register(mousepad_items_db)  
admin.site.register(headphone_items_db)  

#-- this to display transactions into the django-admin
admin.site.register(transactions)

#-- this to display defective into the django-admin
admin.site.register(defective_items)

#-- this to display supplier into the django-admin
admin.site.register(all_supplier)
