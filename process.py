
from PIL import Image, ImageChops
from random import randint

# reward records the score from the history of moves
def reward(moves):
    n = len(moves)
    i = 0
    while moves[n-1-i] != 1:
        print(i,n)
        i += 1
        if i>= n-1: return sum(moves)
    else: return sum(moves) + i
    

if __name__ == '__main__':
    # deriving score from screen
    example = Image.open(".\\screenshots\\image25.png") # 836 x 470

    # os path this
    zero = Image.open(".\\digits\\0-crop.jpg") 
    one = Image.open(".\\digits\\1-crop.jpg") 
    two = Image.open(".\\digits\\2-crop.jpg") 
    three = Image.open(".\\digits\\3-crop.jpg") 
    four = Image.open(".\\digits\\4-crop.jpg") 
    five = Image.open(".\\digits\\5-crop.jpg") 
    six = Image.open(".\\digits\\6-crop.jpg") 
    seven = Image.open(".\\digits\\7-crop.jpg") 
    eight = Image.open(".\\digits\\8-crop.jpg") 
    nine = Image.open(".\\digits\\9-crop.jpg") 

    # dif = ImageChops.difference(two, example)
    # print(dif)

    # all digits have 42 pixel width 42 except 1 which has width 25
    print(example.width, example.height)
    start_width=7
    one_dig_loc = (7,start_width,7+25,start_width+42)
    dig_loc = (7,start_width,7+42,start_width+42)
    cropped = example.copy().crop(one_dig_loc)
    cropped.save(".\\screenshots\\croppped.png")


    # close opened images
    zero.close()
    one.close()
    two.close()
    three.close()
    four.close()
    five.close()
    six.close()
    seven.close()
    eight.close()
    nine.close()

    example.close()


