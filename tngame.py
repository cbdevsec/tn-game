import random

def bindecode_game():
    n_decimal = random.randint(1, 999)
    n_binary = bin(n_decimal).replace("0b", "")
    print (n_binary)
    answer = input('your answer is: ')
    if answer == n_decimal :
        print('Correct!')
    else: 
        print('wrong')
        print(n_decimal)

def binencode_game():
    n_decimal = random.randint(1, 999)
    n_binary = bin(n_decimal).replace("0b", "")
    print(n_decimal)
    answer = input('your answer is: ')
    if answer == n_binary :
        print('Correct!')
    else: 
        print('Wrong')
        print(n_binary)

def binaddition_game():
    n_1 = bin(random.randint(1,999)).replace("0b", "")
    n_2 = bin(random.randint(1,999)).replace("0b", "")
    print(n_1 + " + " + n_2)
    right_answer = bin(int(n_1, 2) + int(n_2, 2))
    answer = input('your answer is: ')
    if answer == right_answer[2:] :
        print('Correct!')
    else: 
        print('wrong')
        print(right_answer)

def binsubstraction_game():
    n_1 = bin(random.randint(1,999)).replace("0b", "")
    n_2 = bin(random.randint(1,999)).replace("0b", "")
    print(n_1 + " - " + n_2)
    right_answer = bin(int(n_1) - int(n_2)).replace("0b", "")
    answer = input('your answer is: ')
    if answer == right_answer[2:] :
        print('Correct!')
    else: 
        print('wrong')
        print(right_answer)

def binmultiplication_game():
    n_1 = bin(random.randint(1,999)).replace("0b", "")
    n_2 = bin(random.randint(1,999)).replace("0b", "")
    print(n_1 + " x " + n_2)
    right_answer = bin(int(n_1) * int(n_2)).replace("0b", "")
    answer = input('your answer is: ')
    if answer == right_answer[2:] :
        print('Correct!')
    else: 
        print('wrong')
        print(right_answer)

def bindiv_game():
    n_1 = bin(random.randint(1,999)).replace("0b", "")
    n_2 = bin(random.randint(1,999)).replace("0b", "")
    print(n_1 + " / " + n_2)
    right_answer = bin(int(n_1) / int(n_2)).replace("0b", "")
    answer = input('your answer is: ')
    if answer == right_answer[2:] :
        print('Correct!')
    else: 
        print('wrong')
        print(right_answer)

def hexdecode_game():
    n_decimal = random.randint(1, 999)
    n_hex = hex(n_decimal).replace("0x", "")
    print (n_hex)
    answer = input('your answer is: ')
    if answer == n_decimal :
        print('Correct!')
    else: 
        print('wrong')
        print(n_decimal)


def hexencode_game():
    n_decimal = random.randint(1, 999)
    n_hex = hex(n_decimal).replace("0x", "")
    print(n_decimal)
    answer = input('your answer is: ')
    if answer == n_hex :
        print('Correct!')
    else: 
        print('Wrong')
        print(n_hex)

## def hexaddition_game():
##    n_1 = hex(random.randint(1,999)).replace("0x", "")
##    n_2 = hex(random.randint(1,999)).replace("0x", "")
##    print(n_1 + " + " + n_2)
##    right_answer = hex(int(n_1) + int(n_2)).replace("0x", "")
##   answer = input('your answer is: ')
##    if answer == right_answer[2:] :
 ##       print('Correct!')
 ##   else: 
 ##       print('wrong')
 ##       print(right_answer)

##def hexsubstraction_game():
##    n_1 = hex(random.randint(1,999)).replace("0x", "")
 ##   n_2 = hex(random.randint(1,999)).replace("0x", "")
##    print(n_1 + " - " + n_2)
 ##   right_answer = hex(int(n_1) - int(n_2)).replace("0x", "")
 ##   answer = input('your answer is: ')
##    if answer == right_answer[2:] :
 ##       print('Correct!')
  ##  else: 
  ##      print('wrong')
  ##      print(right_answer)

##def hexmultiplication_game():
##    n_1 = hex(random.randint(1,999)).replace("0x", "")
##    n_2 = hex(random.randint(1,999)).replace("0x", "")
##    print(n_1 + " x " + n_2)
##    right_answer = hex(int(n_1) * int(n_2)).replace("0x", "")
##    answer = input('your answer is: ')
##    if answer == right_answer[2:] :
##        print('Correct!')
##    else: 
##        print('wrong')
##        print(right_answer)

