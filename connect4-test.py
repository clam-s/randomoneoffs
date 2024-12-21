import pytest
from connect4 import winCheck

verticalwin = [
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['B','-','-','-','-','-','-'],
    ['B','-','-','-','-','-','-'],
    ['B','-','-','-','-','-','-'],
    ['B','-','-','-','-','-','-']
]

horizontalwin = [
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['B','B','B','B','-','-','-']
]

digonalL = [
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','B','-','-','-'],
    ['-','-','B','-','-','-','-'],
    ['-','B','-','-','-','-','-'],
    ['B','-','-','-','-','-','-']
]

diagonalR = [
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['B','-','-','-','-','-','-'],
    ['-','B','-','-','-','-','-'],
    ['-','-','B','-','-','-','-'],
    ['-','-','-','B','-','-','-']
]

assert winCheck(0,5,verticalwin) is True, "Bottom vertical fail"
assert winCheck(0,4,verticalwin) is True, "Bottom middle vertical fail"
assert winCheck(0,3,verticalwin) is True, "top middle vertical fail"
assert winCheck(0,2,verticalwin) is True, "top vertical fail"
assert winCheck(0,5, horizontalwin) is True, "left horizontal fail"
assert winCheck(1,5, horizontalwin) is True, "left horizontal fail"
assert winCheck(2,5, horizontalwin) is True, "left horizontal fail"
assert winCheck(3,5, horizontalwin) is True, "left horizontal fail"
assert winCheck(0,5, digonalL) is True, "Ldiagnol fail"
assert winCheck(1,4, digonalL) is True, "Ldiagnol fail"
assert winCheck(2,3, digonalL) is True, "Ldiagnol fail"
assert winCheck(3,2, digonalL) is True, "Ldiagnol fail"
assert winCheck(0,2,diagonalR) is True, "Rdiagnonal fail"
assert winCheck(1,3,diagonalR) is True, "Rdiagnonal fail"
assert winCheck(2,4,diagonalR) is True, "Rdiagnonal fail"
assert winCheck(3,5,diagonalR) is True, "Rdiagnonal fail"
