from django.test import TestCase
from orders.models import Order



class OrderModelTest(TestCase):
    def test_creating_a_new_order_and_saving(self):
        order = Order()
        order.ticket = 'Ticket 1234'
        #
        order.save()
        all_orders = Order.objects.all()
        self.assertEqual(len(all_orders), 1)
        only_order = all_orders[0]
        self.assertEqual(only_order,order)
        self.assertEqual(only_order.ticket, order.ticket)

