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
FONT_CODE_LARGE = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 38)
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
CLIPS_DIR = os.path.join(OUTPUT_DIR, "clips_l2")
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
    """Scene 1: Introduction and Computer Language [00:00 - 00:50]"""
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "Curso de Desarrollo Web", "Lección 2: Tu primera página HTML")
    
    draw.rounded_rectangle([120, 130, 1800, 900], radius=20, fill=CARD_BG, outline=CARD_BORDER, width=2)
    draw.rounded_rectangle([120, 130, 1800, 140], radius=4, fill=ACCENT_AMBER)
    
    draw.text((180, 180), "Estructura Básica y Etiquetas", font=FONT_HEADING, fill=ACCENT_AMBER)
    draw.text((180, 240), "El idioma con el que se comunican los navegadores", font=FONT_TITLE, fill=TEXT_WHITE)
    draw.text((180, 310), "Aprende cómo darle instrucciones exactas a la computadora para estructurar texto", font=FONT_SUBTITLE, fill=TEXT_MUTED)
    
    cards = [
        ("Sin Botones", "A diferencia de Word o Docs, en web\nno usamos botones de negrita.\nEscribimos código directo.", ACCENT_CYAN),
        ("Etiquetas Precisas", "Cada título, subtítulo y párrafo\nvive dentro de una etiqueta\ncon reglas claras de apertura y cierre.", ACCENT_AMBER),
        ("Jerarquía Lógica", "Aprende a ordenar tus ideas:\ndesde el gran título <h1>\nhasta párrafos normales con <p>.", ACCENT_GREEN)
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
        
    draw.rounded_rectangle([180, 720, 1740, 840], radius=12, fill=(15, 23, 42), outline=ACCENT_AMBER, width=1)
    draw.text((220, 745), "CONSEJO CLAVE:", font=FONT_BODY_BOLD, fill=ACCENT_CYAN)
    draw.text((220, 785), "El navegador es una máquina estricta: lee cada símbolo en orden. Si abres una etiqueta, ¡siempre debes cerrarla!", font=FONT_BODY, fill=TEXT_WHITE)
    
    draw_lower_third(draw, "00:00 - 00:50", "Bienvenida y el Idioma de la Web",
                     '"¡Hola de nuevo y bienvenido a la Lección 2! Hoy aprenderás cómo entiende la computadora lo que queremos escribir..."',
                     elapsed_str, "05:15", progress_pct)
    return img

def create_scene_2(elapsed_str="01:25", progress_pct=0.27):
    """Scene 2: Anatomy of an HTML Element [00:50 - 02:05]"""
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "Sintaxis Básica", "Anatomía de una etiqueta HTML: Apertura, Contenido y Cierre")
    
    # Large central diagram card
    draw.rounded_rectangle([100, 110, 1820, 910], radius=18, fill=CARD_BG, outline=CARD_BORDER, width=2)
    draw.text((140, 135), "Descomposición de un Elemento HTML", font=FONT_HEADING, fill=ACCENT_CYAN)
    draw.text((140, 185), "Un elemento HTML completo está compuesto por 3 partes esenciales:", font=FONT_BODY, fill=TEXT_MUTED)
    
    # Big code breakdown box
    draw.rounded_rectangle([140, 240, 1780, 420], radius=14, fill=(15, 23, 42), outline=CARD_BORDER, width=2)
    
    # Visual boxes for <p>, Hola mundo web, and </p>
    draw.rounded_rectangle([200, 280, 450, 380], radius=10, fill=(20, 45, 65), outline=ACCENT_CYAN, width=2)
    draw.text((280, 305), "<p>", font=FONT_CODE_LARGE, fill=ACCENT_CYAN)
    
    draw.text((475, 305), "+", font=FONT_CODE_LARGE, fill=TEXT_MUTED)
    
    draw.rounded_rectangle([520, 280, 1220, 380], radius=10, fill=(30, 41, 59), outline=TEXT_WHITE, width=2)
    draw.text((560, 305), "Hola, mundo web", font=FONT_CODE_LARGE, fill=TEXT_WHITE)
    
    draw.text((1245, 305), "+", font=FONT_CODE_LARGE, fill=TEXT_MUTED)
    
    draw.rounded_rectangle([1290, 280, 1540, 380], radius=10, fill=(55, 25, 25), outline=ACCENT_ROSE, width=2)
    draw.text((1360, 305), "</p>", font=FONT_CODE_LARGE, fill=ACCENT_ROSE)
    
    # Explanatory labels below each box
    draw.text((210, 395), "1. ETIQUETA DE APERTURA", font=FONT_BODY_BOLD, fill=ACCENT_CYAN)
    draw.text((540, 395), "2. CONTENIDO (Lo que ve el usuario)", font=FONT_BODY_BOLD, fill=TEXT_WHITE)
    draw.text((1295, 395), "3. ETIQUETA DE CIERRE", font=FONT_BODY_BOLD, fill=ACCENT_ROSE)
    
    # 2 Detail cards below
    # Card Left: Opening vs Closing
    draw.rounded_rectangle([140, 460, 940, 880], radius=14, fill=(20, 28, 45), outline=ACCENT_CYAN, width=2)
    draw.text((170, 485), "La Regla de la Pareja", font=FONT_HEADING, fill=ACCENT_CYAN)
    
    points_l = [
        "- Se escriben entre los signos menor que (<) y mayor que (>).",
        "- La etiqueta de apertura avisa dónde comienza el elemento.",
        "- La etiqueta de cierre avisa exactamente dónde termina.",
        "- La barra diagonal (/) antes del nombre indica el FIN.",
        "- Sin etiquetas de cierre, el formato se propaga sin control."
    ]
    y = 550
    for p in points_l:
        draw.text((170, y), p, font=FONT_BODY, fill=TEXT_WHITE)
        y += 55
        
    # Card Right: What happens if you forget / ?
    draw.rounded_rectangle([980, 460, 1780, 880], radius=14, fill=(20, 28, 45), outline=ACCENT_ROSE, width=2)
    draw.text((1010, 485), "PELIGRO: ¿Qué pasa si olvidas la barra / ?", font=FONT_HEADING, fill=ACCENT_ROSE)
    
    points_r = [
        "- Si abres <h1> y olvidas </h1>, todo el resto se vuelve gigante.",
        "- El navegador no adivina: asume que todo lo demás es el título.",
        "- Las páginas se desordenan y los párrafos pierden su tamaño.",
        "- REGLA DE ORO: 'Etiqueta que se abre, etiqueta que se cierra'.",
        "- Revisa siempre tus barras diagonales (/) antes de guardar."
    ]
    y = 550
    for p in points_r:
        draw.text((1010, y), p, font=FONT_BODY, fill=TEXT_WHITE)
        y += 55
    
    draw_lower_third(draw, "00:50 - 02:05", "Anatomía de una Etiqueta HTML",
                     '"En HTML todo funciona con etiquetas en pareja: apertura, contenido y cierre con barra diagonal..."',
                     elapsed_str, "05:15", progress_pct)
    return img

