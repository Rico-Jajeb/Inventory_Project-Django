from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

#--this is the all items table in model
from .models import cpu_items_db, gpu_items_db, mobo_items_db, ram_items_db, storage_items_db, keyboard_items_db, monitor_items_db, mouse_items_db, psu_items_db, cpu_fan_items_db, case_items_db, mousepad_items_db, headphone_items_db 

from .models import   transactions #-- this is the transactions table in model
from .models import   defective_items #-- this is the defective table in model
from .models import   all_supplier #-- this is the defective table in model


from django.db.models import Q #--this is for the query to filter the data to be searched
from django.core.paginator import Paginator  #-- this is for the pagination of items Tables

#--- this is for the update form for transaction, items, defective, supplier
from templates.forms.forms  import Items_form, transaction_form, defective_form, supplier_form, contact_form

#---- this is for the url of the page to change color ---
from django.urls import resolve


# Create your views here.


def MainPage(request):
    return render(request,'MainPage.html');

def sample(request):
    return render(request,'sample.html');

def dashboard(request):
    # --Get the number of items in all items
    all_cpu_items = cpu_items_db.objects.all().count()
    all_gpu_items = gpu_items_db.objects.all().count()
    all_mobo_items = mobo_items_db.objects.all().count()
    all_ram_items = ram_items_db.objects.all().count()
    all_storage_items = storage_items_db.objects.all().count()
    all_keyboard_items = keyboard_items_db.objects.all().count()
    all_monitor_items = monitor_items_db.objects.all().count()
    all_mouse_items = mouse_items_db.objects.all().count()
    all_psu_items = psu_items_db.objects.all().count()
    all_cpu_fan_items = cpu_fan_items_db.objects.all().count()
    all_case_items = case_items_db.objects.all().count()
    all_mousepad_items = mousepad_items_db.objects.all().count()
    all_headphone_items = headphone_items_db.objects.all().count()

    all_items = all_cpu_items + all_gpu_items + all_mobo_items + all_ram_items + all_storage_items + all_keyboard_items + all_monitor_items + all_mouse_items + all_psu_items + all_cpu_fan_items + all_case_items + all_mousepad_items + all_headphone_items
    #-- get the number of items that is out of stock
    out_of_stock_cpu = cpu_items_db.objects.filter(quantity=0).count()
    out_of_stock_gpu = gpu_items_db.objects.filter(quantity=0).count()
    out_of_stock_mobo = mobo_items_db.objects.filter(quantity=0).count()
    out_of_stock_ram = ram_items_db.objects.filter(quantity=0).count()
    out_of_stock_storage = storage_items_db.objects.filter(quantity=0).count()
    out_of_stock_keyboard = keyboard_items_db.objects.filter(quantity=0).count()
    out_of_stock_monitor = monitor_items_db.objects.filter(quantity=0).count()
    out_of_stock_mouse = mouse_items_db.objects.filter(quantity=0).count()
    out_of_stock_psu = psu_items_db.objects.filter(quantity=0).count()
    out_of_stock_cpu_fan = cpu_fan_items_db.objects.filter(quantity=0).count()
    out_of_stock_case = case_items_db.objects.filter(quantity=0).count()
    out_of_stock_mousepad = mousepad_items_db.objects.filter(quantity=0).count()
    out_of_stock_headphone = headphone_items_db.objects.filter(quantity=0).count()

    out_of_stock = out_of_stock_cpu + out_of_stock_gpu + out_of_stock_mobo + out_of_stock_ram + out_of_stock_storage + out_of_stock_keyboard + out_of_stock_monitor + out_of_stock_mouse + out_of_stock_psu + out_of_stock_cpu_fan + out_of_stock_case + out_of_stock_mousepad + out_of_stock_headphone

    #-- get the number of items that is low of stock
    low_of_stock_cpu = cpu_items_db.objects.filter(quantity__lte=5).filter(quantity__gt=0).count()
    low_of_stock_gpu = gpu_items_db.objects.filter(quantity__lte=5).filter(quantity__gt=0).count()
    low_of_stock_mobo = mobo_items_db.objects.filter(quantity__lte=5).filter(quantity__gt=0).count()
    low_of_stock_ram = ram_items_db.objects.filter(quantity__lte=5).filter(quantity__gt=0).count()
    low_of_stock_storage = storage_items_db.objects.filter(quantity__lte=5).filter(quantity__gt=0).count()
    low_of_stock_keyboard = keyboard_items_db.objects.filter(quantity__lte=5).filter(quantity__gt=0).count()
    low_of_stock_monitor = monitor_items_db.objects.filter(quantity__lte=5).filter(quantity__gt=0).count()
    low_of_stock_mouse = mouse_items_db.objects.filter(quantity__lte=5).filter(quantity__gt=0).count()
    low_of_stock_psu = psu_items_db.objects.filter(quantity__lte=5).filter(quantity__gt=0).count()
    low_of_stock_cpu_fan = cpu_fan_items_db.objects.filter(quantity__lte=5).filter(quantity__gt=0).count()
    low_of_stock_case = case_items_db.objects.filter(quantity__lte=5).filter(quantity__gt=0).count()
    low_of_stock_mousepad = mousepad_items_db.objects.filter(quantity__lte=5).filter(quantity__gt=0).count()
    low_of_stock_headphone = headphone_items_db.objects.filter(quantity__lte=5).filter(quantity__gt=0).count()

    low_of_stock = low_of_stock_cpu + low_of_stock_gpu + low_of_stock_mobo + low_of_stock_ram + low_of_stock_storage + low_of_stock_keyboard + low_of_stock_monitor + low_of_stock_mouse + low_of_stock_psu + low_of_stock_cpu_fan + low_of_stock_case + low_of_stock_mousepad + low_of_stock_headphone
    out_and_low = out_of_stock + low_of_stock
    remain_product = all_items - out_and_low
    return render(request, 'dashboard/dashboard.html', {'all_items':all_items, 'out_of_stock':out_of_stock, 'low_of_stock':low_of_stock , 'remain_product':remain_product});


