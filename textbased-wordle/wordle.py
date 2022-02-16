import random, time, os
# from tkinter import messagebox

# start = time.time()

os.chdir(r'C:\Users\imnot\OneDrive\Desktop') #personalised to my pc

def generateWord():
    try:
        with open("wordlist.txt", "r") as f:
            word = f.read().splitlines() 
            global answer
            answer = [char for char in random.choice(word)]
            print(answer)
    except FileNotFoundError:
        print(f"Error: File not found!\nIs it in the correct directory: {os.getcwd()}?\nIs it one of these files: {os.listdir()}?")

def start():
    print("\n--Welcome to the text-based Wordle game! Start by typing in a 5 letter word.--\n")
    tries = 0
    status = False

    while tries < 6 and not status:
        while True:
            attempt = input()
            if len(attempt) != 5:
                print("\n--Please enter a 5 letter word.--\n")
                # messagebox.showerror("", "Not a 5 letter word!")
            else:
                break    
    
        a = [char for char in attempt]
        temp = ""
        if a == answer:
            temp = "🟩"*5
            status = True
            print(temp + "\n\nExcellent!")
        else:
            for x in range(len(a)):
                if a[x] == answer[x]:
                    temp += "🟩"
                elif a[x] in answer:
                    temp += "🟨"
                else:
                    temp += "⬛"
            print(temp)
        
        tries += 1 
    
    print(f"\nattempts: {tries}/6")
       
    if not status:
        print("\n--Game over--")
    
def main():
    generateWord()
    start()

main()

# print(time.time()-start)
