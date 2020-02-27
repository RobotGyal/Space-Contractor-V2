from django.test import TestCase
from cart.models import Item
from django.utils import timezone
from django.contrib.auth.models import User

# models test
class WhateverTest(TestCase):

    def create_item(self, name="only a test", content="yes, this is only a test"):
        return Item.objects.create(name=name, content=content)

    def test_item_creation(self):
        rocket = self.create_item()
        self.assertTrue(isinstance(rocket, Item))
        self.assertEqual(rocket.__unicode__(), rocket.name)