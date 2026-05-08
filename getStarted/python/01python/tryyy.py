import random
import msvcrt
import sys
words=("world","paper","botel","cat","dog","book","tree","fish","bird","lamp","desk","door","rock","moon","star","computer","elephant","mountain","keyboard","telephone","building","butterfly","chocolate","adventure","happiness","beautiful","wonderful","crocodile","fantastic","incredible")
heart=4
guessed_letters=[]
ans_Char=[]

live=True
hangman=[
    '''
       
                                                         _______
                                                        |/      |
                                                        |      
                                                        |      
     Welcome to Hangman Game!                           |       
                                                        |      
                                                        |
                                                       _|___
    

    ''',
                                                                 


    ''''

                                                         _______
                                                        |/      |
                                                        |      (_)
        Wrong! You have {heart} heart                         |      
                                                        |       
                                                        |      
                                                        |
                                                       _|___
    
''',
    ''''

                                                         _______
                                                        |/      |
                                                        |      (_)
        Wrong! You have {heart} heart                         |       |
                                                        |       |
                                                        |      
                                                        |
                                                       _|___
    
''',
    ''''

                                                         _______
                                                        |/      |
                                                        |      (_)
        Wrong! You have {heart} heart                         |      \\|/
                                                        |       |
                                                        |      
                                                        |
                                                       _|___
    
''',
    ''''

                                                         _______
                                                        |/      |
                                                        |      (_)
        Wrong! You are dead                             |      \\|/
            Game over                                   |       |
                                                        |      / \\
                                                        |
                                                       _|___
    
''',

   ]
def Counter(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    print(count_dict)
    return count_dict

def checkAnswer(randword, dword):
    global heart
    allChar=[]
    while heart>0:
        print(f"Guess the word: {randword}")
        donut=randword.split("_")
        for i in range(randword.count("_")):
            sys.stdout.write(f"\x1b[1A\x1b[{16+len(donut[i])}C")
            sys.stdout.flush()
            ch=msvcrt.getche().decode("utf-8")
            allChar.append(ch)
            sys.stdout.write(f"\x1b[1B\x1b[16D")
            sys.stdout.flush()
        print(allChar)
        print(ans_Char)
        if Counter(allChar)==Counter(ans_Char):
            guessed_letters.append(dword)
            print("You win!")
            allChar.clear()
            ans_Char.clear()
            break
        else:
            
            heart-=1
            print(hangman[4-heart].format(heart=heart))
            allChar.clear()
    
def randPicker(words):
    
    randword=random.choice(words)
    if randword in guessed_letters:
        randPicker(words)
        return
    if guessed_letters==words:
        print("You have guessed all words! Congratulations!")
        return

    perrandword=randword
    if len(randword)>5:
        i=0
        while i<2:
            randword=replaceChar(randword)
            
            i+=1
        
           
    else:
        randword=replaceChar(randword)

    
    checkAnswer(randword, perrandword)
   
        
             
    

    
def replaceChar(randword):
    
    randnum=random.randint(0,len(randword)-1)

    remlet=randword[randnum]
    if remlet in ans_Char:
        return replaceChar(randword)
    ans_Char.append(remlet)

    updated=randword.replace(remlet,"_",1)
    
    return updated

def qnsLoader():
    print(f"{hangman[0].format(heart=heart)}"
)
    Continue=True
    randPicker(words)
   
    while Continue:
        if heart<=0:
            choice2=input("Do you want to see the words you guessed? (y/n): ")    
            if choice2.lower()=="y":
                print("You guessed the following words:")
                for word in guessed_letters:
                    print(word)  
            Continue=False
        else:
            choice=input("Do you want to play again? (y/n): ")
            if choice.lower()!="y":  
                choice2=input("Do you want to see the words you guessed? (y/n): ")    
                if choice2.lower()=="y":
                    print("You guessed the following words:")
                    for word in guessed_letters:
                        print(word)  
                Continue=False
                print("Thanks for playing Hangman!")
      
            else:
                randPicker(words)

            
        
qnsLoader()