def out_of_stock_result(request): #-- this is for the list of items that has zero stock
    out_of_stock_cpu = cpu_items_db.objects.filter(quantity=0)
    out_of_stock_gpu = gpu_items_db.objects.filter(quantity=0)
    out_of_stock_mobo = mobo_items_db.objects.filter(quantity=0)
    out_of_stock_ram = ram_items_db.objects.filter(quantity=0)
    out_of_stock_storage = storage_items_db.objects.filter(quantity=0)
    out_of_stock_keyboard = keyboard_items_db.objects.filter(quantity=0)
    out_of_stock_monitor = monitor_items_db.objects.filter(quantity=0)
    out_of_stock_mouse = mouse_items_db.objects.filter(quantity=0)
    out_of_stock_psu = psu_items_db.objects.filter(quantity=0)
    out_of_stock_cpu_fan = cpu_fan_items_db.objects.filter(quantity=0)
    out_of_stock_case = case_items_db.objects.filter(quantity=0)
    out_of_stock_mousepad = mousepad_items_db.objects.filter(quantity=0)
    out_of_stock_headphone = headphone_items_db.objects.filter(quantity=0)

    return render(request, 'dashboard/out_of_stock_list.html', {'out_of_stock_cpu':out_of_stock_cpu, 'out_of_stock_gpu':out_of_stock_gpu, 'out_of_stock_mobo':out_of_stock_mobo, 'out_of_stock_ram':out_of_stock_ram, 'out_of_stock_storage':out_of_stock_storage, 'out_of_stock_keyboard':out_of_stock_keyboard, 'out_of_stock_monitor':out_of_stock_monitor, 'out_of_stock_mouse':out_of_stock_mouse, 'out_of_stock_psu':out_of_stock_psu, 'out_of_stock_cpu_fan':out_of_stock_cpu_fan, 'out_of_stock_case':out_of_stock_case, 'out_of_stock_mousepad':out_of_stock_mousepad, 'out_of_stock_headphone':out_of_stock_headphone })

def low_of_stock_result(request):
    low_of_stock_cpu = cpu_items_db.objects.filter(quantity__lte=5).filter(quantity__gt=0)
    low_of_stock_gpu = gpu_items_db.objects.filter(quantity__lte=5).filter(quantity__gt=0)
    low_of_stock_mobo = mobo_items_db.objects.filter(quantity__lte=5).filter(quantity__gt=0)
    low_of_stock_ram = ram_items_db.objects.filter(quantity__lte=5).filter(quantity__gt=0)
    low_of_stock_storage = storage_items_db.objects.filter(quantity__lte=5).filter(quantity__gt=0)
    low_of_stock_keyboard = keyboard_items_db.objects.filter(quantity__lte=5).filter(quantity__gt=0)
    low_of_stock_monitor = monitor_items_db.objects.filter(quantity__lte=5).filter(quantity__gt=0)
    low_of_stock_mouse = mouse_items_db.objects.filter(quantity__lte=5).filter(quantity__gt=0)
    low_of_stock_psu = psu_items_db.objects.filter(quantity__lte=5).filter(quantity__gt=0)
    low_of_stock_cpu_fan = cpu_fan_items_db.objects.filter(quantity__lte=5).filter(quantity__gt=0)
    low_of_stock_case = case_items_db.objects.filter(quantity__lte=5).filter(quantity__gt=0)
    low_of_stock_mousepad = mousepad_items_db.objects.filter(quantity__lte=5).filter(quantity__gt=0)
    low_of_stock_headphone = headphone_items_db.objects.filter(quantity__lte=5).filter(quantity__gt=0)

    return render(request, 'dashboard/low_of_stock_list.html', {'low_of_stock_cpu':low_of_stock_cpu, 'low_of_stock_gpu':low_of_stock_gpu, 'low_of_stock_mobo':low_of_stock_mobo, 'low_of_stock_ram':low_of_stock_ram, 'low_of_stock_storage':low_of_stock_storage, 'low_of_stock_keyboard':low_of_stock_keyboard, 'low_of_stock_monitor':low_of_stock_monitor, 'low_of_stock_mouse':low_of_stock_mouse, 'low_of_stock_psu':low_of_stock_psu, 'low_of_stock_cpu_fan':low_of_stock_cpu_fan, 'low_of_stock_case':low_of_stock_case, 'low_of_stock_mousepad':low_of_stock_mousepad, 'low_of_stock_headphone':low_of_stock_headphone })







#------------------------------- form for items -------------------------
def item_form(request): #---This is the forms for updating the items
    submitted = False
    if request.method=='POST':
        form = Items_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('item_form?submitted=True')
    else:
        form = Items_form
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'forms/add_item.html', {'form': form, 'submitted': submitted});



#-------------------------- searching an items  ------------

def search(request): #this is for the item that will display when you search
    if request.method == "POST":
        searched = request.POST['searched']
        cpu_item_search = cpu_items_db.objects.filter(Q(name_model__contains=searched) | Q(brand__contains=searched) )
        gpu_item_search = gpu_items_db.objects.filter(Q(name_model__contains=searched) | Q(brand__contains=searched) )
        mobo_item_search = mobo_items_db.objects.filter(Q(name_model__contains=searched) | Q(brand__contains=searched) )
        ram_item_search = ram_items_db.objects.filter(Q(name_model__contains=searched) | Q(brand__contains=searched) )
        storage_item_search = storage_items_db.objects.filter(Q(name_model__contains=searched) | Q(brand__contains=searched) )
        keyboard_item_search = keyboard_items_db.objects.filter(Q(name_model__contains=searched) | Q(brand__contains=searched) )
        monitor_item_search = monitor_items_db.objects.filter(Q(name_model__contains=searched) | Q(brand__contains=searched) )
        mouse_item_search = mouse_items_db.objects.filter(Q(name_model__contains=searched) | Q(brand__contains=searched) )
        psu_item_search = psu_items_db.objects.filter(Q(name_model__contains=searched) | Q(brand__contains=searched) )
        cpu_fan_item_search = cpu_fan_items_db.objects.filter(Q(name_model__contains=searched) | Q(brand__contains=searched) )
        case_item_search = case_items_db.objects.filter(Q(name_model__contains=searched) | Q(brand__contains=searched) )
        mousepad_item_search = mousepad_items_db.objects.filter(Q(name_model__contains=searched) | Q(brand__contains=searched) )
        headphone_item_search = headphone_items_db.objects.filter(Q(name_model__contains=searched) | Q(brand__contains=searched) )
        item_search = list(cpu_item_search) + list(gpu_item_search) + list(mobo_item_search) + list(ram_item_search) + list(storage_item_search) + list(keyboard_item_search) + list(monitor_item_search) + list(mouse_item_search) + list(psu_item_search) + list(cpu_fan_item_search) + list(case_item_search) + list(mousepad_item_search) + list(headphone_item_search) 
        
        if not item_search:
            no_result_found = "no item found"
            return render(request, 'search/search.html', {'searched': searched, 'no_result_found': True})
        else:
            return render(request, 'search/search.html', {'searched': searched, 'item_search':item_search});
    else:
        
        return render(request, 'search/search.html',);


