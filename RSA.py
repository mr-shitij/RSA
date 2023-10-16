from numbers.prime_generator import get_prime
from numbers.exponent_generator import get_exponent
from numbers.modulo_inverse import get_inverse

class RSA():
    def __init__(self):
        self.message = []

        self.prime_size = 1028

        self.p = get_prime(self.prime_size)
        self.q = get_prime(self.prime_size)

        self.N = self.p * self.q
        self.FI_N = (self.p - 1) * (self.q - 1) 

        self.e = get_exponent(self.FI_N)
        self.d = get_inverse(self.e, self.FI_N)
    
    def set_message(self, message):
        self.message = [ord(m) for m in message]

    def encrypt(self):
        chiper_text = []
        for m in self.message:
            chiper_text.append(pow(m, self.e, self.N))            
        return chiper_text

    def decrypt(self, chiper_text):
        #chiper = [ord(m) for m in chiper_text]
        chiper = chiper_text
        plain_text = ''
        for m in chiper:
            plain_text += chr(pow(m, self.d, self.N))
        return plain_text

algo = RSA()

algo.set_message("HI")
chiper = algo.encrypt()
print("Cipher : ", chiper)

text = algo.decrypt(chiper)
print("Text : ", text)
