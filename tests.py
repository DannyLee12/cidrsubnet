from unittest import TestCase

from cidrsubnet import cidrsubnet


class TestCidrSubnet(TestCase):
    def test_a(self):
        self.assertEqual(cidrsubnet("10.1.2.0/24", 4, 15), "10.1.2.240/28")

    def test_b(self):
        self.assertEqual(cidrsubnet("172.16.0.0/12", 4, 2), "172.18.0.0/16")

    def test_ip6(self):
        with self.assertRaises(ValueError):
            cidrsubnet("fd00:fd12:3456:7890::/56", 16, 162)
