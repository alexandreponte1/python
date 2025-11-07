# acronyms = {'LOL' : 'laugh out loud', 
#             'IDK' : "I don't know",
#             'TBH' : 'to be honest'}
            
# acronym_to_find = 'BTW'
 
# try:
#     definition = acronyms[acronym_to_find]
#     print(f"Definition of '{acronym_to_find}' is '{definition}'")
# except KeyError:
#     print(f"The key '{acronym_to_find}' does not exist.")
# finally:
#     print('The acronyms we have defined are:')
#     for acronym in acronyms:
#         print(acronym)
 
# print('The program keeps going')


def remainder_division(a,b):
    if b == 0:
        raise Exception('The divisor cannot be 0')
    
    result  = a//b
    remainder = a%b
    return result, remainder
    print(a, '/', b, 'is', result, 'remainder', remainder)

#main program
remainder_division(10,0)



