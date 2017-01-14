"""This is the entry point of the program."""


def create_box(height, width, character):
    if height>=1 and width>=1:
        box=character*int(width)
    box = heibox+'\n'
        return box
    else:
        return 'Error'
        
def crehollow_box(height, width, character):
    if height>=1 and width>=1:
        toprow=character*int(width)
        midrow=character+' '*(width-2)+character
        hollow_box = toprow + '\n' + (height-2)*(midrow+'\n') + toprow
        return hollow_box
    else:
        return 'Error'
        
if  __name__ == '__main__':
    create_box(3, 4, '*')
    create_hollow_box(3,4,'*')
