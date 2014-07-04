from django.contrib import admin
from naughtylist.models import Voice
from django.forms import TextInput, Textarea
from django.db import models

class VoiceAdmin(admin.ModelAdmin):
	
	SHOW_FUZZY = True
	
	def toggle_fuzzy(modeladmin, request, queryset):
		VoiceAdmin.SHOW_FUZZY = not VoiceAdmin.SHOW_FUZZY
	toggle_fuzzy.short_description = "Toggle visibility of non-fuzzy voices. Select at least 1 voice before using this."
	
	list_display = ('datetime_added', 'user', 'offender', 'reason', 'message', 'naughty', 'fuzzy', 'verified')
    
	formfield_overrides = {
		models.TextField: {'widget': Textarea(attrs={'rows':4})},
	}	
	
	actions = [toggle_fuzzy]
    
	def queryset(self, request):
		qs = super(VoiceAdmin, self).queryset(request)
		if VoiceAdmin.SHOW_FUZZY:
			return qs
		else:
			return qs.filter(fuzzy=True)

admin.site.register(Voice, VoiceAdmin)
