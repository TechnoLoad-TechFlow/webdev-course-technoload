import os
import sys
import time
import subprocess
from PIL import Image, ImageDraw, ImageFont

# Dimensions
WIDTH = 1920
HEIGHT = 1080

# Fonts
FONT_TITLE = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 46)
FONT_SUBTITLE = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 28)
FONT_HEADING = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 36)
FONT_BODY = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 24)
FONT_BODY_BOLD = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 24)
FONT_SMALL = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 20)
FONT_CODE = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 22)
FONT_CODE_BOLD = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 22)
FONT_TELE_TITLE = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 22)
FONT_TELE_CUE = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 19)
FONT_TIMER = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 22)

# Colors
BG_COLOR = (15, 23, 42)        # Slate 900
CARD_BG = (30, 41, 59)         # Slate 800
CARD_BORDER = (51, 65, 85)     # Slate 700
TEXT_WHITE = (248, 250, 252)   # Slate 50
TEXT_MUTED = (148, 163, 184)   # Slate 400
ACCENT_BLUE = (59, 130, 246)   # Blue 500
ACCENT_CYAN = (56, 189, 248)   # Cyan 400
ACCENT_GREEN = (16, 185, 129)  # Emerald 500
ACCENT_AMBER = (245, 158, 11)  # Amber 500
ACCENT_ORANGE = (249, 115, 22) # Orange 500
ACCENT_ROSE = (244, 63, 94)    # Rose 500
LOWER_BG = (10, 15, 30)        # Dark lower third

OUTPUT_DIR = "video-production"
CLIPS_DIR = os.path.join(OUTPUT_DIR, "clips")
os.makedirs(CLIPS_DIR, exist_ok=True)

def draw_play_icon(draw, x, y, size=14, color=(255, 255, 255)):
    draw.polygon([(x, y), (x, y + size), (x + size * 0.9, y + size / 2)], fill=color)

def draw_header(draw, category, title):
    # Top header banner
    draw.rectangle([0, 0, WIDTH, 75], fill=(15, 23, 42))
    draw.line([0, 75, WIDTH, 75], fill=(30, 41, 59), width=2)
    # Category badge
    draw.rounded_rectangle([60, 18, 420, 56], radius=6, fill=(30, 41, 59), outline=(56, 189, 248), width=1)
    draw.text((75, 24), category.upper(), font=FONT_SMALL, fill=ACCENT_CYAN)
    # Title
    draw.text((450, 20), title, font=FONT_HEADING, fill=TEXT_WHITE)

def draw_lower_third(draw, section_time, section_title, teleprompter_cue, elapsed_str, total_str, progress_pct):
    # Lower third background
    draw.rectangle([0, 955, WIDTH, HEIGHT], fill=LOWER_BG)
    # Top progress bar track
    draw.rectangle([0, 955, WIDTH, 963], fill=(30, 41, 59))
    # Filled progress bar
    fill_w = int(WIDTH * progress_pct)
    if fill_w > 0:
        draw.rectangle([0, 955, fill_w, 963], fill=ACCENT_CYAN)
    
    # Section pill
    draw.rounded_rectangle([50, 975, 480, 1010], radius=6, fill=(30, 41, 59), outline=CARD_BORDER, width=1)
    draw.text((65, 980), f"{section_time} - {section_title}".upper(), font=FONT_TELE_TITLE, fill=ACCENT_CYAN)
    
    # Timer
    timer_text = f"TIEMPO: {elapsed_str} / {total_str}"
    draw.text((WIDTH - 280, 980), timer_text, font=FONT_TIMER, fill=TEXT_MUTED)
    
    # Teleprompter cue line
    draw.text((50, 1025), "NARRACION: " + teleprompter_cue, font=FONT_TELE_CUE, fill=(226, 232, 240))

