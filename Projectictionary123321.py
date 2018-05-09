import random
def check_word(y):
    if y in worddict:
        print(y)
        print(worddict[y])
def test():
    test={}
    print("Enter the meaning of following word")
    right_num=0
    wrong_num=len(worddict)
    print('ratio'+str(ratio))
    for i in range(0,3):
            rr=random.randrange(1,100,1)
            print(rr)
            if (rr<=ratio):
                test=right
            elif(rr>ratio):
                test=worddict
            word,me=random.choice(list(test.items()))
            print(word)            
            x=input()
            if(x.strip()==me.strip()):
                print('correct')
                right_num=right_num+1
                wrong_num=wrong_num-1
                worddict.pop(word)
                cright[word]=me
            else:
                print('Wrong Meaning Entered, the correct one is- '+me)   
try:
    m=open('Meaning.txt','r+')
    worddict={}
    worddict2=worddict
    right={}
    cright={}
    for i in m:
        (word,meaning)=i.split('-')
        worddict[word]=meaning
    lenword=len(worddict)
    c=open('Correct.txt','r+')
    for j in c:
        try:
            (cword,cmeaning)=j.split('-')
            right[cword]=meaning
        except ValueError as vrr:
            pass
    for w in right:
        if w in worddict:
            worddict.pop(w)
    lenright=len(right)
    ratio=round((lenright/lenword)*50,2)
    print("Enter F to find meaning or Enter T for Test")
    y=input()
    if(y=='F'):
        print("Enter your Word")
        check_word(input())
    if(y=='T'):
        test()
    print('\n',file=c)
    for k in cright:
        if k not in right:
            print(k+'-'+cright[k], file=c)
        elif k in right:
            pass
except IOError as err:
    print(str(err))
finally:
    c.close()
    m.close()
