import docx
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=60, bottom=60, left=100, right=100):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}>'
                      f'<w:top w:w="{top}" w:type="dxa"/>'
                      f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
                      f'<w:left w:w="{left}" w:type="dxa"/>'
                      f'<w:right w:w="{right}" w:type="dxa"/>'
                      f'</w:tcMar>')
    tcPr.append(tcMar)

def set_table_borders(table, color="B0C4DE", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:left w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'  <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:insideV w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def build_course_plan_docx(output_path):
    doc = docx.Document()
    
    # Page setup - A4
    for section in doc.sections:
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)
        section.top_margin = Cm(2.0)
        section.bottom_margin = Cm(2.0)
        section.left_margin = Cm(2.0)
        section.right_margin = Cm(2.0)
        
    # Institutional Header
    p_inst = doc.add_paragraph()
    p_inst.paragraph_format.space_before = Pt(0)
    p_inst.paragraph_format.space_after = Pt(2)
    p_inst.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_inst = p_inst.add_run("UNIVERSIDAD PERUANA DE CIENCIAS APLICADAS")
    r_inst.font.name = "Calibri"
    r_inst.font.size = Pt(11)
    r_inst.font.bold = True
    r_inst.font.color.rgb = RGBColor(0, 51, 102)
    
    p_fac = doc.add_paragraph()
    p_fac.paragraph_format.space_before = Pt(0)
    p_fac.paragraph_format.space_after = Pt(2)
    p_fac.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_fac = p_fac.add_run("FACULTAD DE INGENIERÍA | CARRERA DE INGENIERÍA DE SOFTWARE")
    r_fac.font.name = "Calibri"
    r_fac.font.size = Pt(9.5)
    r_fac.font.color.rgb = RGBColor(80, 80, 80)
    
    p_course = doc.add_paragraph()
    p_course.paragraph_format.space_before = Pt(0)
    p_course.paragraph_format.space_after = Pt(12)
    p_course.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_course = p_course.add_run("1ASI0730 - Aplicaciones Web  |  NRC: 8093  |  Periodo Académico: 2026-20\nDocente: Bautista Ubillús, Efraín Ricardo")
    r_course.font.name = "Calibri"
    r_course.font.size = Pt(9)
    r_course.font.color.rgb = RGBColor(100, 100, 100)
    
    # Document Title
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(6)
    p_title.paragraph_format.space_after = Pt(4)
    p_title.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("Plan de Curso: Fundamentos de Desarrollo Web")
    r_title.font.name = "Calibri"
    r_title.font.size = Pt(17)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(0, 51, 102)
    
    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(14)
    p_sub.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("Iniciativa de Responsabilidad Social Universitaria para Estudiantes Escolares")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(11)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(70, 70, 70)
    
    # Metadata Table
    meta_table = doc.add_table(rows=2, cols=4)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(meta_table, color="1B365D", sz="6")
    
    meta_data = [
        [("Nombre de Startup:", True), ("TechnoLoad", False), ("Nombre de Producto:", True), ("TechFlow", False)],
        [("Organización GitHub:", True), ("TechnoLoad-TechFlow", False), ("Team Leader:", True), ("Castillo Guevara, Mathias Alejandro", False)]
    ]
    
    col_widths_meta = [Cm(3.8), Cm(4.7), Cm(3.8), Cm(4.7)]
    for r_idx, row in enumerate(meta_table.rows):
        for c_idx, cell in enumerate(row.cells):
            cell.width = col_widths_meta[c_idx]
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
            label_text, is_bold = meta_data[r_idx][c_idx]
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            if is_bold:
                set_cell_background(cell, "EAEFF5")
                p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
                r = p.add_run(label_text)
                r.font.name = "Calibri"
                r.font.size = Pt(9.5)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0, 51, 102)
            else:
                p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
                r = p.add_run(label_text)
                r.font.name = "Calibri"
                r.font.size = Pt(9.5)
                r.font.bold = False
                r.font.color.rgb = RGBColor(20, 20, 20)
                
    doc.add_paragraph().paragraph_format.space_after = Pt(12)
    
    # Section 1: Resumen
    p_sec1 = doc.add_paragraph()
    p_sec1.paragraph_format.space_before = Pt(10)
    p_sec1.paragraph_format.space_after = Pt(4)
    r_s1 = p_sec1.add_run("1. Resumen Ejecutivo del Curso")
    r_s1.font.name = "Calibri"
    r_s1.font.size = Pt(13)
    r_s1.font.bold = True
    r_s1.font.color.rgb = RGBColor(0, 51, 102)
    
    p_desc = doc.add_paragraph()
    p_desc.paragraph_format.space_after = Pt(8)
    p_desc.paragraph_format.line_spacing = 1.15
    r_d = p_desc.add_run(
        "El presente curso de Fundamentos de Desarrollo Web está diseñado como una intervención educativa de alto impacto "
        "para acercar la programación web a adolescentes escolares de 12 a 17 años en el Perú y Latinoamérica. "
        "Estructurado en 10 lecciones micro-learning de 5 minutos cada una (duración total: 50 minutos), "
        "el programa elimina completamente las barreras de entrada tecnológica: no requiere instalación de software, "
        "ni configuración de compiladores, ni registro previo obligatorio. Todo el trabajo se realiza de forma 100% interactiva "
        "en el editor en línea JSFiddle directamente desde el navegador web."
    )
    r_d.font.name = "Calibri"
    r_d.font.size = Pt(9.5)
    r_d.font.color.rgb = RGBColor(40, 40, 40)
    
    # Features List
    features = [
        ("Duración total:", " 50 minutos (10 lecciones prácticas de 5 minutos cada una)."),
        ("Público objetivo:", " Estudiantes escolares de 12 a 17 años sin experiencia previa en tecnología."),
        ("Prerrequisitos:", " Ninguno. Solo acceso a un navegador web (Chrome, Firefox, Edge o Safari)."),
        ("Herramienta en línea seleccionada:", " JSFiddle (https://jsfiddle.net/) — entorno web instantáneo con previsualización en tiempo real."),
        ("Repositorio institucional en GitHub:", " https://github.com/TechnoLoad-TechFlow/webdev-course-technoload")
    ]
    for feat_k, feat_v in features:
        p_f = doc.add_paragraph()
        p_f.paragraph_format.space_before = Pt(1)
        p_f.paragraph_format.space_after = Pt(2)
        p_f.paragraph_format.left_indent = Cm(0.8)
        rfk = p_f.add_run(f"• {feat_k}")
        rfk.font.name = "Calibri"
        rfk.font.size = Pt(9.5)
        rfk.font.bold = True
        rfk.font.color.rgb = RGBColor(0, 51, 102)
        rfv = p_f.add_run(feat_v)
        rfv.font.name = "Calibri"
        rfv.font.size = Pt(9.5)
        rfv.font.color.rgb = RGBColor(40, 40, 40)
        
    doc.add_paragraph().paragraph_format.space_after = Pt(12)
    
    # Section 2: Secuencia de Lecciones
    p_sec2 = doc.add_paragraph()
    p_sec2.paragraph_format.space_before = Pt(10)
    p_sec2.paragraph_format.space_after = Pt(6)
    r_s2 = p_sec2.add_run("2. Secuencia Curricular y Contenidos de Aprendizaje")
    r_s2.font.name = "Calibri"
    r_s2.font.size = Pt(13)
    r_s2.font.bold = True
    r_s2.font.color.rgb = RGBColor(0, 51, 102)
    
    lessons = [
        ("Lección 01", "¿Qué es el desarrollo web? Tu primer vistazo a JSFiddle",
         "Aprende qué es un sitio web, la sinergia entre HTML (contenido) y CSS (diseño), y conoce el entorno en línea JSFiddle.",
         "Sitio web = Estructura (HTML) + Estilo (CSS). No requiere registro ni descargas.",
         "Castillo Guevara, Mathias Alejandro"),
        ("Lección 02", "Tu primera página HTML: etiquetas y estructura básica",
         "Descubre qué son las etiquetas de apertura y cierre, jerarquía de encabezados (<h1> a <h3>) y párrafos (<p>).",
         "Toda etiqueta abierta debe cerrarse correctamente. <h1> es el título principal.",
         "Castillo Guevara, Mathias Alejandro"),
        ("Lección 03", "Atributos y enlaces: conectando páginas web",
         "Aprende a enriquecer etiquetas con atributos y crea enlaces navegables usando <a> con href y target=\"_blank\".",
         "href indica el destino del enlace y target=\"_blank\" abre en una nueva pestaña.",
         "Castillo Guevara, Mathias Alejandro"),
        ("Lección 04", "Imágenes y listas: páginas más visuales y ordenadas",
         "Inserta imágenes con <img> (src, alt) y organiza información en listas con viñetas (<ul>) y numeradas (<ol>).",
         "El atributo alt mejora la accesibilidad. Cada ítem de lista se define con <li>.",
         "Gutiérrez Lizarbe, Wilmer Sebastián"),
        ("Lección 05", "Introducción a CSS: selectores y reglas de estilo",
         "Comprende la sintaxis de una regla CSS: selector, propiedades, valores entre llaves y terminación en punto y coma.",
         "Sintaxis: selector { propiedad: valor; }. El punto y coma es imprescindible.",
         "Gutiérrez Lizarbe, Wilmer Sebastián"),
        ("Lección 06", "Colores y tipografía: personalidad para tu sitio web",
         "Personaliza el color de fuente, color de fondo (background-color) y familias tipográficas manteniendo contraste.",
         "Mantén contraste alto entre fondo y texto para garantizar legibilidad.",
         "Gutiérrez Lizarbe, Wilmer Sebastián"),
        ("Lección 07", "Espaciado, bordes y centrado: diseño limpio en CSS",
         "Aplica el modelo de caja: margen exterior (margin), relleno interior (padding), bordes redondeados y alineación centrada.",
         "padding es espacio interno; margin es espacio externo; border-radius redondea esquinas.",
         "Tantalean Granda, Nicolas"),
        ("Lección 08", "Proyecto Final (Parte 1): Estructura HTML de tu tarjeta de perfil",
         "Construye la arquitectura semántica de una tarjeta de perfil personal: contenedor principal, foto, bio y enlaces sociales.",
         "Usa contenedores <div class=\"tarjeta\"> para modularizar y agrupar componentes.",
         "Tantalean Granda, Nicolas"),
        ("Lección 09", "Proyecto Final (Parte 2): Estilizando tu tarjeta con CSS moderno",
         "Aplica estilos a la tarjeta de perfil: centrado con márgenes automáticos, foto circular, sombras y botones estilizados.",
         "border-radius: 50% para imagen circular; box-shadow para profundidad visual moderna.",
         "Diaz Caruzo, Edgar Daniel"),
        ("Lección 10", "Errores comunes, recomendaciones y próximos pasos",
         "Identifica y soluciona los errores más frecuentes al iniciar en web (etiquetas sin cerrar, comas por puntos y comas) y guía de ruta.",
         "Revisa la consola del navegador y consulta recursos gratuitos como MDN Web Docs.",
         "Diaz Caruzo, Edgar Daniel")
    ]
    
    les_table = doc.add_table(rows=1 + len(lessons), cols=4)
    les_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(les_table, color="B0C4DE", sz="4")
    
    les_headers = ["Lección", "Tema y Objetivos", "Concepto Clave", "Responsable"]
    les_widths = [Cm(2.2), Cm(6.5), Cm(4.8), Cm(3.5)]
    
    for c_idx, title in enumerate(les_headers):
        cell = les_table.rows[0].cells[c_idx]
        cell.width = les_widths[c_idx]
        set_cell_background(cell, "1B365D")
        set_cell_margins(cell, top=60, bottom=60, left=60, right=60)
        p = cell.paragraphs[0]
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(title)
        r.font.name = "Calibri"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    for l_idx, (num, topic, desc, key, resp) in enumerate(lessons):
        row_cells = les_table.rows[1 + l_idx].cells
        bg_col = "F7FAFC" if l_idx % 2 == 1 else "FFFFFF"
        for c_idx, cell in enumerate(row_cells):
            cell.width = les_widths[c_idx]
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            set_cell_background(cell, bg_col)
            set_cell_margins(cell, top=40, bottom=40, left=50, right=50)
            
        # Col 0: Num
        p0 = row_cells[0].paragraphs[0]
        p0.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r0 = p0.add_run(num)
        r0.font.name = "Calibri"
        r0.font.size = Pt(8)
        r0.font.bold = True
        r0.font.color.rgb = RGBColor(0, 51, 102)
        
        # Col 1: Topic + Desc
        p1 = row_cells[1].paragraphs[0]
        p1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r1_t = p1.add_run(topic + "\n")
        r1_t.font.name = "Calibri"
        r1_t.font.size = Pt(8)
        r1_t.font.bold = True
        r1_t.font.color.rgb = RGBColor(20, 20, 20)
        r1_d = p1.add_run(desc)
        r1_d.font.name = "Calibri"
        r1_d.font.size = Pt(7.5)
        r1_d.font.color.rgb = RGBColor(60, 60, 60)
        
        # Col 2: Key concept
        p2 = row_cells[2].paragraphs[0]
        p2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r2 = p2.add_run(key)
        r2.font.name = "Calibri"
        r2.font.size = Pt(7.5)
        r2.font.color.rgb = RGBColor(40, 40, 40)
        
        # Col 3: Responsible
        p3 = row_cells[3].paragraphs[0]
        p3.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r3 = p3.add_run(resp)
        r3.font.name = "Calibri"
        r3.font.size = Pt(7.5)
        r3.font.italic = True
        r3.font.color.rgb = RGBColor(0, 51, 102)

    doc.add_paragraph().paragraph_format.space_after = Pt(12)
    
    # Section 3: Datos del Equipo y Startup
    p_sec3 = doc.add_paragraph()
    p_sec3.paragraph_format.space_before = Pt(10)
    p_sec3.paragraph_format.space_after = Pt(4)
    r_s3 = p_sec3.add_run("3. Equipo de Trabajo y Responsabilidades")
    r_s3.font.name = "Calibri"
    r_s3.font.size = Pt(13)
    r_s3.font.bold = True
    r_s3.font.color.rgb = RGBColor(0, 51, 102)
    
    team_members = [
        ("Castillo Guevara, Mathias Alejandro", "U202323911", "Team Leader / Líder de Proyecto", "Lecciones 01, 02 y 03"),
        ("Gutiérrez Lizarbe, Wilmer Sebastián", "U202410783", "Desarrollador Web & Instructor de Estilos", "Lecciones 04, 05 y 06"),
        ("Tantalean Granda, Nicolas", "U202412044", "Desarrollador Web & Editor Multimedia", "Lecciones 07 y 08"),
        ("Diaz Caruzo, Edgar Daniel", "U202410728", "Desarrollador Web & Control de Calidad", "Lecciones 09 y 10")
    ]
    
    t_table = doc.add_table(rows=1 + len(team_members), cols=4)
    t_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_table, color="B0C4DE", sz="4")
    
    t_headers = ["Integrante", "Código UPC", "Rol Asignado", "Lecciones a Cargo"]
    t_widths = [Cm(5.0), Cm(2.8), Cm(5.2), Cm(4.0)]
    
    for c_idx, title in enumerate(t_headers):
        cell = t_table.rows[0].cells[c_idx]
        cell.width = t_widths[c_idx]
        set_cell_background(cell, "1B365D")
        set_cell_margins(cell, top=60, bottom=60, left=60, right=60)
        p = cell.paragraphs[0]
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(title)
        r.font.name = "Calibri"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    for m_idx, (name, code, role, less) in enumerate(team_members):
        row_cells = t_table.rows[1 + m_idx].cells
        bg_col = "F7FAFC" if m_idx % 2 == 1 else "FFFFFF"
        for c_idx, cell in enumerate(row_cells):
            cell.width = t_widths[c_idx]
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            set_cell_background(cell, bg_col)
            set_cell_margins(cell, top=40, bottom=40, left=50, right=50)
            
        p0 = row_cells[0].paragraphs[0]
        r0 = p0.add_run(name)
        r0.font.name = "Calibri"
        r0.font.size = Pt(8)
        r0.font.bold = True
        
        p1 = row_cells[1].paragraphs[0]
        p1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r1 = p1.add_run(code)
        r1.font.name = "Calibri"
        r1.font.size = Pt(8)
        
        p2 = row_cells[2].paragraphs[0]
        r2 = p2.add_run(role)
        r2.font.name = "Calibri"
        r2.font.size = Pt(8)
        
        p3 = row_cells[3].paragraphs[0]
        p3.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r3 = p3.add_run(less)
        r3.font.name = "Calibri"
        r3.font.size = Pt(8)
        r3.font.bold = True
        r3.font.color.rgb = RGBColor(0, 51, 102)

    doc.save(output_path)
    print(f"Plan de Curso DOCX generado en: {output_path}")

if __name__ == "__main__":
    docx_file = "upc-pre-202620-1asi0730-8093-technoload-course-plan.docx"
    build_course_plan_docx(docx_file)
