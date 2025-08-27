import math

class Fraction():
    def __init__(self, a, b):
        self.num = a
        if b != 0:
            self.den = b
        else:
            print("denominator can not be zero")

    def show(self):
        print(self.num , "/" , self.den)

    def sum(self, other):
        result_num = self.num * other.den + self.den * other.num
        result_den = self.den * other.den
        frac_new = Fraction(result_num, result_den)
        return frac_new

    def sub(self, other):
        result_num = self.num * other.den - other.num * self.den
        result_den = self.den *other.den
        frac_new = Fraction(result_num, result_den)
        return frac_new

    def mul(self, other):
        result_num = self.num * other.num
        result_den = self.den * other.den
        frac_new = Fraction(result_num, result_den)
        return frac_new

    def divide(self, other):
        result_num = self.num * other.den
        result_den = self.den * other.num
        new_frac = Fraction(result_num, result_den)
        return new_frac
    
    def convert_to_number(self):
        number = self.num / self.den
        return number
    
    def simple(self):
        gcd = math.gcd(self.num, self.den)
        new_frac = Fraction(self.num/gcd, self.den/gcd)
        return new_frac

# a = Fraction(10, 20)
# b = Fraction(20, 25)
# c = a.sum(b)
# c.show()
# d = a.sub(b)
# d.show()
# e = a.mul(b)
# e.show()
# f = a.divide(b)
# f.show()
# print(a.convert_to_number())
# a.simple().show()
