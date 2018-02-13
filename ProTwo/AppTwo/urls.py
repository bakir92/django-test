from django.conf.urls import url
from AppTwo import views

app_name = "AppTwo"
urlpatterns = [
    url(r'^$',views.user,name='user'),
    # url(r'^AppTwo/',views.help,name='help'),
    url(r'^users/',views.user,name='user'),
    url(r'^show_user/',views.show_user,name='show_user'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]
