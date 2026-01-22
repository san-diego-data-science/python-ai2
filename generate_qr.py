import qrcode
img = qrcode.make('https://pythonai2.sandiegodata.science')
img.save('qrcode.png')
