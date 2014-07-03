from django.contrib import admin
from naughtylist.models import Voice
from django.forms import TextInput, Textarea
from django.db import models

class VoiceAdmin(admin.ModelAdmin):
    list_display = (Voice._meta.get_all_field_names())
    
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':4})},
    }


admin.site.register(Voice, VoiceAdmin)
