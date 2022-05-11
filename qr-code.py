# a programm thats aks me for a url and then generates a qr code for it
import qrcode

link = input("Enter a link to be converted to a QR code: ")

qr = qrcode.QRCode(
version=1,
error_correction=qrcode.constants.ERROR_CORRECT_L,
box_size=10,
border=4,
)
qr.add_data(link)
qr.make(fit=True)
img = qr.make_image(fill_color="white", back_color=0xFF0000)
bild = img.save("qr-code.png")

bild.show()