import pyqrcode
import png
link = "google.com"
qr_code = pyqrcode.create(link)
qr_code.png("gogole.png", scale=5)



