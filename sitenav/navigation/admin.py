from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin, TreeRelatedFieldListFilter
from .models import NavigationItem, DomainModel


class NavigationItemAdmin(DraggableMPTTAdmin):
    # specify pixel amount for this ModelAdmin only:
    fields = ['name', 'parent', 'domain']
    mptt_level_indent = 20


class DomainModelAdmin(DraggableMPTTAdmin):
    # specify pixel amount for this ModelAdmin only:
    fields = ['name', 'parent']
    mptt_level_indent = 20


admin.site.register(
    NavigationItem,
    NavigationItemAdmin,
    list_filter=
    (
        ('parent', TreeRelatedFieldListFilter),
    )
)

admin.site.register(
    DomainModel,
    DomainModelAdmin,
    list_filter=
    (
        ('parent', TreeRelatedFieldListFilter),
    )
)
