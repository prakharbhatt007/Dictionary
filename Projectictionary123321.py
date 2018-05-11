import random
right={}
def check_word(y):
    if y in worddict:
        print(y)
        print(worddict[y])
def test():
    if(len(worddict)<3):
        print("Too less words in the database, please add some more")
        return
    test={}
    print("Enter the meaning of following word")
    right_num=0
    for i in range(0,3):
            if(random.randrange(0,100,1)<=ratio):
                test=right
            else:
                test=worddict
            word,me=random.choice(list(test.items()))
            print(word)            
            x=input()
            if(x.strip()==me.strip()):
                print('correct')
                worddict.pop(word)                
                cright[word]=me
            else:
                print('Wrong Meaning Entered, the correct one is- '+me)   
try:
    m=open('Meaning.txt','r+')
    c=open('Correct.txt','r+')
    worddict={}
    worddict2={}
    cright={}
    for i in m:
        (word,meaning)=i.split('-')
        worddict[word]=meaning
    for k in c:
        try:
            (word,meaning)=k.split('-')
            right[word]=meaning
        except ValueError as vr:
            pass
    lenright=len(right)
    lentotal=len(worddict)
    ratio=round(lenright/lentotal)*50
    print("Enter F to find meaning or Enter T for Test")
    y=input()
    if(y=='F'):
        print("Enter your Word")
        check_word(input())
    if(y=='T'):
        test()
    for z in cright:
        if z not in right:
            print(cright+'-'+cright[z],file=m)
        else:
            pass
except IOError as err:
    print(str(err))
finally:
    m.close()
    c.close()
