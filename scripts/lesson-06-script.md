# Guion Lección 6: Colores y tipografía: personalidad para tu sitio web

- **Duración objetivo**: 5:00 minutos
- **Responsable sugerido**: Estudiante 2
- **Herramienta en línea**: [JSFiddle](https://jsfiddle.net/)
- **Archivos asociados**: `starter-files/lesson-06/` y `completed-examples/lesson-06/`

---

## [00:00 - 00:35] Introducción
- **[En pantalla]**: Título: *"Lección 6: Colores y Tipografía en CSS"*.
- **[Narración en off]**:
  > "¡Hola! Seguro notaste que todas las páginas que hicimos hasta ahora usan la misma letra clásica de periódico. Hoy vas a aprender a cambiar las fuentes, el tamaño del texto y a usar colores modernos para darle personalidad única a tu sitio."

## [00:35 - 02:00] Formas de escribir colores y contraste
- **[En pantalla]**: Tres ejemplos equivalentes:
  - Nombre: `tomato`
  - Hexadecimal: `#ff6347`
  - Consejo visual: *"Texto oscuro sobre fondo claro (o viceversa) para leer sin cansar la vista"*.
- **[Narración en off]**:
  > "En CSS puedes escribir colores con nombres en inglés como `tomato`, `navy` o `gold`, pero los diseñadores web usan casi siempre códigos **hexadecimales**, que empiezan con `#` seguido de seis caracteres, como `#1e293b`. Una regla de oro: cuida el **contraste**. Nunca pongas texto amarillo claro sobre fondo blanco porque nadie podrá leerlo."

## [02:00 - 03:45] Aplicando fuentes y tamaños en JSFiddle
- **[Acción en JSFiddle]**: Abrir `starter-files/lesson-06/`. En el panel **CSS**, escribir:
  ```css
  body {
    font-family: Arial, Helvetica, sans-serif;
    background-color: #0f172a;
    color: #f8fafc;
  }

  h1 {
    font-size: 36px;
    color: #38bdf8;
  }

  p {
    font-size: 18px;
    line-height: 1.6;
  }
  ```
  Presionar **Run** y mostrar el cambio a "modo oscuro".
- **[En pantalla]**: Flechas señalando `font-family` (tipo de letra), `font-size` (tamaño en `px`) y `line-height` (espacio entre líneas).
- **[Narración en off]**:
  > "Vamos a JSFiddle y transformemos esta página en un modo oscuro súper moderno. Con `font-family` cambiamos la letra a `Arial, sans-serif`, que es limpia y sin adornos. Le damos un fondo azul muy oscuro al `body` y texto casi blanco para que resalte. Al `h1` le subimos el `font-size` a `36px` con un celeste vibrante, y a los párrafos `18px` con `line-height: 1.6` para que las líneas respiren. Presionamos **Run** y... ¡mira qué diferencia!"

## [03:45 - 04:30] Pausa interactiva
- **[En pantalla]**: Recuadro: *"Pausa el video — Cambia el color del `h1` por `#a855f7` (morado) o `#4ade80` (verde) y prueba `font-family: Georgia, serif;`"*.
- **[Narración en off]**:
  > "Pausa el video ahora y experimenta en JSFiddle: cambia el color del título principal y prueba cómo cambia el estilo si usas `Georgia, serif` en lugar de `Arial`."

## [04:30 - 05:00] Cierre
- **[En pantalla]**: Checklist: `color`, `background-color`, `font-family`, `font-size`.
- **[Narración en off]**:
  > "¡Increíble! Tu página ya tiene carácter propio. En la Lección 7 vamos a aprender a centrar contenido, poner bordes redondeados y dar espacio alrededor de nuestros elementos."
