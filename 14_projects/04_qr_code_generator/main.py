import qrcode

link = input("Enter the link or text to encode in the QR code: ")
filename = input("Enter the filename to save the QR code without extension: ").lower()

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill_color= "black" , back_color= "white")
img.save(f"{filename}.png")

print(f"QR code saved as {filename}.png")