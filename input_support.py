#Functions that convert input to appropriate data types or transform outcomes
#for better visualization.

def str2nlist(string):
    """
    Convert a string like '1,2,15' to a list like [1,2,15].
    
    Return the list.
    """
    i = 0
    result = []
    sn = ''
    while i < len(string):
        if string[i] != ',':
            sn += string[i]
        else:
            result.append(int(sn)-1)
            sn = ''
        i += 1
    result.append(int(sn)-1)
    return result

def add_num(names):
    """
    Add a number in front of each string element of the list.

    For example: ["Betty", "Jimmy"] will become ["1. Betty", "2. Jimmy"].

    Return the modified list.
    """
    nnames = []
    for i in range(len(names)):
        nnames.append('{}. {}'.format(str(i+1), names[i]))
    return nnames

def str2bool(string):
    """
    Convert yes/no answer to boolean true/false.
    """
    if string == "Yes":
        return True
    else:
        return False
