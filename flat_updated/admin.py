from django.contrib import admin

from django.contrib import admin
from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin

from .models import HomePage, Slide

class SlideInline(TabularDynamicInlineAdmin):
    model = Slide
    fields = ("homepage", "image", "heading", "subheading", "url")

class HomePageAdmin(PageAdmin):
    inlines = (SlideInline,)

admin.site.register(HomePage, HomePageAdmin)