def create_scene_3(elapsed_str="02:40", progress_pct=0.51):
    """Scene 3: Heading Hierarchy h1 to h6 and p [02:05 - 03:20]"""
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "Jerarquía de Contenido", "Encabezados (<h1> a <h6>) y Párrafos (<p>)")
    
    draw.rounded_rectangle([100, 110, 1820, 910], radius=18, fill=CARD_BG, outline=CARD_BORDER, width=2)
    draw.text((140, 135), "La Escala de Encabezados en HTML", font=FONT_HEADING, fill=ACCENT_AMBER)
    draw.text((140, 185), "La letra 'h' viene de 'Heading'. Ordena tu contenido de mayor a menor importancia:", font=FONT_BODY, fill=TEXT_MUTED)
    
    # Hierarchy Visual Ladder (Left)
    draw.rounded_rectangle([140, 240, 1050, 880], radius=14, fill=(20, 28, 45), outline=ACCENT_AMBER, width=2)
    
    headings = [
        ("<h1>", "Título Principal", "42px", "(Solo uno por página, el más importante)", ACCENT_CYAN, 36),
        ("<h2>", "Subtítulo de Sección", "32px", "(Capítulos y divisiones de tema)", ACCENT_AMBER, 30),
        ("<h3>", "Subsección de Detalle", "26px", "(Subtemas específicos)", ACCENT_GREEN, 24),
        ("<h4> - <h6>", "Encabezados Menores", "18px", "(Detalles secundarios pequeños)", TEXT_MUTED, 20),
        ("<p>", "Párrafo Regular", "16px", "(Texto normal para oraciones y explicaciones)", TEXT_WHITE, 20)
    ]
    
    y = 265
    for tag, desc, sz, note, col, fsz in headings:
        draw.rounded_rectangle([165, y, 1025, y + 105], radius=10, fill=(15, 23, 42), outline=CARD_BORDER, width=1)
        # Tag badge
        draw.rounded_rectangle([180, y + 20, 320, y + 85], radius=8, fill=(30, 41, 59), outline=col, width=2)
        f_tag = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 26)
        draw.text((205, y + 35), tag, font=f_tag, fill=col)
        
        # Heading name and note
        draw.text((345, y + 25), f"{desc} [{sz}]", font=FONT_BODY_BOLD, fill=col)
        draw.text((345, y + 65), note, font=FONT_SMALL, fill=TEXT_MUTED)
        y += 120
        
    # Crucial Rule Box (Right): Whitespace collapse
    draw.rounded_rectangle([1090, 240, 1780, 880], radius=14, fill=(20, 28, 45), outline=ACCENT_CYAN, width=2)
    draw.text((1125, 270), "EL MISTERIO DE LA TECLA ENTER", font=FONT_HEADING, fill=ACCENT_CYAN)
    
    notes_enter = [
        "¿Qué pasa si presionas ENTER 5 veces en HTML?",
        "¡El navegador IGNORA los saltos de línea vacíos!",
        "",
        "En desarrollo web esto se llama 'colapso de espacios'.",
        "Para el navegador, 10 espacios o 5 Enters equivalen a",
        "un solo espacio simple.",
        "",
        "LA UNICA FORMA CORRECTA DE SEPARAR PARRAFOS:",
        "Envolver cada bloque de texto dentro de su propia",
        "pareja de etiquetas: <p>...</p>",
        "",
        "Ejemplo:",
        "  <p>Primer párrafo con su idea.</p>",
        "  <p>Segundo párrafo en línea separada.</p>"
    ]
    y = 330
    for line in notes_enter:
        if "LA UNICA FORMA" in line:
            draw.text((1125, y), line, font=FONT_BODY_BOLD, fill=ACCENT_AMBER)
        elif line.startswith("  <p>"):
            draw.text((1125, y), line, font=FONT_CODE_BOLD, fill=ACCENT_GREEN)
        else:
            draw.text((1125, y), line, font=FONT_BODY, fill=TEXT_WHITE)
        y += 38
        
    draw_lower_third(draw, "02:05 - 03:20", "Jerarquía de Títulos y Párrafos",
                     '"HTML clasifica la importancia con h1 a h6... y recuerda: para separar párrafos siempre usamos la etiqueta p..."',
                     elapsed_str, "05:15", progress_pct)
    return img