##def hexdiv_game():
##    n_1 = hex(random.randint(1,999)).replace("0x", "")
##    n_2 = hex(random.randint(1,999)).replace("0x", "")
##    print(n_1 + " / " + n_2)
##    right_answer = hex(int(n_1) / int(n_2)).replace("0x", "")
##    answer = input('your answer is: ')
##    if answer == right_answer[2:] :
##        print('Correct!')
##    else: 
##        print('wrong')
##        print(right_answer)


def octdecode_game():
    n_decimal = random.randint(1, 999)
    n_oct = oct(n_decimal)
    print (n_oct)
    answer = input('your answer is: ')
    if answer == n_decimal :
        print('Correct!')
    else: 
        print('wrong')
        print(n_decimal)


def octencode_game():
    n_decimal = random.randint(1, 999)
    n_oct = oct(n_decimal)
    print(n_decimal)
    answer = input('your answer is: ')
    if answer == n_oct :
        print('Correct!')
    else: 
        print('Wrong')
        print(n_oct)

##def octaddition_game():
##    n_1 = oct(random.randint(1,999))
##    n_2 = oct(random.randint(1,999))
##    print(n_1 + " + " + n_2)
##    right_answer = oct(int(n_1) + int(n_2))
##    answer = input('your answer is: ')
##    if answer == right_answer :
##        print('Correct!')
##    else: 
##        print('wrong')
 ##       print(right_answer)

##def octsubstraction_game():
##    n_1 = oct(random.randint(1,999))
##    n_2 = oct(random.randint(1,999))
 ##   print(n_1 + " - " + n_2)
 ##   right_answer = oct(int(n_1) - int(n_2))
 ##   answer = input('your answer is: ')
 ##   if answer == right_answer :
##        print('Correct!')
 ##   else: 
 ##       print('wrong')
 ##       print(right_answer)

##def octmultiplication_game():
##    n_1 = oct(random.randint(1,999))
##    n_2 = oct(random.randint(1,999))
##    print(n_1 + " x " + n_2)
####    right_answer = oct(int(n_1) * int(n_2))
##    answer = input('your answer is: ')
##    if answer == right_answer :
 ##       print('Correct!')
 ##   else: 
 ##       print('wrong')
 ##       print(right_answer)

##def octdiv_game():
##    n_1 = oct(random.randint(1,999))
##    n_2 = oct(random.randint(1,999))
##    print(n_1 + " / " + n_2)
##    right_answer = oct(int(n_1) / int(n_2))
##    answer = input('your answer is: ')
##    if answer == right_answer :
 ##       print('Correct!')
 ##   else: 
 ##       print('wrong')
 ##       print(right_answer)


while True:
    choice = input('choose game: 1: decode, 2: encode, 3: addition, 4: substraction, 5: multiplication, 6: division ')
    if choice == '1':
        mode = input('choose mode: 1: bin, 2: hex, 3: oct')
        if mode == '1':
            bindecode_game()
        if mode == '2':
            hexdecode_game()
        if mode == '3':
            octdecode_game()
    if choice == '2':
        mode = input('choose mode: 1: bin, 2: hex, 3: oct')
        if mode == '1':
            binencode_game()
        if mode == '2':
            hexencode_game()
        if mode == '3':
            octencode_game()
    if choice == '3':
        mode = input('choose mode: 1: bin, 2: hex, 3: oct')
        if mode == '1':
            binaddition_game()
       ## if mode == '2':
           ## hexaddition_game()
       ## if mode == '3':
            ##octaddition_game()
    if choice == '4':
        mode = input('choose mode: 1: bin, 2: hex, 3: oct')
        if mode == '1':
            binsubstraction_game()
        ##if mode == '2':
        ##    hexsubstraction_game()
       ## if mode == '3':
        ##    octsubstraction_game()
    if choice == '5':
        mode = input('choose mode: 1: bin, 2: hex, 3: oct')
        if mode == '1':
            binmultiplication_game()
        ##if mode == '2':
        ##    hexmultiplication_game()
        ##if mode == '3':
         ##   octmultiplication_game()
    if choice == '6':
        mode = input('choose mode: 1: bin, 2: hex, 3: oct')
        if mode == '1':
            bindiv_game()
        ##if mode == '2':
        ##    hexdiv_game()
        ##if mode == '3':
        ##    octdecode_game()
    