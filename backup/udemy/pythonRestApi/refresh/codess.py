l = ["Alexandre", "Andre", "Alex"] # listas 
t = ("Alexandre", "Andre", "Alex") # tuplas, não podem ser mudadas depois de criadas
s = {"Alexandre", "Andre", "Alex"} # sets, não tem ordem

print(l[0])
l[2] = "goku"
print(l)
l[2] = "Alex"
print(l)

l.append("goku")

print(l)
l.remove("goku")
print(l)


