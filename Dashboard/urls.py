from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path('',views.MainPage, name='MainPage'),
 
#--------------------- dashboard ------------------------
   path('dashboard',views.dashboard, name='dashboard'),
   path('sample',views.sample, name='sample'),

    #-- this is for out_of_stock items in dashboard
   path('out_of_stock_result',views.out_of_stock_result, name='out_of_stock_result'),

    #-- this is for low_of_stock items in dashboard
   path('low_of_stock_result',views.low_of_stock_result, name='low_of_stock_result'),



#-------------------- form for update -----------------------
    path('item_form',views.item_form, name='item_form'),


#--------------------- (urls for search Items) -----------------------
    path('search',views.search, name='search'),

    #-- url link for the item searched
    path('search_item_redirect/<item_id>',views.search_item_redirect, name='search_item_redirect'),




#--------------------- (urls display Items) -----------------------
    path('allitems',views.allitems, name='allitems'), #-- To display item Section

    path('cpu_table',views.cpu_table, name='cpu_table'), #-- To display cpu_table
    path('gpu_table',views.gpu_table, name='gpu_table'), #-- To display gpu_table
    path('mobo_table',views.mobo_table, name='mobo_table'), #-- To display mother board _table
    path('ram_table',views.ram_table, name='ram_table'), #-- To display ram table
    path('storage_table',views.storage_table, name='storage_table'), #-- To display storage tab;e
    path('keyboard_table',views.keyboard_table, name='keyboard_table'), #-- To display keyboard_table
    path('monitor_table',views.monitor_table, name='monitor_table'), #-- To display monitor_table
    path('mouse_table',views.mouse_table, name='mouse_table'), #-- To display mouse_table
    path('psu_table',views.psu_table, name='psu_table'), #-- To display psu_table
    path('cpu_fan_table',views.cpu_fan_table, name='cpu_fan_table'), #-- To display cpu_fan_table
    path('case_table',views.case_table, name='case_table'), #-- To display System unit case_table
    path('mousepad_table',views.mousepad_table, name='mousepad_table'), #-- To display mousepad_table
    path('headphone_table',views.headphone_table, name='headphone_table'), #-- To display headphone_table



#--------------------- (urls insert items data) --------------------
    path('insert_cpu_items',views.insert_cpu_items, name='insert_cpu_items'), #-- to insert data into cpu
    path('insert_gpu_items',views.insert_gpu_items, name='insert_gpu_items'), #-- to insert data into gpu
    path('insert_mobo_items',views.insert_mobo_items, name='insert_mobo_items'), #-- to insert data into mobo
    path('insert_ram_items',views.insert_ram_items, name='insert_ram_items'), #-- to insert data into ram
    path('insert_storage_items',views.insert_storage_items, name='insert_storage_items'), #-- to insert data into storage
    path('insert_keyboard_items',views.insert_keyboard_items, name='insert_keyboard_items'), #-- to insert data into Keyboard
    path('insert_monitor_items',views.insert_monitor_items, name='insert_monitor_items'), #-- to insert data into Monitor
    path('insert_mouse_items',views.insert_mouse_items, name='insert_mouse_items'), #-- to insert data into Mouse
    path('insert_psu_items',views.insert_psu_items, name='insert_psu_items'), #-- to insert data into power supply
    path('insert_cpu_fan_items',views.insert_cpu_fan_items, name='insert_cpu_fan_items'), #-- to insert data into cpu cooler/fan
    path('insert_case_items',views.insert_case_items, name='insert_case_items'), #-- to insert data into  system unit case
    path('insert_mousepad_items',views.insert_mousepad_items, name='insert_mousepad_items'), #-- to insert data into  mousepad
    path('insert_headphone_items',views.insert_headphone_items, name='insert_headphone_items'), #-- to insert data into  headphone
  
 


#--------------------- (urls delete items data) --------------------
    path('delete_cpu_items/<item_id>',views.delete_cpu_items, name='delete_cpu_items'), #-- to delete cpu item data
    path('delete_gpu_items/<item_id>',views.delete_gpu_items, name='delete_gpu_items'), #-- to delete gpu item data
    path('delete_mobo_items/<item_id>',views.delete_mobo_items, name='delete_mobo_items'), #-- to delete mobo item data
    path('delete_ram_items/<item_id>',views.delete_ram_items, name='delete_ram_items'), #-- to delete ram item data
    path('delete_storage_items/<item_id>',views.delete_storage_items, name='delete_storage_items'), #-- to delete storage item data
    path('delete_keyboard_items/<item_id>',views.delete_keyboard_items, name='delete_keyboard_items'), #-- to delete storage item data
    path('delete_monitor_items/<item_id>',views.delete_monitor_items, name='delete_monitor_items'), #-- to delete monitor item data
    path('delete_mouse_items/<item_id>',views.delete_mouse_items, name='delete_mouse_items'), #-- to delete Mouse item data
    path('delete_psu_items/<item_id>',views.delete_psu_items, name='delete_psu_items'), #-- to delete powerSupply item data
    path('delete_cpu_fan_items/<item_id>',views.delete_cpu_fan_items, name='delete_cpu_fan_items'), #-- to delete cpu cooler/fan item data
    path('delete_case_items/<item_id>',views.delete_case_items, name='delete_case_items'), #-- to delete system unit case item data
    path('delete_mousepad_items/<item_id>',views.delete_mousepad_items, name='delete_mousepad_items'), #-- to delete mousepad item data
    path('delete_headphone_items/<item_id>',views.delete_headphone_items, name='delete_headphone_items'), #-- to delete headphone item data



    path('delete_all_cpu_items',views.delete_all_cpu_items, name='delete_all_cpu_items'), #-- Delete all Cpu Data
    path('delete_all_gpu_items',views.delete_all_gpu_items, name='delete_all_gpu_items'), #-- Delete all gpu Data
    path('delete_all_mobo_items',views.delete_all_mobo_items, name='delete_all_mobo_items'), #-- Delete all motherboard Data
    path('delete_all_ram_items',views.delete_all_ram_items, name='delete_all_ram_items'), #-- Delete all Ram Data
    path('delete_all_storage_items',views.delete_all_storage_items, name='delete_all_storage_items'), #-- Delete all storage Data
    path('delete_all_keyboard_items',views.delete_all_keyboard_items, name='delete_all_keyboard_items'), #-- Delete all keyboard Data
    path('delete_all_monitor_items',views.delete_all_monitor_items, name='delete_all_monitor_items'), #-- Delete all monitor Data
    path('delete_all_mouse_items',views.delete_all_mouse_items, name='delete_all_mouse_items'), #-- Delete all mouse Data
    path('delete_all_psu_items',views.delete_all_psu_items, name='delete_all_psu_items'), #-- Delete all powerSupply Data
    path('delete_all_cpu_fan_items',views.delete_all_cpu_fan_items, name='delete_all_cpu_fan_items'), #-- Delete all cpu cooler/fan Data
    path('delete_all_case_items',views.delete_all_case_items, name='delete_all_case_items'), #-- Delete all system unit case Data
    path('delete_all_mousepad_items',views.delete_all_mousepad_items, name='delete_all_mousepad_items'), #-- Delete all mousepad Data
    path('delete_all_headphone_items',views.delete_all_headphone_items, name='delete_all_headphone_items'), #-- Delete all headphone Data
    

