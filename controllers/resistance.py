class resistence:
    total = 0
    minValue = 0
    maxValue = 0

    def __init__(self, total, minValue, maxValue):
        self.total = total
        self.minValue = minValue
        self.maxValue = maxValue


def calculateDataOfResistence(bands):
    number = bands.band1.data + bands.band2.data
    total = int(number) * int(bands.band3.data)
    minValue = total - (total * float(int(bands.band4.data) / 100))
    maxValue = total + (total * float(int(bands.band4.data) / 100))

    data = resistence(total, minValue, maxValue)
    return data


def getColorBandOne(bands):
    if (bands.band1.data == '0'):
        return ['Negro', 'black', 'white']
    if (bands.band1.data == '1'):
        return ['Cafe', 'brown', 'white']
    if (bands.band1.data == '2'):
        return ['Rojo', 'red', 'black']
    if (bands.band1.data == '3'):
        return ['Naranja', 'orange', 'black']
    if (bands.band1.data == '4'):
        return ['Amarillo', 'yellow', 'black']
    if (bands.band1.data == '5'):
        return ['Verde', 'green', 'white']
    if (bands.band1.data == '6'):
        return ['Azul', 'blue', 'white']
    if (bands.band1.data == '7'):
        return ['Violeta', 'violet', 'white']
    if (bands.band1.data == '8'):
        return ['Gris', 'gray', 'black']
    if (bands.band1.data == '1'):
        return ['Blanco', 'white', 'black']


def getColorBandTwo(bands):
    if (bands.band2.data == '0'):
        return ['Negro', 'black', 'white']
    if (bands.band2.data == '1'):
        return ['Cafe', 'brown', 'white']
    if (bands.band2.data == '2'):
        return ['Rojo', 'red', 'black']
    if (bands.band2.data == '3'):
        return ['Naranja', 'orange', 'black']
    if (bands.band2.data == '4'):
        return ['Amarillo', 'yellow', 'black']
    if (bands.band2.data == '5'):
        return ['Verde', 'green', 'white']
    if (bands.band2.data == '6'):
        return ['Azul', 'blue', 'white']
    if (bands.band2.data == '7'):
        return ['Violeta', 'violet', 'white']
    if (bands.band2.data == '8'):
        return ['Gris', 'gray', 'black']
    if (bands.band2.data == '1'):
        return ['Blanco', 'white', 'black']


def getColorBandThree(bands):
    if (bands.band3.data == '1'):
        return ['Negro', 'black', 'white']
    if (bands.band3.data == '10'):
        return ['Cafe', 'brown', 'white']
    if (bands.band3.data == '100'):
        return ['Rojo', 'red', 'black']
    if (bands.band3.data == '1000'):
        return ['Naranja', 'orange', 'black']
    if (bands.band3.data == '10000'):
        return ['Amarillo', 'yellow', 'black']
    if (bands.band3.data == '100000'):
        return ['Verde', 'green', 'white']
    if (bands.band3.data == '1000000'):
        return ['Azul', 'blue', 'white']
    if (bands.band3.data == '10000000'):
        return ['Violeta', 'violet', 'white']
    if (bands.band3.data == '100000000'):
        return ['Gris', 'gray', 'black']
    if (bands.band3.data == '1000000000'):
        return ['Blanco', 'white', 'black']


def getColorBandFour(bands):
    if (bands.band4.data == '2'):
        return ['Rojo', 'red', 'black']
    if (bands.band4.data == '5'):
        return ['Dorado', 'Gold', 'black']
    if (bands.band4.data == '10'):
        return ['Plata', 'Silver', 'black']
