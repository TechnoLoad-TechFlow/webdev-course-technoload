import os
import sys
import time
import subprocess
from PIL import Image, ImageDraw, ImageFont

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
FONT_CODE_LARGE = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 32)
FONT_TELE_TITLE = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 22)
FONT_TELE_CUE = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 19)
FONT_TIMER = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 22)

# Colors
BG_COLOR = (15, 23, 42)
CARD_BG = (30, 41, 59)
CARD_BORDER = (51, 65, 85)
TEXT_WHITE = (248, 250, 252)
TEXT_MUTED = (148, 163, 184)
ACCENT_BLUE = (59, 130, 246)
ACCENT_CYAN = (56, 189, 248)
ACCENT_GREEN = (16, 185, 129)
ACCENT_AMBER = (245, 158, 11)
ACCENT_ORANGE = (249, 115, 22)
ACCENT_ROSE = (244, 63, 94)
LOWER_BG = (10, 15, 30)

OUTPUT_DIR = "video-production"
CLIPS_DIR = os.path.join(OUTPUT_DIR, "clips_l3")
os.makedirs(CLIPS_DIR, exist_ok=True)

def draw_play_icon(draw, x, y, size=14, color=(255, 255, 255)):
    draw.polygon([(x, y), (x, y + size), (x + size * 0.9, y + size / 2)], fill=color)

def draw_header(draw, category, title):
    draw.rectangle([0, 0, WIDTH, 75], fill=(15, 23, 42))
    draw.line([0, 75, WIDTH, 75], fill=(30, 41, 59), width=2)
    draw.rounded_rectangle([60, 18, 420, 56], radius=6, fill=(30, 41, 59), outline=(56, 189, 248), width=1)
    draw.text((75, 24), category.upper(), font=FONT_SMALL, fill=ACCENT_CYAN)
    draw.text((450, 20), title, font=FONT_HEADING, fill=TEXT_WHITE)

def draw_lower_third(draw, section_time, section_title, teleprompter_cue, elapsed_str, total_str, progress_pct):
    draw.rectangle([0, 955, WIDTH, HEIGHT], fill=LOWER_BG)
    draw.rectangle([0, 955, WIDTH, 963], fill=(30, 41, 59))
    fill_w = int(WIDTH * progress_pct)
    if fill_w > 0:
        draw.rectangle([0, 955, fill_w, 963], fill=ACCENT_CYAN)
    
    draw.rounded_rectangle([50, 975, 480, 1010], radius=6, fill=(30, 41, 59), outline=CARD_BORDER, width=1)
    draw.text((65, 980), f"{section_time} - {section_title}".upper(), font=FONT_TELE_TITLE, fill=ACCENT_CYAN)
    
    timer_text = f"TIEMPO: {elapsed_str} / {total_str}"
    draw.text((WIDTH - 280, 980), timer_text, font=FONT_TIMER, fill=TEXT_MUTED)
    draw.text((50, 1025), "NARRACION: " + teleprompter_cue, font=FONT_TELE_CUE, fill=(226, 232, 240))

