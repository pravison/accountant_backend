from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TenantRegistrationForm, RegistrationForm, InvoiceForm
from . models import Client, Domain, IntrestedClient, Invoice
#from django_tenants.utils import schema_context
from users.models import User
from django.contrib.auth.decorators import login_required
from homepage.models import Company, Contact_us, Social_Links

# Create your views here.

def tenantRegistration(request):
    infos = Company.objects.order_by('id')[:1]
    contacts_infos = Contact_us.objects.order_by('id')[:1]
    links = Social_Links.objects.all()
    if request.method == 'POST':
        form = TenantRegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            business_name = form.cleaned_data['business_name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            location = form.cleaned_data['location']
            refferal_code = form.cleaned_data['refferal_code']
            # will write th elogic to handle ontrial and paid until
            on_trial = True
            paid_until = '2024-07-05'

            def remove(business_name):
                return "".join(business_name.split())
            business = remove(business_name)
            business_lower = business.lower()

            #create tenant
            new_tenant = Client(schema_name=business_lower, name=name, business_name=business_name, refferal_code=refferal_code, email=email, phone=phone, location=location, on_trial=on_trial, paid_until=paid_until)
            new_tenant.save()

            domain = Domain()
            #domain.domain = business_lower + '.localhost'
            domain.domain = business_lower + '.accountsmonitor.co.ke/'
            domain.tenant = new_tenant
            domain.is_primary= True
            domain.save()

            #return redirect('http://localhost:3000/')
            return redirect('https://frontend-accounts.vercel.app/')
    else:
        form = TenantRegistrationForm()
    context = {
        'form':form,
        'infos': infos,
        'contacts_infos': contacts_infos,
        'links' :links

    }
    return render(request, 'register.html', context)

def registration(request):
    infos = Company.objects.order_by('id')[:1]
    contacts_infos = Contact_us.objects.order_by('id')[:1]
    links = Social_Links.objects.all()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        if form.is_valid():
            name = form.cleaned_data['name']
            business_name = form.cleaned_data['business_name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            location = form.cleaned_data['location']
            refferal_code = form.cleaned_data['refferal_code']
            password = form.cleaned_data['password']

            #create tenant
            new_tenant = IntrestedClient(name=name, username=username, business_name=business_name, refferal_code=refferal_code, email=email, phone=phone, location=location)
            new_tenant.save()
            messages.success(request, 'Thanks for taking a step to join us, we look forward working with you!!!')
            #register user
            user = User.objects.create_user(
                        username= username,
                        password=password,
                        phone=phone,
                    )
            #create invoice
            Invoice.objects.create(
                customer = new_tenant
            )

            return redirect('customer_invoice')
            #return redirect('https://frontendaccountsmonitor.vercel.app/')
    else:
        form = RegistrationForm()
    context = {
        'form':form,
        'infos': infos,
        'contacts_infos': contacts_infos,
        'links' :links

    }
    return render(request, 'register.html', context)

@login_required
def customerInvoice(request):
    username= request.user.username
    try:
        customer = IntrestedClient.objects.get(username= username)
    except IntrestedClient.DoesNotExist:
        customer = None
    if customer:
        invoices  = Invoice.objects.filter(customer=customer)
        context = {'invoices': invoices, 'username':username, 'customer': customer}
        return render(request, 'customer_invoice.html', context)
    else:
        messages.error(request, 'You have to register first as our customer to access the page!!!')
        return redirect('homepage')
    

@login_required
def editInvoice(request, id):
    if request.method == 'POST':
        invoice= Invoice.objects.get(id=id)
        form = InvoiceForm(request.POST, instance=invoice)

        if form.is_valid():
            form.save
            context= {
                'form': form,
                'invoice': invoice,
                }
            return render(request, 'edit_profile.html', context)
    else:
        invoice= Invoice.objects.get(id=id)
        form = InvoiceForm(instance=invoice)

    context= {
                'form': form,
                'invoice': invoice
            }



























































































































































            
    return render(request, 'edit_invoice.html', context)
 