# QR Code Generator Learning Project

This is a simple Python script that generates a QR code image from a user-provided URL. The project documents my learning process and improvements made while solving issues related to file naming and URL sanitization.

You will find 2 files. One contains my first attempt and second attempt after doing research and the other contains the solution from the course I am following. Both versions are well commented to show my thought process and document my learning process. I am a beginner programmer and new to github as well.

---

## Features

- Generates a QR code from any URL input.
- Cleans the URL string to create a safe filename by removing protocols (`http://`, `https://`), replacing special characters, and stripping domain extensions.
- Saves the QR code as a PNG image with the sanitized URL as the filename.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/scriptz0340/mypythonprojects/basics/qr-code-generator.git
   cd qr-code-generator
2. (Optional) Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies:
   pip install qrcode pillow
4. Run the script:
   python3 qr_code_generator.py
   
   (Note) you will have to comment out one section of the code because the file contains 2 programs. I included my first attempt as well as my second after doing some research. The code is well commented so it wont be hard to tell what to comment out.

5. Enter a URL when prompted.

6. The QR code will be saved as a .png file in the current directory with a sanitized 
   filename.

---

## NOTES

- Filenames are sanitized to avoid issues with special characters that are invalid in file names.

- Domain extensions (like .com, .co.uk) are removed for simplicity.

- Regex is used for URL cleaning — I'm still learning regex, so this is a work in progress!


---

### Input / Output Examples

| User Input                  | Output Message                  | Filename Saved        |
|-----------------------------|--------------------------------|-----------------------|
| `https://facebook.com`       | `QR code saved as facebook.png.` | `facebook.png`        |
| `http://example.co.uk/path` | `QR code saved as example_path.png.` | `example_path.png`    |
| `some/random:url`            | `QR code saved as some_random_url.png.` | `some_random_url.png` |
| `mywebsite.org`              | `QR code saved as mywebsite.png.` | `mywebsite.png`       |

---


