from django.contrib import admin
from .models import *

admin.site.register(BlogCategory)
admin.site.register(Blog)

admin.site.register(LinkVolume)
admin.site.register(Feature)
admin.site.register(Plan)
admin.site.register(PlanPricing)
admin.site.register(PlanFeatureValue)