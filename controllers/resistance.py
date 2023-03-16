class resistence:
    band1 = ''
    band2 = ''
    band3 = ''
    band4 = ''
    total = 0
    minValue = 0
    maxValue = 0

    def __init__(self, band1, band2, band3, band4, total, minValue, maxValue):
        self.band1 = band1
        self.band2 = band2
        self.band3 = band3
        self.band4 = band4
        self.total = total
        self.minValue = minValue
        self.maxValue = maxValue


def calculateDataOfResistence(bands):
    number = '{}{}'.format(getColorBandOne(bands), getColorBandTwo(bands))
    total = int(number) * getColorBandThree(bands)
    minValue = total - \
        (total * float(getColorBandFour(bands) / 100))
    maxValue = total + \
        (total * float(getColorBandFour(bands) / 100))

    data = resistence(bands.band1.data, bands.band2.data,
                      bands.band3.data, bands.band4.data, total, minValue, maxValue)
    return data


def getColorBandOne(bands):
    if (bands.band1.data == 'Negro'):
        return '0'
    if (bands.band1.data == 'Cafe'):
        return '1'
    if (bands.band1.data == 'Rojo'):
        return '2'
    if (bands.band1.data == 'Naranja'):
        return '3'
    if (bands.band1.data == 'Amarillo'):
        return '4'
    if (bands.band1.data == 'Verde'):
        return '5'
    if (bands.band1.data == 'Azul'):
        return '6'
    if (bands.band1.data == 'Violeta'):
        return '7'
    if (bands.band1.data == 'Gris'):
        return '8'
    if (bands.band1.data == 'Blanco'):
        return '9'


def getColorBandTwo(bands):
    if (bands.band2.data == 'Negro'):
        return '0'
    if (bands.band2.data == 'Cafe'):
        return '1'
    if (bands.band2.data == 'Rojo'):
        return '2'
    if (bands.band2.data == 'Naranja'):
        return '3'
    if (bands.band2.data == 'Amarillo'):
        return '4'
    if (bands.band2.data == 'Verde'):
        return '5'
    if (bands.band2.data == 'Azul'):
        return '6'
    if (bands.band2.data == 'Violeta'):
        return '7'
    if (bands.band2.data == 'Gris'):
        return '8'
    if (bands.band2.data == 'Blanco'):
        return '9'


def getColorBandThree(bands):
    if (bands.band3.data == 'Negro'):
        return 1
    if (bands.band3.data == 'Café'):
        return 10
    if (bands.band3.data == 'Rojo'):
        return 100
    if (bands.band3.data == 'Naranja'):
        return 1000
    if (bands.band3.data == 'Amarillo'):
        return 10000
    if (bands.band3.data == 'Verde'):
        return 100000
    if (bands.band3.data == 'Azul'):
        return 1000000
    if (bands.band3.data == 'Violeta'):
        return 10000000
    if (bands.band3.data == 'Gris'):
        return 100000000
    if (bands.band3.data == 'Blanco'):
        return 1000000000


def getColorBandFour(bands):
    if (bands.band4.data == 'Rojo'):
        return 2
    if (bands.band4.data == 'Dorado'):
        return 5
    if (bands.band4.data == 'Plata'):
        return 10
