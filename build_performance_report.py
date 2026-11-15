import docx
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    """Set the background color of a table cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=60, bottom=60, left=100, right=100):
    """Set inner cell padding in dxa (1 pt = 20 dxa)."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}>'
                      f'<w:top w:w="{top}" w:type="dxa"/>'
                      f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
                      f'<w:left w:w="{left}" w:type="dxa"/>'
                      f'<w:right w:w="{right}" w:type="dxa"/>'
                      f'</w:tcMar>')
    tcPr.append(tcMar)

def set_table_borders(table, color="B0C4DE", sz="4", val="single"):
    """Set standard table borders."""
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

def build_performance_report_docx(output_path):
    doc = docx.Document()
    
    # Page setup - A4 with 1.6 cm margins for perfect 2-page fit
    for section in doc.sections:
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)
        section.top_margin = Cm(1.6)
        section.bottom_margin = Cm(1.6)
        section.left_margin = Cm(1.6)
        section.right_margin = Cm(1.6)
    
    # Header institution
    p_inst = doc.add_paragraph()
    p_inst.paragraph_format.space_before = Pt(0)
    p_inst.paragraph_format.space_after = Pt(1)
    p_inst.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_inst = p_inst.add_run("UNIVERSIDAD PERUANA DE CIENCIAS APLICADAS")
    run_inst.font.name = "Calibri"
    run_inst.font.size = Pt(11)
    run_inst.font.bold = True
    run_inst.font.color.rgb = RGBColor(0, 51, 102) # Navy
    
    p_fac = doc.add_paragraph()
    p_fac.paragraph_format.space_before = Pt(0)
    p_fac.paragraph_format.space_after = Pt(1)
    p_fac.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_fac = p_fac.add_run("FACULTAD DE INGENIERÍA | CARRERA DE INGENIERÍA DE SOFTWARE")
    run_fac.font.name = "Calibri"
    run_fac.font.size = Pt(9)
    run_fac.font.color.rgb = RGBColor(80, 80, 80)
    
    p_course = doc.add_paragraph()
    p_course.paragraph_format.space_before = Pt(0)
    p_course.paragraph_format.space_after = Pt(8)
    p_course.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_course = p_course.add_run("1ASI0730 - Aplicaciones Web  |  NRC: 8093  |  Periodo Académico: 2026-20  |  Docente: Bautista Ubillús, Efraín Ricardo")
    run_course.font.name = "Calibri"
    run_course.font.size = Pt(8.5)
    run_course.font.color.rgb = RGBColor(100, 100, 100)
    
    # Document Title
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(2)
    p_title.paragraph_format.space_after = Pt(2)
    p_title.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_title = p_title.add_run("Participant Performance Report")
    run_title.font.name = "Calibri"
    run_title.font.size = Pt(15)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(0, 51, 102)
    
    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(8)
    p_sub.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_sub = p_sub.add_run("Trabajo Complementario - Responsabilidad Social (Anexo B)")
    run_sub.font.name = "Calibri"
    run_sub.font.size = Pt(10)
    run_sub.font.italic = True
    run_sub.font.color.rgb = RGBColor(70, 70, 70)
    
    # Metadata Table (Anexo B)
    meta_table = doc.add_table(rows=2, cols=4)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(meta_table, color="1B365D", sz="6")
    
    meta_data = [
        [("Nombre de Startup:", True), ("TechnoLoad", False), ("Nombre de Producto:", True), ("TechFlow", False)],
        [("Entrega:", True), ("Trabajo Complementario - Responsabilidad Social", False), ("Team Leader:", True), ("Castillo Guevara, Mathias Alejandro", False)]
    ]
    
    col_widths_meta = [Cm(3.8), Cm(5.1), Cm(3.8), Cm(5.1)]
    for r_idx, row in enumerate(meta_table.rows):
        for c_idx, cell in enumerate(row.cells):
            cell.width = col_widths_meta[c_idx]
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            set_cell_margins(cell, top=60, bottom=60, left=100, right=100)
            label_text, is_bold = meta_data[r_idx][c_idx]
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            if is_bold:
                set_cell_background(cell, "EAEFF5")
                p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
                r = p.add_run(label_text)
                r.font.name = "Calibri"
                r.font.size = Pt(9)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0, 51, 102)
            else:
                p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
                r = p.add_run(label_text)
                r.font.name = "Calibri"
                r.font.size = Pt(9)
                r.font.bold = False
                r.font.color.rgb = RGBColor(20, 20, 20)
                
    p_sep = doc.add_paragraph()
    p_sep.paragraph_format.space_before = Pt(0)
    p_sep.paragraph_format.space_after = Pt(6)
    
    # Team members & responsibilities
    students = [
        {
            "item": "1",
            "name": "Castillo Guevara, Mathias Alejandro",
            "code": "U202323911",
            "role": "Team Leader / Líder de Proyecto",
            "grade": "20",
            "tasks": [
                "Coordinación general del proyecto de responsabilidad social y planificación de hitos de entrega del equipo.",
                "Creación, administración y control de versiones del repositorio público en GitHub (TechnoLoad-TechFlow/webdev-course-technoload).",
                "Diseño pedagógico y curricular del curso de 10 lecciones (5 min c/u) enfocado en escolares de 12 a 17 años sin conocimientos previos.",
                "Redacción técnica de los guiones didácticos y código base para las Lecciones 01, 02 y 03 (Fundamentos, estructura HTML y enlaces).",
                "Grabación y locución técnica de los videos prácticos de las Lecciones 01, 02 y 03 en el entorno en línea JSFiddle.",
                "Consolidación, revisión de estilo formal y elaboración del Documento de Plan de Curso (Course Plan) y del Informe de Desempeño (Performance Report)."
            ]
        },
        {
            "item": "2",
            "name": "Gutiérrez Lizarbe, Wilmer Sebastián",
            "code": "U202410783",
            "role": "Desarrollador Web & Instructor de Estilos",
            "grade": "20",
            "tasks": [
                "Gestión de accesos y permisos de colaboradores en la organización de GitHub para todo el equipo de trabajo.",
                "Creación de plantillas iniciales (starter-files) y entornos de prueba en JSFiddle para las sesiones prácticas de estilos CSS.",
                "Redacción de guiones didácticos y código base para las Lecciones 04, 05 y 06 (Imágenes, listas HTML, selectores CSS, tipografía y colores).",
                "Grabación y locución instruccional de las Lecciones 04, 05 y 06 en JSFiddle sin requerir instalaciones locales.",
                "Pruebas de compatibilidad cross-browser (Chrome, Firefox, Edge) y verificación de simplicidad de interfaz para principiantes."
            ]
        },
        {
            "item": "3",
            "name": "Tantalean Granda, Nicolas",
            "code": "U202412044",
            "role": "Desarrollador Web & Editor Multimedia",
            "grade": "20",
            "tasks": [
                "Diseño de la estructura de maquetación moderna con CSS (modelo de caja, espaciado con padding/margin, bordes redondeados y centrado).",
                "Elaboración de guiones técnicos y código terminado de las Lecciones 07 y 08 (Espaciado, bordes y estructura inicial de la tarjeta de perfil).",
                "Grabación audiovisual y locución instruccional de las Lecciones 07 y 08 demostrando técnicas de diseño web responsivo.",
                "Postproducción audiovisual y edición multimedia: masterización de audio, eliminación de ruido de fondo, normalización de sonoridad (-14 LUFS).",
                "Renderizado de video a resolución Full HD (1080p a 30 fps) y verificación de accesibilidad visual y contraste cromático."
            ]
        },
        {
            "item": "4",
            "name": "Diaz Caruzo, Edgar Daniel",
            "code": "U202410728",
            "role": "Desarrollador Web & Control de Calidad",
            "grade": "20",
            "tasks": [
                "Diseño e implementación del proyecto práctico integrador final: Tarjeta interactiva de perfil personal y portafolio escolar.",
                "Redacción de guiones didácticos y desarrollo de código terminado para las Lecciones 09 y 10 (Estilizado de tarjeta, resolución de errores frecuentes y cuestionario).",
                "Grabación y locución instruccional de las Lecciones 09 y 10 en el editor en línea JSFiddle.",
                "Maquetación y formateo de los documentos oficiales de entrega en formatos Word (.docx) y PDF (.pdf) conforme al Anexo B.",
                "Auditoría y control de calidad de redacción académica UPC (Anexo C), verificando estricto rigor léxico y ausencia de anglicismos."
            ]
        }
    ]
    
    # Calculate total table rows needed: 1 header + sum(len(tasks) for student)
    total_data_rows = sum(len(s["tasks"]) for s in students)
    table = doc.add_table(rows=1 + total_data_rows, cols=8)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table, color="B0C4DE", sz="4")
    
    headers = [
        "Ítem",
        "Estudiante",
        "Responsabilidades",
        "Cumplió a tiempo",
        "cumplió a destiempo",
        "cumplió parcialmente",
        "no cumplió (Cero)",
        "Calificación asignada (20 / 16 / 13 / 07 / 0)"
    ]
    
    col_widths = [
        Cm(0.9),  # Ítem
        Cm(4.0),  # Estudiante
        Cm(6.5),  # Responsabilidades
        Cm(1.2),  # Cumplió a tiempo
        Cm(1.2),  # a destiempo
        Cm(1.3),  # parcialmente
        Cm(1.1),  # no cumplió
        Cm(1.6)   # Calificación
    ]
    
    # Style Header Row
    hdr_cells = table.rows[0].cells
    for i, title in enumerate(headers):
        hdr_cells[i].width = col_widths[i]
        hdr_cells[i].vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        set_cell_background(hdr_cells[i], "1B365D")
        set_cell_margins(hdr_cells[i], top=50, bottom=50, left=45, right=45)
        p = hdr_cells[i].paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(title)
        run.font.name = "Calibri"
        run.font.size = Pt(7.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)
        
    current_row_idx = 1
    
    for s_idx, student in enumerate(students):
        num_tasks = len(student["tasks"])
        student_start_row = current_row_idx
        
        bg_color = "F7FAFC" if s_idx % 2 == 1 else "FFFFFF"
        
        for t_idx, task_text in enumerate(student["tasks"]):
            row_cells = table.rows[current_row_idx].cells
            for c_idx, cell in enumerate(row_cells):
                cell.width = col_widths[c_idx]
                cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                set_cell_margins(cell, top=30, bottom=30, left=40, right=40)
                set_cell_background(cell, bg_color)
                
            # Col 0: Item (only in first row of student)
            p0 = row_cells[0].paragraphs[0]
            p0.paragraph_format.space_before = Pt(0)
            p0.paragraph_format.space_after = Pt(0)
            p0.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
            if t_idx == 0:
                r0 = p0.add_run(student["item"])
                r0.font.name = "Calibri"
                r0.font.size = Pt(8.5)
                r0.font.bold = True
                r0.font.color.rgb = RGBColor(0, 51, 102)
                
            # Col 1: Student info (only in first row of student)
            p1 = row_cells[1].paragraphs[0]
            p1.paragraph_format.space_before = Pt(0)
            p1.paragraph_format.space_after = Pt(0)
            p1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
            if t_idx == 0:
                r1_name = p1.add_run(student["name"] + "\n")
                r1_name.font.name = "Calibri"
                r1_name.font.size = Pt(8)
                r1_name.font.bold = True
                r1_name.font.color.rgb = RGBColor(20, 20, 20)
                
                r1_code = p1.add_run(f"Código: {student['code']}\n")
                r1_code.font.name = "Calibri"
                r1_code.font.size = Pt(7.5)
                r1_code.font.color.rgb = RGBColor(70, 70, 70)
                
                r1_role = p1.add_run(f"Rol: {student['role']}")
                r1_role.font.name = "Calibri"
                r1_role.font.size = Pt(7)
                r1_role.font.italic = True
                r1_role.font.color.rgb = RGBColor(0, 51, 102)
                
            # Col 2: Task
            p2 = row_cells[2].paragraphs[0]
            p2.paragraph_format.space_before = Pt(0)
            p2.paragraph_format.space_after = Pt(0)
            p2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
            r2 = p2.add_run(f"• {task_text}")
            r2.font.name = "Calibri"
            r2.font.size = Pt(7.5)
            r2.font.color.rgb = RGBColor(30, 30, 30)
            
            # Col 3: Cumplió a tiempo (X)
            p3 = row_cells[3].paragraphs[0]
            p3.paragraph_format.space_before = Pt(0)
            p3.paragraph_format.space_after = Pt(0)
            p3.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r3 = p3.add_run("X")
            r3.font.name = "Calibri"
            r3.font.size = Pt(8.5)
            r3.font.bold = True
            r3.font.color.rgb = RGBColor(0, 100, 0) # Green check
            
            # Col 4, 5, 6: Empty
            for empty_col in [4, 5, 6]:
                p_empty = row_cells[empty_col].paragraphs[0]
                p_empty.paragraph_format.space_before = Pt(0)
                p_empty.paragraph_format.space_after = Pt(0)
                
            # Col 7: Calificación asignada (only in first row of student)
            p7 = row_cells[7].paragraphs[0]
            p7.paragraph_format.space_before = Pt(0)
            p7.paragraph_format.space_after = Pt(0)
            p7.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
            if t_idx == 0:
                r7 = p7.add_run(student["grade"])
                r7.font.name = "Calibri"
                r7.font.size = Pt(10)
                r7.font.bold = True
                r7.font.color.rgb = RGBColor(0, 51, 102)
                
            current_row_idx += 1
            
        # Merge cells for item, student and grade across student's task rows
        if num_tasks > 1:
            # Merge Col 0
            cell_0_start = table.rows[student_start_row].cells[0]
            cell_0_end = table.rows[student_start_row + num_tasks - 1].cells[0]
            cell_0_start.merge(cell_0_end)
            
            # Merge Col 1
            cell_1_start = table.rows[student_start_row].cells[1]
            cell_1_end = table.rows[student_start_row + num_tasks - 1].cells[1]
            cell_1_start.merge(cell_1_end)
            
            # Merge Col 7
            cell_7_start = table.rows[student_start_row].cells[7]
            cell_7_end = table.rows[student_start_row + num_tasks - 1].cells[7]
            cell_7_start.merge(cell_7_end)

    # Team Leader Declaration / Notes
    p_notes_title = doc.add_paragraph()
    p_notes_title.paragraph_format.space_before = Pt(6)
    p_notes_title.paragraph_format.space_after = Pt(2)
    run_nt = p_notes_title.add_run("Declaración de Conformidad del Coordinador (Team Leader)")
    run_nt.font.name = "Calibri"
    run_nt.font.size = Pt(9.5)
    run_nt.font.bold = True
    run_nt.font.color.rgb = RGBColor(0, 51, 102)
    
    p_decl = doc.add_paragraph()
    p_decl.paragraph_format.space_before = Pt(0)
    p_decl.paragraph_format.space_after = Pt(10)
    p_decl.paragraph_format.line_spacing = 1.1
    run_decl = p_decl.add_run(
        "En mi calidad de Team Leader del equipo TechnoLoad (producto TechFlow), certifico que todos los integrantes del grupo "
        "han cumplido a cabalidad, dentro de los plazos establecidos y con un alto nivel de rigor técnico y compromiso pedagógico, "
        "con cada una de las actividades asignadas para el Trabajo Complementario de Responsabilidad Social. "
        "Las 10 lecciones prácticas, sus respectivos guiones, los entornos en línea en JSFiddle y las grabaciones audiovisuales "
        "han sido verificadas y puestas a disposición de manera pública en la organización de GitHub del equipo. "
        "Por tanto, se asigna la calificación unánime de veinte (20) a todos los integrantes."
    )
    run_decl.font.name = "Calibri"
    run_decl.font.size = Pt(8)
    run_decl.font.color.rgb = RGBColor(50, 50, 50)
    
    # Signature Box Table
    sig_table = doc.add_table(rows=1, cols=2)
    sig_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    col_sig = [Cm(8.9), Cm(8.9)]
    for c_idx, cell in enumerate(sig_table.rows[0].cells):
        cell.width = col_sig[c_idx]
        set_cell_margins(cell, top=35, bottom=35, left=50, right=50)
        
    p_sig1 = sig_table.rows[0].cells[0].paragraphs[0]
    p_sig1.paragraph_format.space_before = Pt(0)
    p_sig1.paragraph_format.space_after = Pt(0)
    p_sig1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r_sig1 = p_sig1.add_run(
        "_________________________________________\n"
        "Castillo Guevara, Mathias Alejandro\n"
        "Team Leader - Código U202323911\n"
        "TechnoLoad / TechFlow"
    )
    r_sig1.font.name = "Calibri"
    r_sig1.font.size = Pt(8)
    r_sig1.font.color.rgb = RGBColor(50, 50, 50)
    
    p_sig2 = sig_table.rows[0].cells[1].paragraphs[0]
    p_sig2.paragraph_format.space_before = Pt(0)
    p_sig2.paragraph_format.space_after = Pt(0)
    p_sig2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_sig2 = p_sig2.add_run(
        "Lima, 15 de noviembre de 2026\n"
        "Universidad Peruana de Ciencias Aplicadas\n"
        "Facultad de Ingeniería\n"
        "Carrera de Ingeniería de Software"
    )
    r_sig2.font.name = "Calibri"
    r_sig2.font.size = Pt(8)
    r_sig2.font.color.rgb = RGBColor(80, 80, 80)
    
    doc.save(output_path)
    print(f"Documento DOCX generado exitosamente en: {output_path}")

if __name__ == "__main__":
    docx_file = "upc-pre-202620-1asi0730-8093-technoload-course-plan-performance.docx"
    build_performance_report_docx(docx_file)