def create_scene_1(elapsed_str="00:25", progress_pct=0.08):
    """Scene 1: Introduction and the World Wide Web [00:00 - 00:50]"""
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "Curso de Desarrollo Web", "Lección 3: Atributos y Enlaces")
    
    draw.rounded_rectangle([120, 130, 1800, 900], radius=20, fill=CARD_BG, outline=CARD_BORDER, width=2)
    draw.rounded_rectangle([120, 130, 1800, 140], radius=4, fill=ACCENT_CYAN)
    
    draw.text((180, 180), "La Magia de la Telaraña Mundial", font=FONT_HEADING, fill=ACCENT_CYAN)
    draw.text((180, 240), "Conectando tu página web con todo el planeta", font=FONT_TITLE, fill=TEXT_WHITE)
    draw.text((180, 310), "Descubre cómo los hipervínculos convirtieron páginas aisladas en una red viva", font=FONT_SUBTITLE, fill=TEXT_MUTED)
    
    cards = [
        ("La Etiqueta <a>", "Viene de 'Anchor' (ancla).\nAncla o une dos documentos\ndistintos a través de internet.", ACCENT_CYAN),
        ("Atributos Especiales", "Superpoderes dentro de la etiqueta:\nel atributo obligatorio href='...'\nindica la dirección de destino.", ACCENT_AMBER),
        ("Pestaña Nueva", "Aprende el truco target='_blank'\npara abrir páginas externas sin que\nel visitante abandone tu sitio.", ACCENT_GREEN)
    ]
    cx = 180
    for title, desc, col in cards:
        draw.rounded_rectangle([cx, 400, cx + 460, 680], radius=16, fill=(20, 28, 45), outline=col, width=2)
        draw.text((cx + 30, 430), title, font=FONT_HEADING, fill=col)
        draw.line([cx + 30, 485, cx + 430, 485], fill=(40, 50, 75), width=2)
        y = 510
        for l in desc.split("\n"):
            draw.text((cx + 30, y), l, font=FONT_BODY, fill=TEXT_WHITE)
            y += 40
        cx += 520
        
    draw.rounded_rectangle([180, 720, 1740, 840], radius=12, fill=(15, 23, 42), outline=ACCENT_CYAN, width=1)
    draw.text((220, 745), "DATO HISTORICO:", font=FONT_BODY_BOLD, fill=ACCENT_AMBER)
    draw.text((220, 785), "Antes de los hipervínculos, los documentos digitales estaban aislados. Los enlaces crearon la 'Web' que hoy todos usamos.", font=FONT_BODY, fill=TEXT_WHITE)
    
    draw_lower_third(draw, "00:00 - 00:50", "Introducción: La Telaraña Mundial",
                     '"¡Hola de nuevo y bienvenido a la Lección 3! Hoy aprenderás por qué llamamos web a internet: por los enlaces..."',
                     elapsed_str, "05:15", progress_pct)
    return img

