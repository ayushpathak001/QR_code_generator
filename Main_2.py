import qrcode
import qrcode.constants 

from PIL import Image 
user_name = input("Enter the name of image ")
user = input("Enter something for create QR code : ")
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10 , border=4, )

qr.add_data(user)
qr.make(fit=True)
image = qr.make_image(fill_color = "green" , back_color = "white" )
image.save(user_name+".png")