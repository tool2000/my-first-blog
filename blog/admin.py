from django.conf.urls import include, url
from django.contrib import admin
#from .models import Post

#admin.site.register(Post)
# Register your models here.

urlpatterns = [
    url('^admin/', admin.site.urls),
    url('', include('blog.urls'))
]
