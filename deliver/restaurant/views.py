from django.shortcuts import render
from django.views import View
from django.utils.timezone import datetime
from customer.models import OrderModel

class Dashboard(View):
    def get(self, request, *args, **kwargs):
        # Get the current date
        today = datetime.today()
        orders = OrderModel.objects.filter(created_on__year=today.year, created_on__month=today.month,
                                           created_on__day=today.day)


        # Loop through the orders and add the price value

        # Pass total number of orders and total revenue into template

        return render(request, 'restaurant/dashboard.html')
