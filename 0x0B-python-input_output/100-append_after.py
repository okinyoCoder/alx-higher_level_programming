#!/usr/bin/python3
'''  Search and update '''

def append_after(filename="", search_string="", new_string=""):
    ''' function that inserts a line of text to a file '''

    with open(filename, "r+") as f_object:
        lines = f_object.readlines()
        changed = []
        for line in range(len(lines)):
            changed.append(lines[line])
            if search_string in lines[line]:
                changed.append(new_string)

        f_object.seek(0)
        f_object.write("".join(changed))
