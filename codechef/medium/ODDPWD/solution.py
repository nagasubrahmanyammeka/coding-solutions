# cook your dish here
def password(word):
    passw = word[0]+word[2]+word[4]
    return passw
    
    
word = input()
print(password(word))