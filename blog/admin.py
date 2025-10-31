from django.contrib import admin
from .models import Post, About, Contact, PrivacyPolicy, TermsOfUse

# Register your models here.
admin.site.register(Post)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(PrivacyPolicy)
admin.site.register(TermsOfUse)
