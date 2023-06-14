#Tests

#Doctest


def to_absolute(number):
    """
        Return the absolute value

        :param number: Initial number
        :return:  The absolute value

        >>> to_absolute(3)
        3
		>>> to_absolute(-10)
		10
    """
    if number <= 0:
        return -number
    return number

#commande pour lancer doctest:
#python -m doctest -v <nom du fichier>

#Pytest

def reverse_str(initial_string):
    final_string = ''
    index = len(initial_string)
    while index > 0:
        final_string += initial_string[index - 1] #Remplacer index - 2 par index - 1
        index = index - 1
    return final_string




    


#Unitest


def is_prime(number):
    if number == 1:
        return False

    for x in range(2, number):
        if number % x == 0:
            return False

    return True



