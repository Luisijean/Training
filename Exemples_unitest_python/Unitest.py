#Unitest


"""
Une fois l'implémentation des tests terminée, vous pouvez exécuter une 
des commandes suivantes sur le terminal pour lancer les tests. 
Supposons que le fichier de test s’appellenom_du_fichier.py : 

Un module de test : 
python -m unittest nom_du_fichier
python nom_du_fichier.py

Un scénario spécifique dans un module de test :  python -m unittest nom_du_fichier.<nom du test>

L’ensemble des modules de test contenus dans un répertoire :  python -m unittest discover <nom du répertoire de test>/

"""

#python -m unittest -v Unitest.py

import unittest

#exemple unitest sans code main

class TestString(unittest.TestCase):
    def test_should_capitalize_string(self):
        string = "hello"
        expected_value = "Hello"
        self.assertEqual(string.capitalize(), expected_value)


    def test_should_upper_string(self):
        string = "hello"
        expected_value = "HELLO"
        self.assertEqual(string.upper(), expected_value)


    def test_should_trim_string(self):
        string = "  hello "
        expected_value = "hello"
        self.assertEqual(string.strip(), expected_value)

from main_doctest import is_prime


class TestIsPrime(unittest.TestCase):
	def test_should_return_true_with_prime_number(self):
		self.assertEqual(is_prime(5), True)

	def test_should_return_false_with_non_prime_number(self):
		self.assertEqual(is_prime(4), False)

	def test_should_return_false_with_number_one(self):
		self.assertFalse(is_prime(1))



if __name__ == "__main__":
    unittest.main()



