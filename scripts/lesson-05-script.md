# Guion Lección 5: Introducción a CSS: selectores y reglas de estilo

- **Duración objetivo**: 5:00 minutos
- **Responsable sugerido**: Estudiante 2
- **Herramienta en línea**: [JSFiddle](https://jsfiddle.net/)
- **Archivos asociados**: `starter-files/lesson-05/` y `completed-examples/lesson-05/`

---

## [00:00 - 00:40] Introducción
- **[En pantalla]**: Título: *"Lección 5: Introducción a CSS"*.
- **[Narración en off]**:
  > "¡Llegamos a la parte más creativa del curso: **CSS**! Si HTML era el esqueleto y los ladrillos de nuestra página, CSS (*Cascading Style Sheets*) es el diseño, los colores y la magia visual. Hoy aprenderás cómo se escribe una regla CSS y cómo elegir exactamente qué elemento quieres transformar."

## [00:40 - 02:00] Anatomía de una regla CSS
- **[En pantalla]**: Diagrama grande de la regla:
  ```css
  h1 {
    color: royalblue;
  }
  ```
  Con etiquetas señalando: `h1` = **Selector** | `{ }` = **Llaves** | `color` = **Propiedad** | `royalblue` = **Valor** | `;` = **Punto y coma**.
- **[Narración en off]**:
  > "Una regla en CSS siempre tiene la misma estructura, súper fácil de recordar. Primero va el **selector**, que le dice al navegador a quién vamos a pintar, por ejemplo todos los `h1`. Luego abrimos llaves `{ }`. Adentro escribimos qué queremos cambiar —eso es la **propiedad**, como `color`—, ponemos dos puntos `:`, el **valor** que queremos —como `royalblue`—, y cerramos la línea con punto y coma `;`. Sin ese punto y coma, CSS puede confundirse si pones varias reglas juntas."

## [02:00 - 03:40] Probando selectores de etiqueta y de clase en JSFiddle
- **[Acción en JSFiddle]**: Abrir `starter-files/lesson-05/`. Mostrar el HTML que tiene un `<h1>`, dos `<p>`, y uno de ellos con `class="destacado"`. En el panel **CSS**, escribir:
  ```css
  body {
    background-color: #f0f9ff;
  }

  h1 {
    color: #1d4ed8;
  }

  .destacado {
    color: #be123c;
  }
  ```
  Presionar **Run**.
- **[En pantalla]**: Anotación: *"`.destacado` con un punto adelante selecciona cualquier elemento con `class="destacado"`"*.
- **[Narración en off]**:
  > "En JSFiddle vamos directo al panel de **CSS**; JSFiddle ya lo conecta automáticamente con nuestro HTML. Si escribimos `body` y cambiamos su `background-color`, pintamos toda la página. Si ponemos `h1`, cambiamos el título. ¿Y si tengo dos párrafos pero solo quiero resaltar uno? En HTML le agregamos `class="destacado"`, y en CSS lo llamamos poniendo un punto adelante: `.destacado`. Presionamos **Run** y solo ese párrafo cambia de color."

## [03:40 - 04:30] Pausa interactiva
- **[En pantalla]**: Recuadro: *"Pausa el video — Cambia el color de `.destacado` a `green` y agrega una regla para `p` con `color: #334155;`"*
- **[Narración en off]**:
  > "Pausa el video y haz la prueba en tu JSFiddle: cambia el color de `.destacado` y crea una nueva regla para `p` que cambie el color de los párrafos normales."

## [04:30 - 05:00] Cierre
- **[En pantalla]**: Resumen: `selector { propiedad: valor; }` | `.clase` selecciona por clase.
- **[Narración en off]**:
  > "¡Buenísimo! Ya sabes escribir reglas CSS y usar selectores de etiqueta y de clase. En la Lección 6 vamos a explorar cómo combinar colores y tipos de letra para que tu página se vea profesional."
