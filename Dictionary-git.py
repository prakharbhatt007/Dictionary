import random
right={}

def check_word(y):
    if y in worddict:
        print(y)
        print(worddict[y])
def test():
    print("Enter the meaning of following word")
    right_num=0
    wrong_num=len(worddict)
    for i in range(0,3):
            word,me=random.choice(list(worddict.items()))
            print(word)            
            x=input()
            if(x.strip()==me.strip()):
                print('correct')
                right_num=right_num+1
                wrong_num=wrong_num-1
                worddict.pop(word)
                print(right_num)
                print(wrong_num)
                right[word]=me
            else:
                print('Wrong Meaning Entered, the correct one is- '+me)   
try:
    m=open('Meaning.txt','r+')
    worddict={}
    for i in m:
        (word,meaning)=i.split('-')
        worddict[word]=meaning
    print("Enter F to find meaning or Enter T for Test")
    y=input()
    if(y=='F'):
        print("Enter your Word")
        check_word(input())
    if(y=='T'):
        test()
    print(str(right)+'-'+str(me),file=m)
    print(worddict,file=m)
except IOError as err:
    print(str(err))
