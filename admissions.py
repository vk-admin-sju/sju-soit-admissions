"""SJU SoIT Admissions 2026 - terminal edition."""
import sys
import time

import qrcode
from rich.align import Align
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

# ---- EDIT THESE ----------------------------------------------------------
APPLY_URL = "https://www.sju.edu.in/admissions"
BROCHURE_URL = "https://lnkd.in/p/gepwHKCe"
WEBSITE = "www.sju.edu.in"
LIGHT_QR_ON_DARK = True   # True: light QR on dark terminal. False: dark QR on white box (safest to scan)
# --------------------------------------------------------------------------

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

console = Console()


DARK = {"cornflower_blue": "navy_blue", "spring_green1": "dark_green"}


def qr_text(url, color):
    """Turn a URL into a compact coloured QR using half-block characters."""
    qr = qrcode.QRCode(border=2, error_correction=qrcode.constants.ERROR_CORRECT_M)
    qr.add_data(url)
    qr.make(fit=True)
    m = qr.get_matrix()
    if len(m) % 2:
        m.append([False] * len(m[0]))
    out = Text(no_wrap=True)
    style = color if LIGHT_QR_ON_DARK else f"{DARK[color]} on white"
    for y in range(0, len(m), 2):
        for x in range(len(m[0])):
            top, bot = m[y][x], m[y + 1][x]
            out.append("█" if top and bot else "▀" if top else "▄" if bot else " ", style=style)
        out.append("\n")
    return out


def qr_card(label, url, color):
    body = Group(Align.center(qr_text(url, color)), Align.center(Text(label, style=f"bold {color}")))
    return Panel(body, border_style="yellow", padding=(0, 1))


def type_out(text, style, delay=0.012):
    for ch in text:
        console.print(ch, style=style, end="")
        time.sleep(delay)
    console.print()


def main():
    console.clear()

    title = Text("SJU_SOIT_ADMISSIONS.2026", style="bold yellow", justify="center")

    heading = Text()
    heading.append("ST JOSEPH'S UNIVERSITY\n", style="bold white")
    heading.append("SCHOOL OF INFORMATION TECHNOLOGY\n", style="bold white")
    heading.append("BENGALURU", style="bold white")

    banner = Text()
    banner.append("ADMISSIONS OPEN\n", style="bold plum1")
    banner.append("Join the future of technology", style="yellow")

    card1 = qr_card("apply_now.sh", APPLY_URL, "cornflower_blue")
    card2 = qr_card("brochures.zip", BROCHURE_URL, "spring_green1")
    if console.width >= 90:
        qrs = Table.grid(padding=(0, 3))
        qrs.add_row(card1, card2)
    else:  # narrow window: stack them
        qrs = Group(Align.center(card1), Align.center(card2))

    links = Text()
    links.append("Apply    ", style="bold cornflower_blue")
    links.append(APPLY_URL + "\n", style="underline")
    links.append("Brochure ", style="bold spring_green1")
    links.append(BROCHURE_URL, style="underline")

    footer = Panel(Align.center(Text(WEBSITE, style="yellow")), border_style="yellow")

    body = Group(
        Align.center(title), Text(""),
        heading, Text(""),
        banner, Text(""),
        Align.center(qrs), Text(""),
        links, Text(""),
        footer,
    )
    console.print(Panel(body, border_style="light_sky_blue1", padding=(1, 2)))
    console.print("[dim]Scan with your phone camera, or copy the links above.[/dim]\n")


if __name__ == "__main__":
    main()
