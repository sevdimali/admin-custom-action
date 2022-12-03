from django.contrib import admin
from django.http import HttpResponseRedirect

from core.models import Company


class CompanyAdmin(admin.ModelAdmin):

    @admin.action(description='Export')
    def export_objects(self, request, queryset):
        selected = queryset.values_list('pk', flat=True)
        return HttpResponseRedirect('/export/?ids=%s' % (
            ','.join(str(pk) for pk in selected),
        ))

    list_display = ['name', 'company_type', 'founded', 'status']

    actions = [export_objects]

    list_filter = ['company_type']


admin.site.register(Company, CompanyAdmin)