def search_item_redirect(request, item_id): #this is for the item search and when click get redirected to the item
    # Search for the item in all items databases
    try:
        cpu_items = [cpu_items_db.objects.get(pk=item_id)]
    except cpu_items_db.DoesNotExist:
        cpu_items = []
    try:
        gpu_items = [gpu_items_db.objects.get(pk=item_id)]
    except gpu_items_db.DoesNotExist:
        gpu_items = []
    try:
        mobo_items = [mobo_items_db.objects.get(pk=item_id)]
    except mobo_items_db.DoesNotExist:
        mobo_items = []
    try:
        ram_items = [ram_items_db.objects.get(pk=item_id)]
    except ram_items_db.DoesNotExist:
        ram_items = []
    try:
        storage_items = [storage_items_db.objects.get(pk=item_id)]
    except storage_items_db.DoesNotExist:
        storage_items = []
    try:
        keyboard_items = [keyboard_items_db.objects.get(pk=item_id)]
    except keyboard_items_db.DoesNotExist:
        keyboard_items = []
    try:
        monitor_items = [monitor_items_db.objects.get(pk=item_id)]
    except monitor_items_db.DoesNotExist:
        monitor_items = []
    try:
        mouse_items = [mouse_items_db.objects.get(pk=item_id)]
    except mouse_items_db.DoesNotExist:
        mouse_items = []
    try:
        psu_items = [psu_items_db.objects.get(pk=item_id)]
    except psu_items_db.DoesNotExist:
        psu_items = []
    try:
        cpu_fan_items = [cpu_fan_items_db.objects.get(pk=item_id)]
    except cpu_fan_items_db.DoesNotExist:
        cpu_fan_items = []
    try:
        case_items = [case_items_db.objects.get(pk=item_id)]
    except case_items_db.DoesNotExist:
        case_items = []
    try:
        mousepad_items = [mousepad_items_db.objects.get(pk=item_id)]
    except mousepad_items_db.DoesNotExist:
        mousepad_items = []
    try:
        headphone_items = [headphone_items_db.objects.get(pk=item_id)]
    except headphone_items_db.DoesNotExist:
        headphone_items = []

    # Render the template with both lists of items
    return render(request, 'search/search_bar_items.html', {'cpu_items': cpu_items, 'gpu_items': gpu_items, 'mobo_items':mobo_items, 'ram_items':ram_items, 'storage_items':storage_items, 'keyboard_items':keyboard_items, 'monitor_items':monitor_items, 'mouse_items':mouse_items, 'psu_items':psu_items, 'cpu_fan_items':cpu_fan_items, 'case_items':case_items, 'mousepad_items':mousepad_items, 'headphone_items':headphone_items})





#--------------------------------- (Display Items) ------------------------------
def allitems(request):  #-- To go into the Item Section in dashboard --
    return render(request, 'items/items.html',);


def cpu_table(request): #-- To display cpu items into table ------>
    cpu_items = cpu_items_db.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            if q.isdigit():
                cpu_paginate = cpu_items_db.objects.filter(Q(name_model__contains=q) | Q(brand__contains=q) | Q(quantity=q))
            else:
                cpu_paginate = cpu_items_db.objects.filter(Q(name_model__contains=q) | Q(brand__contains=q))
        else:
            return redirect('cpu_table')
    else:
        cpu_paginate = cpu_items_db.objects.all()
    #set up for pagination 
    paginate = Paginator(cpu_paginate, 5)
    page = request.GET.get('page', 1)
    cpu_paginate = paginate.page(page)
    return render(request, 'items/item_table/cpu_tb.html', {'cpu_items': cpu_items, 'cpu_paginate':cpu_paginate});


def gpu_table(request): #-- To display gpu items into table ------>
    gpu_items = gpu_items_db.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            if q.isdigit():
                gpu_paginate = gpu_items_db.objects.filter(Q(name_model__contains=q) | Q(brand__contains=q) | Q(quantity=q))
            else:
                gpu_paginate = gpu_items_db.objects.filter(Q(name_model__contains=q) | Q(brand__contains=q))
        else:
            return redirect('gpu_table')
    else:
        gpu_paginate = gpu_items_db.objects.all()
    #set up for pagination 
    paginate = Paginator(gpu_paginate, 5)
    page = request.GET.get('page', 1)
    gpu_paginate = paginate.page(page)
    return render(request, 'items/item_table/gpu_tb.html', {'gpu_items': gpu_items, 'gpu_paginate':gpu_paginate});


def mobo_table(request): #-- To display motherboard items into table ------>
    mobo_items = mobo_items_db.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            if q.isdigit():
                mobo_paginate = mobo_items_db.objects.filter(Q(name_model__contains=q) | Q(brand__contains=q) | Q(quantity=q))
            else:
                mobo_paginate = mobo_items_db.objects.filter(Q(name_model__contains=q) | Q(brand__contains=q))
        else:
            return redirect('mobo_table')
    else:
        mobo_paginate = mobo_items_db.objects.all()
    #set up for pagination 
    paginate = Paginator(mobo_paginate, 5)
    page = request.GET.get('page', 1)
    mobo_paginate = paginate.page(page)
    return render(request, 'items/item_table/mobo_tb.html', {'mobo_items': mobo_items, 'mobo_paginate':mobo_paginate});


