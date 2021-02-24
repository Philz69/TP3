totalNotes = input("Enter the total amount of notes")
notes = []
while True:
    inputString = input("Entrez une note:")
    try:
        note = float(inputString)
        notes.append(note) 
    except ValueError:
        pass
    print(notes)
