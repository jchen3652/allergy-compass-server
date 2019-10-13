from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    #path("", hello.views.index, name="index"),
    #path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path("images", hello.views.images, name = "images"),
    path("preferenceUpdate", hello.views.preferenceUpdate, name = "preferenceUpdate"),
    path("addUser", hello.views.addUser, name = "addUser"),
    path("login", hello.views.login, name = "login"),
    path("getPrefs", hello.views.getPrefs, name="getPrefs"),
    path("getSoy", hello.views.getSoy, name = "getSoy"),
    path("getDairy", hello.views.getDairy, name = "getDairy"),
    path("getSeafood", hello.views.getSeafood, name="getSeafood"),
    path("getNuts",hello.views.getNuts, name = "getNuts")
]
