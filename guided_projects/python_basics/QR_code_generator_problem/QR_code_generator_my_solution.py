## My solution (first try):
import qrcode

url = input("Enter URL: ")

img = qrcode.make(url)

file_name = f"{url}.png"

img.save(file_name)



## I was able to do everything except for one thing:
#  I kept getting a file not found error if i used a full URL to a website 
#  (ex: https://facebook.com), but if i entered a random string of text it would work
#  and save the image to a .png file with the value of the 'Url' variable as the file name.
#  Also, created a virtual environment to install the qrcode and pillow libraries.



## My solution after doing some research:
import qrcode 
import re

def generate_qr_code(url): # accepts a url to generate the qr code image
    qr_code = qrcode.make(url)
    return qr_code # returns the qr_code object
def clean_url(url): # accepts a url and cleans it 
    # 1. Remove the protocol (http:// or https://)
    step1 = re.sub(r'https?://', '', url)

    # 2. Replace slashes and colons with underscores
    step2 = step1.replace('/', '_').replace(':', '_')

    # 3. Remove any domain extension at the end (e.g., .com, .co.uk)
    # The regex `\.[a-z]{2,}(?=_|$)` finds a period followed by 2 or more letters,
    # then removes it if it's followed by an underscore or the end of the string.
    cleaned_url = re.sub(r'\.[a-z]{2,}(?=_|$)', '', step2, flags=re.IGNORECASE)

    return cleaned_url # returns a cleaned url

def main():
    url = input("Enter URL: ")
    img = generate_qr_code(url) # qr_code object is stored to the 'img' variable.
    sanitized_url = clean_url(url) # cleaned_url object is stored in 'clean_url' variable.
    filename = f"{sanitized_url}.png" # 'cleaned_url.png' is stored in the 'filename' variable.
    img.save(filename) # qr_code object is saved with the cleaned_url value as filename.
    print(f"QR code saved as {filename}.") # confirmation message


main()


## After research reflection:
#  The problem was that i was trying to save a file to my computer that included certain
#  special characters in the file name that aren't allowed on my OS. The fix was to 
#  sanitize the user input to either remove or replace special characters with
#  acceptable ones. I decided to also get rid of the domain name extentions as well
#  even though it wasn't required. To do this i imported the 're' module and 
#  used a couple ready made regular expression patterns. 
#  (Im not super experienced with regex, yet, but i do plan to learn it)