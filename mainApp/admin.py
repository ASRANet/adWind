from django.contrib import admin
from django import forms
from mainApp.models import InfoPage, Item, SiteSetting
from ckeditor.widgets import CKEditorWidget


class ItemAdminForm(forms.ModelForm):

    text = forms.CharField(widget=CKEditorWidget())
    order = str(forms.IntegerField)

    class Meta:
        model = Item
        fields = ('page', 'headline', 'order', 'text')


class ItemAdmin(admin.ModelAdmin):

    list_display = ('page', 'order', 'headline')
    search_fields = ('headline', 'element_id')
    ordering = ('page', 'order')
    form = ItemAdminForm


admin.site.register(Item, ItemAdmin)
admin.site.register(InfoPage)
admin.site.register(SiteSetting)
