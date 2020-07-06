# write your code here
def letter():
    global count
    if count % 2 == 0:
        return 'X'
    else:
        return 'O'


def check(coord_):
    # print(coord_)
    nos = '1234567890'
    nos1 = '123'
    if coord_[0] not in nos:
        if coord_[1] not in nos:
            print('You should enter numbers!')
            return False
    if coord_[0] in nos1:
        if coord_[1] in nos1:
            return True
    print('Coordinates should be from 1 to 3!')
    return False


def coord():
    x = input('Enter the coordinates:').split()
    return x


def coord_empty(x):

    if cells[x] == '_' or cells[x] == ' ':
        return True
    print('This cell is occupied! Choose another one!')
    return False


def print_cell():
    print(f"""
    ---------
    | {cells[0]} {cells[1]} {cells[2]} |
    | {cells[3]} {cells[4]} {cells[5]} |
    | {cells[6]} {cells[7]} {cells[8]} |
    ---------
    """)


def change(coord_):
    global cells
    if check(coord_):
        if coord_ == ['1', '1']:
            if coord_empty(6):
                cells = cells[:6] + letter() + cells[7:]
                print_cell()
            else:
                coord__ = coord()
                change(coord__)
        elif coord_ == ['1', '2']:
            if coord_empty(3):
                cells = cells[:3] + letter() + cells[4:]
                print_cell()
            else:
                coord__ = coord()
                change(coord__)
        elif coord_ == ['1', '3']:
            if coord_empty(0):
                cells = letter() + cells[1:]
                print_cell()
            else:
                coord__ = coord()
                change(coord__)
        elif coord_ == ['2', '1']:
            if coord_empty(7):
                cells = cells[:7] + letter() + cells[8:]
                print_cell()
            else:
                coord__ = coord()
                change(coord__)
        elif coord_ == ['2', '2']:
            if coord_empty(4):
                cells = cells[:4] + letter() + cells[5:]
                print_cell()
            else:
                coord__ = coord()
                change(coord__)
        elif coord_ == ['2', '3']:
            if coord_empty(1):
                cells = cells[:1] + letter() + cells[2:]
                print_cell()
            else:
                coord__ = coord()
                change(coord__)
        elif coord_ == ['3', '1']:
            if coord_empty(8):
                cells = cells[:8] + letter()
                print_cell()
            else:
                coord__ = coord()
                change(coord__)
        elif coord_ == ['3', '2']:
            if coord_empty(5):
                cells = cells[:5] + letter() + cells[6:]
                print_cell()
            else:
                coord__ = coord()
                change(coord__)
        elif coord_ == ['3', '3']:
            if coord_empty(2):
                cells = cells[:2] + 'X' + cells[3:]
                print_cell()
            else:
                coord__ = coord()
                change(coord__)
    else:
        coord__ = coord()
        change(coord__)


def empty():
    letter1 = [x for x in cells]
    if '_' in letter1:
        return True
    if ' ' in letter1:
        return True
    return False


def o_wins():
    if cells[0] == cells[1] == cells[2] == 'O':
        return True
    if cells[3] == cells[4] == cells[5] == 'O':
        return True
    if cells[6] == cells[7] == cells[8] == 'O':
        return True
    if cells[0] == cells[4] == cells[8] == 'O':
        return True
    if cells[2] == cells[4] == cells[6] == 'O':
        return True
    if cells[0] == cells[3] == cells[6] == 'O':
        return True
    if cells[1] == cells[4] == cells[7] == 'O':
        return True
    if cells[2] == cells[5] == cells[8] == 'O':
        return True
    return False


def x_wins():
    if cells[0] == cells[1] == cells[2] == 'X':
        return True
    if cells[3] == cells[4] == cells[5] == 'X':
        return True
    if cells[6] == cells[7] == cells[8] == 'X':
        return True
    if cells[0] == cells[4] == cells[8] == 'X':
        return True
    if cells[2] == cells[4] == cells[6] == 'X':
        return True
    if cells[0] == cells[3] == cells[6] == 'X':
        return True
    if cells[1] == cells[4] == cells[7] == 'X':
        return True
    if cells[2] == cells[5] == cells[8] == 'X':
        return True
    return False


def not_fin():
    if empty():
        return True


def draw():
    if x_wins() or o_wins() or empty():
        return False
    return True


def cell_wins():

    if o_wins():
        return 'O'
    if x_wins():
        return 'X'


def imp():
    if o_wins() and x_wins():
        return True
    elif cells.count('O') - cells.count('X') > 1:
        return True
    elif cells.count('X') - cells.count('O') > 1:
        return True


def printing():
    print('empty', empty())
    print('o win', o_wins())
    print('x win', x_wins())
    print(cell_wins())
    print('not finish', not_fin())
    print('draw', draw())
    print('impossible1', imp())


def state():
    # printing()
    if imp():
        return 'Impossible'
    if cell_wins():
        return f'{cell_wins()} wins'
    elif not_fin():
        return "Game not finished"
    elif draw():
        return 'Draw'


cells = '         '
count = 0
print_cell()

con = [imp(), o_wins(), x_wins(), draw()]
while not_fin():
    coordinates = coord()
    change(coordinates)
    count += 1
    # print([imp(), o_wins(), x_wins(), draw()])
    # if any(con):
    #         print(con)
    #         print(state())
    #         exit()
    if x_wins() or o_wins():
        print(f'{cell_wins()} wins')
        exit()
else:
    print('Draw')
