from django.conf.urls import url
from django.contrib import admin

from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$',views.preRegister, name = "singUp"),
    url(r'^$',views.register, name = "register"),
    url(r'^register/',views.register, name = "register"),
    url(r'^login/',views.login,name = "login"),
    url(r'^chat/',views.chat,name = "chat"),
    url(r'^edit_firebase/',views.edit_firebase,name = "edit_firebase"),
    url(r'^edit_application/',views.edit_application,name = "edit_application"),
    url(r'^excel_file/',views.products,name='excel_file'),
    url(r'^uploaded_file/',views.upload_to_firebase),
    url(r'^view_applications/',views.view_applications,name='view_applications'),


]
