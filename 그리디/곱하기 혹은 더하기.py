number = input()
max_val = 0
for i in number:
    if max_val*int(i) == 0 :
        max_val = max_val+int(i)
    else :
        max_val = max_val*int(i)
print(max_val)