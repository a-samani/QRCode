from math import e
import qrcode

name = input('Enter your full name : \t')
phone = input('Enter your phone Number : \t')
address = input('Enter your address : \t')
postalcode = input('Enter your postal-code : \t')

data = {'name': name , 'phone':phone, 'address' : address 
    , 'postalcode': postalcode}

QRGenerator = qrcode.QRCode(error_correction=qrcode.ERROR_CORRECT_H)

QRGenerator.add_data(data)
QRGenerator.make_image().save('QRcode.jpg')
