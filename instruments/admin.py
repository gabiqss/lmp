from django.contrib import admin

from instruments.models import InstrumentTypes, InstrumentsBands, InstrumentsInstruments, InstrumentsModels

# Register your models here.
admin.site.register(InstrumentTypes)
admin.site.register(InstrumentsModels)
admin.site.register(InstrumentsBands)
admin.site.register(InstrumentsInstruments)
