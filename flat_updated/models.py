from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to


class HomePage(Page, RichText):
        heading = models.CharField(max_length=200, help_text="The heading of HomePage")
        subheading = models.CharField(max_length=200, help_text="The subheading of HomePage")

        class Meta:
            verbose_name = _("Home page")
            verbose_name_plural = _("Home pages")


class Slide(Orderable):
    homepage = models.ForeignKey(HomePage, related_name="slides")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("theme.Slide.image", "slider"),
        format="Image", max_length=255, null=True, blank=True)
    heading = models.CharField(max_length=200, help_text="The heading of slide the icon blurbs")
    subheading = models.CharField(max_length=200, help_text="The subheading of slide")
    url = models.CharField(max_length=200, help_text="URL of slide", default = "#")
