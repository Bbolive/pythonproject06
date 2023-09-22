def inputX( ):
    x = float(input('ป้อนค่า x : '))
    return x

def calY( x ) :
    y = (2*(x**2)) + (2*x) + 1
    return y

def showY( y ) :
    print(f'สมการ : {y:.2f}')

x = inputX()
showY( calY( x ))