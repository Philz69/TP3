def note_moyenne(notes, totalNotes):
    moyenne = 0.0;
    for note in notes:
        moyenne = moyenne + note/totalNotes
    return moyenne

def ecart_type(notes, totalNotes):
    moyenne = note_moyenne(notes, totalNotes)
    ecartType = 0.0;
    for note in notes:
        ecartType = ecartType + ((note - moyenne)**2)
    ecartType = ecartType/totalNotes
    ecartType = ecartType**(1/2)
    return ecartType

while True:
    totalNotes = input("Enter the total amount of notes")
    if totalNotes.isnumeric():
        totalNotes = int(totalNotes)
        break

notes = []
while len(notes) < totalNotes:
    inputString = input("Entrez une note:")
    try:
        note = float(inputString)
        notes.append(note) 
    except ValueError:
        pass

print(notes)
print(note_moyenne(notes,totalNotes))
print(ecart_type(notes,totalNotes))