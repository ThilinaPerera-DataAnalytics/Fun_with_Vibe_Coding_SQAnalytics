import os

import qrcode

from dotenv import load_dotenv
from PIL import Image, ImageDraw


# ---------------------------------------------------------
# Load environment variables
# ---------------------------------------------------------

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


# ---------------------------------------------------------
# Project paths
# ---------------------------------------------------------

BACKEND_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

LOGO_PATH = os.path.join(
    BACKEND_DIR,
    "icon",
    "SQA.png"
)

OUTPUT_FOLDER = os.path.join(
    BACKEND_DIR,
    "generated_qr"
)


# ---------------------------------------------------------
# QR generation function
# ---------------------------------------------------------

def generate_qr_image(
    short_code: str,
    logo_path: str | None = None
):

    if not BASE_URL:
        raise ValueError(
            "BASE_URL environment variable is not configured."
        )

    redirect_url = f"{BASE_URL}/r/{short_code}"

    # Create QR code with high error correction.
    # Level H allows approximately 30% error recovery,
    # making it suitable for a centered logo.

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(redirect_url)
    qr.make(fit=True)

    qr_image = qr.make_image(
        fill_color="black",
        back_color="white"
    ).convert("RGBA")

    # # -----------------------------------------------------
    # # Add optional centered logo
    # # -----------------------------------------------------

    # selected_logo_path = logo_path or LOGO_PATH

    # if os.path.exists(selected_logo_path):

    #     logo = Image.open(
    #         selected_logo_path
    #     ).convert("RGBA")

    #     qr_width, qr_height = qr_image.size

    #     # Keep logo conservative for reliable scanning.
    #     # Maximum logo width = 18% of QR width.

    #     max_logo_size = int(qr_width * 0.18)

    #     logo.thumbnail(
    #         (max_logo_size, max_logo_size),
    #         Image.Resampling.LANCZOS
    #     )

    #     logo_width, logo_height = logo.size

    #     # Add white safety padding around the logo.

    #     padding = max(
    #         4,
    #         int(qr_width * 0.005)
    #     )

    #     background_width = logo_width + (padding * 2)
    #     background_height = logo_height + (padding * 2)

    #     background = Image.new(
    #         "RGBA",
    #         (background_width, background_height),
    #         "white"
    #     )

    #     background.paste(
    #         logo,
    #         (padding, padding),
    #         logo
    #     )

    #     # Calculate centered position.

    #     position = (
    #         (qr_width - background_width) // 2,
    #         (qr_height - background_height) // 2
    #     )

    #     qr_image.paste(
    #         background,
    #         position,
    #         background
    #     )

    # -----------------------------------------------------
    # Add optional centered logo
    # -----------------------------------------------------

    selected_logo_path = logo_path or LOGO_PATH

    if os.path.exists(selected_logo_path):

        logo = Image.open(
            selected_logo_path
        ).convert("RGBA")

        qr_width, qr_height = qr_image.size

        # Keep logo conservative for reliable scanning.
        # Maximum logo width = 30% of QR width.

        max_logo_size = int(qr_width * 0.3)

        logo.thumbnail(
            (max_logo_size, max_logo_size),
            Image.Resampling.LANCZOS
        )

        logo_width, logo_height = logo.size

        # Add white safety padding around the logo.

        padding = max(
            4,
            int(qr_width * 0.005)
        )

        background_width = logo_width + (padding * 2)
        background_height = logo_height + (padding * 2)

        # Create circular background
        background = Image.new(
            "RGBA",
            (background_width, background_height),
            (255, 255, 255, 0)  # Fully transparent
        )

        # Create a circular mask
        mask = Image.new(
            "L",  # Grayscale mode
            (background_width, background_height),
            0
        )
        
        
        draw = ImageDraw.Draw(mask)
        draw.ellipse(
            (0, 0, background_width - 1, background_height - 1),
            fill=255
        )

        # Create white circle background
        circle_bg = Image.new(
            "RGBA",
            (background_width, background_height),
            "white"
        )
        
        # Apply circular mask to the white background
        background.paste(
            circle_bg,
            (0, 0),
            mask
        )

        # Paste logo onto the circular background
        background.paste(
            logo,
            (padding, padding),
            logo
        )

        # Calculate centered position.

        position = (
            (qr_width - background_width) // 2,
            (qr_height - background_height) // 2
        )

        qr_image.paste(
            background,
            position,
            background
        )

    # -----------------------------------------------------
    # Save generated QR
    # -----------------------------------------------------

    os.makedirs(
        OUTPUT_FOLDER,
        exist_ok=True
    )

    file_path = os.path.join(
        OUTPUT_FOLDER,
        f"{short_code}.png"
    )

    qr_image.convert("RGB").save(
        file_path,
        format="PNG"
    )

    return file_path