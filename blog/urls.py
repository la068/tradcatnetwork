from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
        path("", views.index, name="index"),
        path("posts/<int:post_id>/", views.view_post, name="view_post"),
        path("about/", views.about, name="about"),
        path("privacy_policy/", views.privacy_policy, name="privacy_policy"),
        path("contact/", views.contact, name="contact"),
        path("terms_of_use/", views.terms_of_use, name="terms_of_use"),
        ]
