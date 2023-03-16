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
        band1 = get_number_by_color(arrayResistance[index].band1)
        band2 = get_number_by_color(arrayResistance[index].band2)
        band3 = get_multiplier_by_color(arrayResistance[index].band3)
        band4 = get_tolerance_by_color(arrayResistance[index].band4)
        valuesOfResistance = getDataForResistance(band1, band2, band3, band4)
        arrayResistance[index].total = valuesOfResistance[0]
        arrayResistance[index].minValue = valuesOfResistance[1]
        arrayResistance[index].maxValue = valuesOfResistance[2]

    return arrayResistance


def get_number_by_color(color):
    setNumber = 0
    colors = ['Negro', 'Cafe', 'Rojo', 'Naranja', 'Amarillo',
              'Verde', 'Azul', 'Violeta', 'Gris', 'Blanco']

    for index in range(len(colors)):
        if (color == colors[index]):
            setNumber = index
            break

    return setNumber


def get_tolerance_by_color(color):
    setTolerance = ''
    data_tolerances = {'Rojo': 2, 'Dorado': 5, 'Plata': 10}

    for key in data_tolerances.keys():
        if (color == key):
            setTolerance = data_tolerances[key]
            break

    return setTolerance


def get_multiplier_by_color(color):
    setMultiplier = ''
    data_multiplier = {'Negro': 1, 'Café': 10, 'Rojo': 100,
                           'Naranja': 1000, 'Amarillo': 10000, 'Verde': 100000, 'Azul': 1000000, 'Violeta': 10000000, 'Gris': 100000000, 'Blanco': 1000000000}

    for key in data_multiplier.keys():
        if (color == key):
            setMultiplier = data_multiplier[key]
            break

    return setMultiplier


def getDataForResistance(band1, band2, band3, band4):
    number = '{}{}'.format(band1, band2)
    total = int(number) * band3
    minValue = total - (total * float(band4 / 100))
    maxValue = total + (total * float(band4 / 100))

    return [total, minValue, maxValue]
