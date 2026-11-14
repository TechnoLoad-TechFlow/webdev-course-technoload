# Guía de Producción y Reparto para el Equipo (4 Estudiantes)

Esta guía organiza la grabación, edición y publicación de las **10 lecciones de 5 minutos** para que los **4 integrantes del grupo** trabajen de forma equilibrada, mantengan un estilo visual uniforme y cumplan con todos los criterios de la rúbrica de evaluación.

---

## 1. Distribución equitativa de responsabilidades

Como son **10 lecciones** y **4 estudiantes**, el trabajo se divide de forma justa combinando locución/grabación y tareas de postproducción:

| Integrante | Lecciones asignadas (Voz y grabación de pantalla) | Tiempo de video | Rol adicional en el proyecto |
|---|---|---|---|
| **Estudiante 1** | Lección 1, Lección 2, Lección 3 | 15 min | Creación de los Fiddles precargados (Lecciones 1–5) en JSFiddle |
| **Estudiante 2** | Lección 4, Lección 5, Lección 6 | 15 min | Creación de los Fiddles precargados (Lecciones 6–9) y formulario de entrega/cuestionario |
| **Estudiante 3** | Lección 7, Lección 8 | 10 min | Edición unificada de video (anotaciones en pantalla, transiciones, nivelación de audio) de Lecciones 1–5 |
| **Estudiante 4** | Lección 9, Lección 10 | 10 min | Edición unificada de Lecciones 6–10, subida a YouTube (No listado) y exportación de `course-plan.md` a PDF |

> **Importante sobre GitHub**: Cada integrante debe realizar **commits propios** desde su cuenta de GitHub en este repositorio (por ejemplo, confirmando sus guiones revisados, archivos de práctica o actualizaciones de `course-plan.md`), ya que la rúbrica exige evidenciar mediante commits los aportes de todos los miembros del equipo.

---

## 2. Reglas obligatorias antes de grabar

1. **Sin marcas ni referencias personales (Cero branding)**:
   - No muestren el nombre del equipo, universidad, curso ni sus nombres o fotos en los videos, ni en los comentarios del código fuente en JSFiddle.
   - Si usan un perfil de navegador para grabar, cierren marcadores personales, notificaciones y extensiones visibles.
2. **Solo editores en línea**:
   - Graben **únicamente** dentro de **JSFiddle** (`https://jsfiddle.net/`) en el navegador web. No abran VS Code, terminal ni archivos locales durante la grabación.
3. **Legibilidad en pantalla (Criterio C04)**:
   - Configura la resolución de grabación en **1920x1080 (1080p)** a 30 fps.
   - Aumenta el zoom del navegador en JSFiddle a **125% o 150%** para que el código se lea sin esfuerzo incluso desde un celular.
   - En JSFiddle, usa el layout clásico (**Settings → Layout → Classic**) o de columnas claras donde se vean bien **HTML**, **CSS** y **Result**.
4. **Audio nítido**:
   - Graba en un lugar silencioso, con micrófono o manos libres cerca de la boca.
   - Haz una prueba de 10 segundos antes de grabar cada lección para verificar que no haya ruido de fondo ni saturación.
5. **Ritmo de 5 minutos exactos**:
   - Cada guion está medido por bloques de tiempo (`[00:00 - 00:45]`, etc.) para durar alrededor de **5:00 minutos**.
   - Respeta las **pausas para la práctica** (5 segundos en pantalla con el texto *"Pausa el video e inténtalo en JSFiddle"*).

---

## 3. Flujo paso a paso para cada lección

1. **Preparar el Fiddle inicial**:
   - Abre [jsfiddle.net](https://jsfiddle.net/).
   - Copia el código de `starter-files/lesson-XX/` en los paneles HTML y CSS correspondientes.
   - Haz clic en **Save** y copia la URL generada (ese será el enlace precargado para los estudiantes).
2. **Grabar pantalla y narración en off**:
   - Sigue el guion `scripts/lesson-XX-script.md` bloque por bloque.
   - Escribe el código en vivo a ritmo pausado para que un estudiante de 12 a 17 años pueda seguirte.
   - Presiona **Run** cada vez que el guion lo indique para mostrar el resultado visual inmediato.
3. **Editar y añadir elementos visuales**:
   - Añade el **texto en pantalla** y las **anotaciones** (flechas o recuadros resaltando etiquetas/propiedades) indicados en cada sección `[En pantalla: ...]` del guion.
4. **Subir a YouTube**:
   - Visibilidad: **No listado** (*Unlisted*).
   - Título sugerido: `Curso Web desde Cero - Lección X: [Título de la lección]`.
   - En la **descripción del video**, pega el enlace directo al JSFiddle precargado de esa lección y el enlace al repositorio de GitHub.
5. **Actualizar el Plan de Curso**:
   - Reemplaza los enlaces `REEMPLAZAR-LECCION-X` en `course-plan.md` con las URLs reales de YouTube y JSFiddle.
