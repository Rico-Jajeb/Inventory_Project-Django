from django.db import models

# Create your models here.


class cpu_items_db(models.Model): #--- Cpu table ---
    name_model = models.CharField(max_length=100)
    brand      = models.CharField(max_length=100)
    descriptin = models.TextField()
    quantity   = models.IntegerField()
    price      = models.IntegerField()

    def __str__(self):
        return self.name_model

class gpu_items_db(models.Model): #--- Cpu table ---
    name_model = models.CharField(max_length=100)
    brand      = models.CharField(max_length=100)
    descriptin = models.TextField()
    quantity   = models.IntegerField()
    price      = models.IntegerField()

    def __str__(self):
        return self.name_model
        


class mobo_items_db(models.Model): #--- Mobo table ---
    name_model = models.CharField(max_length=100)
    brand      = models.CharField(max_length=100)
    descriptin = models.TextField()
    quantity   = models.IntegerField()
    price      = models.IntegerField()

    def __str__(self):
        return self.name_model

class ram_items_db(models.Model): #--- ram table ---
    name_model = models.CharField(max_length=100)
    brand      = models.CharField(max_length=100)
    descriptin = models.TextField()
    quantity   = models.IntegerField()
    price      = models.IntegerField()

    def __str__(self):
        return self.name_model

class storage_items_db(models.Model): #--- storage table ---
    name_model = models.CharField(max_length=100)
    brand      = models.CharField(max_length=100)
    descriptin = models.TextField()
    quantity   = models.IntegerField()
    price      = models.IntegerField()

    def __str__(self):
        return self.name_model

class keyboard_items_db(models.Model): #--- keyboard table ---
    name_model = models.CharField(max_length=100)
    brand      = models.CharField(max_length=100)
    descriptin = models.TextField()
    quantity   = models.IntegerField()
    price      = models.IntegerField()

    def __str__(self):
        return self.name_model

class monitor_items_db(models.Model): #--- monitor table ---
    name_model = models.CharField(max_length=100)
    brand      = models.CharField(max_length=100)
    descriptin = models.TextField()
    quantity   = models.IntegerField()
    price      = models.IntegerField()

    def __str__(self):
        return self.name_model

class mouse_items_db(models.Model): #--- mouse table ---
    name_model = models.CharField(max_length=100)
    brand      = models.CharField(max_length=100)
    descriptin = models.TextField()
    quantity   = models.IntegerField()
    price      = models.IntegerField()

    def __str__(self):
        return self.name_model

class psu_items_db(models.Model): #--- psu table ---
    name_model = models.CharField(max_length=100)
    brand      = models.CharField(max_length=100)
    descriptin = models.TextField()
    quantity   = models.IntegerField()
    price      = models.IntegerField()

    def __str__(self):
        return self.name_model

class cpu_fan_items_db(models.Model): #--- Cpu table ---
    name_model = models.CharField(max_length=100)
    brand      = models.CharField(max_length=100)
    descriptin = models.TextField()
    quantity   = models.IntegerField()
    price      = models.IntegerField()

    def __str__(self):
        return self.name_model

class case_items_db(models.Model): #--- Cpu table ---
    name_model = models.CharField(max_length=100)
    brand      = models.CharField(max_length=100)
    descriptin = models.TextField()
    quantity   = models.IntegerField()
    price      = models.IntegerField()

    def __str__(self):
        return self.name_model

class mousepad_items_db(models.Model): #--- Cpu table ---
    name_model = models.CharField(max_length=100)
    brand      = models.CharField(max_length=100)
    descriptin = models.TextField()
    quantity   = models.IntegerField()
    price      = models.IntegerField()

    def __str__(self):
        return self.name_model

class headphone_items_db(models.Model): #--- Cpu table ---
    name_model = models.CharField(max_length=100)
    brand      = models.CharField(max_length=100)
    descriptin = models.TextField()
    quantity   = models.IntegerField()
    price      = models.IntegerField()

    def __str__(self):
        return self.name_model




#-----------------------This is for transaction section ------------

class transactions(models.Model): #--- transactions table ---
    transac_date    = models.DateField()
    unit            = models.CharField(max_length=100)
    total_cost      = models.IntegerField()
    transac_person  = models.CharField(max_length=100)
    reference_no    = models.CharField(max_length=100)

    def __str__(self):
        return self.reference_no


#----------------------- This is for defective section ------------
class defective_items(models.Model): #--- defective table ----
    defect_date = models.DateField()
    item        = models.CharField(max_length=100)
    issue       = models.CharField(max_length=100)
    category    = models.CharField(max_length=100)

    def __str__(self):
        return self.item

#----------------------- This is for supplier section ------------
class all_supplier(models.Model): #--- supplier table ----
    supply_date = models.DateField()
    Name        = models.CharField(max_length=100)
    Company     = models.CharField(max_length=100)
    Email     = models.CharField(max_length=100)
    Supp_Item   = models.CharField(max_length=100)
    purchase    = models.IntegerField()

    def __str__(self):
        return self.Company