def create_scene_2(elapsed_str="01:25", progress_pct=0.27):
    """Scene 2: Anatomy of an Attribute [00:50 - 02:05]"""
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "Conceptos Clave", "¿Qué es un atributo HTML? Sintaxis y Reglas de Oro")
    
    draw.rounded_rectangle([100, 110, 1820, 910], radius=18, fill=CARD_BG, outline=CARD_BORDER, width=2)
    draw.text((140, 135), "Anatomía de una Etiqueta con Atributos", font=FONT_HEADING, fill=ACCENT_CYAN)
    draw.text((140, 185), "Los atributos entregan información adicional a la etiqueta. Siempre tienen el formato nombre=\"valor\":", font=FONT_BODY, fill=TEXT_MUTED)
    
    # Big code breakdown box
    draw.rounded_rectangle([140, 235, 1780, 420], radius=14, fill=(15, 23, 42), outline=CARD_BORDER, width=2)
    
    draw.rounded_rectangle([170, 275, 270, 375], radius=10, fill=(20, 45, 65), outline=ACCENT_CYAN, width=2)
    draw.text((195, 305), "<a", font=FONT_CODE_LARGE, fill=ACCENT_CYAN)
    
    draw.rounded_rectangle([290, 275, 870, 375], radius=10, fill=(45, 35, 15), outline=ACCENT_AMBER, width=2)
    draw.text((310, 305), 'href="https://es.wikipedia.org"', font=FONT_CODE_LARGE, fill=ACCENT_AMBER)
    
    draw.rounded_rectangle([890, 275, 1260, 375], radius=10, fill=(20, 45, 45), outline=ACCENT_GREEN, width=2)
    draw.text((910, 305), 'target="_blank"', font=FONT_CODE_LARGE, fill=ACCENT_GREEN)
    
    draw.rounded_rectangle([1280, 275, 1550, 375], radius=10, fill=(30, 41, 59), outline=TEXT_WHITE, width=2)
    draw.text((1305, 305), '>Wikipedia', font=FONT_CODE_LARGE, fill=TEXT_WHITE)
    
    draw.rounded_rectangle([1570, 275, 1740, 375], radius=10, fill=(55, 25, 25), outline=ACCENT_ROSE, width=2)
    draw.text((1600, 305), '</a>', font=FONT_CODE_LARGE, fill=ACCENT_ROSE)
    
    # Labels below
    draw.text((180, 385), "ETIQUETA", font=FONT_SMALL, fill=ACCENT_CYAN)
    draw.text((310, 385), "ATRIBUTO 1: Destino web (href)", font=FONT_SMALL, fill=ACCENT_AMBER)
    draw.text((910, 385), "ATRIBUTO 2: Pestaña nueva", font=FONT_SMALL, fill=ACCENT_GREEN)
    draw.text((1310, 385), "TEXTO VISIBLE", font=FONT_SMALL, fill=TEXT_WHITE)
    draw.text((1600, 385), "CIERRE", font=FONT_SMALL, fill=ACCENT_ROSE)
    
    # 2 Pillar cards below
    # Card Left: 3 Golden Rules
    draw.rounded_rectangle([140, 455, 940, 880], radius=14, fill=(20, 28, 45), outline=ACCENT_AMBER, width=2)
    draw.text((170, 480), "3 Reglas de Oro de los Atributos", font=FONT_HEADING, fill=ACCENT_AMBER)
    points_l = [
        "1. SIEMPRE van en la etiqueta de apertura: <a href=...>",
        "   Nunca los coloques en la etiqueta de cierre </a>.",
        "",
        "2. Estructura exacta: nombre=\"valor\"",
        "   Siempre usa comillas dobles alrededor del valor.",
        "",
        "3. Se separan con un simple espacio:",
        "   Puedes combinar varios atributos dejando un espacio."
    ]
    y = 540
    for p in points_l:
        draw.text((170, y), p, font=FONT_BODY, fill=TEXT_WHITE)
        y += 42
        
    # Card Right: What is href and target?
    draw.rounded_rectangle([980, 455, 1780, 880], radius=14, fill=(20, 28, 45), outline=ACCENT_CYAN, width=2)
    draw.text((1010, 480), "¿Qué significan href y target?", font=FONT_HEADING, fill=ACCENT_CYAN)
    points_r = [
        "- href significa 'Hypertext Reference' (referencia de hipertexto).",
        "  Es la dirección web exacta a donde debe viajar el navegador.",
        "",
        "- Debe incluir el protocolo completo: https://",
        "  Ejemplo: href=\"https://es.wikipedia.org\"",
        "",
        "- target=\"_blank\" le indica al navegador:",
        "  'Abre este enlace en una pestaña nueva para no cerrar mi web'."
    ]
    y = 540
    for p in points_r:
        draw.text((1010, y), p, font=FONT_BODY, fill=TEXT_WHITE)
        y += 42
        
    draw_lower_third(draw, "00:50 - 02:05", "¿Qué es un Atributo HTML?",
                     '"Un atributo le da superpoderes a la etiqueta. En <a> el atributo obligatorio es href con la dirección web..."',
                     elapsed_str, "05:15", progress_pct)
    return img

