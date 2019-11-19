#print(randInt()) # should print a random integer between 0 to 100
import random
def randInt(min='', max=''):
    num = random.random() * 100
    return round(num)
randInt(min=0, max=100)


#print(randInt(max=50)) # should print a random integer between 0 to 50
import random
def randInt(min='', max=''):
    num = random.random() * 50
    return round(num)
randInt(min=0, max=50)

#print(randInt(min=50)) # should print a random integer between 50 to 100
import random
def randInt(min='', max=''):
    num = random.random() * 50 + 50
    return round(num)
randInt(min=50, max=500)


#print(randInt(min=50, max=500)) # should print a random integer between 50 and 500 + BONUS EDGE CASES (eg. min > max, or max < 0)
import random
def randInt(minimum='', maximum=''):
    if minimum > maximum:
        print("Please have min be less than max.")
    if maximum == 0:
        print("Please have max be greater than 0.")
    num = random.random() * 450 + 50
    return round(num)
randInt(minimum=50, maximum=0)
#Please have min be less than max.
#Please have max be greater than 0.