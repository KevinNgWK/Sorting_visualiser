"""
Code that visualises quicksort algorithm
Color Representation:
    Blue: Unsorted
    Green: Sorted
    Yellow: Current indexes
"""
import pygame
import random

def create_dict(arr_size, win_size, bar_width = 20):
    """
    Function that creates a dictionary to map indexes to their corresponding x-coordinate
    Parameters:
        arr_size: size of 1D array (number of integers to be sorted)
        win_size: size of display window
        bar_width: width of bars
    Output:
        index_dict: python dictionary mapping index to x-coordinate
    """
    index_dict = {}

    x = (win_size[0] - (bar_width + 1) * arr_size) // 2
    for i in range(arr_size):
        index_dict[i] = x
        x += (bar_width + 1)

    return index_dict


def initialise_arr(arr_size, num_range):
    """
    Function that initialises array. Will return the initialised array
    Parameters:
        arr_size: size of array (int)
        num_range: range of numbers (start, end)
    Output:
        arr: initialised array
    """
    arr = []
    for i in range(arr_size):
        arr.append(random.randint(num_range[0], num_range[1]))

    return arr


def initialise_bars(arr, index_dict, win, win_size, bar_width=20):
    """
    Function that initialises the bars at first
    """
    for i in range(len(arr)):
        draw_bar(i, arr[i], index_dict, win, win_size, bar_width, color="blue")


def draw_bar(index, value, index_dict, win, win_size, bar_width = 20, color = "yellow"):
    """
    Function to draw a bar
    Parameters:
        index: index position in array. Provides x-axis location to draw bar
        value: value to be drawn. Signifies the height of the bar
        index_dict: python dictionary that maps index to x axis location
        win: display window
        win_size: size of display window (x, y)
        color: color to draw the bar
        bar_width: width of bar to be drawn
    """
    color_dict = {"white":(255,255,255), "grey":(160,160,160), "blue":(0,0,204), "green":(0,255,128), "yellow":(255,255,51)}

    x_pos = index_dict[index]
    y_pos = win_size[1] - value

    pygame.draw.rect(win, color_dict[color], (x_pos, y_pos, bar_width, value))


def swap(index1, index2, arr, index_dict, win, win_size, bar_width = 20, time_delay = 200):
    """
    Function that takes in 2 indexes, and swaps them. When selecting indexes to swap, we first color them red
    """
    value1 = arr[index1]
    value2 = arr[index2]

    #Color the 2 indexes red
    draw_bar(index1, value1, index_dict, win, win_size, bar_width, "yellow")
    draw_bar(index2, value2, index_dict, win, win_size, bar_width, "yellow")
    pygame.display.update()
    pygame.time.delay(time_delay)

    #swap the 2 indexes in display window
    draw_bar(index1, value1, index_dict, win, win_size, bar_width, "white")
    draw_bar(index2, value2, index_dict, win, win_size, bar_width, "white")
    draw_bar(index1, value2, index_dict, win, win_size, bar_width, "blue")
    draw_bar(index2, value1, index_dict, win, win_size, bar_width, "blue")
    pygame.display.update()
    pygame.time.delay(time_delay)

    #Swap the 2 indexes in array
    arr[index1], arr[index2] = arr[index2], arr[index1]


def pivot_swap(pivot_index, index, arr, index_dict, win, win_size, bar_width = 20, time_delay = 200):
    """
    Function that takes in 2 indexes, and swaps them. When selecting indexes to swap, we first color them red
    Pivot will be grey in color
    """
    pivot = arr[pivot_index]
    value = arr[index]

    #Color the 2 indexes red
    draw_bar(pivot_index, pivot, index_dict, win, win_size, bar_width, "grey")
    draw_bar(index, value, index_dict, win, win_size, bar_width, "yellow")
    pygame.display.update()
    pygame.time.delay(time_delay)

    #swap the 2 indexes in display window
    draw_bar(pivot_index, pivot, index_dict, win, win_size, bar_width, "white")
    draw_bar(index, value, index_dict, win, win_size, bar_width, "white")
    draw_bar(pivot_index, value, index_dict, win, win_size, bar_width, "blue")
    draw_bar(index, pivot, index_dict, win, win_size, bar_width, "grey")
    pygame.display.update()
    pygame.time.delay(time_delay)

    #Swap the 2 indexes in array
    arr[pivot_index], arr[index] = arr[index], arr[pivot_index]


