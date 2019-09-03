from django.contrib import admin
from .models import Compound, Protein, ProteinCompound

from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CompoundResource(resources.ModelResource):
    class Meta:
        model = Compound
        fields = ('compound_id', 'compound_name', 'features')
        import_id_fields = ['compound_id']

class CompoundAdmin(ImportExportModelAdmin):
    resource_class = CompoundResource

class ProteinResource(resources.ModelResource):
    class Meta:
        model = Protein
        fields = ('protein_id', 'protein_name')
        import_id_fields = ['protein_id']

class ProteinAdmin(ImportExportModelAdmin):
    resource_class = ProteinResource

class ProteinCompoundResource(resources.ModelResource):
    class Meta:
        model = ProteinCompound
        fields = ('protein_id', 'compound_id', 'activity')
        import_id_fields = ['compound_id']

class ProteinCompoundAdmin(ImportExportModelAdmin):
    resource_class = ProteinCompoundResource

admin.site.register(Compound, CompoundAdmin)
admin.site.register(Protein, ProteinAdmin)
admin.site.register(ProteinCompound, ProteinCompoundAdmin)
