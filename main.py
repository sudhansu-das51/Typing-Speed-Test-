import time
string = 'Siya ek number ki chutiya he'
word_count = len(string.split())
border = '---*---'*20

def creatbox():
    print(border)
    print()
    print('Enter the phrase as fast as posssible and with accuracy')
    print()

while 1:
    t0 = time.time()
    creatbox()
    print(string, '\n')
    inputText = str(input())    
    t1 = time.time()
    lengthofInput = len(inputText.split())
    accuracy = len(set(inputText.split()) & set(string.split()))
    accuracy = (accuracy/word_count)
    timeTaken = (t1 - t0)
    wordsperminute = (lengthofInput/timeTaken)*60
    print('Total words \t :' , lengthofInput)
    print('Time used \t :' , round(timeTaken,2), 'seconds')
    print('Your accuracy \t :' , round(accuracy,3)*100, '%')
    print('Speed is \t :' , round(wordsperminute,2), 'words per minute')
    print('Do you want to retry', end='')
    if input():
        continue
    else:
        print('Thankyou.')
        time.sleep(1.5)
        break