def ram_table(request): #-- To display ram items into table ------>
    item_items = ram_items_db.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            if q.isdigit():
                item_paginate = ram_items_db.objects.filter(Q(name_model__contains=q) | Q(brand__contains=q) | Q(quantity=q))
            else:
                item_paginate = ram_items_db.objects.filter(Q(name_model__contains=q) | Q(brand__contains=q))
        else:
            return redirect('ram_table')
    else:
        item_paginate = ram_items_db.objects.all()
    #set up for pagination 
    paginate = Paginator(item_paginate, 5)
    page = request.GET.get('page', 1)
    item_paginate = paginate.page(page)
    return render(request, 'items/item_table/ram_tb.html', {'item_items': item_items, 'item_paginate':item_paginate});

def storage_table(request): #-- To display storage items into table ------>
    item_items = storage_items_db.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            if q.isdigit():
                item_paginate = storage_items_db.objects.filter(Q(name_model__contains=q) | Q(brand__contains=q) | Q(quantity=q))
            else:
                item_paginate = storage_items_db.objects.filter(Q(name_model__contains=q) | Q(brand__contains=q))
        else:
            return redirect('storage_table')
    else:
        item_paginate = storage_items_db.objects.all()
    #set up for pagination 
    paginate = Paginator(item_paginate, 5)
    page = request.GET.get('page', 1)
    item_paginate = paginate.page(page)
    return render(request, 'items/item_table/storage_tb.html', {'item_items': item_items, 'item_paginate':item_paginate});

def keyboard_table(request): #-- To display keyboard items into table ------>
    item_items = keyboard_items_db.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            if q.isdigit():
                item_paginate = keyboard_items_db.objects.filter(Q(name_model__contains=q) | Q(brand__contains=q) | Q(quantity=q))
            else:
                item_paginate = keyboard_items_db.objects.filter(Q(name_model__contains=q) | Q(brand__contains=q))
        else:
            return redirect('keyboard_table')
    else:
        item_paginate = keyboard_items_db.objects.all()
    #set up for pagination 
    paginate = Paginator(item_paginate, 5)
    page = request.GET.get('page', 1)
    item_paginate = paginate.page(page)
    return render(request, 'items/item_table/keyboard_tb.html', {'item_items': item_items, 'item_paginate':item_paginate});

def monitor_table(request): #-- To display Monitor items into table ------>
    item_items = monitor_items_db.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            if q.isdigit():
                item_paginate = monitor_items_db.objects.filter(Q(name_model__contains=q) | Q(brand__contains=q) | Q(quantity=q))
            else:
                item_paginate = monitor_items_db.objects.filter(Q(name_model__contains=q) | Q(brand__contains=q))
        else:
            return redirect('monitor_table')
    else:
        item_paginate = monitor_items_db.objects.all()
    #set up for pagination 
    paginate = Paginator(item_paginate, 5)
    page = request.GET.get('page', 1)
    item_paginate = paginate.page(page)
    return render(request, 'items/item_table/monitor_tb.html', {'item_items': item_items, 'item_paginate':item_paginate});

def mouse_table(request): #-- To display mouse items into table ------>
    item_items = mouse_items_db.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            if q.isdigit():
                item_paginate = mouse_items_db.objects.filter(Q(name_model__contains=q) | Q(brand__contains=q) | Q(quantity=q))
            else:
                item_paginate = mouse_items_db.objects.filter(Q(name_model__contains=q) | Q(brand__contains=q))
        else:
            return redirect('mouse_table')
    else:
        item_paginate = mouse_items_db.objects.all()
    #set up for pagination 
    paginate = Paginator(item_paginate, 5)
    page = request.GET.get('page', 1)
    item_paginate = paginate.page(page)
    return render(request, 'items/item_table/mouse_tb.html', {'item_items': item_items, 'item_paginate':item_paginate});


def psu_table(request): #-- To display power supply items into table ------>
    item_items = psu_items_db.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            if q.isdigit():
                item_paginate = psu_items_db.objects.filter(Q(name_model__contains=q) | Q(brand__contains=q) | Q(quantity=q))
            else:
                item_paginate = psu_items_db.objects.filter(Q(name_model__contains=q) | Q(brand__contains=q))
        else:
            return redirect('psu_table')
    else:
        item_paginate = psu_items_db.objects.all()
    #set up for pagination 
    paginate = Paginator(item_paginate, 5)
    page = request.GET.get('page', 1)
    item_paginate = paginate.page(page)
    return render(request, 'items/item_table/psu_tb.html', {'item_items': item_items, 'item_paginate':item_paginate});

def cpu_fan_table(request): #-- To display cpu cooler/fan items into table ------>
    item_items = cpu_fan_items_db.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            if q.isdigit():
                item_paginate = cpu_fan_items_db.objects.filter(Q(name_model__contains=q) | Q(brand__contains=q) | Q(quantity=q))
            else:
                item_paginate = cpu_fan_items_db.objects.filter(Q(name_model__contains=q) | Q(brand__contains=q))
        else:
            return redirect('cpu_fan_table')
    else:
        item_paginate = cpu_fan_items_db.objects.all()
    #set up for pagination 
    paginate = Paginator(item_paginate, 5)
    page = request.GET.get('page', 1)
    item_paginate = paginate.page(page)
    return render(request, 'items/item_table/cpu_fan_tb.html', {'item_items': item_items, 'item_paginate':item_paginate});