def create_scene_1(elapsed_str="00:25", progress_pct=0.08):
    """Scene 1: Introduction and Hook [00:00 - 00:50]"""
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    draw_header(draw, "Curso de Desarrollo Web", "Lección 1: ¿Qué es el desarrollo web?")
    
    # Main hero card
    draw.rounded_rectangle([120, 130, 1800, 900], radius=20, fill=CARD_BG, outline=CARD_BORDER, width=2)
    
    # Glowing accent line
    draw.rounded_rectangle([120, 130, 1800, 140], radius=4, fill=ACCENT_BLUE)
    
    # Hero Title
    draw.text((180, 180), "Fundamentos de Desarrollo Web", font=FONT_HEADING, fill=ACCENT_CYAN)
    draw.text((180, 240), "¿Qué es realmente un sitio web?", font=FONT_TITLE, fill=TEXT_WHITE)
    draw.text((180, 310), "Aprende cómo funcionan las páginas de internet y crea tu primer proyecto desde cero", font=FONT_SUBTITLE, fill=TEXT_MUTED)
    
    # Three feature cards
    cards = [
        ("100% En Línea", "Sin descargas ni programas pesados.\nSolo necesitas tu navegador favorito:\nChrome, Edge, Firefox o Safari.", ACCENT_CYAN),
        ("HTML + CSS", "Aprende los dos pilares esenciales:\nHTML crea la estructura y el texto.\nCSS diseña los colores y estilos.", ACCENT_AMBER),
        ("Para Principiantes", "Explicaciones visuales paso a paso,\nsin jerga técnica complicada.\nIdeal para estudiantes de secundaria.", ACCENT_GREEN)
    ]
    
    cx = 180
    for title, desc, col in cards:
        draw.rounded_rectangle([cx, 400, cx + 460, 680], radius=16, fill=(20, 28, 45), outline=col, width=2)
        draw.text((cx + 30, 430), title, font=FONT_HEADING, fill=col)
        draw.line([cx + 30, 485, cx + 430, 485], fill=(40, 50, 75), width=2)
        
        lines = desc.split("\n")
        y = 510
        for l in lines:
            draw.text((cx + 30, y), l, font=FONT_BODY, fill=TEXT_WHITE)
            y += 40
        cx += 520
        
    # Callout banner at bottom of card
    draw.rounded_rectangle([180, 720, 1740, 840], radius=12, fill=(15, 23, 42), outline=(56, 189, 248), width=1)
    draw.text((220, 745), "CONSEJO CLAVE:", font=FONT_BODY_BOLD, fill=ACCENT_AMBER)
    draw.text((220, 785), "Cada página que visitas (YouTube, Wikipedia, TikTok) está hecha de archivos de texto que tu navegador traduce al instante.", font=FONT_BODY, fill=TEXT_WHITE)
    
    draw_lower_third(draw, "00:00 - 00:50", "Introducción y Gancho",
                     '"¡Hola y bienvenido a tu primer paso en el desarrollo web! Hoy descubrirás qué hay detrás de tus páginas favoritas..."',
                     elapsed_str, "05:10", progress_pct)
    return img

def create_scene_2(elapsed_str="01:25", progress_pct=0.28):
    """Scene 2: Architecture & House Analogy [00:50 - 02:05]"""
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    draw_header(draw, "Conceptos Fundamentales", "¿Cómo funciona la web? La analogía de la casa")
    
    # Top explanation card: The browser as translator
    draw.rounded_rectangle([100, 110, 1820, 280], radius=16, fill=CARD_BG, outline=CARD_BORDER, width=2)
    draw.text((140, 135), "El Navegador Web como Traductor", font=FONT_HEADING, fill=ACCENT_CYAN)
    draw.text((140, 185), "Cuando entras a una página web, el navegador (Chrome, Edge, Firefox, Safari) recibe archivos de texto plano.", font=FONT_BODY, fill=TEXT_WHITE)
    draw.text((140, 225), "Su trabajo es interpretar dos lenguajes esenciales para dibujar la página final:", font=FONT_BODY, fill=TEXT_MUTED)
    
    # Two comparative pillars (The House Analogy)
    # Left: HTML
    draw.rounded_rectangle([100, 310, 940, 910], radius=16, fill=CARD_BG, outline=ACCENT_AMBER, width=2)
    draw.rounded_rectangle([100, 310, 940, 390], radius=16, fill=(45, 30, 15))
    draw.text((140, 335), "HTML (HyperText Markup Language)", font=FONT_HEADING, fill=ACCENT_AMBER)
    draw.text((140, 410), "ESTRUCTURA: Los Cimientos y Muros de la Casa", font=FONT_BODY_BOLD, fill=TEXT_WHITE)
    
    html_items = [
        "- Decide QUE elementos existen en la página web.",
        "- Los cimientos, muros, columnas, puertas y ventanas.",
        "- Define: Títulos (<h1>), párrafos (<p>), imágenes y enlaces.",
        "- Es el esqueleto: sin HTML no hay contenido.",
        "- Todo el contenido legible vive dentro de etiquetas HTML."
    ]
    y = 470
    for item in html_items:
        draw.text((140, y), item, font=FONT_BODY, fill=TEXT_WHITE)
        y += 45
    
    # Code snippet preview box inside HTML card
    draw.rounded_rectangle([140, 710, 900, 870], radius=10, fill=(15, 23, 42), outline=(60, 45, 20), width=1)
    draw.text((160, 730), "<!-- Ejemplo de estructura en HTML -->", font=FONT_CODE, fill=(100, 116, 139))
    draw.text((160, 770), "<h1>Mi Casa Digital</h1>", font=FONT_CODE_BOLD, fill=ACCENT_CYAN)
    draw.text((160, 810), "<p>Este es el contenido principal.</p>", font=FONT_CODE, fill=TEXT_WHITE)
    
    # Right: CSS
    draw.rounded_rectangle([980, 310, 1820, 910], radius=16, fill=CARD_BG, outline=ACCENT_CYAN, width=2)
    draw.rounded_rectangle([980, 310, 1820, 390], radius=16, fill=(15, 35, 55))
    draw.text((1020, 335), "CSS (Cascading Style Sheets)", font=FONT_HEADING, fill=ACCENT_CYAN)
    draw.text((1020, 410), "DISENO: La Pintura, Colores y Decoración", font=FONT_BODY_BOLD, fill=TEXT_WHITE)
    
    css_items = [
        "- Decide COMO se ve cada elemento en la pantalla.",
        "- El color de la pintura en las paredes y el estilo visual.",
        "- Define: Colores (color), fuentes (font-family) y tamaños.",
        "- Bordes redondeados, sombras, márgenes y alineación.",
        "- Sin CSS, cualquier sitio se vería en blanco y negro."
    ]
    y = 470
    for item in css_items:
        draw.text((1020, y), item, font=FONT_BODY, fill=TEXT_WHITE)
        y += 45
        
    # Code snippet preview box inside CSS card
    draw.rounded_rectangle([1020, 710, 1780, 870], radius=10, fill=(15, 23, 42), outline=(20, 45, 65), width=1)
    draw.text((1040, 730), "/* Ejemplo de diseño con CSS */", font=FONT_CODE, fill=(100, 116, 139))
    draw.text((1040, 770), "h1 { color: #2563eb; font-size: 32px; }", font=FONT_CODE_BOLD, fill=ACCENT_AMBER)
    draw.text((1040, 810), "body { background-color: #f0f9ff; }", font=FONT_CODE, fill=TEXT_WHITE)
    
    draw_lower_third(draw, "00:50 - 02:05", "La Analogía de la Casa (HTML vs. CSS)",
                     '"HTML son los ladrillos y paredes (el contenido); CSS es la pintura y los muebles (el diseño visual)..."',
                     elapsed_str, "05:10", progress_pct)
    return img

