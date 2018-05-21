from itertools import zip_longest

class Polynomial:#I tried my best but it didn't work all the times :/

    def __init__(self, coefficients):
        """coefficients should be a list of numbers with 
        the i-th element being the coefficient a_i."""
        self.coeffic = coefficients

    def degree(self):
        """Return the index of the highest nonzero coefficient.
        If there is no nonzero coefficient, return -1."""
        ind = -1
        for x, y in enumerate(reversed(self.coefficients()), 1):
            if y != 0:
                ind = len(self.coefficients()) - x
                break
        return ind

    def coefficients(self):
        """Return the list of coefficients. 
        The i-th element of the list should be a_i, meaning that the last 
        element of the list is the coefficient of the highest degree term."""
        return self.coeffic

    def __call__(self, x):
        """Return the value of the polynomial evaluated at the number x"""
        val = 0
        for y, item in enumerate(self.coeffic):
            val += (x * item) ** y
        return val

    
    def __add__(self, p):
        """Return the polynomial which is the sum of p and this polynomial
        Should assume p is Polynomial([p]) if p is int. 
        If p is not an int or Polynomial, should raise ArithmeticError."""
        maxLength = max(len(self), len(p))
        if isinstance(p, int):
            p=Polynomial([p])
            
            if isinstance(p, Polynomial):
                self.coeffic += [0]*(maxLength - len(self.coeffic))
                p.coeffic += [0]*(maxLength - len(p.coeffic))
                res_coeffic = self.coeffic

                for x in range(maxLength):
                    res_coeffic[x] += p.coeffic[x]


            """if len(self.coeffic) > len(p.coeffic):
                result_coeff = self.coeffic[:] 
                for i in range(len(p.coeffic)):
                    result_coeff[i] += p.coeffic[i]
            elif len(self.coeffic) < len(p.coeffic): 
                result_coeff = p.coeffic[:] 
                for i in range(len(self.coeffic)):
                    result_coeff[i] += self.coeffic[i]"""
        else:
            raise ArithmeticError
        return Polynomial(res_coeffic)

        
    def __sub__(self, p):
        """Return the polynomial which is the difference of p and this polynomial
        Should assume p is Polynomial([p]) if p is int. 
        If p is not an int or Polynomial, should raise ArithmeticError."""
        if isinstance(p, int):#Det er det mottsatte av add
            p=Polynomial([p])

        if isinstance(p, Polynomial):

            """if len(self.coeffic) > len(p.coeffic):
                result_coeff = self.coeff[:] 
                for i in range(len(p.coeffic)):
                    result_coeff[i] -= p.coeffic[i]
            elif len(self.coeffic) < len(p.coeffic): 
                result_coeff = p.coeffic[:] 
                for i in range(len(self.coeffic)):
                    result_coeff[i] -= self.coeffic[i]"""
        else:
            raise ArithmeticError
        return Polynomial(result_coeff)

    def __mul__(self, c):
        """Return the polynomial which is this polynomial multiplied by given integer.
        Should raise ArithmeticError if c is not an int."""  
        if isinstance(c, int):
            res = map(lambda x: x * c, self.coeffic)

        else:
            raise ArithmeticError
        return Polynomial(res)

        """numb = self.degree + c.degree
        coeff_prod = [0]*(n+1)
        if isinstance(c, int):
            for x in range(0,self.degree + 1):
                for y in range(0,c.degree + 1):
                    coeff_prod[x+y] += self.coeffic[i] * c.coeffic[j]
        else:
            raise ArithmeticError
        return Polynomial(coeff_prod)"""



    def __rmul__(self, c):
        """Return the polynomial which is this polynomial multiplied by some integer"""
        if isinstance(c, int):
            res = map(lambda x: x * c, self.coeffic)

        else:
            raise ArithmeticError
        return Polynomial(res)

        """numb = self.degree + c.degree  #tried different solutions but didn't always work 
        coeff_prod = [0]*(n+1)
        if isinstance(c, int):
            for x in range(0,self.degree + 1):
                for y in range(0,c.degree + 1):
                    coeff_prod[x+y] += self.coeffic[i] * c.coeffic[j]
        else:
            raise ArithmeticError
        return Polynomial(coeff_prod)"""
    
    #def __repr__(self):
        """Return a nice string representation of polynomial.
        
        E.g.: x^6 - 5x^3 + 2x^2 + x - 1
        """
    

    def __eq__(self, p):
        """Check if two polynomials have the same coefficients."""
        return self.coeffic == p.coefficients()

def sample_usage():
    p = Polynomial([1, 2, 1]) # 1 + 2x + x^2
    q = Polynomial([9, 5, 0, 6]) # 9 + 5x + 6x^3
    
    
    print("The value of {} at {} is {}".format(p, 7, p(7)))

    print("The coefficients of {} are {}".format(p, p.coefficients()))

    
    print("\nAdding {} and {} yields {}".format(p, q, p+q))

    p, q, r = map(Polynomial,
                  [
                      [1, 0, 1], [0, 2, 0], [1, 2, 1]
                  ]
    )
    
    print("\nWill adding {} and {} be the same as {}? Answer: {}".format(
        p, q, r, p+q == r
    ))
    print("\nIs {} - {} the same as {}? Answer: {}".format(
        p, q, r, p-q == r
    ))

if __name__ == '__main__':
    sample_usage()