import unittest
import Project
from Project import CoprimeTest
from Project import GeneratingD
from Project import Encryption
from Project import Decryption
from Project import newkeys
from Project import MillerRabin
from Project import isPrime
from Project import GeneratingBigPrime
from Project import GeneratingE

class UnitTest(unittest.TestCase):
    
    def test_coprime(self):
        self.assertEqual(CoprimeTest(13,3), True)
        self.assertEqual(CoprimeTest(15,5), False)
        self.assertEqual(CoprimeTest(92,4), False)
        self.assertEqual(CoprimeTest(17,3), True)
    
    def test_D(self):
        self.assertEqual(GeneratingD(5,192), 77)
        self.assertEqual(GeneratingD(17, 231), 68)
        self.assertEqual(GeneratingD(491, 979), 327)

    def test_encr(self):
        Project.n, Project.E, Project.D, Project.p, Project.q = newkeys()
        self.assertEqual(Decryption(Encryption('Привет')), 'Привет')
        self.assertEqual(Decryption(Encryption('AbCdEfАбВгД')), 'AbCdEfАбВгД')
        self.assertEqual(Decryption(Encryption('!"№%:,.;@#$%^&*∂å∂ƒ√')), '!"№%:,.;@#$%^&*∂å∂ƒ√')
        self.assertEqual(Decryption(Encryption('Фаптш FSF3415__₽')), 'Фаптш FSF3415__₽')

    def test_isprime(self):
        self.assertEqual(isPrime(77), False)
        self.assertEqual(isPrime(7), True)
        self.assertEqual(isPrime(15), False)
        self.assertEqual(isPrime(881), True)
        self.assertEqual(isPrime(1000000), False)
        self.assertEqual(isPrime(2), True)
        self.assertEqual(isPrime(1), False)
        self.assertEqual(isPrime(999983), True)










if __name__ == '__main__':
    unittest.main()