def create_scene_4_frame(step_title, html_lines, res_items, cursor_pos=None, run_clicked=False,
                         elapsed_str="03:45", progress_pct=0.72):
    """Scene 4: JSFiddle live coding simulation for Lesson 2"""
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "Demostración Práctica", "Escribiendo encabezados y párrafos en JSFiddle")
    
    draw.rounded_rectangle([80, 95, 1840, 925], radius=14, fill=(24, 32, 47), outline=CARD_BORDER, width=2)
    
    # Navbar
    draw.rectangle([80, 95, 1840, 155], fill=(15, 23, 42))
    draw.text((110, 112), "JSFiddle", font=FONT_HEADING, fill=TEXT_WHITE)
    
    btn_bg = (5, 150, 105) if run_clicked else (16, 185, 129)
    btn_outline = (110, 231, 183) if run_clicked else (52, 211, 153)
    draw.rounded_rectangle([270, 107, 400, 143], radius=6, fill=btn_bg, outline=btn_outline, width=2)
    draw_play_icon(draw, 290, 118, 14, (255, 255, 255))
    draw.text((315, 113), "Run", font=FONT_BODY_BOLD, fill=TEXT_WHITE)
    
    draw.rounded_rectangle([430, 107, 1200, 143], radius=6, fill=(30, 41, 59))
    draw.text((450, 114), f"PASO ACTUAL: {step_title}", font=FONT_BODY_BOLD, fill=ACCENT_CYAN)
    
    # Layout: Left HTML editor (large), Right Result panel (large)
    x1, y1 = 100, 175
    w_editor = 860
    h_editor = 720
    
    # HTML Editor Panel
    draw.rounded_rectangle([x1, y1, x1 + w_editor, y1 + h_editor], radius=10, fill=(15, 23, 42), outline=ACCENT_AMBER, width=2)
    draw.rectangle([x1, y1, x1 + w_editor, y1 + 45], fill=(30, 41, 59))
    draw.text((x1 + 15, y1 + 10), "Panel HTML (Editor de Código)", font=FONT_BODY_BOLD, fill=ACCENT_AMBER)
    
    y_code = y1 + 75
    for l in html_lines:
        draw.text((x1 + 30, y_code), l, font=FONT_CODE_BOLD, fill=TEXT_WHITE if not l.startswith("<h") else ACCENT_CYAN)
        y_code += 45
        
    # Result Panel (Right)
    xr = x1 + w_editor + 30
    w_res = 820
    draw.rounded_rectangle([xr, y1, xr + w_res, y1 + h_editor], radius=10, fill=(255, 255, 255), outline=ACCENT_GREEN, width=3)
    draw.rectangle([xr, y1, xr + w_res, y1 + 45], fill=(241, 245, 249))
    draw.text((xr + 15, y1 + 10), "Result (Tu Página Web en Vivo)", font=FONT_BODY_BOLD, fill=(15, 23, 42))
    
    y_res = y1 + 75
    for tag_type, text in res_items:
        if tag_type == "h1":
            f_h1 = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 36)
            draw.text((xr + 40, y_res), text, font=f_h1, fill=(15, 23, 42))
            y_res += 55
        elif tag_type == "h2":
            f_h2 = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 28)
            draw.text((xr + 40, y_res), text, font=f_h2, fill=(30, 41, 59))
            y_res += 45
        elif tag_type == "h3":
            f_h3 = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 22)
            draw.text((xr + 40, y_res), text, font=f_h3, fill=(51, 65, 85))
            y_res += 40
        elif tag_type == "p":
            f_p = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 20)
            draw.text((xr + 40, y_res), text, font=f_p, fill=(71, 85, 105))
            y_res += 45
            
    if cursor_pos:
        cx, cy = cursor_pos
        draw.polygon([(cx, cy), (cx + 18, cy + 18), (cx + 10, cy + 22), (cx + 16, cy + 34),
                      (cx + 10, cy + 36), (cx + 5, cy + 24), (cx, cy + 26)], fill=(255, 255, 255), outline=(0, 0, 0))
                      
    draw_lower_third(draw, "03:20 - 04:20", "Demostración Práctica en JSFiddle",
                     '"Escribimos h1 Mi Diario Digital, h2 Sobre mí, párrafos con p y observamos la jerarquía..."',
                     elapsed_str, "05:15", progress_pct)
    return img

