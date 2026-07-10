import os
import qrcode
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BASE_URL = os.getenv("BASE_URL")


def generate_qr_image(short_code: str):

    redirect_url = f"{BASE_URL}/r/{short_code}"

    img = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    img.add_data(redirect_url)
    img.make(fit=True)

    image = img.make_image(fill_color="black", back_color="white")

    output_folder = "generated_qr"

    os.makedirs(output_folder, exist_ok=True)

    file_path = os.path.join(
        output_folder,
        f"{short_code}.png"
    )

    image.save(file_path)

    return file_path