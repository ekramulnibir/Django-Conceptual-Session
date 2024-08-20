from django.shortcuts import render

MyNotes = [{'id': 1, 'title': 'First Note', 'entries':['Entry 1.1','Entry 1.2','Entry 1.3']},
           {'id': 2, 'title': 'Second Note', 'entries':['Entry 2.1','Entry 2.2','Entry 2.3']},
           {'id': 3, 'title': 'Third Note', 'entries':['Entry 3.1','Entry 3.2','Entry 3.3']},
           ]
# Create your views here.
def index(request):
    return render(request,'./notes/index.html')

def notes(request):
    notes = MyNotes
    context = {'notes':notes}
    return render(request, './notes/notes.html', context)

def note(requent, note_id):
    for myNote in MyNotes:
        if myNote['id'] == note_id:
            note = myNote

    entries = note['entries']
    context ={'note':note, 'entries':entries}

    return render(requent, 'notes/note.html', context)
            


