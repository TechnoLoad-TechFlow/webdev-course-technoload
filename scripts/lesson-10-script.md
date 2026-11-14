# Guion Lección 10: Errores comunes, recomendaciones y próximos pasos

- **Duración objetivo**: 5:00 minutos
- **Responsable sugerido**: Estudiante 4
- **Herramienta en línea**: [JSFiddle](https://jsfiddle.net/)
- **Archivos asociados**: Referencia general al curso y `completed-examples/lesson-09/`

---

## [00:00 - 00:40] Introducción
- **[En pantalla]**: Título: *"Lección 10: Errores Comunes y Próximos Pasos"*.
- **[Narración en off]**:
  > "¡Hola y felicidades por llegar a la última lección del curso! Incluso los programadores con años de experiencia cometen errores pequeños todos los días. La diferencia está en saber detectarlos rápido. Hoy repasaremos los **5 errores más comunes** al empezar con HTML y CSS."

## [00:40 - 03:20] Los 5 errores más comunes (demostración rápida en JSFiddle)
- **[Acción en JSFiddle]**: Mostrar brevemente cada error y su corrección en vivo o con tarjetas en pantalla:
  1. **Olvidar cerrar una etiqueta HTML**: `<p>Hola` sin `</p>` → todo lo que sigue hereda el formato.
  2. **Olvidar comillas en atributos**: `<a href=https://...>` → siempre usa `href="https://..."`.
  3. **Olvidar el punto y coma `;` en CSS**: `color: red` seguido de `font-size: 20px;` → la segunda regla deja de funcionar.
  4. **Olvidar el punto `.` al seleccionar una clase en CSS**: escribir `tarjeta { }` en vez de `.tarjeta { }`.
  5. **Escribir mal el nombre de una propiedad** (ej. `colr:` o `backround:`): si el editor no la pinta de color, ¡revísala!
- **[En pantalla]**: Lista numerada del 1 al 5 con icono `❌ Error` vs `✅ Solución`.
- **[Narración en off]**:
  > "Error número uno: **olvidar cerrar una etiqueta**, como abrir `<h1>` y no poner `</h1>`; de pronto toda tu página se vuelve gigante. Error dos: **olvidar las comillas** en atributos como `href` o `src`. Error tres: **olvidar el punto y coma `;`** al final de una línea en CSS, lo que rompe la línea siguiente. Error cuatro: **olvidar el punto adelante** cuando llamas a una clase en CSS, como poner `tarjeta` en lugar de `.tarjeta`. Y error cinco: **un error de ortografía** en inglés, como escribir `backround` sin la `g`. Si algo no funciona, respira y revisa estos cinco puntos."

## [03:20 - 04:20] Buenas prácticas y dónde seguir aprendiendo gratis
- **[En pantalla]**: Recursos gratuitos recomendados:
  - **MDN Web Docs** (`developer.mozilla.org/es/`) — La enciclopedia oficial de HTML y CSS.
  - **JSFiddle** (`jsfiddle.net`) — Para seguir experimentando ideas en segundos.
  - **Validador W3C** (`validator.w3.org`) — Para revisar si tu HTML tiene errores.
- **[Narración en off]**:
  > "¿Y ahora qué sigue? Primero, no memorices todo: ni los profesionales lo hacen. Cuando tengas dudas sobre una etiqueta o propiedad CSS, consulta **MDN Web Docs** en español. Segundo, practica modificando tu tarjeta de perfil: cambia colores, agrega más secciones o inventa una página sobre tu banda o videojuego favorito en JSFiddle. Y tercero, si quieres llevar tus páginas al siguiente nivel, tu próximo paso después de HTML y CSS será aprender **JavaScript**, el lenguaje que da interactividad a la web."

## [04:20 - 05:00] Despedida y llamado a la acción
- **[En pantalla]**: *"¡Gracias por completar el curso! Comparte tu proyecto en el formulario de la descripción. #WebDevBeginners"*.
- **[Narración en off]**:
  > "En la descripción de este video tienes un cuestionario cortito para poner a prueba lo que aprendiste y un enlace para compartir el link de tu página de perfil. ¡Mucho éxito creando en la web, y hasta la próxima!"
