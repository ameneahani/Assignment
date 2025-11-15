
class Complex():
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def show(self):
        print(self.real, "+", self.imaginary,"i")

    def sum(self, other):
        new_real = self.real + other.real
        new_imaginary = self.imaginary + other.imaginary
        new_complex = Complex(new_real, new_imaginary)
        return new_complex

    def sub(self, other):
        new_real = self.real - other.real
        new_imaginary = self.imaginary - other.imaginary
        new_complex = Complex(new_real, new_imaginary)
        return new_complex

    def mul(self, other):
        new_real = self.real * other.real - self.imaginary * other.imaginary
        new_imaginary = self.real * other.imaginary + self.imaginary * other.real
        new_complex = Complex(new_real, new_imaginary)
        return new_complex
    
a = Complex(3,2)
b = Complex(1, 7)
c = a.mul(b).show()

