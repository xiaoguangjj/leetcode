# -*-encoding:UTF-8 -*-

#reverse string
# input "hello"
# output "olleh"

def reverse_string():
    a = "hello"
    b = ""
    for i in a[::-1]:
        b+=i
    print(b)

if __name__=="__main__":
    reverse_string()