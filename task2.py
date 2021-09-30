def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
class Rational:
    def __init__(self,numerator=1,denominator=2):
        try:
            if isinstance(numerator,int) and isinstance(denominator,int):
                self.__numerator = numerator/gcd(numerator,denominator)
                self.__denominator = denominator/gcd(numerator,denominator)
                return None
        except:
            return None
    def print_simple(self):
        try:
            return str(self.__numerator)+"/"+str(self.__denominator)
        except:
            return None
    def print_float(self):
        try:
            return self.__numerator/self.__denominator
        except:
            return None
rational=Rational(2,4)
print(rational.print_simple())
print(rational.print_float())