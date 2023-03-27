sorted_list_note = []


def luke_skywalker(list_note):
    for i_note in list_note:
        if i_note < 40:
            sorted_list_note.append(i_note)

        if i_note > 40:
            if (i_note + 2) % 5 == 0:
                sorted_list_note.append(i_note + 2)
            elif (i_note + 1) % 5 == 0:
                sorted_list_note.append(i_note + 1)
            else:
                sorted_list_note.append(i_note)

    print(sorted_list_note)


luke_skywalker([12, 41, 2, 45, 83, 84, 77, 78, 79])
