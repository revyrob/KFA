"""
Builds the printable donation form PDF for the Kootenay Festival of the Arts.
Run: python3 build_donation_pdf.py
Output: ../public/downloads/donation-form.pdf
"""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

NAVY = (26 / 255, 26 / 255, 46 / 255)
RED = (232 / 255, 64 / 255, 64 / 255)
GREY = (0.3, 0.3, 0.35)
LIGHT_GREY = (0.55, 0.55, 0.6)

HERE = os.path.dirname(os.path.abspath(__file__))
BANNER = os.path.join(HERE, "..", "public", "images", "banner.png")
OUT = os.path.join(HERE, "..", "public", "downloads", "donation-form.pdf")

W, H = letter


def set_color(c, rgb):
    c.setFillColorRGB(*rgb)


def line_field(c, x, y, width, label, font="Helvetica", size=10):
    set_color(c, GREY)
    c.setFont(font, size)
    c.drawString(x, y, label)
    c.setLineWidth(0.75)
    set_color(c, LIGHT_GREY)
    c.line(x, y - 4, x + width, y - 4)


def checkbox(c, x, y, size=10):
    c.setLineWidth(1)
    set_color(c, NAVY)
    c.rect(x, y, size, size)


def build():
    c = canvas.Canvas(OUT, pagesize=letter)

    # --- Banner image ---
    img = ImageReader(BANNER)
    iw, ih = img.getSize()
    banner_w = W
    banner_h = banner_w * ih / iw
    max_banner_h = 1.05 * inch
    if banner_h > max_banner_h:
        banner_h = max_banner_h
        banner_w = banner_h * iw / ih
    c.drawImage(img, (W - banner_w) / 2, H - banner_h - 0.25 * inch,
                width=banner_w, height=banner_h, mask='auto')

    y = H - banner_h - 0.6 * inch

    # --- Title ---
    set_color(c, NAVY)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(W / 2, y, "Donation Form")
    y -= 16

    set_color(c, RED)
    c.setFont("Helvetica-Bold", 9.5)
    c.drawCentredString(W / 2, y, "KOOTENAY MUSIC FESTIVAL SOCIETY  ·  TRAIL, BC")
    y -= 22

    set_color(c, GREY)
    c.setFont("Helvetica-Oblique", 9)
    c.drawCentredString(W / 2, y, "Proud to be affiliated with Performing Arts BC")
    y -= 26

    # --- Intro paragraph ---
    intro = (
        "The Kootenay Music Festival Society is dedicated to providing opportunities for young "
        "performers to achieve excellence. To encourage participation, we work to keep entrance "
        "fees low, while striving to hire high-quality adjudicators. We wish to honour exceptional "
        "performances with a variety of awards. As we depend entirely on voluntary assistance and "
        "support, the society is asking you to consider a cash donation to the festival. Thank you!"
    )
    set_color(c, GREY)
    c.setFont("Helvetica", 10)
    text = c.beginText(0.85 * inch, y)
    text.setLeading(13.5)
    max_chars = 96
    import textwrap
    for line in textwrap.wrap(intro, max_chars):
        text.textLine(line)
    c.drawText(text)
    y -= 13.5 * 4 + 20

    left = 0.85 * inch
    right_col = W / 2 + 0.15 * inch
    field_w_full = W - left - 0.85 * inch

    # --- Donor info ---
    set_color(c, NAVY)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(left, y, "Donor Information")
    y -= 20
    line_field(c, left, y, field_w_full, "Name")
    y -= 28
    line_field(c, left, y, field_w_full, "Address")
    y -= 28
    line_field(c, left, y, 3.2 * inch, "City / Postal Code")
    line_field(c, left + 3.5 * inch, y, field_w_full - 3.5 * inch, "Telephone Number")
    y -= 38

    # --- Two-column: Cheque | E-transfer ---
    col_w = (field_w_full - 0.4 * inch) / 2
    col1_x = left
    col2_x = left + col_w + 0.4 * inch
    box_top = y
    box_h = 1.95 * inch

    set_color(c, (0.97, 0.965, 1.0))
    c.roundRect(col1_x, box_top - box_h, col_w, box_h, 6, fill=1, stroke=0)
    c.roundRect(col2_x, box_top - box_h, col_w, box_h, 6, fill=1, stroke=0)

    pad = 14
    # Cheque column
    ty = box_top - 20
    set_color(c, NAVY)
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(col1_x + pad, ty, "Donate by Cheque")
    ty -= 18
    line_field(c, col1_x + pad, ty, col_w - 2 * pad, "Amount enclosed ($)")
    ty -= 26
    set_color(c, GREY)
    c.setFont("Helvetica", 9)
    c.drawString(col1_x + pad, ty, "Payable to:")
    ty -= 13
    set_color(c, NAVY)
    c.setFont("Helvetica-Bold", 9.5)
    for line in ["Kootenay Music Festival Society", "Box 1724, 1889 Nevada St.", "Rossland, BC   V0G 1Y0"]:
        c.drawString(col1_x + pad, ty, line)
        ty -= 12.5

    # E-transfer column
    ty = box_top - 20
    set_color(c, NAVY)
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(col2_x + pad, ty, "Donate by E-transfer")
    ty -= 18
    set_color(c, GREY)
    c.setFont("Helvetica", 9)
    c.drawString(col2_x + pad, ty, "Send to:")
    ty -= 13
    set_color(c, RED)
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(col2_x + pad, ty, "treasurertrail@")
    ty -= 12.5
    c.drawString(col2_x + pad, ty, "kootenayfestivalofthearts.ca")
    ty -= 18
    set_color(c, GREY)
    c.setFont("Helvetica-Oblique", 8.5)
    text2 = c.beginText(col2_x + pad, ty)
    text2.setLeading(11.5)
    for line in textwrap.wrap(
        "Please add specific identifiable information to the e-transfer message so we can match your donation to this form.",
        int((col_w - 2 * pad) / 4.6)
    ):
        text2.textLine(line)
    c.drawText(text2)

    y = box_top - box_h - 28

    # --- Recognition / preferences ---
    set_color(c, NAVY)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(left, y, "Donation Preferences")
    y -= 10
    set_color(c, GREY)
    c.setFont("Helvetica", 8.5)
    c.drawString(left, y - 10, "Donors are identified to be thanked on the Kootenay Festival of the Arts website.")
    y -= 28

    c.setFont("Helvetica", 10)
    set_color(c, GREY)
    c.drawString(left, y, "I wish my donation to be anonymous:")
    checkbox(c, left + 2.55 * inch, y - 8, 10)
    c.drawString(left + 2.75 * inch, y, "Yes, please")
    checkbox(c, left + 4.05 * inch, y - 8, 10)
    c.drawString(left + 4.25 * inch, y, "No, thank you")
    y -= 30

    line_field(c, left, y, field_w_full, "I wish my donation to be applied to an award for")
    y -= 40

    # --- Thank you ---
    set_color(c, RED)
    c.setFont("Helvetica-BoldOblique", 12)
    c.drawCentredString(W / 2, y, "Thank you!")

    # --- Footer ---
    set_color(c, LIGHT_GREY)
    c.setFont("Helvetica", 7.5)
    c.drawCentredString(W / 2, 0.5 * inch,
                         "Kootenay Festival of the Arts  ·  kootenayfestivalofthearts.ca  ·  Box 1724, 1889 Nevada St., Rossland, BC  V0G 1Y0")

    c.showPage()
    c.save()
    print("Wrote", OUT)


if __name__ == "__main__":
    build()