def create_scene_3(highlight="all", elapsed_str="02:40", progress_pct=0.52):
    """Scene 3: Tour of JSFiddle Interface [02:05 - 03:20]"""
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    draw_header(draw, "Herramienta en Línea", "JSFiddle: Tu laboratorio de código sin descargas")
    
    # JSFiddle Container Frame
    draw.rounded_rectangle([80, 100, 1840, 920], radius=14, fill=(24, 32, 47), outline=CARD_BORDER, width=2)
    
    # Top navbar of JSFiddle
    draw.rectangle([80, 100, 1840, 160], fill=(15, 23, 42))
    draw.text((110, 118), "JSFiddle", font=FONT_HEADING, fill=TEXT_WHITE)
    
    # Run button (prominent)
    run_col = (16, 185, 129) if highlight in ["all", "run", "result"] else (30, 41, 59)
    draw.rounded_rectangle([270, 112, 400, 148], radius=6, fill=run_col, outline=(52, 211, 153), width=2)
    draw_play_icon(draw, 290, 123, 14, (255, 255, 255))
    draw.text((315, 118), "Run", font=FONT_BODY_BOLD, fill=TEXT_WHITE)
    
    # Other mockup buttons
    draw.rounded_rectangle([420, 112, 510, 148], radius=6, fill=(30, 41, 59))
    draw.text((440, 120), "Save", font=FONT_BODY, fill=TEXT_MUTED)
    draw.rounded_rectangle([530, 112, 640, 148], radius=6, fill=(30, 41, 59))
    draw.text((545, 120), "Settings", font=FONT_BODY, fill=TEXT_MUTED)
    
    draw.text((1400, 120), "jsfiddle.net - 100% Gratis y sin registro", font=FONT_SMALL, fill=ACCENT_CYAN)
    
    # 4 Panels calculation
    x1, y1 = 100, 180
    w_half = 810
    h_half = 340
    
    # Panel 1: HTML (Top Left)
    border_html = ACCENT_AMBER if highlight in ["all", "html"] else (51, 65, 85)
    draw.rounded_rectangle([x1, y1, x1 + w_half, y1 + h_half], radius=10, fill=(15, 23, 42), outline=border_html, width=2)
    draw.rectangle([x1, y1, x1 + w_half, y1 + 45], fill=(30, 41, 59))
    draw.text((x1 + 15, y1 + 10), "HTML (Estructura y Texto)", font=FONT_BODY_BOLD, fill=ACCENT_AMBER)
    # Mock code
    draw.text((x1 + 25, y1 + 70), "<h1>¡Hola, mundo web!</h1>", font=FONT_CODE_BOLD, fill=ACCENT_CYAN)
    draw.text((x1 + 25, y1 + 115), "<p>Esta es mi primera página en JSFiddle.</p>", font=FONT_CODE, fill=TEXT_WHITE)
    
    # Panel 2: CSS (Bottom Left)
    y2 = y1 + h_half + 20
    border_css = ACCENT_CYAN if highlight in ["all", "css"] else (51, 65, 85)
    draw.rounded_rectangle([x1, y2, x1 + w_half, y2 + h_half], radius=10, fill=(15, 23, 42), outline=border_css, width=2)
    draw.rectangle([x1, y2, x1 + w_half, y2 + 45], fill=(30, 41, 59))
    draw.text((x1 + 15, y2 + 10), "CSS (Diseño y Colores)", font=FONT_BODY_BOLD, fill=ACCENT_CYAN)
    # Mock code
    draw.text((x1 + 25, y2 + 70), "h1 {", font=FONT_CODE_BOLD, fill=ACCENT_AMBER)
    draw.text((x1 + 55, y2 + 110), "color: #2563eb;", font=FONT_CODE, fill=ACCENT_CYAN)
    draw.text((x1 + 55, y2 + 150), "font-family: Arial, sans-serif;", font=FONT_CODE, fill=TEXT_WHITE)
    draw.text((x1 + 25, y2 + 190), "}", font=FONT_CODE_BOLD, fill=ACCENT_AMBER)
    
    # Panel 3: JS (Top Right - Muted)
    xr = x1 + w_half + 30
    draw.rounded_rectangle([xr, y1, xr + w_half, y1 + h_half], radius=10, fill=(15, 23, 42), outline=(51, 65, 85), width=1)
    draw.rectangle([xr, y1, xr + w_half, y1 + 45], fill=(25, 32, 45))
    draw.text((xr + 15, y1 + 10), "JavaScript (Avanzado - No lo usaremos en este curso)", font=FONT_BODY, fill=TEXT_MUTED)
    draw.text((xr + 25, y1 + 80), "// Este panel queda vacío por ahora", font=FONT_CODE, fill=(80, 95, 120))
    draw.text((xr + 25, y1 + 120), "// Nos enfocamos al 100% en HTML y CSS", font=FONT_CODE, fill=(80, 95, 120))
    
    # Panel 4: Result (Bottom Right)
    border_res = ACCENT_GREEN if highlight in ["all", "result"] else (51, 65, 85)
    draw.rounded_rectangle([xr, y2, xr + w_half, y2 + h_half], radius=10, fill=(255, 255, 255), outline=border_res, width=3)
    # Browser window header
    draw.rectangle([xr, y2, xr + w_half, y2 + 45], fill=(241, 245, 249))
    draw.text((xr + 15, y2 + 10), "Result (Tu Página Web en Vivo)", font=FONT_BODY_BOLD, fill=(15, 23, 42))
    # Rendered web content inside result
    font_h1_res = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 34)
    font_p_res = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 22)
    draw.text((xr + 40, y2 + 80), "¡Hola, mundo web!", font=font_h1_res, fill=(37, 99, 235))
    draw.text((xr + 40, y2 + 150), "Esta es mi primera página en JSFiddle.", font=font_p_res, fill=(51, 65, 85))
    
    draw_lower_third(draw, "02:05 - 03:20", "Recorrido Guiado por JSFiddle",
                     '"JSFiddle divide la pantalla en 4 paneles: HTML arriba, CSS abajo, y Result a la derecha donde cobra vida tu web..."',
                     elapsed_str, "05:10", progress_pct)
    return img

