from django.contrib import admin
from .models import * # SprFgosVo, SprCompulsoryDiscipline, SprCompetency, SprSpecialization,


# class CompDisciplinesInline(admin.TabularInline):
#     model = SprFgosVo.compulsory_disciplines.through
#
# class FgosVoAdminView(admin.ModelAdmin):
#     list_display = [f.name for f in SprFgosVo._meta.fields]
#
#     inlines = [
#         CompDisciplinesInline,
#     ]



@admin.register(SprCompulsoryDiscipline)
class CompDiscipline(admin.ModelAdmin):
    list_display = [f.name for f in SprCompulsoryDiscipline._meta.fields]


@admin.register(SprFgosVo)
class FgosAdmin(admin.ModelAdmin):
    list_display = [f.name for f in SprFgosVo._meta.fields]

admin.site.register(SprCompetency)
admin.site.register(SprSpecialization)
admin.site.register(DCompetencyCode)
admin.site.register(DSpecialozationType)
admin.site.register(DTypeStandard)
admin.site.register(DGeneration)
admin.site.register(TblRealizedOkso)