def case_table(request): #-- To display system unit case items into table ------>
    item_items = case_items_db.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            if q.isdigit():
                item_paginate = case_items_db.objects.filter(Q(name_model__contains=q) | Q(brand__contains=q) | Q(quantity=q))
            else:
                item_paginate = case_items_db.objects.filter(Q(name_model__contains=q) | Q(brand__contains=q))
        else:
            return redirect('case_table')
    else:
        item_paginate = case_items_db.objects.all()
    #set up for pagination 
    paginate = Paginator(item_paginate, 5)
    page = request.GET.get('page', 1)
    item_paginate = paginate.page(page)
    return render(request, 'items/item_table/case_tb.html', {'item_items': item_items, 'item_paginate':item_paginate});

def mousepad_table(request): #-- To display mousepad items into table ------>
    item_items = mousepad_items_db.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            if q.isdigit():
                item_paginate = mousepad_items_db.objects.filter(Q(name_model__contains=q) | Q(brand__contains=q) | Q(quantity=q))
            else:
                item_paginate = mousepad_items_db.objects.filter(Q(name_model__contains=q) | Q(brand__contains=q))
        else:
            return redirect('mousepad_table')
    else:
        item_paginate = mousepad_items_db.objects.all()
    #set up for pagination 
    paginate = Paginator(item_paginate, 5)
    page = request.GET.get('page', 1)
    item_paginate = paginate.page(page)
    return render(request, 'items/item_table/mousepad_tb.html', {'item_items': item_items, 'item_paginate':item_paginate});

def headphone_table(request): #-- To display headphone items into table ------>
    item_items = headphone_items_db.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            if q.isdigit():
                item_paginate = headphone_items_db.objects.filter(Q(name_model__contains=q) | Q(brand__contains=q) | Q(quantity=q))
            else:
                item_paginate = headphone_items_db.objects.filter(Q(name_model__contains=q) | Q(brand__contains=q))
        else:
            return redirect('headphone_table')
    else:
        item_paginate = headphone_items_db.objects.all()
    #set up for pagination 
    paginate = Paginator(item_paginate, 5)
    page = request.GET.get('page', 1)
    item_paginate = paginate.page(page)
    return render(request, 'items/item_table/headphone_tb.html', {'item_items': item_items, 'item_paginate':item_paginate});





#--------------------------------- Insert (Items) ---------------------------------

def insert_cpu_items(request):  #--To insert the data into cpu Table --
    if request.method=='POST':
        name_model = request.POST.get('name_model')
        brand = request.POST.get('brand')
        descriptin = request.POST.get('descriptin')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        cpu=cpu_items_db(name_model=name_model,brand=brand,descriptin=descriptin,quantity=quantity,price=price)
        cpu.save()
        success='Item  ' +name_model+ '  Save Successfully!!'
    return HttpResponse(success)

def insert_gpu_items(request):  #--To insert the data into gpu Table --
    if request.method=='POST':
        name_model = request.POST.get('name_model')
        brand = request.POST.get('brand')
        descriptin = request.POST.get('descriptin')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        gpu=gpu_items_db(name_model=name_model,brand=brand,descriptin=descriptin,quantity=quantity,price=price)
        gpu.save()
        success='Item  ' +name_model+ '  Save Successfully!!'
    return HttpResponse(success)

def insert_mobo_items(request):  #--To insert the data into gpu Table --
    if request.method=='POST':
        name_model = request.POST.get('name_model')
        brand = request.POST.get('brand')
        descriptin = request.POST.get('descriptin')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        mobo=mobo_items_db(name_model=name_model,brand=brand,descriptin=descriptin,quantity=quantity,price=price)
        mobo.save()
        success='Item  ' +name_model+ '  Save Successfully!!'
    return HttpResponse(success)

def insert_ram_items(request):  #--To insert the data into ram Table --
    if request.method=='POST':
        name_model = request.POST.get('name_model')
        brand = request.POST.get('brand')
        descriptin = request.POST.get('descriptin')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        item=ram_items_db(name_model=name_model,brand=brand,descriptin=descriptin,quantity=quantity,price=price)
        item.save()
        success='Item  ' +name_model+ '  Save Successfully!!'
    return HttpResponse(success)

def insert_storage_items(request):  #--To insert the data into storage Table --
    if request.method=='POST':
        name_model = request.POST.get('name_model')
        brand = request.POST.get('brand')
        descriptin = request.POST.get('descriptin')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        item=storage_items_db(name_model=name_model,brand=brand,descriptin=descriptin,quantity=quantity,price=price)
        item.save()
        success='Item  ' +name_model+ '  Save Successfully!!'
    return HttpResponse(success)

def insert_keyboard_items(request):  #--To insert the data into storage Table --
    if request.method=='POST':
        name_model = request.POST.get('name_model')
        brand = request.POST.get('brand')
        descriptin = request.POST.get('descriptin')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        item=keyboard_items_db(name_model=name_model,brand=brand,descriptin=descriptin,quantity=quantity,price=price)
        item.save()
        success='Item  ' +name_model+ '  Save Successfully!!'
    return HttpResponse(success)


def insert_monitor_items(request):  #--To insert the data into Monitor Table --
    if request.method=='POST':
        name_model = request.POST.get('name_model')
        brand = request.POST.get('brand')
        descriptin = request.POST.get('descriptin')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        item=monitor_items_db(name_model=name_model,brand=brand,descriptin=descriptin,quantity=quantity,price=price)
        item.save()
        success='Item  ' +name_model+ '  Save Successfully!!'
    return HttpResponse(success)

def insert_mouse_items(request):  #--To insert the data into Mouse Table --
    if request.method=='POST':
        name_model = request.POST.get('name_model')
        brand = request.POST.get('brand')
        descriptin = request.POST.get('descriptin')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        item=mouse_items_db(name_model=name_model,brand=brand,descriptin=descriptin,quantity=quantity,price=price)
        item.save()
        success='Item  ' +name_model+ '  Save Successfully!!'
    return HttpResponse(success)

def insert_psu_items(request):  #--To insert the data into power supply Table --
    if request.method=='POST':
        name_model = request.POST.get('name_model')
        brand = request.POST.get('brand')
        descriptin = request.POST.get('descriptin')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        item=psu_items_db(name_model=name_model,brand=brand,descriptin=descriptin,quantity=quantity,price=price)
        item.save()
        success='Item  ' +name_model+ '  Save Successfully!!'
    return HttpResponse(success)

