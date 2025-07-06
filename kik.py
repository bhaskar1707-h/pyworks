import qrcode

def generate_qr():
    # Get user input
    data = input("Enter text or URL to generate QR code: ").strip()

    if not data:
        print("❌ No input provided. Exiting.")
        return

    # Create QR code
    qr = qrcode.QRCode(
        version=1,  # controls size (1 = small, 40 = large)
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create and save the image
    img = qr.make_image(fill_color="black", back_color="white")
    filename = "qrcode.png"
    img.save(filename)

    print(f"✅ QR code saved as '{filename}'")

# Run the function
if __name__ == "__main__":
    generate_qr()
