from django.contrib import admin

from main.models import Contacts_Customers, Contatos, CustomerSectors, Customers_main, Suppliers

# Register your models here.
admin.site.register(Customers_main)
admin.site.register(Contacts_Customers)
admin.site.register(CustomerSectors)
admin.site.register(Contatos)
admin.site.register(Suppliers)

