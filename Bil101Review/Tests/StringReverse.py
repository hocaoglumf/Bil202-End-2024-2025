def reverse_string(s):
    sr=""
    for i in range(len(s)-1,-1,-1):
        sr +=s[i]
    return sr


name="Bil202 Programlama"

print(reverse_string(name))