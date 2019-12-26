from django.shortcuts import render,redirect
from  django.http import HttpResponse
from .models import *
from .models import products
from .forms import OrderForm
# Create your views here.


def home(request):
    orders= order.objects.all()
    customers_list= Customer.objects.all()

    total_coustomer=customers_list.count()
    total_order=orders.count()
    delivered_ord=orders.filter(status='Delivered').count()
    pending_ord=orders.filter(status='Pending').count()
    context={'orders':orders,'customers_list':customers_list,'total_coustomer':total_coustomer,
             'total_order':total_order,'delivered_ord':delivered_ord,'pending_ord':pending_ord}
    return render(request,'accounts/dashboard.html',context)

def products_list(request):
    Products_list   =  products.objects.all()

    return render(request,'accounts/products.html',{'list':Products_list})

def customer(request,pk_test):
    customer= Customer.objects.get(id=pk_test)
    orders=customer.order_set.all()
    context={
        'customer':customer,'orders':orders
    }
    return render(request,'accounts/customer.html',context)

def CreateOrder(request):
    form = OrderForm()
    if request.method =='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
    'form':form
    }
    return render(request,'accounts/order_form.html',context)

def UpdateOrder(request, pk_update):
    Order=order.objects.get(id=pk_update)
    form=OrderForm(instance=Order)
    if request.method=='POST':
        form=OrderForm(request.POST, instance=Order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
        'form':form
    }
    return render(request,'accounts/update_order.html',context)


def delateOrder(request, pk):
    Order=order.objects.get(id=pk)
    if request.method=="POST":
        Order.delete()
        return redirect('/')
    context=    {'item':Order}
    return render(request,'accounts/delete.html',context)