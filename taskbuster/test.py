__author__ = 'the_fegati'
# _*_ coding: utf-8 _8_
from django.test import TestCase
from django.core.urlresolvers import reverse


class TestHomepage(TestCase):

    def test_uses_index_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "taskbuster/index.html")

    def test_uses_base_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response,"base.html")
