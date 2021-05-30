from simpleimage import SimpleImage
import random
""" Program wil count Fibonacci numbers and set images in Fibonaci numbers order"""
''' Impotring and making image list'''

guitar1 = SimpleImage('guitar1.jpg')
guitar2 = SimpleImage('guitar2.jpeg')
guitar3 = SimpleImage('guitar3.jpg')
guitar4 = SimpleImage('guitar4.jpg')
guitar5 = SimpleImage('guitar5.jpg')
guitar6 = SimpleImage('guitar6.jpg')
guitar7 = SimpleImage('guitar7.jpg')
guitar8 = SimpleImage('guitar8.jpg')
guitar9 = SimpleImage('guitar9.png')
guitar10 = SimpleImage('guitar10.jpg')
guitar11 = SimpleImage('guitar11.jpg')
guitar12 = SimpleImage('guitar12.jpg')
guitar13 = SimpleImage('guitar13.jpg')
guitar14 = SimpleImage('guitar14.jpg')
guitar15 = SimpleImage('guitar15.jpg')
guitar16 = SimpleImage('guitar16.jpg')
guitar17 = SimpleImage('guitar17.jpg')
guitar18 = SimpleImage('guitar18.jpg')
guitar19 = SimpleImage('guitar19.jpg')
guitar20 = SimpleImage('guitar20.jpg')


guitars = [guitar1, guitar2, guitar3, guitar4, guitar5, guitar6, guitar7, guitar8, guitar9, guitar10, guitar11, guitar12, guitar13, guitar14, guitar15, guitar16, guitar17, guitar18, guitar19, guitar20 ]


""" Funcion will count Fibonnaci numbers"""

NUMBER =12

def fibonacci_numbers(NUMBER):
    if NUMBER == 0:
        fib = 0
    x = 0
    y = 1
    fibonacci_num = []
    fib = 1
    for i in range(NUMBER -1):
        fibonacci_num.append(fib)
        fib = x + y
        x = y
        y = fib
    return fib

''' Making blank image and inserting images from guitar list'''
        
def fib_images(cordinates, blank_image):
    for i in range(NUMBER):
        bl_image = SimpleImage.blank(fibonacci_numbers(cordinates[i][0]), fibonacci_numbers(cordinates[i][0]))
        git_choice =random.choice(guitars)
        git_choice.make_as_big_as(bl_image)
        width = git_choice.width
        height = git_choice.height
        guitars.remove(git_choice)
        
        
        for y in range(height):
            for x in range (width):
                pixel = git_choice.get_pixel(x, y)
                blank_image.set_pixel(x +cordinates[i][1], y + cordinates[i][2], pixel)
    blank_image.show()

''' Evrey image shoud have pozicion and size. To count that I split all images in 4 groups. Each group have diferent reminder divided by 4.
Funcion count_x_reminder_1 wil count x point for all images with reminder 1... 
Funcion cordinares_reminder_1() wil make list [number of image, x cordinate, y cordinate] for all images with reminder 1...'''

#cordinates for all images with reminder 1
def count_x_reminder_1():  
    my_dict = {}
    x_point = 0
    for i in range(NUMBER, 0, -1):
        if i%4 ==1:
            x_point +=fibonacci_numbers(i +3)
            my_dict[i] = x_point
    return (my_dict)



def count_y_reminder_1():  
    my_dict = {}
    x_point = fibonacci_numbers(NUMBER)
    for i in range(NUMBER, 0, -1):
        if i % 4 == 1 and i < NUMBER - 2:
            x_point -=fibonacci_numbers(i)
            my_dict[i] = x_point
    return(my_dict)


a = count_x_reminder_1()
b = count_y_reminder_1()



def cordinates_reminder_1():
    x_rem_1 = []
    for key in a:
        x = ([key, a[key]])
        x_rem_1.append(x)
    ys = []
    for key in b:
        y = ([key, b[key]])
        ys.append(y)
    for i in x_rem_1:
        for k in ys:
            if i[0] == k[0]:
                i.append(k[1])
    return (x_rem_1)


