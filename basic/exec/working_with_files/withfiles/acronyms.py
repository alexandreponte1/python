

def find_acronym():
    look_up = input("What software acronym would you like to look up?\n")
    found = False
    try:
        with open('acronyms.txt') as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
        if not found:
            print('The acronym does not exist')
    except FileNotFoundError as e:
        print('File not found')
        return False

 
def add_acronym():
    acronym = input('What acronym do you want to add?\n')
    definition = input('What is the definition?\n')
    with open('acronyms.txt', 'a') as file:
        file.write(acronym + ' - ' + definition + '\n')



def main():
    # Perguntar para o usuário se ele quer achar ou adicionar um acronym
    choice = input('Do you want to find(F) or add(A) an acronym?\n')
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()


if __name__ == "__main__":
    main()


















# # def find_acronym(filename, acronym):
# #     try:
# #         with open(filename) as file:
# #             for line in file:
# #                 if acronym in line:
# #                     print(line)
# #                     return line
# #     except FileNotFoundError as e:
# #         print('File not found')
# #         return False
    
# #     # The entire file was parsed and we didn't find that acronym
# #     print('The acronym does not exist')
# #     return False

# # def add_acronym(filename, acronym, definition):
# #     try:
# #         with open(filename, 'a') as file:
# #             #file.write(acronym + ' - ' + definition + '\n')
# #             file.write(f"{acronym} - {definition}\n")
# #             return True
# #     except OSError:
# #         print('Cannot open file for writing.')
# #     return False

# # if __name__ == "__main__":
# #     # Ask the user whether they want to find or add an acronym
# #     filename = 'software_acronyms.txt'
# #     choice = input('Do you want to find(F) or add(A) an acronym?')
# #     if choice == 'F':
# #         look_up = input("What software acronym would you like to look up?\n")
# #         find_acronym(filename, look_up)
# #     elif choice == 'A':
# #         acronym = input('What acronym do you want to add?\n')
# #         definition = input('What is the definition?\n')
# #         add_acronym(filename, acronym, definition)