def partition(start_index, end_index, arr, index_dict, win, win_size, bar_width=20, time_delay = 200):
    """
    Function that does the partition of the algorithm
    Returns the index of pivot
    """
    #Step 1: create a random pivot, and place it at the end 
    pivot_index = random.randint(start_index, end_index)
    pivot = arr[pivot_index]
    pivot_swap(pivot_index, end_index, arr, index_dict, win, win_size, bar_width, time_delay)

    #Step 2: iterate through the other indexes, and arrange them to the left/right of pivot
    j = start_index
    for i in range(start_index,end_index):
        if arr[i] <= pivot:
            swap(i, j, arr, index_dict, win, win_size, bar_width, time_delay)
            j += 1
        else:
            continue

    #Step 3: swap the pivot with its correct position
    pivot_swap(end_index, j, arr, index_dict, win, win_size, bar_width)
    draw_bar(j, pivot, index_dict, win, win_size, bar_width, "green")

    return j


def quicksort_section(index_tuple, arr, index_dict, win, win_size, bar_width = 20, time_delay = 200):
    """
    Function that does quicksort on one section of the array
    Parameters:
        index_tuple: A tuple containing start and end index. (start_index, end_index)
        arr: array of integers
        index_dict: Python dictionary mapping indexes to their display window x-coordinates
        win: display window
        win_size: size of display window
        bar_width: width of a bar
    Output:
        left_index_tuple: A tuple containing start and end index of left half of partition (start_index, end_index)
        right_index_tuple: A tuple containing start and end index of right half of partition (start_index, end_index)
    """
    start_index = index_tuple[0]
    end_index = index_tuple[1]

    if end_index-start_index <= 0:      #Base case (if section no longer requires sorting)
        draw_bar(start_index, arr[start_index], index_dict, win, win_size, bar_width, "green")
        pygame.display.update()
        pygame.time.delay(200)
        return 0,0

    #Partition the section
    p = partition(start_index, end_index, arr, index_dict, win, win_size, bar_width, time_delay)

    if p == end_index:
        right_index_tuple = 0
    else:
        right_index_tuple = (p+1, end_index)
    if p == start_index:
        left_index_tuple = 0
    else:
        left_index_tuple = (start_index, p-1)

    return left_index_tuple, right_index_tuple


def full_quicksort(arr_size, arr, index_dict, win, win_size, bar_width = 20, time_delay = 200):
    """
    Main Function to be called to do entire quicksort visualisation
    """
    #This queue is a queue of tuples that indicate start and end indexes
    queue = [(0, arr_size-1)]
    while len(queue) != 0:
        index_tuple = queue.pop(0)
        left_index_tuple, right_index_tuple = quicksort_section(index_tuple, arr, index_dict, win, win_size, bar_width, time_delay)
        if left_index_tuple != 0:
            queue.append(left_index_tuple)
        if right_index_tuple != 0:
            queue.append(right_index_tuple)


#Settings
win_size = (1200, 600)      #Size of window
arr_size = 100               #Size of array
num_range = (100,500)       #Range of integers (values)
bar_width = 10              #Width of a bar
time_delay = 10            #Adjust speed of swaps

#Initialise Pygame and display background
pygame.init()
win = pygame.display.set_mode(win_size)
pygame.display.set_caption("QuickSort Visualiser")
win.fill((255,255,255))

#Initialise parameters needed
index_dict = create_dict(arr_size, win_size, bar_width=bar_width)       #Maps index to coordinate
arr = initialise_arr(arr_size, num_range)                               #Initialise array with random int
initialise_bars(arr, index_dict, win, win_size, bar_width=bar_width)    #Initialise starting bars

pygame.display.update()

#Main loop
main_run = True
algo_run = False
restart = False
while main_run:
    pygame.time.delay(10)

    for event in pygame.event.get():        #Event so that user can quit program
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RETURN]:
        if algo_run == False and restart == True:   #Press Enter to restart
            win.fill((255,255,255))
            arr = initialise_arr(arr_size, num_range)
            initialise_bars(arr, index_dict, win, win_size, bar_width=bar_width)
            restart = False

        elif algo_run == True and restart == False: #Press Enter to start sorting
            full_quicksort(arr_size, arr, index_dict, win, win_size, bar_width, time_delay)
            algo_run = False
            restart = True

        elif algo_run == False and restart == False:
            algo_run = True

    pygame.display.update()