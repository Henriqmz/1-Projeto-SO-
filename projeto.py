import os
import sys

def main():
    history = []
    while True:
        directory = os.getcwd()
        prompt = input(f"-> {directory} > ")
        history.append(prompt)
        while prompt.startswith("rec "):
            if prompt.startswith("rec "):
                try:
                    prompt = history[int(prompt[4:])-1]
                except IndexError:
                    print("Not that many commands have been executed yet.")
                    break
                except ValueError:
                    print("That is not an integer.")
                    break

        if prompt == "history":
            for i in range(len(history)):
                print (f"{i+1} - {history[i]}")

        elif prompt.startswith("cd "):
            try:
                    os.chdir(prompt[3:])
            except FileNotFoundError:
                    print("This directory does not exist. ")

        elif prompt == "exit":
            break

        elif prompt == "clear history":
            history = []
            history.append(prompt)

        elif prompt.startswith("rec ") == False:
            test_command = os.system(prompt)
            if test_command != 0:
                for i in range(2):
                    sys.stdout.write('\x1b[1A') #move o cursor para a linha de cima
                    sys.stdout.write('\x1b[2K') #apaga a linha
                print ("\nInvalid command.")
                print ("Here's a list of some valid commands:\nmd, cd, dir, color, ping,\necho, del, whoami, tasklist,\nchkdsk, history, rec, exit.\n")
        
        else:
            continue
main()