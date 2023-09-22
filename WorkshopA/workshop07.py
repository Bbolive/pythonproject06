def inputData( ):
    number = int(input('ป้อนตัวเลขที่ต้องการทาย : '))
    return number

def cal( number ):
    if number ==  25 :
        result = 'Correct, You are the winner'
    else:
       result = 'Not Correct!!!!!!'
    return result

def show ( result ) :
    print(f'{result}')

number = inputData( )
show(cal( number ))