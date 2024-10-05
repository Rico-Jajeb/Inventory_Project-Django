from django import forms
from django.forms import ModelForm
from Dashboard.models import cpu_items_db, transactions, defective_items, all_supplier


#--Create a item forms 
class Items_form(ModelForm):
    class Meta:
        model = cpu_items_db
        fields = ('name_model', 'brand', 'descriptin', 'quantity', 'price')

        widgets = {
            'name_model': forms.TextInput(attrs={'class':'itmInput_update', }),
            'brand': forms.TextInput(attrs={'class':'itmInput_update', }),
            'descriptin': forms.TextInput(attrs={'class':'itmInput_update'}),
            'quantity': forms.NumberInput(attrs={'class':'itmInput_update'}),
            'price': forms.NumberInput(attrs={'class':'itmInput_update', }),
        }

        # fields = "__all__"   #para makuha tanan na column an aadto ha model like an name/brand/price etc



class transaction_form(ModelForm): #---- this is for transaction form ----
    class Meta:
        model = transactions
        fields = ('transac_date', 'unit', 'total_cost', 'transac_person', 'reference_no')

        widgets = {
            'transac_date': forms.DateInput(attrs={'class':'itmInput_update'}),
            'unit': forms.TextInput(attrs={'class':'itmInput_update', }),
            'total_cost': forms.NumberInput(attrs={'class':'itmInput_update'}),
            'transac_person': forms.TextInput(attrs={'class':'itmInput_update', }),
            'reference_no': forms.TextInput(attrs={'class':'itmInput_update', }),
        }


class defective_form(ModelForm): #---- this is for defective form ----
    class Meta:
        model = defective_items
        fields = ('defect_date', 'item', 'issue', 'category')

        widgets = {
            'defect_date': forms.DateInput(attrs={'class':'itmInput_update'}),
            'item': forms.TextInput(attrs={'class':'itmInput_update', }),
            'issue': forms.TextInput(attrs={'class':'itmInput_update'}),
            'category': forms.TextInput(attrs={'class':'itmInput_update', }),
        }

class supplier_form(ModelForm): #---- this is for supplier form ----
    class Meta:
        model = all_supplier
        fields = ('supply_date', 'Name', 'Company', 'Email', 'Supp_Item', 'purchase')

        widgets = {
            'supply_date': forms.DateInput(attrs={'class':'itmInput_update'}),
            'Name': forms.TextInput(attrs={'class':'itmInput_update', }),
            'Company': forms.TextInput(attrs={'class':'itmInput_update'}),
            'Email': forms.EmailInput(attrs={'class':'itmInput_update', }),
            'Supp_Item': forms.TextInput(attrs={'class':'itmInput_update', }),
            'purchase': forms.NumberInput(attrs={'class':'itmInput_update', }),
        }

class contact_form(ModelForm): #---- this is for supplier form ----
    class Meta:
        model = all_supplier
        fields = ('Name',  'Email')

        widgets = {
            'Name': forms.TextInput(attrs={'class':'form-control mb-3', }),
            'Email': forms.EmailInput(attrs={'class':'form-control mb-3', }),

        }


