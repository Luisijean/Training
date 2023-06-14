#Pytest


"""
J'ai écrit ensuite une nouvelle fonction, dans le fichiertest.py, pour tester la fonctionreverse_str(initial_string).

Je commence en la nommanttest_should_reverse_stringcar il s'agit d'un test qui permettra de vérifier
 si la fonction renvoie bien l’inverse de la chaîne de caractères. 
 À l'intérieur, j'utilise le mot-cléassert, puis un espace, et écris ce que je souhaite tester. 
 Ainsi, si l’assertion n’est pas soulevée, le test passe ! 

Dans mon cas, je souhaite tester que le résultat de l'exécution de la fonctionreverse_str('abc') 
renvoie bien une valeur égale à la chaîne de caractères"cba".

"""

from main_doctest import reverse_str

#toujours commencer par nommer la fonction test_ afin de lancer l'ensemble des tests du projet

def test_should_reverse_string():
    assert reverse_str('abc') == 'cba'


#commande à lancer:
#pytest Pytest.py

