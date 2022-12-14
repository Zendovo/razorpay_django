from django.urls import path, include

urlpatterns = [
    path('', OrderFormView.as_view()),
    path('<id:int>', PaymentView.as_view()),
    path('', OrderFormView.as_view()),
]