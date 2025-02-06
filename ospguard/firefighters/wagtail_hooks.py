from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import Firefighter

class FirefighterAdmin(ModelAdmin):
    model = Firefighter
    menu_label = "Strażacy"
    menu_icon = "user"
    menu_order = 200
    add_to_settings_menu = False
    add_to_admin_menu = True
    list_display = ("first_name", "last_name", "birth_date", "phone_number", "email")
    search_fields = ("first_name", "last_name")

modeladmin_register(FirefighterAdmin)
