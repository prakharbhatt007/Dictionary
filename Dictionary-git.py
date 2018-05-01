import random
wrong={}
right={}
try:
    def check_word(y):
        if y in worddict:
            print(y)
            print(worddict[y])
    def test():
        print("Enter the meaning of following word")
        for i in range(0,3):
                word,me=random.choice(list(worddict.items()))
                print(word)
                
                wrong_num=0
                right_num=0
                x=input()
                if(x.strip()==me.strip()):
                    print('correct')
                    right_num=right_num+1
                    right[word]=me
                else:
                    print('Wrong Meaning Entered, the correct one is- '+me)
                    wrong_num=wrong_num+1
                    wrong[word]=me
        print(right)
        print(wrong)
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
except IOError as err:
    print(str(err))
