import random

def hawkID():
    return "lldeng"

class Box:
    def __init__(self, centerX = 0.0, centerY = 0.0, centerZ = 0.0, width = 1.0, height = 1.0, depth = 1.0):
        self.centerX = centerX
        self.centerY = centerY
        self.centerZ = centerZ
        self.width = width
        self.height = height
        self.depth = depth
        
    def setCenter(self, x, y, z):
        self.centerX = x
        self.centerY = y
        self.centerZ = z
        
    def setWidth(self, width):
        self.width = width
        
    def setHeight(self, height):
        self.height = height
        
    def setDepth(self, depth):
        self.depth = depth
        
    def volume(self):
        return self.width * self.height * self.depth
    
    def surfaceArea(self):
        return 2 * ((self.width * self.height) + (self.width * self.depth) + (self.height * self.depth))
    
    def touches(self, otherBox):
        distanceBetweenCentersX = abs(self.centerX - otherBox.centerX)
        distanceBetweenCentersY = abs(self.centerY - otherBox.centerY)
        distanceBetweenCentersZ = abs(self.centerZ - otherBox.centerZ)
        combinedWidth = (self.width + otherBox.width) / 2
        combinedHeight = (self.height + otherBox.height) / 2
        combinedDepth = (self.depth + otherBox.depth) / 2
        if combinedWidth >= distanceBetweenCentersX and combinedHeight >= distanceBetweenCentersY and combinedDepth >= distanceBetweenCentersZ:
            return True
        else:
            return False
        
    def contains(self, otherBox):
        selfXUpper = self.centerX + (self.width / 2)
        selfXLower = self.centerX - (self.width / 2)
        selfYUpper = self.centerY + (self.height / 2)
        selfYLower = self.centerY - (self.height / 2)
        selfZUpper = self.centerZ + (self.depth / 2)
        selfZLower = self.centerZ - (self.depth / 2)
        otherXUpper = otherBox.centerX + (otherBox.width / 2)
        otherXLower = otherBox.centerX - (otherBox.width / 2)
        otherYUpper = otherBox.centerY + (otherBox.height / 2)
        otherYLower = otherBox.centerY - (otherBox.height / 2)
        otherZUpper = otherBox.centerZ + (otherBox.depth / 2)
        otherZLower = otherBox.centerZ - (otherBox.depth / 2)
        if otherXUpper < selfXUpper and otherXLower > selfXLower and otherYUpper < selfYUpper and otherYLower > selfYLower and otherZUpper < selfZUpper and otherZLower > selfZLower:
            return True
        else:
            return False
        
    def __repr__(self):
        return "< box with width {} height {} and depth {} centered at ({},{},{}) >".format(self.width, self.height, self.depth, self.centerX, self.centerY, self.centerZ)
    
class NimGame:
    def __init__(self, heapList = []):
        self.heapList = heapList
        
    def __repr__(self):
        segment1 = "< Nim game with {} heaps.\n".format(len(self.heapList))
        segment2 = ""
        for i in range(len(self.heapList)):
            segment2 = segment2 + "Heap {}: {} balls\n".format(i, self.heapList[i])
        segment3 = ">"
        fullString = segment1 + segment2 + segment3
        return fullString
    
    def gameOver(self):
        for heap in self.heapList:
            if heap != 0:
                return False
        return True
    
    def remove(self, heap, amount):
        if heap >= len(self.heapList):
            print("Heap [] does not exist.".format(heap))
        elif amount > self.heapList[heap]:
            print("You can't take that many balls from heap {}. Try again.".format(heap))
        else:
            self.heapList[heap] = self.heapList[heap] - amount
            print("You took {} balls from heap {}.".format(amount, heap))
            if self.gameOver():
                print("You win!")
            else:
                selectedHeap = 0
                while self.heapList[selectedHeap] == 0:
                    selectedHeap = selectedHeap + 1
                selectedAmount = random.randint(1, self.heapList[selectedHeap])
                self.heapList[selectedHeap] = self.heapList[selectedHeap] - selectedAmount
                print("Computer took {} balls from heap {}.".format(selectedAmount, selectedHeap))
                if self.gameOver():
                    print("Computer wins!")

class Animal ():
    
    numAnimals = 0

    def __init__ (self, name = 'NoName', numLegs = 0):
        self.name = name
        self.numLegs = numLegs
        Animal.numAnimals = Animal.numAnimals + 1
        self.id = Animal.numAnimals

    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def getNumLegs(self):
        return self.numLegs
   
    def speak(self):
        print("...")

    def __repr__(self):
        return ('<{} the animal. ID:{}>'.format(self.name, self.id))

class Cat(Animal):
    def __init__(self, name = 'noname', furColor = 'unknown'):
        Animal.__init__(self, name, 4)
        self.color = furColor
    
    def speak(self):
        print('meow')

    def getFurColor(self):
        return self.color

    def __repr__(self):
        return ('<{} the {} cat. ID: {}>'.format(self.name, self.color, self.id))

class Dog(Animal):
    
    def __init__(self, name = 'rover'):
        Animal.__init__(self, name, 4)
    
    def speak(self):
        print('woof')
        
    def fetch(self):
        print("I'm fetching ...")

    def __repr__(self):
        return '<{} the dog. ID:{}>'.format(self.name, self.id)

class Bird(Animal):
    def __init__(self, name = "Polly"):
        Animal.__init__(self, name, 2)

    def speak(self):
        print("caw")

    def fly(self):
        print("I'm flying around...")

    def __repr__(self):
        return("<{} the bird. ID:{}>".format(self.name, self.id))
        
def testAnimal():
    c1 = Cat("Milo")
    c2 = Cat(furColor = "black")
    d1 = Dog()
    d2 = Dog()
    b1 = Bird()
    b2 = Bird("Tweety")
    for animal in [c1, c2, d1, d2, b1, b2]:
        print(animal)
        animal.speak()
    d1.fetch()
    print(c2.getFurColor())
    b1.fly()
