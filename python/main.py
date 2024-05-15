"""x = int(input('Enter first Number: '))
y = int(input('Enter second Number: '))
z = input('auto or your num: ')

def returns(a, b):
    result_list = []
    my_list = []
    global z  # Add this line to use the global variable 'z' inside the function

    if z == 'auto':
        # Assuming 'z' should be set to the product of 'a' and 'b' if it's 'auto'
        z = a * b
        for xc in range(1, 11):
            my_list.append(z * xc)
        print(my_list)

        for xvc in range(0, 10):
            if my_list[xvc] == a:
                result_list.append({a:xvc})
            if my_list[xvc] == b:
                result_list.append({b:xvc})
    else:
        z = int(z)
        for xc in range(0, 11):
            my_list.append(z * xc)
        print(my_list)

        for xvc in range(0, 10):
            if my_list[xvc] == a:
                result_list.append({a: xvc - 1})
            if my_list[xvc] == b:
                result_list.append({b: xvc - 1})

    print(result_list)




returns(x, y)



    for xc in range(1, 11):
        my_list.append(4 * xc)
    print(my_list)

    for xvc in range(0, 10):
        if my_list[xvc] == a:
            result_list.append({a:xvc+1})
        if my_list[xvc] == b:
            result_list.append({b:xvc+1})

x = int(input('Enter a Number: '))


bolem = True
numX = 0
numY = 0
resultNum = []

while bolem:
    numX += 1
    if numY * numX == x:
        resultNum.clear()
        resultNum.append({x:[numY,numX]})
        print(resultNum)
        bolem = False
    elif numX == 11:
        numY += 1
        numX = 0
    else:
        print(numY,numX,"=",numY*numX)
"""


try:
    i = int(input('Enter a number: '))
    print(f"Your number is {i}")
except Exception as e:
    print(e)

print('end')