def create_scene_3(elapsed_str="02:40", progress_pct=0.51):
    """Scene 3: Links in Action and target="_blank" [02:05 - 03:20]"""
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "Comportamiento del Navegador", "Enlaces en Acción: El valor de target='_blank'")
    
    draw.rounded_rectangle([100, 110, 1820, 910], radius=18, fill=CARD_BG, outline=CARD_BORDER, width=2)
    draw.text((140, 135), "Cómo se ven y cómo se comportan los enlaces", font=FONT_HEADING, fill=ACCENT_CYAN)
    draw.text((140, 185), "El navegador aplica un estilo visual automático a las etiquetas <a>: texto azul y subrayado.", font=FONT_BODY, fill=TEXT_MUTED)
    
    # Left: Mockup of code with links
    draw.rounded_rectangle([140, 240, 930, 880], radius=14, fill=(15, 23, 42), outline=ACCENT_AMBER, width=2)
    draw.text((170, 270), "Código HTML en JSFiddle", font=FONT_HEADING, fill=ACCENT_AMBER)
    
    code_lines = [
        "<h1>Mis sitios favoritos</h1>",
        "",
        "<p>",
        "  Mi enciclopedia favorita es",
        '  <a href="https://es.wikipedia.org"',
        '     target="_blank">Wikipedia</a>.',
        "</p>",
        "",
        "<p>",
        "  También puedes aprender más en",
        '  <a href="https://developer.mozilla.org"',
        '     target="_blank">MDN Web Docs</a>.',
        "</p>"
    ]
    y = 330
    for cl in code_lines:
        col = ACCENT_CYAN if "<a" in cl or "</a>" in cl else (ACCENT_AMBER if "href=" in cl or "target=" in cl else TEXT_WHITE)
        draw.text((170, y), cl, font=FONT_CODE_BOLD, fill=col)
        y += 40
        
    # Right: The 2 behaviors compared
    draw.rounded_rectangle([970, 240, 1780, 880], radius=14, fill=(20, 28, 45), outline=ACCENT_CYAN, width=2)
    draw.text((1000, 270), "¿Por qué usar target='_blank'?", font=FONT_HEADING, fill=ACCENT_CYAN)
    
    # Box 1: Without target
    draw.rounded_rectangle([1000, 330, 1750, 560], radius=12, fill=(45, 20, 20), outline=ACCENT_ROSE, width=2)
    draw.text((1030, 355), "SIN target='_blank' (Comportamiento por defecto)", font=FONT_BODY_BOLD, fill=ACCENT_ROSE)
    draw.text((1030, 405), "• El enlace se abre en la MISMA pestaña actual.", font=FONT_BODY, fill=TEXT_WHITE)
    draw.text((1030, 445), "• El usuario se va de tu sitio web y probablemente no regrese.", font=FONT_BODY, fill=TEXT_WHITE)
    draw.text((1030, 485), "• Pierdes a tus visitantes.", font=FONT_BODY, fill=(254, 205, 211))
    
    # Box 2: With target="_blank"
    draw.rounded_rectangle([1000, 600, 1750, 840], radius=12, fill=(15, 45, 30), outline=ACCENT_GREEN, width=2)
    draw.text((1030, 625), "CON target='_blank' (Mejor experiencia de usuario)", font=FONT_BODY_BOLD, fill=ACCENT_GREEN)
    draw.text((1030, 675), "• El enlace se abre en una PESTAÑA NUEVA del navegador.", font=FONT_BODY, fill=TEXT_WHITE)
    draw.text((1030, 715), "• Tu sitio web sigue abierto en la pestaña anterior.", font=FONT_BODY, fill=TEXT_WHITE)
    draw.text((1030, 755), "• Excelente para enlaces hacia sitios externos.", font=FONT_BODY, fill=(167, 243, 208))
    
    draw_lower_third(draw, "02:05 - 03:20", "Enlaces en Acción y target='_blank'",
                     '"Con target=_blank el enlace se abre en una pestaña nueva sin perder a tu visitante..."',
                     elapsed_str, "05:15", progress_pct)
    return img

