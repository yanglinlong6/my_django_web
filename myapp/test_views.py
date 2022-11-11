from unittest import TestCase

from .models import models


class Test(TestCase):
    def test_index(self):
        self.fail()
        fields = models.App1.get_deferred_fields()
        print(fields)
