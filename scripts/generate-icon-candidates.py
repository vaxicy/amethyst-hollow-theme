"""Amethyst Hollow Theme - icon candidates.

Code-drawn marks, a light/dark contact sheet and an inline strip.

Run from the project root:  py -3 scripts/generate-icon-candidates.py
"""

import io
import math
import os

from PIL import Image, ImageDraw, ImageFont

S = 3
W = 1024

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "logo-candidates")

DEEP = (76, 35, 101, 255)         # #4C2365
MID = (127, 93, 153, 255)         # #7F5D99
SOFT = (158, 126, 181, 255)       # #9E7EB5
LIGHT = (196, 164, 218, 255)      # #C4A4DA
WHITE = (255, 255, 255, 255)

LIGHT_BG = (246, 242, 248, 255)
DARK_BG = (32, 20, 42, 255)
LIGHT_INK = (60, 40, 78, 255)
DARK_INK = (230, 216, 240, 255)

FONT_DIR = r"C:\Windows\Fonts"


def font(name, size):
    try:
        return ImageFont.truetype(os.path.join(FONT_DIR, name), size)
    except Exception:
        return ImageFont.load_default()


def scr(p):
    return (p[0] * S, p[1] * S)


def wd(v):
    return max(1, int(round(v * S)))


def canvas():
    return Image.new("RGBA", (W * S, W * S), (0, 0, 0, 0))


def finish(img):
    return img.resize((W, W), Image.LANCZOS)


def poly(draw, pts, fill):
    draw.polygon([scr(p) for p in pts], fill=fill)


def disc(draw, center, r, fill):
    draw.ellipse([center[0] * S - r * S, center[1] * S - r * S,
                  center[0] * S + r * S, center[1] * S + r * S], fill=fill)


def prism(draw, base_cx, base_y, top_cx, top_y, half_w, left, right):
    """Hexagonal crystal: two shaded faces plus a pointed cap."""
    shoulder_l = (base_cx - half_w, base_y - 70)
    shoulder_r = (base_cx + half_w, base_y - 70)
    tip = (top_cx, top_y)
    upper_l = (top_cx - half_w * 0.72, top_y + 120)
    upper_r = (top_cx + half_w * 0.72, top_y + 120)
    poly(draw, [(base_cx - half_w, base_y), shoulder_l, upper_l, tip,
                upper_r, shoulder_r, (base_cx + half_w, base_y)], left)
    poly(draw, [(top_cx, top_y), upper_r, shoulder_r, (base_cx + half_w, base_y),
                (base_cx + half_w * 0.1, base_y)], right)
    poly(draw, [upper_l, tip, (top_cx, top_y), (top_cx - half_w * 0.1, top_y + 120)],
         SOFT)


# ---------------------------------------------------------------- candidates

def cand_cluster():
    img = canvas()
    d = ImageDraw.Draw(img)

    prism(d, 330, 800, 286, 372, 96, MID, SOFT)
    prism(d, 690, 806, 736, 424, 88, SOFT, LIGHT)
    prism(d, 512, 828, 512, 246, 128, DEEP, MID)

    return finish(img)


def cand_geode():
    img = canvas()
    d = ImageDraw.Draw(img)

    disc(d, (512, 512), 330, DEEP)
    disc(d, (512, 512), 268, MID)

    # crystal shards inside the cavity
    for i in range(10):
        ang = 2 * math.pi * i / 10 - math.pi / 2
        r_out = 250
        cx = 512 + math.cos(ang) * r_out * 0.62
        cy = 512 + math.sin(ang) * r_out * 0.62
        half = 40
        tipx = 512 + math.cos(ang) * r_out
        tipy = 512 + math.sin(ang) * r_out
        nx, ny = -math.sin(ang) * half, math.cos(ang) * half
        poly(d, [(cx + nx, cy + ny), (tipx, tipy), (cx - nx, cy - ny)],
             LIGHT if i % 2 == 0 else SOFT)

    disc(d, (512, 512), 96, LIGHT)

    return finish(img)


def cand_hollow_arch():
    img = canvas()
    d = ImageDraw.Draw(img)

    # outer arch
    d.pieslice([scr((182, 236)), scr((842, 896))], 180, 360, fill=DEEP)
    d.rectangle([scr((182, 566)), scr((842, 896))], fill=DEEP)
    # cavity
    d.pieslice([scr((300, 366)), scr((724, 790))], 180, 360, fill=SOFT)
    d.rectangle([scr((300, 578)), scr((724, 790))], fill=SOFT)
    # glowing floor
    d.pieslice([scr((356, 500)), scr((668, 812))], 180, 360, fill=LIGHT)
    d.rectangle([scr((356, 656)), scr((668, 812))], fill=LIGHT)

    # steps
    for y, w in ((768, 238), (816, 300)):
        d.line([scr((512 - w, y)), scr((512 + w, y))], fill=DEEP, width=wd(18))

    return finish(img)


def cand_faceted_gem():
    img = canvas()
    d = ImageDraw.Draw(img)

    top = (512, 210)
    up_l = (330, 380)
    up_r = (694, 380)
    lo_l = (386, 812)
    lo_r = (638, 812)
    bottom = (512, 862)

    poly(d, [top, up_l, (512, 470)], DEEP)
    poly(d, [top, up_r, (512, 470)], MID)
    poly(d, [up_l, (512, 470), lo_l], SOFT)
    poly(d, [up_r, (512, 470), lo_r], LIGHT)
    poly(d, [up_l, lo_l, bottom, (512, 470)], SOFT)

    # outline
    d.line([scr(top), scr(up_r), scr(lo_r), scr(bottom), scr(lo_l), scr(up_l), scr(top)],
           fill=DEEP, width=wd(22), joint="curve")
    d.line([scr(up_l), scr((512, 470)), scr(up_r)], fill=DEEP, width=wd(20), joint="curve")
    d.line([scr((512, 470)), scr(bottom)], fill=DEEP, width=wd(20))

    return finish(img)