def create_scene_4_frame(step_name="init", html_text="¡Hola, mundo web!", css_val="#2563eb;",
                         res_color=(37, 99, 235), cursor_pos=None, run_clicked=False,
                         elapsed_str="03:45", progress_pct=0.72):
    """Scene 4: Live interactive typing in JSFiddle [03:20 - 04:20]"""
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    draw_header(draw, "Demostración Práctica", "Modificando HTML y CSS en tiempo real")
    
    # Outer frame
    draw.rounded_rectangle([80, 95, 1840, 925], radius=14, fill=(24, 32, 47), outline=CARD_BORDER, width=2)
    
    # Navbar
    draw.rectangle([80, 95, 1840, 155], fill=(15, 23, 42))
    draw.text((110, 112), "JSFiddle", font=FONT_HEADING, fill=TEXT_WHITE)
    
    # Run button
    btn_bg = (5, 150, 105) if run_clicked else (16, 185, 129)
    btn_outline = (110, 231, 183) if run_clicked else (52, 211, 153)
    draw.rounded_rectangle([270, 107, 400, 143], radius=6, fill=btn_bg, outline=btn_outline, width=2)
    draw_play_icon(draw, 290, 118, 14, (255, 255, 255))
    draw.text((315, 113), "Run", font=FONT_BODY_BOLD, fill=TEXT_WHITE)
    
    # Step indicator pill in navbar
    draw.rounded_rectangle([430, 107, 1050, 143], radius=6, fill=(30, 41, 59))
    draw.text((450, 114), f"PASO ACTUAL: {step_name}", font=FONT_BODY_BOLD, fill=ACCENT_CYAN)
    
    # Panels
    x1, y1 = 100, 175
    w_half = 810
    h_half = 345
    
    # Panel 1: HTML
    draw.rounded_rectangle([x1, y1, x1 + w_half, y1 + h_half], radius=10, fill=(15, 23, 42), outline=ACCENT_AMBER, width=2)
    draw.rectangle([x1, y1, x1 + w_half, y1 + 45], fill=(30, 41, 59))
    draw.text((x1 + 15, y1 + 10), "Panel HTML", font=FONT_BODY_BOLD, fill=ACCENT_AMBER)
    # Active HTML text
    draw.text((x1 + 25, y1 + 70), "<h1>", font=FONT_CODE_BOLD, fill=ACCENT_CYAN)
    draw.text((x1 + 85, y1 + 70), html_text, font=FONT_CODE_BOLD, fill=TEXT_WHITE)
    t_w = int(draw.textlength(html_text, font=FONT_CODE_BOLD))
    draw.text((x1 + 85 + t_w, y1 + 70), "</h1>", font=FONT_CODE_BOLD, fill=ACCENT_CYAN)
    draw.text((x1 + 25, y1 + 120), "<p>Esta es mi primera página en JSFiddle.</p>", font=FONT_CODE, fill=TEXT_MUTED)
    
    # Panel 2: CSS
    y2 = y1 + h_half + 20
    draw.rounded_rectangle([x1, y2, x1 + w_half, y2 + h_half], radius=10, fill=(15, 23, 42), outline=ACCENT_CYAN, width=2)
    draw.rectangle([x1, y2, x1 + w_half, y2 + 45], fill=(30, 41, 59))
    draw.text((x1 + 15, y2 + 10), "Panel CSS", font=FONT_BODY_BOLD, fill=ACCENT_CYAN)
    # Active CSS text
    draw.text((x1 + 25, y2 + 70), "h1 {", font=FONT_CODE_BOLD, fill=ACCENT_AMBER)
    draw.text((x1 + 55, y2 + 115), "color: ", font=FONT_CODE, fill=ACCENT_CYAN)
    draw.text((x1 + 145, y2 + 115), css_val, font=FONT_CODE_BOLD, fill=ACCENT_AMBER if css_val=="#2563eb;" else ACCENT_ORANGE)
    draw.text((x1 + 55, y2 + 160), "font-family: Arial, sans-serif;", font=FONT_CODE, fill=TEXT_MUTED)
    draw.text((x1 + 25, y2 + 205), "}", font=FONT_CODE_BOLD, fill=ACCENT_AMBER)
    
    # Panel 3: JS (Muted)
    xr = x1 + w_half + 30
    draw.rounded_rectangle([xr, y1, xr + w_half, y1 + h_half], radius=10, fill=(15, 23, 42), outline=(51, 65, 85), width=1)
    draw.rectangle([xr, y1, xr + w_half, y1 + 45], fill=(25, 32, 45))
    draw.text((xr + 15, y1 + 10), "JavaScript (No usado)", font=FONT_BODY, fill=TEXT_MUTED)
    
    # Panel 4: Result
    draw.rounded_rectangle([xr, y2, xr + w_half, y2 + h_half], radius=10, fill=(255, 255, 255), outline=ACCENT_GREEN, width=3)
    draw.rectangle([xr, y2, xr + w_half, y2 + 45], fill=(241, 245, 249))
    draw.text((xr + 15, y2 + 10), "Result (Vista Previa en Vivo)", font=FONT_BODY_BOLD, fill=(15, 23, 42))
    
    font_h1_res = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 34)
    font_p_res = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 22)
    draw.text((xr + 40, y2 + 80), html_text, font=font_h1_res, fill=res_color)
    draw.text((xr + 40, y2 + 150), "Esta es mi primera página en JSFiddle.", font=font_p_res, fill=(51, 65, 85))
    
    # Draw simulated mouse pointer if pos given
    if cursor_pos:
        cx, cy = cursor_pos
        # Cursor arrow
        draw.polygon([(cx, cy), (cx + 18, cy + 18), (cx + 10, cy + 22), (cx + 16, cy + 34),
                      (cx + 10, cy + 36), (cx + 5, cy + 24), (cx, cy + 26)], fill=(255, 255, 255), outline=(0, 0, 0))
    
    draw_lower_third(draw, "03:20 - 04:20", "Demostración Práctica en Vivo",
                     '"Cambiamos el texto en HTML, luego cambiamos el color a darkorange en CSS y presionamos Run..."',
                     elapsed_str, "05:10", progress_pct)
    return img

