from django.urls import path
from . import views

urlpatterns = [
    path ("", views.index, name="ShopHome"),
    path ("about/", views.about, name="About_Us"),
    path ("contact/", views.contact, name="Contact_Us"),
    path ("tracker/", views.tracker, name="Tracking_Status"),
    path ("search/", views.search, name="Search"),
    path ("products/<int:myid>", views.prodView, name="prodView"),
    path ("checkout/", views.checkout, name="Checkout"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
    path ("new/", views.new, name="new"),


]
