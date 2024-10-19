from django.contrib import admin
from main.models import *
# Register your models here.



class LanguageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Language, LanguageAdmin)


class NewsAdmin(admin.ModelAdmin):
    pass
admin.site.register(News, NewsAdmin)

class ContactAdmin(admin.ModelAdmin):
    pass
admin.site.register(Contact, ContactAdmin)

class InformationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Information, InformationAdmin)

class NavbarAdmin(admin.ModelAdmin):
    pass
admin.site.register(Navbar, NavbarAdmin)


class DonateAdmin(admin.ModelAdmin):
    pass
admin.site.register(Donate, DonateAdmin)

class JoinToGroupAdmin(admin.ModelAdmin):
    pass
admin.site.register(JoinToGroup, JoinToGroupAdmin)