def create_scene_5(elapsed_str="04:35", progress_pct=0.88):
    """Scene 5: Interactive practice challenge [04:20 - 04:55]"""
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "Actividad Práctica", "¡Pausa el video y crea tu propia estructura!")
    
    draw.rounded_rectangle([140, 120, 1780, 910], radius=20, fill=CARD_BG, outline=ACCENT_AMBER, width=3)
    draw.rounded_rectangle([180, 160, 1740, 260], radius=14, fill=(45, 30, 15), outline=ACCENT_AMBER, width=2)
    draw.text((220, 185), "PAUSA EL VIDEO: Tómate 1 minuto para practicar en tu JSFiddle", font=FONT_TITLE, fill=ACCENT_AMBER)
    
    steps = [
        ("Paso 1", "Abre tu JSFiddle y borra cualquier código anterior del panel HTML.", ACCENT_CYAN),
        ("Paso 2", "Escribe un <h1> con el título de tu videojuego, película o serie favorita.", ACCENT_AMBER),
        ("Paso 3", "Agrega un <h2> que diga '¿De qué trata?' y un párrafo <p> explicándolo.", ACCENT_GREEN),
        ("Paso 4", "Agrega un <h3> que diga 'Mi personaje favorito' y otro <p> con su nombre.", ACCENT_ORANGE)
    ]
    y = 295
    for tag, desc, col in steps:
        draw.rounded_rectangle([180, y, 1740, y + 105], radius=12, fill=(20, 28, 45), outline=CARD_BORDER, width=1)
        draw.rounded_rectangle([210, y + 25, 330, y + 80], radius=8, fill=col)
        draw.text((230, y + 36), tag, font=FONT_HEADING, fill=(15, 23, 42))
        draw.text((360, y + 36), desc, font=FONT_BODY_BOLD, fill=TEXT_WHITE)
        y += 125
        
    draw.rounded_rectangle([180, 810, 1740, 880], radius=10, fill=(15, 23, 42), outline=ACCENT_CYAN, width=1)
    draw.text((220, 830), "REVISION FINAL: Verifica que cada etiqueta tenga su cierre con barra diagonal (</h1>, </h2>, </p>).", font=FONT_BODY, fill=ACCENT_CYAN)
    
    draw_lower_third(draw, "04:20 - 04:55", "Pausa para la Práctica Interactiva",
                     '"Pausa el video durante 1 minuto, entra a tu JSFiddle y crea tu mini página con h1, h2 y párrafos..."',
                     elapsed_str, "05:15", progress_pct)
    return img