def cand_shards():
    img = canvas()
    d = ImageDraw.Draw(img)

    prism(d, 372, 812, 300, 470, 78, MID, SOFT)
    prism(d, 556, 826, 604, 330, 92, DEEP, MID)
    prism(d, 720, 812, 800, 528, 66, SOFT, LIGHT)

    return finish(img)


def cand_drop():
    img = canvas()
    d = ImageDraw.Draw(img)

    # teardrop body
    d.pieslice([scr((266, 372)), scr((758, 864))], 0, 360, fill=DEEP)
    poly(d, [(512, 190), (742, 660), (282, 660)], DEEP)
    d.pieslice([scr((286, 392)), scr((738, 844))], 0, 360, fill=DEEP)

    # inner light
    disc(d, (512, 610), 176, MID)
    disc(d, (512, 610), 106, SOFT)
    disc(d, (470, 566), 44, WHITE)

    return finish(img)


CANDIDATES = [
    ("01", "cluster", cand_cluster),
    ("02", "geode", cand_geode),
    ("03", "hollow-arch", cand_hollow_arch),
    ("04", "faceted-gem", cand_faceted_gem),
    ("05", "shards", cand_shards),
    ("06", "drop", cand_drop),
]


# ---------------------------------------------------------------- sheet bits

def centered_text(d, center, text, fnt, fill):
    b = d.textbbox((0, 0), text, font=fnt)
    x = center[0] - (b[2] - b[0]) / 2 - b[0]
    y = center[1] - (b[3] - b[1]) / 2 - b[1]
    d.text((x, y), text, font=fnt, fill=fill)


def contact_sheet(icons, bg, ink, path):
    cell_w, cell_h = 420, 540
    margin, gap = 40, 26
    head = 118
    sheet_w = margin * 2 + cell_w * 3 + gap * 2
    sheet_h = margin + head + cell_h * 2 + gap + margin

    sheet = Image.new("RGBA", (sheet_w, sheet_h), bg)
    d = ImageDraw.Draw(sheet)

    f_title = font("segoeuib.ttf", 40)
    f_num = font("segoeuib.ttf", 30)
    f_name = font("segoeui.ttf", 26)
    f_small = font("segoeui.ttf", 20)

    centered_text(d, (sheet_w / 2, margin + 34), "AMETHYST HOLLOW THEME", f_title, ink)
    centered_text(d, (sheet_w / 2, margin + 82), "icon candidates", f_small, ink)

    for idx, (num, name, icon) in enumerate(icons):
        row, col = divmod(idx, 3)
        gx = margin + col * (cell_w + gap)
        gy = margin + head + row * (cell_h + gap)

        sheet.alpha_composite(icon.resize((260, 260), Image.LANCZOS),
                              (gx + (cell_w - 260) // 2, gy + 30))

        centered_text(d, (gx + cell_w / 2, gy + 330), num, f_num, ink)
        centered_text(d, (gx + cell_w / 2, gy + 372), name, f_name, ink)
        centered_text(d, (gx + cell_w / 2, gy + 404), "1024 x 1024  PNG", f_small, ink)

        thumb = icon.resize((32, 32), Image.LANCZOS)
        tx, ty = gx + cell_w - 32 - 22, gy + cell_h - 32 - 22
        d.rectangle([tx - 10, ty - 10, tx + 42, ty + 42],
                    outline=(ink[0], ink[1], ink[2], 70), width=1)
        sheet.alpha_composite(thumb, (tx, ty))

    save_png(sheet.convert("RGB"), path)


def inline_strip(icons, path):
    size, gap, margin = 150, 18, 30
    strip_w = margin * 2 + size * len(icons) + gap * (len(icons) - 1)
    strip_h = margin * 2 + size + 34
    strip = Image.new("RGBA", (strip_w, strip_h), LIGHT_BG)
    d = ImageDraw.Draw(strip)
    f_num = font("segoeuib.ttf", 20)

    for idx, (num, _name, icon) in enumerate(icons):
        x = margin + idx * (size + gap)
        strip.alpha_composite(icon.resize((size, size), Image.LANCZOS), (x, margin))
        centered_text(d, (x + size / 2, margin + size + 16), num, f_num, LIGHT_INK)

    save_png(strip.convert("RGB"), path)


def save_png(img, path):
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(buf.getvalue())


def main():
    os.makedirs(OUT, exist_ok=True)

    icons = []
    for num, name, fn in CANDIDATES:
        icon = fn()
        box = icon.getbbox()
        if box is None:
            raise AssertionError("%s rendered empty" % name)
        left, top, right, bottom = box
        lo, hi = 70, 954
        if left < lo or top < lo or right > hi or bottom > hi:
            raise AssertionError("%s out of safe area: %s" % (name, box))
        path = os.path.join(OUT, "%s-%s.png" % (num, name))
        save_png(icon, path)
        print("wrote", os.path.relpath(path, ROOT), box)
        icons.append((num, name, icon))

    contact_sheet(icons, LIGHT_BG, LIGHT_INK, os.path.join(OUT, "contact-light.png"))
    contact_sheet(icons, DARK_BG, DARK_INK, os.path.join(OUT, "contact-dark.png"))
    inline_strip(icons, os.path.join(OUT, "inline-strip.png"))
    print("wrote contact-light.png / contact-dark.png / inline-strip.png")


if __name__ == "__main__":
    main()
