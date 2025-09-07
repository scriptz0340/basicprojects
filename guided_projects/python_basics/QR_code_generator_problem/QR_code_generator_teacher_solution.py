## Solution from course:
import qrcode 

data = input("Enter thet text or URL: ").strip()
filename = input("Enter the filename: ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)

print(f"QR code saved as {filename}.")



## Solution from course reflection:
#  Much more simple/clean than what i ended up with in my solution. This example also gets 
#  into the customization of the actual qr code image itself which is good to learn.
#  This version is better practice, but i think i learned some valuable things 
#  while troubleshooting my solution on my own. 