def create_scene_4_frame(step_title, error_mode=False, elapsed_str="03:45", progress_pct=0.72):
    """Scene 4: Live JSFiddle demonstration of links and common mistakes"""
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "Demostración Práctica", "Escribiendo enlaces y evitando errores comunes")
    
    draw.rounded_rectangle([80, 95, 1840, 925], radius=14, fill=(24, 32, 47), outline=CARD_BORDER, width=2)
    
    # Navbar
    draw.rectangle([80, 95, 1840, 155], fill=(15, 23, 42))
    draw.text((110, 112), "JSFiddle", font=FONT_HEADING, fill=TEXT_WHITE)
    
    draw.rounded_rectangle([270, 107, 400, 143], radius=6, fill=(16, 185, 129), outline=(52, 211, 153), width=2)
    draw_play_icon(draw, 290, 118, 14, (255, 255, 255))
    draw.text((315, 113), "Run", font=FONT_BODY_BOLD, fill=TEXT_WHITE)
    
    draw.rounded_rectangle([430, 107, 1200, 143], radius=6, fill=(30, 41, 59))
    draw.text((450, 114), f"PASO ACTUAL: {step_title}", font=FONT_BODY_BOLD, fill=ACCENT_CYAN)
    
    x1, y1 = 100, 175
    w_editor = 860
    h_editor = 720
    
    # HTML Editor Panel
    draw.rounded_rectangle([x1, y1, x1 + w_editor, y1 + h_editor], radius=10, fill=(15, 23, 42), outline=ACCENT_AMBER, width=2)
    draw.rectangle([x1, y1, x1 + w_editor, y1 + 45], fill=(30, 41, 59))
    draw.text((x1 + 15, y1 + 10), "Panel HTML (Editor de Código)", font=FONT_BODY_BOLD, fill=ACCENT_AMBER)
    
    if not error_mode:
        code = [
            "<h1>Mis sitios favoritos</h1>",
            "",
            "<p>",
            "  Mi enciclopedia favorita es",
            '  <a href="https://es.wikipedia.org"',
            '     target="_blank">Wikipedia</a>.',
            "</p>",
            "",
            "<p>",
            "  También puedes aprender más en",
            '  <a href="https://developer.mozilla.org/es/"',
            '     target="_blank">MDN Web Docs</a>.',
            "</p>"
        ]
    else:
        code = [
            "<!-- ERROR TIPICO 1: Olvidar https:// -->",
            '<p><a href="wikipedia.org">Wikipedia</a></p>',
            "<!-- El navegador lo busca como carpeta local! Error 404 -->",
            "",
            "<!-- ERROR TIPICO 2: Olvidar las comillas -->",
            '<p><a href=https://es.wikipedia.org>Wikipedia</a></p>',
            "<!-- Rompe atributos con espacios o caracteres raros -->",
            "",
            "<!-- FORMA CORRECTA: -->",
            '<p><a href="https://es.wikipedia.org" target="_blank">',
            "   Wikipedia</a></p>"
        ]
        
    y_c = y1 + 70
    for l in code:
        if l.startswith("<!--"):
            draw.text((x1 + 30, y_c), l, font=FONT_CODE, fill=ACCENT_AMBER)
        elif 'href=' in l:
            draw.text((x1 + 30, y_c), l, font=FONT_CODE_BOLD, fill=ACCENT_CYAN)
        else:
            draw.text((x1 + 30, y_c), l, font=FONT_CODE, fill=TEXT_WHITE)
        y_c += 45
        
    # Result Panel (Right)
    xr = x1 + w_editor + 30
    w_res = 820
    draw.rounded_rectangle([xr, y1, xr + w_res, y1 + h_editor], radius=10, fill=(255, 255, 255), outline=ACCENT_GREEN, width=3)
    draw.rectangle([xr, y1, xr + w_res, y1 + 45], fill=(241, 245, 249))
    draw.text((xr + 15, y1 + 10), "Result (Tu Página Web en Vivo)", font=FONT_BODY_BOLD, fill=(15, 23, 42))
    
    # Rendered result
    f_h1 = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 36)
    f_p = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 22)
    f_link = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 22)
    
    draw.text((xr + 40, y1 + 80), "Mis sitios favoritos", font=f_h1, fill=(15, 23, 42))
    
    # Parrafo 1
    draw.text((xr + 40, y1 + 160), "Mi enciclopedia favorita es ", font=f_p, fill=(51, 65, 85))
    draw.text((xr + 325, y1 + 160), "Wikipedia", font=f_link, fill=(37, 99, 235))
    draw.line([xr + 325, y1 + 185, xr + 425, y1 + 185], fill=(37, 99, 235), width=2)
    draw.text((xr + 430, y1 + 160), ".", font=f_p, fill=(51, 65, 85))
    
    # Parrafo 2
    draw.text((xr + 40, y1 + 230), "También puedes aprender más en ", font=f_p, fill=(51, 65, 85))
    draw.text((xr + 40, y1 + 270), "MDN Web Docs", font=f_link, fill=(37, 99, 235))
    draw.line([xr + 40, y1 + 295, xr + 195, y1 + 295], fill=(37, 99, 235), width=2)
    draw.text((xr + 200, y1 + 270), ".", font=f_p, fill=(51, 65, 85))
    
    # Explanatory card inside Result
    draw.rounded_rectangle([xr + 40, y1 + 350, xr + 770, y1 + 650], radius=12, fill=(240, 249, 255), outline=ACCENT_CYAN, width=2)
    draw.text((xr + 65, y1 + 375), "DETECCIÓN AUTOMÁTICA DEL NAVEGADOR:", font=FONT_BODY_BOLD, fill=(3, 105, 161))
    draw.text((xr + 65, y1 + 425), "• Texto azul (#2563eb)", font=FONT_BODY, fill=(15, 23, 42))
    draw.text((xr + 65, y1 + 475), "• Línea inferior (subrayado)", font=FONT_BODY, fill=(15, 23, 42))
    draw.text((xr + 65, y1 + 525), "• Cursor en forma de mano al pasar por encima", font=FONT_BODY, fill=(15, 23, 42))
    draw.text((xr + 65, y1 + 575), "• Al hacer clic -> Abre en nueva pestaña gracias a target='_blank'", font=FONT_BODY, fill=(16, 185, 129))
    
    draw_lower_third(draw, "03:20 - 04:20", "Demostración Práctica en JSFiddle",
                     '"Escribimos los enlaces con href y target=_blank y repasamos errores típicos como olvidar https://..."',
                     elapsed_str, "05:15", progress_pct)
    return img