def insert_cpu_fan_items(request):  #--To insert the data into cpu cooler/fan Table --
    if request.method=='POST':
        name_model = request.POST.get('name_model')
        brand = request.POST.get('brand')
        descriptin = request.POST.get('descriptin')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        item=cpu_fan_items_db(name_model=name_model,brand=brand,descriptin=descriptin,quantity=quantity,price=price)
        item.save()
        success='Item  ' +name_model+ '  Save Successfully!!'
    return HttpResponse(success)

def insert_case_items(request):  #--To insert the data into system unit case Table --
    if request.method=='POST':
        name_model = request.POST.get('name_model')
        brand = request.POST.get('brand')
        descriptin = request.POST.get('descriptin')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        item=case_items_db(name_model=name_model,brand=brand,descriptin=descriptin,quantity=quantity,price=price)
        item.save()
        success='Item  ' +name_model+ '  Save Successfully!!'
    return HttpResponse(success)

def insert_mousepad_items(request):  #--To insert the data into mouse Table --
    if request.method=='POST':
        name_model = request.POST.get('name_model')
        brand = request.POST.get('brand')
        descriptin = request.POST.get('descriptin')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        item=mousepad_items_db(name_model=name_model,brand=brand,descriptin=descriptin,quantity=quantity,price=price)
        item.save()
        success='Item  ' +name_model+ '  Save Successfully!!'
    return HttpResponse(success)

def insert_headphone_items(request):  #--To insert the data into headphone Table --
    if request.method=='POST':
        name_model = request.POST.get('name_model')
        brand = request.POST.get('brand')
        descriptin = request.POST.get('descriptin')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        item=headphone_items_db(name_model=name_model,brand=brand,descriptin=descriptin,quantity=quantity,price=price)
        item.save()
        success='Item  ' +name_model+ '  Save Successfully!!'
    return HttpResponse(success)






#--------------------------------- Delete (Items) ---------------------------------

def delete_cpu_items(request, item_id): #-- to delete single cpu items -->
    cpu_item = cpu_items_db.objects.get(pk=item_id)
    cpu_item.delete()
    return redirect('cpu_table')

def delete_gpu_items(request, item_id): #-- to delete single cpu items -->
    gpu_item = gpu_items_db.objects.get(pk=item_id)
    gpu_item.delete()
    return redirect('gpu_table')

def delete_mobo_items(request, item_id): #-- to delete single motherboard items -->
    item = mobo_items_db.objects.get(pk=item_id)
    item.delete()
    return redirect('mobo_table')

def delete_ram_items(request, item_id): #-- to delete single ram items -->
    item = ram_items_db.objects.get(pk=item_id)
    item.delete()
    return redirect('ram_table')

def delete_storage_items(request, item_id): #-- to delete single storage items -->
    item = storage_items_db.objects.get(pk=item_id)
    item.delete()
    return redirect('storage_table')

def delete_keyboard_items(request, item_id): #-- to delete single keyboard items -->
    item = keyboard_items_db.objects.get(pk=item_id)
    item.delete()
    return redirect('keyboard_table')

def delete_monitor_items(request, item_id): #-- to delete single monitor items -->
    item = monitor_items_db.objects.get(pk=item_id)
    item.delete()
    return redirect('monitor_table')

def delete_mouse_items(request, item_id): #-- to delete single monitor items -->
    item = mouse_items_db.objects.get(pk=item_id)
    item.delete()
    return redirect('mouse_table')

def delete_psu_items(request, item_id): #-- to delete single monitor items -->
    item = psu_items_db.objects.get(pk=item_id)
    item.delete()
    return redirect('psu_table')

def delete_cpu_fan_items(request, item_id): #-- to delete single monitor items -->
    item = cpu_fan_items_db.objects.get(pk=item_id)
    item.delete()
    return redirect('cpu_fan_table')

def delete_case_items(request, item_id): #-- to delete single monitor items -->
    item = case_items_db.objects.get(pk=item_id)
    item.delete()
    return redirect('case_table')


def delete_mousepad_items(request, item_id): #-- to delete single mousepad items -->
    item = mousepad_items_db.objects.get(pk=item_id)
    item.delete()
    return redirect('mousepad_table')

def delete_headphone_items(request, item_id): #-- to delete single headphone items -->
    item = headphone_items_db.objects.get(pk=item_id)
    item.delete()
    return redirect('headphone_table')



#--------------------------------- Delete all (items) ------------------------------

def delete_all_cpu_items(self):  #--to delete all cpu items -->
    cpu_items_db.objects.all().delete()
    return redirect('cpu_table')

def delete_all_gpu_items(self):  #--to delete all gpu items -->
    gpu_items_db.objects.all().delete()
    return redirect('gpu_table')

def delete_all_mobo_items(self):  #--to delete all motherboard items -->
    mobo_items_db.objects.all().delete()
    return redirect('mobo_table')

def delete_all_ram_items(self):  #--to delete all Ram items -->
    ram_items_db.objects.all().delete()
    return redirect('ram_table')

def delete_all_storage_items(self):  #--to delete all storage items -->
    storage_items_db.objects.all().delete()
    return redirect('storage_table')

def delete_all_keyboard_items(self):  #--to delete all storage items -->
    keyboard_items_db.objects.all().delete()
    return redirect('keyboard_table')

def delete_all_monitor_items(self):  #--to delete all Monitor items -->
    monitor_items_db.objects.all().delete()
    return redirect('monitor_table')

def delete_all_mouse_items(self):  #--to delete all Monitor items -->
    mouse_items_db.objects.all().delete()
    return redirect('mouse_table')

def delete_all_psu_items(self):  #--to delete all powerSupply items -->
    psu_items_db.objects.all().delete()
    return redirect('psu_table')

def delete_all_cpu_fan_items(self):  #--to delete all Cpu cooler/fan items -->
    cpu_fan_items_db.objects.all().delete()
    return redirect('cpu_fan_table')


