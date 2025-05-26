acronyms = {'LOL':'laugh out Loud', 
            'IDK':"I Don't Know",
            'TBH':'to be honest'
            }

menu = {'Soup': 5, 
        'Salad': 6
        }

mycidt = {10: 'hello',
          2: 6.5
          }
# print(acronyms['TBH'])
# print(menu, mycidt)

# acronyms['TBH'] = 'honestly'
# print(acronyms)

# del acronyms['TBH']

# print(acronyms)
# definition = acronyms.get('TBH')
# # print(definition)

# if definition:
#    print(definition)
# else:
#    print("key dosen't exist")


sentence = 'IDK' + ' what happend ' + 'TBH'
translation = acronyms.get('IDK') + ' what happend ' + acronyms.get('TBH')

print('sentence:', sentence)
print('translation:', translation)