import qrcode


qr_image = qrcode.make('http://127.0.0.1:8000')
qr_image.save('qr_image.png')