def delete_all_case_items(self):  #--to delete all system unit case items -->
    case_items_db.objects.all().delete()
    return redirect('case_table')

def delete_all_mousepad_items(self):  #--to delete all mousepad items -->
    mousepad_items_db.objects.all().delete()
    return redirect('mousepad_table')

def delete_all_headphone_items(self):  #--to delete all mousepad items -->
    headphone_items_db.objects.all().delete()
    return redirect('headphone_table')




#--------------------------------- update (Items) ---------------------------------

def update_cpu_items(request, item_id): #--to update cpu items -->
    cpu_item = cpu_items_db.objects.get(pk=item_id)

    form = Items_form(request.POST or None ,instance=cpu_item)
    if form.is_valid():
        form.save()
        return redirect('cpu_table')
    return render(request, 'items/update_item/update_cpu_items.html', {'cpu_item': cpu_item, 'form':form});


def update_gpu_items(request, item_id): #--to update cpu items -->
    cpu_item = gpu_items_db.objects.get(pk=item_id)

    form = Items_form(request.POST or None ,instance=cpu_item)
    if form.is_valid():
        form.save()
        return redirect('gpu_table')
    return render(request, 'items/update_item/update_cpu_items.html', {'cpu_item': cpu_item, 'form':form});

def update_mobo_items(request, item_id): #--to update cpu items -->
    cpu_item = mobo_items_db.objects.get(pk=item_id)

    form = Items_form(request.POST or None ,instance=cpu_item)
    if form.is_valid():
        form.save()
        return redirect('mobo_table')
    return render(request, 'items/update_item/update_cpu_items.html', {'cpu_item': cpu_item, 'form':form});

def update_ram_items(request, item_id): #--to update ram items -->
    cpu_item = ram_items_db.objects.get(pk=item_id)

    form = Items_form(request.POST or None ,instance=cpu_item)
    if form.is_valid():
        form.save()
        return redirect('ram_table')
    return render(request, 'items/update_item/update_cpu_items.html', {'cpu_item': cpu_item, 'form':form});


def update_storage_items(request, item_id): #--to update ram items -->
    cpu_item = storage_items_db.objects.get(pk=item_id)

    form = Items_form(request.POST or None ,instance=cpu_item)
    if form.is_valid():
        form.save()
        return redirect('storage_table')
    return render(request, 'items/update_item/update_cpu_items.html', {'cpu_item': cpu_item, 'form':form});

def update_keyboard_items(request, item_id): #--to update keyboard items -->
    cpu_item = keyboard_items_db.objects.get(pk=item_id)

    form = Items_form(request.POST or None ,instance=cpu_item)
    if form.is_valid():
        form.save()
        return redirect('keyboard_table')
    return render(request, 'items/update_item/update_cpu_items.html', {'cpu_item': cpu_item, 'form':form});

def update_monitor_items(request, item_id): #--to update monitor items -->
    cpu_item = monitor_items_db.objects.get(pk=item_id)

    form = Items_form(request.POST or None ,instance=cpu_item)
    if form.is_valid():
        form.save()
        return redirect('monitor_table')
    return render(request, 'items/update_item/update_cpu_items.html', {'cpu_item': cpu_item, 'form':form});


def update_mouse_items(request, item_id): #--to update mouse items -->
    cpu_item = mouse_items_db.objects.get(pk=item_id)

    form = Items_form(request.POST or None ,instance=cpu_item)
    if form.is_valid():
        form.save()
        return redirect('mouse_table')
    return render(request, 'items/update_item/update_cpu_items.html', {'cpu_item': cpu_item, 'form':form});

def update_psu_items(request, item_id): #--to update powersupply items -->
    cpu_item = psu_items_db.objects.get(pk=item_id)

    form = Items_form(request.POST or None ,instance=cpu_item)
    if form.is_valid():
        form.save()
        return redirect('psu_table')
    return render(request, 'items/update_item/update_cpu_items.html', {'cpu_item': cpu_item, 'form':form});

def update_cpu_fan_items(request, item_id): #--to update cpu cooler/fan items -->
    cpu_item = cpu_fan_items_db.objects.get(pk=item_id)

    form = Items_form(request.POST or None ,instance=cpu_item)
    if form.is_valid():
        form.save()
        return redirect('cpu_fan_table')
    return render(request, 'items/update_item/update_cpu_items.html', {'cpu_item': cpu_item, 'form':form});

def update_case_items(request, item_id): #--to update system unit case items -->
    cpu_item = case_items_db.objects.get(pk=item_id)

    form = Items_form(request.POST or None ,instance=cpu_item)
    if form.is_valid():
        form.save()
        return redirect('case_table')
    return render(request, 'items/update_item/update_cpu_items.html', {'cpu_item': cpu_item, 'form':form});

def update_mousepad_items(request, item_id): #--to update system unit case items -->
    cpu_item = mousepad_items_db.objects.get(pk=item_id)

    form = Items_form(request.POST or None ,instance=cpu_item)
    if form.is_valid():
        form.save()
        return redirect('mousepad_table')
    return render(request, 'items/update_item/update_cpu_items.html', {'cpu_item': cpu_item, 'form':form});


def update_headphone_items(request, item_id): #--to update system unit case items -->
    cpu_item = headphone_items_db.objects.get(pk=item_id)

    form = Items_form(request.POST or None ,instance=cpu_item)
    if form.is_valid():
        form.save()
        return redirect('headphone_table')
    return render(request, 'items/update_item/update_cpu_items.html', {'cpu_item': cpu_item, 'form':form});






#***********************************************  this is transaction section *********************************************** 

def transaction_table(request): #-- To display transactions into table ------>
    transaction_items = transactions.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            if q.isdigit():
                transaction_paginate = transactions.objects.filter(Q(transac_person__contains=q) | Q(reference_no__contains=q) | Q(total_cost=q))
            else:
                transaction_paginate = transactions.objects.filter(Q(transac_person__contains=q) | Q(reference_no__contains=q))
        else:
            return redirect('transaction_table')
    else:
        transaction_paginate = transactions.objects.all()
    #set up for pagination 
    paginate = Paginator(transaction_paginate, 5)
    page = request.GET.get('page', 1)
    transaction_paginate = paginate.page(page)
    return render(request, 'transaction/transaction.html', {'transaction_items':transaction_items, 'transaction_paginate':transaction_paginate })

