
(function () {

  function getNombre(tr) {
    const celdaNombre = tr.querySelector('td');
    return (celdaNombre?.textContent || 'esta cancha').trim();
  }
  function getFecha(tr) {
    return tr.querySelector('input[type="date"]');
  }
  function getHora(tr) {
    return tr.querySelector('select');
  }
  function getError(tr) {
    return tr.querySelector('.error-text');
  }
  function getEstadoTexto(tr) {
    const lbl = tr.querySelector('td label');
    return (lbl?.textContent || '').trim().toLowerCase(); // habilitada/reservada/inhabilitada
  }
  function getBoton(tr) {
    return tr.querySelector('td:last-child button');
  }
  function getAnchor(tr) {
    return tr.querySelector('td:last-child button a, td:last-child a');
  }

  // --- Validación por FILA (no crea ni toca filas) ---
  function validarFila(tr) {
    const nombre = getNombre(tr);
    const fecha = getFecha(tr);
    const hora = getHora(tr);
    const error = getError(tr);

    const sinFecha = !fecha || !fecha.value;
    const horaSinSeleccion = !hora || hora.selectedIndex === 0;

    if (sinFecha || horaSinSeleccion) {
      if (error) error.textContent = `⚠️ Completa los campos para ${nombre}.`;
      return false;
    }
    if (error) error.textContent = '';
    return true;
  }

  // --- Delegación de eventos: NO agrega filas ---
  const tbody = document.querySelector('.Table-Body');
  if (!tbody) return;

  tbody.addEventListener('click', function (e) {
    const target = e.target;
    if (!(target instanceof HTMLElement)) return;

    const boton = target.closest('button');
    const anchor = target.closest('a');
    if (!boton && !anchor) return;

    const tr = target.closest('tr');
    if (!tr) return;

    // Si el botón está disabled, no seguimos
    const buttonEl = getBoton(tr);
    if (buttonEl && buttonEl.disabled) return;

    // Respeta el estado (solo permite si dice "Habilitada")
    const estado = getEstadoTexto(tr); // 'habilitada' | 'reservada' | 'inhabilitada'
    if (estado !== 'habilitada') {
      e.preventDefault();
      return;
    }

    // Validar fecha/hora
    if (!validarFila(tr)) {
      e.preventDefault();
      return;
    }



  });
})();