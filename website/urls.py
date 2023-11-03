from django.urls import path
from website.views import *

urlpatterns = [
    path("", home, name="home"),
    # path("login/", login_user, name="login_user"),
    path("logout/", logout_user, name="logout"),
    path("register/", register_user, name="register"),
    path("record/<int:pk>/", customer_record, name="record"),
    path("delete_record/<int:pk>/", delete_record, name="delete_record"),
    path("add_record/", add_record, name="add_record"),
    path("update_record/<int:pk>/", update_record, name="update_record"),
]
