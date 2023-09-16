import random

class Problem:
    def __init__(self):
        pass

    def _dig_gen(self, digits):
        """
        Checking if the size is correct.
        Helper function for add_sub.
        """
        dig = int("9" * digits)
        num = random.randint(-dig, dig)

        # If digits == 1, make sure it is not 0
        if digits == 1:
            if len(str(abs(num))) == digits and num != 0:
                return num
            else:
                return self._dig_gen(digits)
        else:
            if len(str(abs(num))) == digits:
                return num
            else:
                return self._dig_gen(digits)

    def _pos_gen(self, digits):
        """     
        Generates a positive integer that n digits long,
        given digits.
        """
        dig = int("9" * digits)
        num = random.randint(1, dig)
        if len(str(num)) == digits:
            return num
        else:
            return self._pos_gen(digits)

    def add_sub(self, numbers, digits):
        """
        Given numbers and digits, this function
        will return an array of random numbers
        that sums positively.
        """
        if numbers <= 0 and digits <= 0:
            return None
        
        rand_lst = []
        while len(rand_lst) != numbers:
            num_x = self._dig_gen(digits)
            rand_lst.append(num_x)
            if sum(rand_lst) <= 0:
                rand_lst.pop()

        return rand_lst


    def mult(self, num1, num2):
        """
        Given num1 and num2, this function will
        return an array of size 2. The elements
        inside the array will be positive integers,
        so that the multiplied numbers are positive.
        """
        n1 = self._pos_gen(num1)
        n2 = self._pos_gen(num2)
        return [n1, n2] 
 
    def div(self, num1, num2):
        """
        Given num1 and num2, this function will
        return an array of size 2. It will also
        ensure that the problem is divisible wholy.
        """
        n1 = self._pos_gen(num1)
        n2 = self._pos_gen(num2)
        if n1 % n2 == 0:
            return [n1, n2]
        else:
            return self.div(num1, num2)
        
