from django.urls import path
from .views import Receipt, ReceiptDetails

urlpatterns = [
    path('', Receipt.as_view()),
    path('<int:id>/', ReceiptDetails.as_view()),
]