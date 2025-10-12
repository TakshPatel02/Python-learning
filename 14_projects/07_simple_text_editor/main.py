def simple_text_editor():
    print("Welcome to the simple text editor!")
    filename = input("Enter the filename to open or create: ")

    with open(filename , 'w') as file:
        print(f"Start typing your text. Type 'SAVE' on a new line to save and exit. ")
        lines = []
        
        while True:
            line = input()
            if line.strip().upper() == 'SAVE':
                break
            lines.append(line)
        
        file.write('\n'.join(lines))

    print(f"Your text has been saved to {filename}")

simple_text_editor()