def create_scene_5(elapsed_str="04:35", progress_pct=0.88):
    """Scene 5: Interactive practice pause [04:20 - 04:55]"""
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    draw_header(draw, "Actividad Práctica", "¡Pausa el video y experimenta en tu JSFiddle!")
    
    # Main challenge card
    draw.rounded_rectangle([140, 120, 1780, 910], radius=20, fill=CARD_BG, outline=ACCENT_AMBER, width=3)
    
    # Big Pause Banner
    draw.rounded_rectangle([180, 160, 1740, 260], radius=14, fill=(45, 30, 15), outline=ACCENT_AMBER, width=2)
    draw.text((220, 185), "PAUSA EL VIDEO: Tómate 1 minuto para practicar en tu navegador", font=FONT_TITLE, fill=ACCENT_AMBER)
    
    # 4 Steps to follow
    steps = [
        ("Paso 1", "Haz clic en el enlace de JSFiddle que dejamos en la descripción de este video.", ACCENT_CYAN),
        ("Paso 2", "En el panel HTML, cambia el texto del <h1> por tu nombre o tu frase favorita.", ACCENT_AMBER),
        ("Paso 3", "En el panel CSS, prueba cambiar el color por: crimson, navy, teal o purple.", ACCENT_GREEN),
        ("Paso 4", "Presiona el botón azul Run y mira cómo tu página web se transforma al instante.", ACCENT_ORANGE)
    ]
    
    y = 295
    for tag, desc, col in steps:
        draw.rounded_rectangle([180, y, 1740, y + 105], radius=12, fill=(20, 28, 45), outline=CARD_BORDER, width=1)
        # Tag badge
        draw.rounded_rectangle([210, y + 25, 330, y + 80], radius=8, fill=col)
        draw.text((230, y + 36), tag, font=FONT_HEADING, fill=(15, 23, 42))
        draw.text((360, y + 36), desc, font=FONT_BODY_BOLD, fill=TEXT_WHITE)
        y += 125
        
    # Motivational note
    draw.rounded_rectangle([180, 810, 1740, 880], radius=10, fill=(15, 23, 42), outline=ACCENT_CYAN, width=1)
    draw.text((220, 830), "NOTA: ¡No tengas miedo de experimentar! Si algo se rompe, solo recarga la página y vuelve a empezar.", font=FONT_BODY, fill=ACCENT_CYAN)
    
    draw_lower_third(draw, "04:20 - 04:55", "Pausa para la Práctica Interactiva",
                     '"Pausa el video durante 1 minuto, entra al enlace de JSFiddle, modifica tu título y color, y dale play..."',
                     elapsed_str, "05:10", progress_pct)
    return img

