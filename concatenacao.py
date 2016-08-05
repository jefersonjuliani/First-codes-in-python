'''
    faca um programa que leia uma palavra e troque as vogais por "*"
'''
word = raw_input()
x=0
while  x < len(word):
    if word[x] in 'aeiou':
        word = word[:x] + '*'+ word[x+1:]
    x+=1
print word
