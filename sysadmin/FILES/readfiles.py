# >>> xmen_file = open('xmen_base.txt', 'r')
# >>> xmen_file
# <_io.TextIOWrapper name='xmen_base.txt' mode='r' encoding='UTF-8'>
# >>> xmen_file.read()
# 'Storm\nWolverine\nCyclops\nBishop\nNightcrawler'


# >>> xmen_file.read()
# 'Storm\nWolverine\nCyclops\nBishop\nNightcrawler'
# >>> xmen_file.read()
# ''
# >>> xmen_file.read()
# ''
# >>> xmen_file.seek(0)
# 0
# >>> xmen_file.read()
# 'Storm\nWolverine\nCyclops\nBishop\nNightcrawler'

# 'Storm\nWolverine\nCyclops\nBishop\nNightcrawler'
# >>> xmen_file.seek(6)
# 6
# >>> xmen_file.read()
# 'Wolverine\nCyclops\nBishop\nNightcrawler'



# >>> for line in xmen_file:
# ...     print(line, end="")
# ... 
# Storm
# Wolverine
# Cyclops
# Bishop
# Nightcrawler>>> 


# xmen_file.close()


# >>> xmen_file
# <_io.TextIOWrapper name='xmen_base.txt' mode='r' encoding='UTF-8'>
# >>> xmen_file.name
# 'xmen_base.txt'
# >>> 


#* use sempre with
# >>> with open('xmen_base.txt', 'a') as f:
# ...     f.write("Professor Careca\n")
# ... 
# 17
# >>> f
# <_io.TextIOWrapper name='xmen_base.txt' mode='a' encoding='UTF-8'>
# >>> f.read()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: I/O operation on closed file.
# >>> 


# >>> f = open('xmen_base.txt', 'a')
# >>> with f:
# ...     f.write("Careca Summers\n")