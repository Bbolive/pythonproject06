def inputData( ):
    name = input('ป้อนชื่อสินค้า : ')
    cost = int(input('ป้อนราคาสินค้า : '))
    return name, cost

def calVat( cost ) :
    vat = cost * 0.07
    return vat

def showVat( vat ) :
    print(f'ภาษี : {vat:.2f} บาท')

name, cost = inputData()
showVat( calVat( cost ))