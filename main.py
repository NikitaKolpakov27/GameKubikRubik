import random
import PyQt5
import copy
import test1

cube1 = [["к", "ж"], ["с", "з"]]
cube2 = [["ж", "к"], ["з", "с"]]
cube3 = [["с", "ж"], ["к", "з"]]
cube4 = [["з", "с"], ["к", "ж"]]

def print_array(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j], end=" ")
        print()
    print()

def list_rot_right( data, times = 1 ):
    rot_data = []
    for t in range( times ):
        m = len( data )
        n = len( data[0] )
        rev_data = data[ : : -1]
        rot_data = [ [rev_data[j][i] for j in range( m ) ] for i in range( n ) ]
        data = rot_data
    return rot_data

def get_colours():
    cube = [["o", "o"], ["o", "o"]]
    array_temp = ["к", "ж", "з", "с"]

    elem1 = random.choice(array_temp)
    cube[0][0] = elem1
    array_temp.remove(elem1)

    elem1 = random.choice(array_temp)
    cube[0][1] = elem1
    array_temp.remove(elem1)

    elem1 = random.choice(array_temp)
    cube[1][0] = elem1
    array_temp.remove(elem1)

    elem1 = random.choice(array_temp)
    cube[1][1] = elem1
    array_temp.remove(elem1)

    return cube

def upper_array(arr1, arr2):
    arr_12 = copy.deepcopy(arr1)

    for i in range(len(arr_12)):
        for j in range(len(arr_12[i])):
            arr_12[i].append(arr2[i][j])
    return arr_12

def down_array(arr1, arr2):
    return upper_array(arr1, arr2)

def rot_left_center(cube_full, func):
    cube_center = [["o", "o"], ["o", "o"]]

    cube_center[0][0] = cube_full[1][1]
    cube_center[0][1] = cube_full[1][2]
    cube_center[1][0] = cube_full[2][1]
    cube_center[1][1] = cube_full[2][2]

    cube_center = func(cube_center)
    cube_full[1][1] = cube_center[0][0]
    cube_full[1][2] = cube_center[0][1]
    cube_full[2][1] = cube_center[1][0]
    cube_full[2][2] = cube_center[1][1]
    return cube_full

def rot_right_center(cube_full, func):
    return rot_left_center(cube_full, func)

def list_rot_left(data, times = 1):
    return list_rot_right(data, 4 - times)

# print_array(cube1)
# print()
# print_array(list_rot_right(cube1))
# print()
# print_array(list_rot_left(cube1))
test_cube1 = get_colours()
test_cube2 = get_colours()
test_cube3 = get_colours()
test_cube4 = get_colours()

# arr1 = [[1, 2], [3, 4]]
# arr2 = [[1, 2], [3, 4]]
#
# arr_12 = upper_array(arr1, arr2)
# print_array(arr_12)
# print()
#
# arr1 = list_rot_right(arr1)
# arr_12 = upper_array(arr1, arr2)
# print_array(arr_12)

cube_13 = upper_array(test_cube1, test_cube3)
cube_24 = down_array(test_cube2, test_cube4)
# print_array(cube_13)
# print_array(cube_24)
# print()
cube_full = cube_13 + cube_24
# cube_center = [["o", "o"], ["o", "o"]]
#
# cube_center[0][0] = cube_full[1][1]
# cube_center[0][1] = cube_full[1][2]
# cube_center[1][0] = cube_full[2][1]
# cube_center[1][1] = cube_full[2][2]
# #print_array(cube_center)
#
# cube_center = list_rot_right(cube_center)
# cube_full[1][1] = cube_center[0][0]
# cube_full[1][2] = cube_center[0][1]
# cube_full[2][1] = cube_center[1][0]
# cube_full[2][2] = cube_center[1][1]
#
# print_array(cube_full)

# print_array(cube_full)
# print()
# cube_full = rot_right_center(cube_full, list_rot_right)
# print_array(cube_full)
def isSameElements(array):
    elem = array[0]
    count = 0
    for i in range (len(array)):
        if (elem == array[i]):
            count += 1

    if (count == len(array)):
        return True
    else:
        return False

def checkWin(array):
    sres_1_demo = array[0]
    sres_1 = sres_1_demo[0:4]

    sres_2_demo = array[1]
    sres_2 = sres_2_demo[0:4]

    sres_3_demo = array[2]
    sres_3 = sres_3_demo[0:4]

    sres_4_demo = array[3]
    sres_4 = sres_4_demo[0:4]

    # if (isSameElements(sres_1) and isSameElements(sres_2) and
    #         isSameElements(sres_3) and isSameElements(sres_4)):
    #     return True
    # else:
    #     return False

    if (sres_1 == sres_2 and sres_3 == sres_4):
        return True
    else:
        return False

if __name__ == "__main__":
    arr = [["1", "1", "1", "2"], ["1", "3", "3", "3"], ["3", "3", "4", "4"], ["3", "3", "4", "4"]]
    arr2 = [["r", "r", "g", "g"], ["r", "r", "g", "g"], ["y", "y", "b", "b"], ["y", "y", "b", "b"]]
    arr3 = [["r", "r", "g", "g"], ["r", "r", "g", "g"], ["y", "y", "b", "b"], ["y", "y", "b", "b"]]
    print(checkWin(arr))
    print(checkWin(arr2))
