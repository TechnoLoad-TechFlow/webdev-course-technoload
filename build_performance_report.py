import docx
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_table_black_borders(table):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="single" w:sz="6" w:space="0" w:color="000000"/>'
        f'  <w:bottom w:val="single" w:sz="6" w:space="0" w:color="000000"/>'
        f'  <w:left w:val="single" w:sz="6" w:space="0" w:color="000000"/>'
        f'  <w:right w:val="single" w:sz="6" w:space="0" w:color="000000"/>'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        f'  <w:insideV w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def set_cell_margins(cell, top=30, bottom=30, left=50, right=50):
    """Set inner cell padding in dxa (1 pt = 20 dxa)."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}>'
                      f'<w:top w:w="{top}" w:type="dxa"/>'
                      f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
                      f'<w:left w:w="{left}" w:type="dxa"/>'
                      f'<w:right w:w="{right}" w:type="dxa"/>'
                      f'</w:tcMar>')
    tcPr.append(tcMar)

def create_report(output_path):
    doc = docx.Document()
    
    # Page setup - A4 with 1.8 cm margins to fit on 1 single page cleanly
    section = doc.sections[0]
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(1.8)
    section.bottom_margin = Cm(1.8)
    section.left_margin = Cm(1.8)
    section.right_margin = Cm(1.8)
    
    students = [
        {
            "item": "1",
            "name": "Castillo Guevara,\nMathias Alejandro",
            "grade": "20",
            "tasks": [
                "Coordinación general del proyecto y gestión del repositorio en GitHub.",
                "Definición de la estructura pedagógica del curso (10 lecciones de 5 min).",
                "Redacción de guiones y código de práctica para las Lecciones 1, 2 y 3.",
                "Grabación y locución en video de las Lecciones 1, 2 y 3 en JSFiddle.",
                "Elaboración y consolidación del Plan de Curso y del Informe de Participación."
            ]
        },
        {
            "item": "2",
            "name": "Gutiérrez Lizarbe,\nWilmer Sebastián",
            "grade": "20",
            "tasks": [
                "Configuración y gestión de colaboradores en la organización de GitHub.",
                "Creación de plantillas iniciales (starter-files) en JSFiddle para CSS.",
                "Redacción de guiones y código de práctica para las Lecciones 4, 5 y 6.",
                "Grabación y locución técnica de las Lecciones 4, 5 y 6 en JSFiddle.",
                "Pruebas de compatibilidad y verificación en navegadores web."
            ]
        },
        {
            "item": "3",
            "name": "Tantalean Granda,\nNicolas",
            "grade": "20",
            "tasks": [
                "Diseño de la estructura de maquetación CSS (caja, espaciado y bordes).",
                "Redacción de guiones y código de práctica para las Lecciones 7 y 8.",
                "Grabación y locución técnica de las Lecciones 7 y 8 en JSFiddle.",
                "Postproducción audiovisual, sincronización de audio y renderizado en 1080p.",
                "Revisión y control de calidad de los archivos finales en GitHub."
            ]
        },
        {
            "item": "4",
            "name": "Diaz Caruzo,\nEdgar Daniel",
            "grade": "20",
            "tasks": [
                "Diseño y desarrollo del proyecto práctico integrador (tarjeta de perfil).",
                "Redacción de guiones y código de práctica para las Lecciones 9 y 10.",
                "Grabación y locución técnica de las Lecciones 9 y 10 en JSFiddle.",
                "Generación y maquetación de los documentos oficiales (.docx y .pdf).",
                "Control de calidad de redacción académica según directrices UPC (Anexo C)."
            ]
        }
    ]
    
    total_task_rows = sum(len(s["tasks"]) for s in students)
    # Total rows = Row 0 (Title) + Row 1 (Metadata 1) + Row 2 (Metadata 2) + Row 3 (Headers) + task_rows
    total_rows = 4 + total_task_rows
    
    table = doc.add_table(rows=total_rows, cols=8)
    set_table_black_borders(table)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # Column widths (Total width = 17.4 cm)
    col_widths = [
        Cm(0.9),  # Ítem
        Cm(3.5),  # Estudiante
        Cm(6.8),  # Responsabilidades
        Cm(1.2),  # Cumplió a tiempo
        Cm(1.3),  # cumplió a destiempo
        Cm(1.4),  # cumplió parcialmente
        Cm(1.0),  # no cumplió (Cero)
        Cm(1.3)   # Calificación asignada
    ]
    
    # Row 0: Participant Performance Report
    r0 = table.rows[0]
    r0.cells[0].merge(r0.cells[7])
    set_cell_margins(r0.cells[0], top=40, bottom=40, left=60, right=60)
    p0 = r0.cells[0].paragraphs[0]
    p0.paragraph_format.space_before = Pt(0)
    p0.paragraph_format.space_after = Pt(0)
    p0.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run0 = p0.add_run("Participant Performance Report")
    run0.font.name = "Calibri"
    run0.font.size = Pt(10)
    run0.font.bold = True
    run0.font.color.rgb = RGBColor(0, 0, 0)
    
    # Row 1: Nombre de Startup | TechnoLoad | Nombre de Producto | TechFlow
    r1 = table.rows[1]
    c1_0 = r1.cells[0].merge(r1.cells[1])
    c1_1 = r1.cells[2]
    c1_2 = r1.cells[3].merge(r1.cells[4])
    c1_3 = r1.cells[5].merge(r1.cells[7])
    
    meta_row1 = [
        (c1_0, "Nombre de Startup", True, WD_ALIGN_PARAGRAPH.LEFT),
        (c1_1, "TechnoLoad", False, WD_ALIGN_PARAGRAPH.LEFT),
        (c1_2, "Nombre de Producto", True, WD_ALIGN_PARAGRAPH.LEFT),
        (c1_3, "TechFlow", False, WD_ALIGN_PARAGRAPH.LEFT)
    ]
    for cell, txt, is_b, align in meta_row1:
        set_cell_margins(cell, top=30, bottom=30, left=50, right=50)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.alignment = align
        r = p.add_run(txt)
        r.font.name = "Calibri"
        r.font.size = Pt(9)
        r.font.bold = is_b
        r.font.color.rgb = RGBColor(0, 0, 0)
        
    # Row 2: Entrega | Trabajo Complementario - Responsabilidad Social | Team Leader | Castillo Guevara, Mathias Alejandro
    r2 = table.rows[2]
    c2_0 = r2.cells[0].merge(r2.cells[1])
    c2_1 = r2.cells[2]
    c2_2 = r2.cells[3].merge(r2.cells[4])
    c2_3 = r2.cells[5].merge(r2.cells[7])
    
    meta_row2 = [
        (c2_0, "Entrega", True, WD_ALIGN_PARAGRAPH.LEFT),
        (c2_1, "Trabajo Complementario - Responsabilidad Social", False, WD_ALIGN_PARAGRAPH.LEFT),
        (c2_2, "Team Leader", True, WD_ALIGN_PARAGRAPH.LEFT),
        (c2_3, "Castillo Guevara, Mathias Alejandro", False, WD_ALIGN_PARAGRAPH.LEFT)
    ]
    for cell, txt, is_b, align in meta_row2:
        set_cell_margins(cell, top=30, bottom=30, left=50, right=50)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.alignment = align
        r = p.add_run(txt)
        r.font.name = "Calibri"
        r.font.size = Pt(9)
        r.font.bold = is_b
        r.font.color.rgb = RGBColor(0, 0, 0)
        
    # Row 3: Headers
    headers = [
        "Ítem",
        "Estudiante",
        "Responsabilidades",
        "Cumplió\na tiempo",
        "cumplió a\ndestiempo",
        "cumplió\nparcialmente",
        "no\ncumplió\n(Cero)",
        "Calificación\nasignada\n(20 / 16 /\n13 / 07 / 0)"
    ]
    r3 = table.rows[3]
    for c_idx, h in enumerate(headers):
        cell = r3.cells[c_idx]
        cell.width = col_widths[c_idx]
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        set_cell_margins(cell, top=30, bottom=30, left=30, right=30)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = "Calibri"
        r.font.size = Pt(8)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0, 0, 0)
        
    # Data Rows
    current_row = 4
    for s_idx, student in enumerate(students):
        start_row = current_row
        num_tasks = len(student["tasks"])
        
        for t_idx, task_text in enumerate(student["tasks"]):
            row_cells = table.rows[current_row].cells
            for c_idx, cell in enumerate(row_cells):
                cell.width = col_widths[c_idx]
                cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                set_cell_margins(cell, top=25, bottom=25, left=35, right=35)
                
            # Col 0: Item
            p0 = row_cells[0].paragraphs[0]
            p0.paragraph_format.space_before = Pt(0)
            p0.paragraph_format.space_after = Pt(0)
            p0.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
            if t_idx == 0:
                r0 = p0.add_run(student["item"])
                r0.font.name = "Calibri"
                r0.font.size = Pt(8.5)
                r0.font.color.rgb = RGBColor(0, 0, 0)
                
            # Col 1: Student
            p1 = row_cells[1].paragraphs[0]
            p1.paragraph_format.space_before = Pt(0)
            p1.paragraph_format.space_after = Pt(0)
            p1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
            if t_idx == 0:
                r1 = p1.add_run(student["name"])
                r1.font.name = "Calibri"
                r1.font.size = Pt(8)
                r1.font.color.rgb = RGBColor(0, 0, 0)
                
            # Col 2: Task
            p2 = row_cells[2].paragraphs[0]
            p2.paragraph_format.space_before = Pt(0)
            p2.paragraph_format.space_after = Pt(0)
            p2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
            r2 = p2.add_run(task_text)
            r2.font.name = "Calibri"
            r2.font.size = Pt(8)
            r2.font.color.rgb = RGBColor(0, 0, 0)
            
            # Col 3: Cumplió a tiempo
            p3 = row_cells[3].paragraphs[0]
            p3.paragraph_format.space_before = Pt(0)
            p3.paragraph_format.space_after = Pt(0)
            p3.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r3 = p3.add_run("X")
            r3.font.name = "Calibri"
            r3.font.size = Pt(8.5)
            r3.font.color.rgb = RGBColor(0, 0, 0)
            
            # Col 4, 5, 6: Empty
            for empty_col in [4, 5, 6]:
                p_e = row_cells[empty_col].paragraphs[0]
                p_e.paragraph_format.space_before = Pt(0)
                p_e.paragraph_format.space_after = Pt(0)
                
            # Col 7: Calificación
            p7 = row_cells[7].paragraphs[0]
            p7.paragraph_format.space_before = Pt(0)
            p7.paragraph_format.space_after = Pt(0)
            p7.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
            if t_idx == 0:
                r7 = p7.add_run(student["grade"])
                r7.font.name = "Calibri"
                r7.font.size = Pt(9)
                r7.font.color.rgb = RGBColor(0, 0, 0)
                
            current_row += 1
            
        # Merge vertical cells
        if num_tasks > 1:
            table.rows[start_row].cells[0].merge(table.rows[start_row + num_tasks - 1].cells[0])
            table.rows[start_row].cells[1].merge(table.rows[start_row + num_tasks - 1].cells[1])
            table.rows[start_row].cells[7].merge(table.rows[start_row + num_tasks - 1].cells[7])

    doc.save(output_path)
    print(f"Reporte exacto guardado en: {output_path}")

if __name__ == "__main__":
    out_docx = "upc-pre-202620-1asi0730-8093-technoload-course-plan-performance.docx"
    create_report(out_docx)
