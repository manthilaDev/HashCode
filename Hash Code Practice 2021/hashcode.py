# @Manthila

# Number of Pizza
numOfPizza = 0
#Team Counts (Members)
memTwo = 0
memThree = 0 
memFour = 0

# Flags 
countersStatus = False

pizza_flavours =set ({}) # Accepts only unique vlaues 

def setCounters(modifiedLine):
    # setting global variables (Reading the first line)
    global numOfPizza 
    global memTwo
    global memThree 
    global memFour 
    global countersStatus
    numOfPizza = modifiedLine[0]
    memTwo = modifiedLine[1]
    memThree = modifiedLine[2]
    memFour = modifiedLine[3]
    countersStatus = True

def readDataSet():
    with open('a_example','r',encoding="UTF-8")as f:
        for line in f:
            modifiedLine=line.replace('\n','').strip()
            modifiedLine = modifiedLine.split(' ')
            if (countersStatus == False):
                setCounters(modifiedLine)
            else:
                modifiedLine.sort()
                flavour_tuple  = tuple(modifiedLine)
                pizza_flavours.add(flavour_tuple)
                #print(pizza_flavours)
                print(modifiedLine)
    print(pizza_flavours)

readDataSet()



#{('3', 'chicken', 'mushroom', 'pepper'), 
# #('2', 'basil', 'chicken'), 
# ('3', 'basil', 'mushroom', 'tomato'), 
# ('3', 'olive', 'onion', 'pepper')}