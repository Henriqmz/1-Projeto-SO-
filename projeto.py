import os

def main():
    history = []
    while True:
        directory = os.getcwd()
        prompt = input(f"-> {directory} > ")
        history.append(prompt)

        while prompt.startswith("rec "):
            if prompt == "rec 0":
                print("Tried to use rec 0 (Program starts counting from 1).")
                break
            else:
                try:
                    prompt = history[int(prompt[4:])-1]
                except IndexError:
                    print("Not that many commands have been executed yet.")
                    break
                except ValueError:
                    print("That is not an integer.")
                    break

        if prompt == "rec":
            try:
                prompt = history[-2]
                if prompt == "rec":
                    print ("Last command was a rec")
                    continue
            except IndexError:
                print ("Tried to use 'rec' as first command")
                continue

        if prompt == "history":
            for i in range(len(history)):
                print (f"{i+1} - {history[i]}")

        elif prompt == "cd":
            os.chdir(os.environ["USERPROFILE"])

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
                print('\x1b[2A') #move o cursor para a linha de cima
                print('\x1b[2K') #apaga a linha
                print('\x1b[3A')
                print('\x1b[2K')
                print ("Invalid command.")
                print ("Here's a list of some valid commands:\nmd, cd, dir, color, ping,\necho, del, whoami, tasklist,\nchkdsk, history, rec, exit.\n")
        
        else:
            continue
main()