#cordinates for all images with reminder 2
'''----------------------------------------------------------------------------'''
def count_x_reminder_2():  
    my_dict = {}
    x_point = 1
    #print(x_point(type))
    for i in range(1, NUMBER + 1):
        if i % 4 == 0:
            x_point +=fibonacci_numbers(i)
    for i in range(1, NUMBER + 1):
        if i%4 ==2:
            num = i
            if num > 3:
                x_point += fibonacci_numbers(i-4)
            my_dict[num] = x_point
    return(my_dict)
            


def count_y_reminder_2():  
    my_dict = {}
    x_point = 0
    for i in range(NUMBER, 0, -1):
        if i % 4 == 2:
            num = i
            x_point += fibonacci_numbers(i + 1)
            my_dict[num] = x_point
    return(my_dict)

c = count_x_reminder_2()
d = count_y_reminder_2()



def cordinates_reminder_2():
    x_rem_2 = []
    for key in c:
        x = ([key, c[key]])
        x_rem_2.append(x)
    ys = []
    for key in d:
        y = ([key, d[key]])
        ys.append(y)
    for i in x_rem_2:
        for k in ys:
            if i[0] == k[0]:
                i.append(k[1])
    return (x_rem_2)


#cordinates for all images with reminder 3
'''---------------------------------------------------------------------------------------------'''
def count_x_reminder_3():  
    my_dict = {}
    x_point = 0
    for i in range(NUMBER, 0, -1):
        
        if i%4 ==3:
            num = i
            x_point += fibonacci_numbers(i +1)
            my_dict[num] = x_point
    return (my_dict)


def count_y_reminder_3():  
    my_dict = {}
    x_point = 0
    my_dict[NUMBER- 1] = x_point
    for i in range(NUMBER, 0, -1):
        if i % 4 == 3 and i < NUMBER -1:
            x_point += fibonacci_numbers(i + 4)
            my_dict[i] = x_point
    return(my_dict)


e = count_x_reminder_3()
f = count_y_reminder_3()



def cordinates_reminder_3():
    x_rem_3 = []
    for key in e:
        x = ([key, e[key]])
        x_rem_3.append(x)
    ys = []
    for key in f:
        y = ([key, f[key]])
        ys.append(y)
    for i in x_rem_3:
        for k in ys:
            if i[0] == k[0]:
                i.append(k[1])
    return (x_rem_3)


#cordinates for all images with reminder 0
'''----------------------------------------------------------------------------'''
def count_x_reminder_0():  
    my_dict = {}
    x_point = 0
    my_dict[NUMBER] = x_point
    for i in range(NUMBER, 0, -1):
        if i % 4 == 0 and i < NUMBER:
            num = i
            x_point +=fibonacci_numbers(i + 4)
            my_dict[num] = x_point
    return(my_dict)


def count_y_reminder_0():  
    my_dict = {}
    x_point = 0
    my_dict[NUMBER] = x_point
    for i in range(NUMBER, 0, -1):
        if i % 4 == 0 and i < 10:
            x_point +=fibonacci_numbers(i + 3)
            my_dict[i] = x_point
    return(my_dict)




g = count_x_reminder_0()
h = count_y_reminder_0()


def cordinates_reminder_0():
    x_rem_0 = []
    for key in g:
        x = ([key, g[key]])
        x_rem_0.append(x)
    ys = []
    for key in h:
        y = ([key, h[key]])
        ys.append(y)
    for i in x_rem_0:
        for k in ys:
            if i[0] == k[0]:
                i.append(k[1])
    return (x_rem_0)

''' Maling list of all images with cordinates and making blank imagw'''
def main():
    cordinates = cordinates_reminder_0() + cordinates_reminder_1() + cordinates_reminder_2() + cordinates_reminder_3()
    blank_image = SimpleImage.blank(fibonacci_numbers(NUMBER) + fibonacci_numbers((NUMBER -1)), fibonacci_numbers(NUMBER))
    fib_images(cordinates, blank_image)
    


if __name__ == '__main__':
    main()