def insert_transaction(request):  #--To insert the data into headphone Table --
    if request.method=='POST':
        transac_date = request.POST.get('transac_date')
        unit = request.POST.get('unit')
        total_cost = request.POST.get('total_cost')
        transac_person = request.POST.get('transac_person')
        reference_no = request.POST.get('reference_no')

        transac=transactions(transac_date=transac_date,unit=unit,total_cost=total_cost,transac_person=transac_person,reference_no=reference_no)
        transac.save()
        success='Transaction  ' +reference_no+ '  Save Successfully!!'
    return HttpResponse(success)

def delete_transactions(request, item_id): #-- to delete single transactions -->
    transac = transactions.objects.get(pk=item_id)
    transac.delete()
    return redirect('transaction_table')

def delete_all_transactions(self):  #--to delete all transaction data -->
    transactions.objects.all().delete()
    return redirect('transaction_table')

def update_transactions(request, item_id): #--to update system unit case items -->
    transac_ref = transactions.objects.get(pk=item_id)
    form = transaction_form(request.POST or None ,instance=transac_ref)
    if form.is_valid():
        form.save()
        return redirect('transaction_table')
    return render(request, 'transaction/update_transactions.html', {'transac_ref': transac_ref, 'form':form});






#*********************************************** this is Defective items section *********************************************** 

def defective_table(request): #-- To display transactions into table ------>
    defective = defective_items.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            if q.isdigit():
                defective_paginate = defective_items.objects.filter(Q(item__contains=q) | Q(category__contains=q) | Q(issue=q))
            else:
                defective_paginate = defective_items.objects.filter(Q(item__contains=q) | Q(category__contains=q))
        else:
            return redirect('defective_table')
    else:
        defective_paginate = defective_items.objects.all()
    #set up for pagination 
    paginate = Paginator(defective_paginate, 5)
    page = request.GET.get('page', 1)
    defective_paginate = paginate.page(page)
    return render(request, 'defective/defective.html', {'defective':defective, 'defective_paginate':defective_paginate })


def insert_defective(request): #-------- to insert data into defective table --
    success = ""  # default value for 'success'
    if request.method=='POST':
        defect_date = request.POST.get('defect_date')
        item = request.POST.get('item')
        issue = request.POST.get('issue')
        category = request.POST.get('category')
      

        defect=defective_items(defect_date=defect_date, item=item, issue=issue, category=category,)
        defect.save()
        success='Defective  ' +category+ '  Save Successfully!!'
    return HttpResponse(success)


def delete_defective(request, item_id): #-- to delete single defective -->
    defect = defective_items.objects.get(pk=item_id)
    defect.delete()
    return redirect('defective_table')


def delete_all_defective(self):  #--to delete all transaction data -->
    defective_items.objects.all().delete()
    return redirect('defective_table')


def update_defective(request, item_id): #--to update system unit case items -->
    items = defective_items.objects.get(pk=item_id)

    form = defective_form(request.POST or None ,instance=items)
    if form.is_valid():
        form.save()
        return redirect('defective_table')
    return render(request, 'defective/update_defective.html', {'items': items, 'form':form});



#****************************************************************************************** 
#                                THIS IS SUPPLIER SECTION
#******************************************************************************************

def supplier_table(request): #-- To display suppliers into table ------>
    supply = all_supplier.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            if q.isdigit():
                supplier_paginate = all_supplier.objects.filter(Q(Name__contains=q) | Q(Company__contains=q) | Q(purchase=q))
            else:
                supplier_paginate = all_supplier.objects.filter(Q(Name__contains=q) | Q(Company__contains=q))
        else:
            return redirect('defective_table')
    else:
        supplier_paginate = all_supplier.objects.all()
    #set up for pagination 
    paginate = Paginator(supplier_paginate, 5)
    page = request.GET.get('page', 1)
    supplier_paginate = paginate.page(page)
    return render(request, 'supplier/supplier.html', {'supply':supply, 'supplier_paginate':supplier_paginate })


def insert_supplier(request): #-------- to insert data into defective table --
    success = ""  # default value for 'success'
    if request.method=='POST':
        supply_date = request.POST.get('supply_date')
        Name = request.POST.get('Name')
        Company = request.POST.get('Company')
        Email = request.POST.get('Email')
        Supp_Item = request.POST.get('Supp_Item')
        purchase = request.POST.get('purchase')
      

        supply=all_supplier(supply_date=supply_date, Name=Name, Company=Company, Email=Email, Supp_Item=Supp_Item, purchase=purchase)
        supply.save()
        success='Defective  ' +Name+ '  Save Successfully!!'
    return HttpResponse(success)


def delete_supplier(request, item_id): #-- to delete single defective -->
    delete = all_supplier.objects.get(pk=item_id)
    delete.delete()
    return redirect('supplier_table')


def delete_all_supplier(self):  #--to delete all transaction data -->
    all_supplier.objects.all().delete()
    return redirect('supplier_table')


def update_supplier(request, item_id): #--to update system unit case items -->
    supply = all_supplier.objects.get(pk=item_id)

    form = supplier_form(request.POST or None ,instance=supply)
    if form.is_valid():
        form.save()
        return redirect('supplier_table')
    return render(request, 'supplier/update_supplier.html', {'supply': supply, 'form':form});


def contact(request, item_id): #-- to contact the supplier -->
    supply = all_supplier.objects.get(pk=item_id)
    
    form = contact_form(request.POST or None ,instance=supply)
    return render(request, 'supplier/contact.html', {'form':form})


#--------------------------- This is for user section -----------

def settings(request):
    return render(request, 'user/settings.html');

def about(request):
    return render(request, 'user/about.html');
def address(request):
    return render(request, 'user/address.html');
def user_contact(request):
    return render(request, 'user/contact.html');