def create_scene_5(elapsed_str="04:35", progress_pct=0.88):
    """Scene 5: Interactive practice challenge [04:20 - 04:55]"""
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "Actividad Práctica", "¡Pausa el video y crea tus propios enlaces!")
    
    draw.rounded_rectangle([140, 120, 1780, 910], radius=20, fill=CARD_BG, outline=ACCENT_AMBER, width=3)
    draw.rounded_rectangle([180, 160, 1740, 260], radius=14, fill=(45, 30, 15), outline=ACCENT_AMBER, width=2)
    draw.text((220, 185), "PAUSA EL VIDEO: Tómate 1 minuto para practicar en tu JSFiddle", font=FONT_TITLE, fill=ACCENT_AMBER)
    
    steps = [
        ("Paso 1", "Entra a tu JSFiddle y crea un nuevo párrafo <p> con tu recomendación favorita.", ACCENT_CYAN),
        ("Paso 2", "Elige un sitio: Spotify, YouTube, la NASA, Twitch o tu página de juegos.", ACCENT_AMBER),
        ("Paso 3", "Envuelve el nombre en <a href=\"https://...\"> con la dirección completa.", ACCENT_GREEN),
        ("Paso 4", "Agrega target=\"_blank\" para que se abra en una nueva pestaña sin cerrar tu web.", ACCENT_ORANGE)
    ]
    y = 295
    for tag, desc, col in steps:
        draw.rounded_rectangle([180, y, 1740, y + 105], radius=12, fill=(20, 28, 45), outline=CARD_BORDER, width=1)
        draw.rounded_rectangle([210, y + 25, 330, y + 80], radius=8, fill=col)
        draw.text((230, y + 36), tag, font=FONT_HEADING, fill=(15, 23, 42))
        draw.text((360, y + 36), desc, font=FONT_BODY_BOLD, fill=TEXT_WHITE)
        y += 125
        
    draw.rounded_rectangle([180, 810, 1740, 880], radius=10, fill=(15, 23, 42), outline=ACCENT_CYAN, width=1)
    draw.text((220, 830), "RECUERDA: Siempre verifica que la dirección empiece con https:// y que tenga comillas dobles.", font=FONT_BODY, fill=ACCENT_CYAN)
    
    draw_lower_third(draw, "04:20 - 04:55", "Pausa para la Práctica Interactiva",
                     '"Pausa el video durante 1 minuto, entra a tu JSFiddle y agrega un enlace con https:// y target=_blank..."',
                     elapsed_str, "05:15", progress_pct)
    return img

