import logging
logging.basicConfig(filename='Programming Assignment_5.log',level=logging.DEBUG,format= '%(asctime)s %(levelname)s %(message)s')

#1.	Write a Python Program to Find LCM?
logging.info('The code for LCM')
class LCM:
    logging.info('We entered LCM class')
    def lcm(self):
        a = int(input('Enter the number: '))
        logging.info(f'The first number {a}')
        b = int(input('Enter the number: '))
        logging.info(f'The second number {b}')
        if a >= b:
            g = a
        else:
            g = b
        while True:
            if g % a == 0 and g % b == 0:
                break
            g = g + 1
        logging.info(f'The lCM of {a} and {b} is {g}')
        return 'the LCM is',g
o= LCM()
print(o.lcm())
#2.	Write a Python Program to Find HCF?
logging.info('The program for HCF')
class HCF:
    def hcf(self,a,b):
        if a>b:
            s=b
        else:
            s=a
        i= 1
        while i<=s:
            if a%i==0 and b%i==0:
                j=i
            i=i+1
        logging.info(f'the HCF of {a} and {b} is {j}')
        return j

o1= HCF()
print(o1.hcf(22,44))
#3.	Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
logging.info('Let start basic calculator')
class calculator:
    def add(self,a,b):
        logging.info(f'We are going to add {a},{b}')
        try :
            logging.info(f'the sum of numbers is {a + b}')
            return a + b
        except Exception as e:
            logging.exception(e)
            return e


    def sub(self,a,b):
        logging.info(f'We are going to subtract {a} ,{b}')
        try:
            logging.info(f'the subtration is {a - b}')
            return a - b
        except Exception as e:
            logging.exception(e)
            return e


    def multi(self,a,b):
        logging.info(f'We are going to mutliply {a},{b}')
        try:
            logging.info(f'the mutliplication is {a * b}')
            return a * b
        except Exception as e:
            logging.exception(e)
            return e


    def divide(self,a,b):
        logging.info(f'We are going to divide {a},{b}')
        try:
            logging.info(f'the division is {a / b}')
            return a / b
        except Exception as e:
            logging.exception(e)
            return e


o3= calculator()
print(o3.divide(1235,5))
#4.	Write a Python Program To Find ASCII value of a character?
logging.info('We are going to check ASCII value of a cahracter')
class ascii_value:
    def ch(self,a):
        logging.info(f'the ASCII value of {a} is {ord(a)}')
        return f'The ASCII value of {a} is {ord(a)}'
oj= ascii_value()
print(oj.ch('O'))
#5.	Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
logging.info('We going convert decimal to binary,octal and hexadecimal')
class d:
    logging.info('We can enter only integer in the fuction')

    def conver(self,a):
        try:
            logging.info(f'After conversion {a} into binary--{bin(a)}  octal--{oct(a)} hexadecimal--{hex(a)}')
            return f'After conversion {a} into binary--{bin(a)}  octal--{oct(a)} hexadecimal--{hex(a)}'
        except Exception as e:
            logging.error(e)
            return e

oo= d()
print(oo.conver(5893))