from django.test import TestCase
from . import Menu

class MenuTest(TestCase):
    def test_menu_str_representation(self):
        menu = Menu.objects.create(
            ID=1,
            Title='Pizza',
            Price=15.50,
            Inventory=100
        )
        self.assertEqual(str(menu), 'Pizza : 15.50')