def create_scene_6(elapsed_str="05:05", progress_pct=0.98):
    """Scene 6: Summary and Next Lesson [04:55 - 05:15]"""
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "Resumen de la Lección", "¡Tu página ya está conectada a la Red Mundial!")
    
    draw.rounded_rectangle([140, 120, 1780, 910], radius=20, fill=CARD_BG, outline=ACCENT_GREEN, width=3)
    draw.text((200, 170), "¡Excelente trabajo! Has completado la Lección 3", font=FONT_TITLE, fill=TEXT_WHITE)
    draw.text((200, 235), "Ahora ya sabes cómo conectar documentos y usar atributos en HTML:", font=FONT_SUBTITLE, fill=TEXT_MUTED)
    
    checks = [
        ("[OK] Enlaces Interactivos con <a>", "Anchor ancla dos páginas distintas y permite la navegación."),
        ("[OK] Atributo href Obligatorio", "Define el destino exacto: siempre con https:// y comillas dobles."),
        ("[OK] Pestañas Nuevas con target='_blank'", "Mantiene a tus visitantes en tu sitio mientras exploran el enlace.")
    ]
    y = 310
    for title, desc in checks:
        draw.rounded_rectangle([200, y, 1720, y + 110], radius=12, fill=(20, 28, 45), outline=(52, 211, 153), width=1)
        draw.text((240, y + 20), title, font=FONT_HEADING, fill=ACCENT_GREEN)
        draw.text((240, y + 65), desc, font=FONT_BODY, fill=TEXT_WHITE)
        y += 135
        
    draw.rounded_rectangle([200, 740, 1720, 870], radius=14, fill=(15, 35, 55), outline=ACCENT_CYAN, width=2)
    draw.text((240, 765), "PROXIMA LECCION (Lección 4 de 10):", font=FONT_BODY_BOLD, fill=ACCENT_AMBER)
    draw.text((240, 805), "Imágenes (<img>) y Listas (<ul>, <ol>): haciendo tu página visual y ordenada", font=FONT_HEADING, fill=TEXT_WHITE)
    
    draw_lower_third(draw, "04:55 - 05:15", "Resumen y Próxima Lección",
                     '"En la Lección 4 aprenderemos a insertar imágenes con img y listas numeradas y con viñetas..."',
                     elapsed_str, "05:15", progress_pct)
    return img

