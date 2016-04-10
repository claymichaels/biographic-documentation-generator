def joinname( fname, mname, lname, suffix ):
    name = ''
    if mname == '':
        name = fname + ' ' + lname
    else:
        name = fname + ' ' + mname + ' ' + lname
    if suffix != '':
        name = name + ' ' + suffix
    return name

def joinname( namelist ):
    name = ''
    if namelist[1] == '':
        name = namelist[0] + ' ' + namelist[2]
    else:
        name = namelist[0] + ' ' + namelist[1] + ' ' + namelist[2]
    if namelist[3] != '':
        name = name + ' ' + namelist[3]
    return name
