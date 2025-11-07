acronym = input('What acronym do you want to add?\n')
definition = input('What is the definition?\n')
with open('acronyms.txt', 'a') as file:
    file.write(acronym + ' - ' + definition + '\n')


# perguntat o acronysmo que ele quer
#perguntar a definição
# open o arquivo 
# escrever o arquivo e a definição no arquivo.