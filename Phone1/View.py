import Model


def printPhoneBook():
    # Важно !!! енумерате - чтобы управлять  записями и по кею удалять и т .п
    for i, item in enumerate(Model.phonebook):
        print(i , item)

def printSearch():
    # Важно !!! енумерате - чтобы управлять  записями и по кею удалять и т .п
    for i, item in enumerate(Model.searchArr):
        print(i , item)