def create_scene_6(elapsed_str="05:05", progress_pct=0.98):
    """Scene 6: Summary and Next Lesson [04:55 - 05:15]"""
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "Resumen de la Lección", "¡Dominaste la estructura de texto en HTML!")
    
    draw.rounded_rectangle([140, 120, 1780, 910], radius=20, fill=CARD_BG, outline=ACCENT_GREEN, width=3)
    draw.text((200, 170), "¡Excelente trabajo! Has completado la Lección 2", font=FONT_TITLE, fill=TEXT_WHITE)
    draw.text((200, 235), "Ahora ya sabes cómo organizar texto con estructura profesional:", font=FONT_SUBTITLE, fill=TEXT_MUTED)
    
    checks = [
        ("[OK] Anatomía de Elementos", "Apertura <etiqueta>, contenido visible y cierre con barra </etiqueta>."),
        ("[OK] Jerarquía con h1 a h6", "h1 para el título principal, h2 y h3 para secciones ordenadas."),
        ("[OK] Párrafos Claros con <p>", "El navegador necesita <p> para separar bloques de lectura sin colapsar.")
    ]
    y = 310
    for title, desc in checks:
        draw.rounded_rectangle([200, y, 1720, y + 110], radius=12, fill=(20, 28, 45), outline=(52, 211, 153), width=1)
        draw.text((240, y + 20), title, font=FONT_HEADING, fill=ACCENT_GREEN)
        draw.text((240, y + 65), desc, font=FONT_BODY, fill=TEXT_WHITE)
        y += 135
        
    draw.rounded_rectangle([200, 740, 1720, 870], radius=14, fill=(15, 35, 55), outline=ACCENT_CYAN, width=2)
    draw.text((240, 765), "PROXIMA LECCION (Lección 3 de 10):", font=FONT_BODY_BOLD, fill=ACCENT_AMBER)
    draw.text((240, 805), "Atributos y enlaces (<a>): conectando tu página con el resto de internet", font=FONT_HEADING, fill=TEXT_WHITE)
    
    draw_lower_third(draw, "04:55 - 05:15", "Resumen y Próxima Lección",
                     '"En la Lección 3 descubriremos los atributos y crearemos enlaces interactivos con la etiqueta a..."',
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
    
    # 4.1: h1 title (15s)
    img_41 = create_scene_4_frame(
        step_title="1. Escribiendo el título principal <h1>",
        html_lines=["<h1>Mi Diario Digital</h1>"],
        res_items=[("h1", "Mi Diario Digital")],
        cursor_pos=(335, 125),
        run_clicked=True,
        elapsed_str="03:30",
        progress_pct=0.67
    )
    p_41 = os.path.join(CLIPS_DIR, "sc4_1.mp4")
    render_clip_from_image(img_41, 15, p_41)
    sub_clips.append(p_41)
    
    # 4.2: h2 and paragraph (18s)
    img_42 = create_scene_4_frame(
        step_title="2. Agregando subtítulo <h2> y párrafo <p>",
        html_lines=[
            "<h1>Mi Diario Digital</h1>",
            "<h2>Sobre mí</h2>",
            "<p>Hola, estoy aprendiendo a crear páginas web desde cero.</p>"
        ],
        res_items=[
            ("h1", "Mi Diario Digital"),
            ("h2", "Sobre mí"),
            ("p", "Hola, estoy aprendiendo a crear páginas web desde cero.")
        ],
        cursor_pos=(335, 125),
        run_clicked=True,
        elapsed_str="03:48",
        progress_pct=0.73
    )
    p_42 = os.path.join(CLIPS_DIR, "sc4_2.mp4")
    render_clip_from_image(img_42, 18, p_42)
    sub_clips.append(p_42)
    
    # 4.3: h3 and second paragraph (17s)
    img_43 = create_scene_4_frame(
        step_title="3. Agregando subsección <h3> y segundo párrafo",
        html_lines=[
            "<h1>Mi Diario Digital</h1>",
            "<h2>Sobre mí</h2>",
            "<p>Hola, estoy aprendiendo a crear páginas web desde cero.</p>",
            "<h3>Mis metas</h3>",
            "<p>Quiero diseñar mi propio sitio web este mes.</p>"
        ],
        res_items=[
            ("h1", "Mi Diario Digital"),
            ("h2", "Sobre mí"),
            ("p", "Hola, estoy aprendiendo a crear páginas web desde cero."),
            ("h3", "Mis metas"),
            ("p", "Quiero diseñar mi propio sitio web este mes.")
        ],
        cursor_pos=(335, 125),
        run_clicked=True,
        elapsed_str="04:05",
        progress_pct=0.78
    )
    p_43 = os.path.join(CLIPS_DIR, "sc4_3.mp4")
    render_clip_from_image(img_43, 17, p_43)
    sub_clips.append(p_43)
    
    # 4.4: Completed hierarchy showcase (10s)
    img_44 = create_scene_4_frame(
        step_title="4. ¡Estructura HTML limpia, ordenada y completa!",
        html_lines=[
            "<h1>Mi Diario Digital</h1>",
            "<h2>Sobre mí</h2>",
            "<p>Hola, estoy aprendiendo a crear páginas web desde cero.</p>",
            "<h3>Mis metas</h3>",
            "<p>Quiero diseñar mi propio sitio web este mes.</p>"
        ],
        res_items=[
            ("h1", "Mi Diario Digital"),
            ("h2", "Sobre mí"),
            ("p", "Hola, estoy aprendiendo a crear páginas web desde cero."),
            ("h3", "Mis metas"),
            ("p", "Quiero diseñar mi propio sitio web este mes.")
        ],
        cursor_pos=None,
        run_clicked=False,
        elapsed_str="04:15",
        progress_pct=0.81
    )
    p_44 = os.path.join(CLIPS_DIR, "sc4_4.mp4")
    render_clip_from_image(img_44, 10, p_44)
    sub_clips.append(p_44)
    
    list_txt = os.path.join(CLIPS_DIR, "sc4_list.txt")
    with open(list_txt, "w") as f:
        for sc in sub_clips:
            f.write(f"file '{os.path.basename(sc)}'\n")
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", list_txt, "-c", "copy", output_path],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    print("=== Generador de Video Base para Lección 2 (5:15 min) ===")
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
        
    final_output = os.path.join(OUTPUT_DIR, "leccion-02-ejecucion-5min.mp4")
    cmd_master = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", master_list,
        "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
        "-c:v", "copy", "-c:a", "aac", "-shortest", final_output
    ]
    subprocess.run(cmd_master, check=True)
    dur_sec = 50 + 75 + 75 + 60 + 35 + 20
    print(f"\n✅ Video Lección 2 generado: {final_output}")
    print(f"⏱️ Duración: {dur_sec} segundos ({dur_sec//60}:{dur_sec%60:02d} min)")
    print(f"⚡ Tiempo: {time.time() - t_start:.2f} s")

if __name__ == "__main__":
    main()
