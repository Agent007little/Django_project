from django.contrib import admin
from posts.models import Massage, Hashtag, MassageHashtag, PostImage

admin.site.register(Massage)
admin.site.register(Hashtag)
admin.site.register(MassageHashtag)
admin.site.register(PostImage)
