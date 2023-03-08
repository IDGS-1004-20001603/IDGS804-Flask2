class ColorsBand:
    band1 = ''
    band2 = ''
    band3 = ''
    band4 = ''

    def __init__(self, band1, band2, band3, band4):
        self.band1 = band1
        self.band2 = band2
        self.band3 = band3
        self.band4 = band4


def writeColors(textToAdd):
    colors = '{},{},{},{}'.format(
        textToAdd.band1.data, textToAdd.band2.data, textToAdd.band3.data, textToAdd.band4.data)
    fileColors = open('colorsToResistance.txt', 'a')
    fileColors.write(',' + colors)
    fileColors.close()


def readColors():
    arrayResistances = []
    arrayStart = 0
    arrayEnd = 4
    indexOfNumberResistances = 0

    fileColors = open('colorsToResistance.txt', 'r')
    arrayNumbers = fileColors.read().split(',')
    numberOfResistance = int(arrayNumbers.__len__() / 4)

    while indexOfNumberResistances < numberOfResistance:
        getColorBands = arrayNumbers[arrayStart: arrayEnd]
        arrayResistances.append(ColorsBand(
            getColorBands[0], getColorBands[1], getColorBands[2], getColorBands[3]))
        indexOfNumberResistances = indexOfNumberResistances + 1
        arrayStart = arrayStart + 4
        arrayEnd = arrayEnd + 4

    return arrayResistances


def sendColorsToApp():
    arrayResistance = readColors()

    for index in range(len(arrayResistance)):
        band1 = getColorByNumber(arrayResistance[index].band1)
        band2 = getColorByNumber(arrayResistance[index].band2)
        band3 = getMultiplierByNumber(arrayResistance[index].band3)
        band4 = getToleranceByNumber(arrayResistance[index].band4)
        valuesOfResistance = getDataForResistance(arrayResistance[index])
        arrayResistance[index].band1 = band1
        arrayResistance[index].band2 = band2
        arrayResistance[index].band3 = band3
        arrayResistance[index].band4 = band4
        arrayResistance[index].total = valuesOfResistance[0]
        arrayResistance[index].minValue = valuesOfResistance[1]
        arrayResistance[index].maxValue = valuesOfResistance[2]
    
    return arrayResistance


def getColorByNumber(number):
    setColor = ''
    colors = ['Negro', 'Café', 'Rojo', 'Naranja', 'Amarillo',
              'Verde', 'Azul', 'Violeta', 'Gris', 'Blanco']

    for index in range(len(colors)):
        if (int(number) == index):
            setColor = colors[index]
            break

    return setColor


def getToleranceByNumber(number):
    setTolerance = ''
    numbers = {'2': 'Rojo', '5': 'Dorado', '10': 'Plata'}

    for key in numbers.keys():
        if (number == key):
            setTolerance = numbers[key]
            break

    return setTolerance


def getMultiplierByNumber(number):
    setMultiplier = ''
    numbersOfMultiplier = {'1': 'Negro', '10': 'Café', '100': 'Rojo',
                           '1000': 'Naranja', '10000': 'Amarillo', '100000': 'Verde', '1000000': 'Azul', '10000000': 'Violeta', '100000000': 'Gris', '100000000': 'Blanco'}
    
    for key in numbersOfMultiplier.keys():
        if(number == key):
            setMultiplier = numbersOfMultiplier[key]
            break
    
    return setMultiplier

def getDataForResistance(arrayOfNumbers):
    number = '{}{}'.format(arrayOfNumbers.band1, arrayOfNumbers.band2)
    total = int(number) *  int(arrayOfNumbers.band3)
    minValue = total - (total * float(int(arrayOfNumbers.band4) / 100))
    maxValue = total + (total * float(int(arrayOfNumbers.band4) / 100))

    return [total, minValue, maxValue]