#--------------------- (urls to update items) ---------------------
    path('update_cpu_items/<item_id>',views.update_cpu_items, name='update_cpu_items'), #-- to update cpu items
    path('update_gpu_items/<item_id>',views.update_gpu_items, name='update_gpu_items'), #-- to update gpu items
    path('update_mobo_items/<item_id>',views.update_mobo_items, name='update_mobo_items'), #-- to update motherboard items
    path('update_ram_items/<item_id>',views.update_ram_items, name='update_ram_items'), #-- to update motherboard items
    path('update_storage_items/<item_id>',views.update_storage_items, name='update_storage_items'), #-- to update motherboard items
    path('update_keyboard_items/<item_id>',views.update_keyboard_items, name='update_keyboard_items'), #-- to update keyboard items
    path('update_monitor_items/<item_id>',views.update_monitor_items, name='update_monitor_items'), #-- to update monitor items
    path('update_mouse_items/<item_id>',views.update_mouse_items, name='update_mouse_items'), #-- to update mouse items
    path('update_psu_items/<item_id>',views.update_psu_items, name='update_psu_items'), #-- to update powersupply items
    path('update_cpu_fan_items/<item_id>',views.update_cpu_fan_items, name='update_cpu_fan_items'), #-- to update cpu cooler/fan items
    path('update_case_items/<item_id>',views.update_case_items, name='update_case_items'), #-- to update system unit case items
    path('update_mousepad_items/<item_id>',views.update_mousepad_items, name='update_mousepad_items'), #-- to update mousepad items
    path('update_headphone_items/<item_id>',views.update_headphone_items, name='update_headphone_items'), #-- to update headphone items


#---------------------------------------------- this is for Transaction section ------------------------------------>
   
    #-------- url to display transaction table --------
    path('transaction_table', views.transaction_table, name='transaction_table'),

    #-------- url to insert transaction data ---------
    path('insert_transaction', views.insert_transaction, name='insert_transaction'),

    #-------- to delete transaction  data --------------
    path('delete_transactions/<item_id>',views.delete_transactions, name='delete_transactions'), 

    #-------- url to delete all transaction data -------------
    path('delete_all_transactions', views.delete_all_transactions, name='delete_all_transactions'),

    #-------- to update transactions --------------------
    path('update_transactions/<item_id>',views.update_transactions, name='update_transactions'),


#---------------------------------------------- this is for Defective section ------------------------------------>
   
    #-------- url to display defective table --------
    path('defective_table', views.defective_table, name='defective_table'),

    #-------- url to insert defective data ---------
    path('insert_defective', views.insert_defective, name='insert_defective'),

    #-------- to delete defective  data --------------
    path('delete_defective/<item_id>',views.delete_defective, name='delete_defective'), 

    #-------- url to delete all defective data -------------
    path('delete_all_defective', views.delete_all_defective, name='delete_all_defective'),

    #-------- to update defective --------------------
    path('update_defective/<item_id>',views.update_defective, name='update_defective'),


#---------------------------------------------- this is for Supplier section ------------------------------------>
   
    #-------- url to display defective table --------
    path('supplier_table', views.supplier_table, name='supplier_table'),

    #-------- url to insert defective data ---------
    path('insert_supplier', views.insert_supplier, name='insert_supplier'),

    #-------- url to delete defective  data --------------
    path('delete_supplier/<item_id>',views.delete_supplier, name='delete_supplier'), 

    #-------- url to delete all defective data -------------
    path('delete_all_supplier', views.delete_all_supplier, name='delete_all_supplier'),

    #-------- url to update defective --------------------
    path('update_supplier/<item_id>',views.update_supplier, name='update_supplier'),
 

    #-------- url to contact supplier ----------------
    # path('contact',views.contact, name='contact'),
    path('contact/<item_id>',views.contact, name='contact'),





#--------------------- this is url for user -------------
    path('settings', views.settings, name='settings'),
    path('about', views.about, name='about'),
    path('address', views.address, name='address'),
    path('user_contact', views.user_contact, name='user_contact'),








]