def create_scene_6(elapsed_str="05:05", progress_pct=0.98):
    """Scene 6: Summary and Next Steps [04:55 - 05:10]"""
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    draw_header(draw, "Resumen de la Lección", "¡Felicidades por completar la Lección 1!")
    
    draw.rounded_rectangle([140, 120, 1780, 910], radius=20, fill=CARD_BG, outline=ACCENT_GREEN, width=3)
    
    # Congratulation banner
    draw.text((200, 170), "¡Excelente trabajo! Has dado tu primer gran paso", font=FONT_TITLE, fill=TEXT_WHITE)
    draw.text((200, 235), "Ya comprendes los conceptos que fundamentan todo el desarrollo web moderno:", font=FONT_SUBTITLE, fill=TEXT_MUTED)
    
    # 3 Summary check cards
    checks = [
        ("[OK] HTML = Estructura y Contenido", "Es el esqueleto y los ladrillos: decide qué títulos, textos y elementos existen."),
        ("[OK] CSS = Diseño y Apariencia", "Es la decoración y pintura: elige los colores, tipos de letra, tamaños y estilos."),
        ("[OK] JSFiddle = Tu Entorno en la Nube", "Editor 100% gratuito y sin registro para crear, experimentar y compartir.")
    ]
    
    y = 310
    for title, desc in checks:
        draw.rounded_rectangle([200, y, 1720, y + 110], radius=12, fill=(20, 28, 45), outline=(52, 211, 153), width=1)
        draw.text((240, y + 20), title, font=FONT_HEADING, fill=ACCENT_GREEN)
        draw.text((240, y + 65), desc, font=FONT_BODY, fill=TEXT_WHITE)
        y += 135
        
    # Next Lesson Banner
    draw.rounded_rectangle([200, 740, 1720, 870], radius=14, fill=(15, 35, 55), outline=ACCENT_CYAN, width=2)
    draw.text((240, 765), "PROXIMA LECCION (Lección 2 de 10):", font=FONT_BODY_BOLD, fill=ACCENT_AMBER)
    draw.text((240, 805), "Tu primera página HTML: etiquetas, apertura, cierre y jerarquía de títulos", font=FONT_HEADING, fill=TEXT_WHITE)
    
    draw_lower_third(draw, "04:55 - 05:10", "Resumen y Próxima Lección",
                     '"En la Lección 2 aprenderemos qué significan las etiquetas, cómo se abren y cierran y la jerarquía de títulos..."',
                     elapsed_str, "05:10", progress_pct)
    return img