def render_clip_from_image(img, duration_sec, output_path):
    temp_png = output_path + ".temp.png"
    img.save(temp_png)
    cmd = [
        "ffmpeg", "-y", "-loop", "1", "-i", temp_png, "-t", str(duration_sec),
        "-c:v", "libx264", "-preset", "ultrafast", "-tune", "stillimage",
        "-pix_fmt", "yuv420p", "-r", "30", output_path
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if os.path.exists(temp_png):
        os.remove(temp_png)

def generate_scene_4_clip(output_path):
    sub_clips = []
    
    # 4.1: Code with Wikipedia link (20s)
    img_41 = create_scene_4_frame(
        step_title="1. Creando el enlace hacia Wikipedia con href",
        error_mode=False,
        elapsed_str="03:30",
        progress_pct=0.67
    )
    p_41 = os.path.join(CLIPS_DIR, "sc4_1.mp4")
    render_clip_from_image(img_41, 20, p_41)
    sub_clips.append(p_41)
    
    # 4.2: Adding MDN link & target="_blank" (20s)
    img_42 = create_scene_4_frame(
        step_title="2. Agregando target='_blank' y segundo enlace a MDN",
        error_mode=False,
        elapsed_str="03:50",
        progress_pct=0.73
    )
    p_42 = os.path.join(CLIPS_DIR, "sc4_2.mp4")
    render_clip_from_image(img_42, 20, p_42)
    sub_clips.append(p_42)
    
    # 4.3: Demonstrating common errors (20s)
    img_43 = create_scene_4_frame(
        step_title="3. Alerta de errores: olvidar https:// o comillas",
        error_mode=True,
        elapsed_str="04:10",
        progress_pct=0.80
    )
    p_43 = os.path.join(CLIPS_DIR, "sc4_3.mp4")
    render_clip_from_image(img_43, 20, p_43)
    sub_clips.append(p_43)
    
    list_txt = os.path.join(CLIPS_DIR, "sc4_list.txt")
    with open(list_txt, "w") as f:
        for sc in sub_clips:
            f.write(f"file '{os.path.basename(sc)}'\n")
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", list_txt, "-c", "copy", output_path],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    print("=== Generador de Video Base para Lección 3 (5:15 min) ===")
    t_start = time.time()
    
    sc1_path = os.path.join(CLIPS_DIR, "scene_1.mp4")
    render_clip_from_image(create_scene_1("00:25", 0.08), 50, sc1_path)
    
    sc2_path = os.path.join(CLIPS_DIR, "scene_2.mp4")
    render_clip_from_image(create_scene_2("01:25", 0.27), 75, sc2_path)
    
    sc3_path = os.path.join(CLIPS_DIR, "scene_3.mp4")
    render_clip_from_image(create_scene_3("02:40", 0.51), 75, sc3_path)
    
    sc4_path = os.path.join(CLIPS_DIR, "scene_4.mp4")
    generate_scene_4_clip(sc4_path)
    
    sc5_path = os.path.join(CLIPS_DIR, "scene_5.mp4")
    render_clip_from_image(create_scene_5("04:35", 0.88), 35, sc5_path)
    
    sc6_path = os.path.join(CLIPS_DIR, "scene_6.mp4")
    render_clip_from_image(create_scene_6("05:05", 0.98), 20, sc6_path)
    
    master_list = os.path.join(CLIPS_DIR, "master_list.txt")
    with open(master_list, "w") as f:
        f.write(f"file '{os.path.basename(sc1_path)}'\n")
        f.write(f"file '{os.path.basename(sc2_path)}'\n")
        f.write(f"file '{os.path.basename(sc3_path)}'\n")
        f.write(f"file '{os.path.basename(sc4_path)}'\n")
        f.write(f"file '{os.path.basename(sc5_path)}'\n")
        f.write(f"file '{os.path.basename(sc6_path)}'\n")
        
    final_output = os.path.join(OUTPUT_DIR, "leccion-03-ejecucion-5min.mp4")
    cmd_master = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", master_list,
        "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
        "-c:v", "copy", "-c:a", "aac", "-shortest", final_output
    ]
    subprocess.run(cmd_master, check=True)
    dur_sec = 50 + 75 + 75 + 60 + 35 + 20
    print(f"\n✅ Video Lección 3 generado: {final_output}")
    print(f"⏱️ Duración: {dur_sec} segundos ({dur_sec//60}:{dur_sec%60:02d} min)")
    print(f"⚡ Tiempo: {time.time() - t_start:.2f} s")

if __name__ == "__main__":
    main()
