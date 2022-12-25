import random


def result_median(arr):
    temp = find_median(arr)
    print ('Sorted version of array which is randomly generated')
    print(temp)
    if len(temp) % 2 != 0:
        return temp[len(temp) / 2]
    return (temp[len(temp) / 2 - 1] + temp[len(temp) / 2]) / 2


def find_median(arr):
    # Base case: if the array has 0 or 1 elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort the two halves
    left = find_median(left)
    right = find_median(right)
    # median the sorted halves back together
    return median(left, right)


def median(left, right):
    # Initialize an empty result array
    result = []

    # While there are elements in both left and right:
    while len(left) > 0 and len(right) > 0:
        # Compare the first elements of left and right
        if left[0] < right[0]:
            # If the first element of left is smaller, append it to the result array and remove it from left
            result.append(left[0])
            left.pop(0)
        else:
            # If the first element of right is smaller, append it to the result array and remove it from right
            result.append(right[0])
            right.pop(0)

    # Append any remaining elements from left or right to the result array
    result.extend(left)
    result.extend(right)

    return result


def create_array():
    # Create a random number for length
    size = random.randint(0, 100)
    arr = []
    for x in range(size):
        arr.append(random.randint(0, 100))

    return arr


def find_max_points(points, n, m):
    d = {'max_points': 0}
    f = {'path': []}

    def dfs(i, j, current_points):

        # Check if the current position is valid
        if i < 0 or i >= n or j < 0 or j >= m:
            return

        # Update the current points
        current_points += points[i][j]

        # Check if the current position is the destination
        if i == n - 1 and j == m - 1:
            # Update the maximum points and the path if necessary
            if current_points > d['max_points']:
                d['max_points'] = current_points
                f['path'].append([(i, j)])
            return

        # Recursively explore the next steps
        dfs(i, j + 1, current_points)
        dfs(i + 1, j, current_points)

    # Start the search from the first position
    dfs(0, 0, 0)
    return d['max_points'], f['path']


def main():
    print ('Welcome to My HW4')
    print ('------------Question 1------------')

    x_Axis = random.randint(4, 20)
    y_Axis = random.randint(4, 20)

    print ('Size of x: {}'.format(x_Axis))
    print ('Size of y: {}'.format(y_Axis))
    # Create 2D array
    game_board = [[0] * x_Axis for i in range(y_Axis)]
    for i in range(y_Axis):
        for j in range(x_Axis):
            game_board[i][j] = random.randint(0, 100)

    print ("Game Board")
    for i in range(y_Axis):
        for j in range(x_Axis):
            print (game_board[i][j]),
        print("")

    print('Calculation Loading...')
    max_points, path = find_max_points(game_board, y_Axis, x_Axis)
    print ('This is max path value')
    print(max_points)
    print(path)
    print ('----------------------------------')

    print ('------------Question 2------------')
    print ('Create random array for question 2')
    arr = create_array()
    print ('Length ( Randomly ) of random array:')
    print (len(arr))
    print ('Randomly generated array is : ')
    print (arr)
    print ('***Lets find median of this random array***')
    number = result_median(arr)
    print ('Median:')
    print (number)
    print ('----------------------------------')


main()
