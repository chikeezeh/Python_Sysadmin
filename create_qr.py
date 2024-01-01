import qrcode
text = 'Chike Ezeh'
qr = qrcode.make(text)
qr.save('chike.jpg')