def render_clip_from_image(img, duration_sec, output_path):
    temp_png = output_path + ".temp.png"
    img.save(temp_png)
    
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1",
        "-i", temp_png,
        "-t", str(duration_sec),
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-tune", "stillimage",
        "-pix_fmt", "yuv420p",
        "-r", "30",
        output_path
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if os.path.exists(temp_png):
        os.remove(temp_png)

def generate_scene_4_clip(output_path):
    """Generates the animated 60-second interactive demonstration clip (Scene 4)"""
    # 4 sub-parts in Scene 4 totaling 60 seconds:
    # 4.1: Initial State & First Run Click (12s)
    # 4.2: Edit HTML text to "¡Bienvenidos a mi espacio digital!" & Run Click (20s)
    # 4.3: Edit CSS color to "darkorange;" & Run Click (18s)
    # 4.4: Final Result Showcase (10s)
    # Total = 12 + 20 + 18 + 10 = 60s
    
    sub_clips = []
    
    # 4.1 Initial State (12s)
    img_41 = create_scene_4_frame(
        step_name="1. Código inicial y clic en Run",
        html_text="¡Hola, mundo web!",
        css_val="#2563eb;",
        res_color=(37, 99, 235),
        cursor_pos=(335, 125),
        run_clicked=True,
        elapsed_str="03:30",
        progress_pct=0.68
    )
    p_41 = os.path.join(CLIPS_DIR, "sc4_1.mp4")
    render_clip_from_image(img_41, 12, p_41)
    sub_clips.append(p_41)
    
    # 4.2 Edit HTML (20s)
    img_42 = create_scene_4_frame(
        step_name="2. Modificando el texto en el panel HTML",
        html_text="¡Bienvenidos a mi espacio digital!",
        css_val="#2563eb;",
        res_color=(37, 99, 235),
        cursor_pos=(335, 125),
        run_clicked=True,
        elapsed_str="03:45",
        progress_pct=0.73
    )
    p_42 = os.path.join(CLIPS_DIR, "sc4_2.mp4")
    render_clip_from_image(img_42, 20, p_42)
    sub_clips.append(p_42)
    
    # 4.3 Edit CSS color to darkorange (18s)
    img_43 = create_scene_4_frame(
        step_name="3. Cambiando color a 'darkorange' en CSS",
        html_text="¡Bienvenidos a mi espacio digital!",
        css_val="darkorange;",
        res_color=(234, 88, 12),
        cursor_pos=(335, 125),
        run_clicked=True,
        elapsed_str="04:05",
        progress_pct=0.79
    )
    p_43 = os.path.join(CLIPS_DIR, "sc4_3.mp4")
    render_clip_from_image(img_43, 18, p_43)
    sub_clips.append(p_43)
    
    # 4.4 Result Showcase (10s)
    img_44 = create_scene_4_frame(
        step_name="4. ¡Cambio en tiempo real completado con éxito!",
        html_text="¡Bienvenidos a mi espacio digital!",
        css_val="darkorange;",
        res_color=(234, 88, 12),
        cursor_pos=None,
        run_clicked=False,
        elapsed_str="04:15",
        progress_pct=0.82
    )
    p_44 = os.path.join(CLIPS_DIR, "sc4_4.mp4")
    render_clip_from_image(img_44, 10, p_44)
    sub_clips.append(p_44)
    
    # Concat subclips
    list_txt = os.path.join(CLIPS_DIR, "sc4_list.txt")
    with open(list_txt, "w") as f:
        for sc in sub_clips:
            f.write(f"file '{os.path.basename(sc)}'\n")
            
    cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", list_txt,
        "-c", "copy",
        output_path
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    print("=== Generador de Video Base para Lección 1 (5:10 min) ===")
    t_start = time.time()
    
    # 1. Scene 1 [00:00 - 00:50] -> 50 seconds
    print("Generando Escena 1 (50s)...")
    sc1_path = os.path.join(CLIPS_DIR, "scene_1.mp4")
    render_clip_from_image(create_scene_1("00:25", 0.08), 50, sc1_path)
    
    # 2. Scene 2 [00:50 - 02:05] -> 75 seconds
    print("Generando Escena 2 (75s)...")
    sc2_path = os.path.join(CLIPS_DIR, "scene_2.mp4")
    render_clip_from_image(create_scene_2("01:25", 0.28), 75, sc2_path)
    
    # 3. Scene 3 [02:05 - 03:20] -> 75 seconds (25s HTML/CSS, 25s Result, 25s overview)
    print("Generando Escena 3 (75s)...")
    sc3a_path = os.path.join(CLIPS_DIR, "scene_3a.mp4")
    render_clip_from_image(create_scene_3("html", "02:25", 0.46), 25, sc3a_path)
    sc3b_path = os.path.join(CLIPS_DIR, "scene_3b.mp4")
    render_clip_from_image(create_scene_3("result", "02:50", 0.54), 25, sc3b_path)
    sc3c_path = os.path.join(CLIPS_DIR, "scene_3c.mp4")
    render_clip_from_image(create_scene_3("all", "03:10", 0.61), 25, sc3c_path)
    
    sc3_path = os.path.join(CLIPS_DIR, "scene_3.mp4")
    sc3_list = os.path.join(CLIPS_DIR, "sc3_list.txt")
    with open(sc3_list, "w") as f:
        f.write(f"file '{os.path.basename(sc3a_path)}'\n")
        f.write(f"file '{os.path.basename(sc3b_path)}'\n")
        f.write(f"file '{os.path.basename(sc3c_path)}'\n")
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", sc3_list, "-c", "copy", sc3_path],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # 4. Scene 4 [03:20 - 04:20] -> 60 seconds
    print("Generando Escena 4 (60s)...")
    sc4_path = os.path.join(CLIPS_DIR, "scene_4.mp4")
    generate_scene_4_clip(sc4_path)
    
    # 5. Scene 5 [04:20 - 04:55] -> 35 seconds
    print("Generando Escena 5 (35s)...")
    sc5_path = os.path.join(CLIPS_DIR, "scene_5.mp4")
    render_clip_from_image(create_scene_5("04:35", 0.88), 35, sc5_path)
    
    # 6. Scene 6 [04:55 - 05:10] -> 15 seconds
    print("Generando Escena 6 (15s)...")
    sc6_path = os.path.join(CLIPS_DIR, "scene_6.mp4")
    render_clip_from_image(create_scene_6("05:05", 0.98), 15, sc6_path)
    
    # Master concat with silent audio track
    print("Concatenando video final completo con pista de audio compatible...")
    master_list = os.path.join(CLIPS_DIR, "master_list.txt")
    with open(master_list, "w") as f:
        f.write(f"file '{os.path.basename(sc1_path)}'\n")
        f.write(f"file '{os.path.basename(sc2_path)}'\n")
        f.write(f"file '{os.path.basename(sc3_path)}'\n")
        f.write(f"file '{os.path.basename(sc4_path)}'\n")
        f.write(f"file '{os.path.basename(sc5_path)}'\n")
        f.write(f"file '{os.path.basename(sc6_path)}'\n")
        
    final_output = os.path.join(OUTPUT_DIR, "leccion-01-ejecucion-5min.mp4")
    
    cmd_master = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", master_list,
        "-f", "lavfi",
        "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
        "-c:v", "copy",
        "-c:a", "aac",
        "-shortest",
        final_output
    ]
    subprocess.run(cmd_master, check=True)
    
    dur_sec = 50 + 75 + 75 + 60 + 35 + 15
    print(f"\n✅ Video generado exitosamente en: {final_output}")
    print(f"⏱️ Duración total: {dur_sec} segundos ({dur_sec//60}:{dur_sec%60:02d} min)")
    print(f"⚡ Tiempo de generación: {time.time() - t_start:.2f} segundos")

if __name__ == "__main__":
    main()
