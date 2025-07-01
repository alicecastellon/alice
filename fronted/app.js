const apiURL = "http://localhost:8000/clientes/";

document.getElementById("clienteForm").addEventListener("submit", function (e) {
  e.preventDefault();
  const nombre = document.getElementById("nombre_cliente").value;
  const correo = document.getElementById("correo_cliente").value;

  const nuevoCliente = { nombre, correo };

  fetch(apiURL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(nuevoCliente)
  })
    .then(res => {
      if (!res.ok) throw new Error("Error al crear cliente");
      return res.json();
    })
    .then(() => {
      document.getElementById("clienteForm").reset();
      cargarClientes();
    })
    .catch(error => console.error(error));
});

function cargarClientes() {
  fetch(apiURL)
    .then(res => res.json())
    .then(clientes => {
      const contenedor = document.getElementById("clientes");
      contenedor.innerHTML = "";
      clientes.forEach(cliente => {
        const div = document.createElement("div");
        div.classList.add("cliente");
        div.innerHTML = `
          <strong>${cliente.nombre}</strong>
          <span>${cliente.correo}</span>
          <div class="acciones">
            <button onclick="editarCliente(${cliente.id_usuario}, '${cliente.nombre}', '${cliente.correo}')">Editar</button>
            <button class="delete" onclick="eliminarCliente(${cliente.id_usuario})">Eliminar</button>
          </div>
        `;
        contenedor.appendChild(div);
      });
    })
    .catch(error => console.error("Error al cargar clientes:", error));
}

function eliminarCliente(id) {
  if (!confirm("¿Seguro que deseas eliminar este cliente?")) return;

  fetch(`${apiURL}${id}`, {
    method: "DELETE"
  })
    .then(res => {
      if (!res.ok) throw new Error("Error al eliminar cliente");
      cargarClientes();
    })
    .catch(error => console.error(error));
}

function editarCliente(id, nombreActual, correoActual) {
  const nuevoNombre = prompt("Editar nombre:", nombreActual);
  const nuevoCorreo = prompt("Editar correo:", correoActual);

  if (nuevoNombre && nuevoCorreo) {
    fetch(`${apiURL}${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ nombre: nuevoNombre, correo: nuevoCorreo })
    })
      .then(res => {
        if (!res.ok) throw new Error("Error al editar cliente");
        return res.json();
      })
      .then(() => {
        cargarClientes();
      })
      .catch(error => console.error(error));
  }
}

// Mostrar los clientes al cargar la página
cargarClientes();

//EMPLEADOS
const api_URL = "http://localhost:8000/empleados/";

document.getElementById("empleadoForm").addEventListener("submit", function (e) {
  e.preventDefault();
  const nombre = document.getElementById("primer_nombre").value;
  const apellido = document.getElementById("primer_apellido").value;
  const identificacion = document.getElementById("identificacion").value;
  const direccion = document.getElementById("direccion_em").value;

  const nuevoEmpleados = { nombre, apellido, identificacion, direccion };

  fetch(api_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(nuevoEmpleados)
  })
    .then(res => {
      if (!res.ok) throw new Error("Error al crear empleado");
      return res.json();
    })
    .then(() => {
      document.getElementById("empleadoForm").reset();
      cargarEmpleados();
    })
    .catch(error => console.error(error));
});

function cargarEmpleados() {
  fetch(api_URL)
    .then(res => res.json())
    .then(empleados => {
      const contenedor = document.getElementById("empleados");
      contenedor.innerHTML = "";
      empleados.forEach(empleados => {
        const div = document.createElement("div");
        div.classList.add("empleados");
        div.innerHTML = `
          <strong>${cliente.nombre}</strong>
          <span>${cliente.apellido}</span>
          <span>${cliente.identificacion}</span>
          <span>${cliente.direccion}</span>
          <div class="acciones">
            <button onclick="editarCliente(${empleados.id_empleado}, '${empleados.nombre}', '${empleados.apellido}', '${empleados.identificacion}', '${empleados.direccion}')">Editar</button>
            <button class="delete" onclick="eliminarCliente(${empleados.id_empleado})">Eliminar</button>
          </div>
        `;
        contenedor.appendChild(div);
      });
    })
    .catch(error => console.error("Error al cargar empleado:", error));
}

function eliminarempleados(id) {
  if (!confirm("¿Seguro que deseas eliminar este empleado?")) return;

  fetch(`${api_URL}${id_empleado}`, {
    method: "DELETE"
  })
    .then(res => {
      if (!res.ok) throw new Error("Error al eliminar empleado");
      cargarEmpleados();
    })
    .catch(error => console.error(error));
}

function editarempleados(id_empleado, nombreActual, apellidoActual, identificacionActual, direccionActual) {
  const nuevoNombre = prompt("Editar nombre:", nombreActual);
  const nuevoapellido = prompt("Editar correo:", apellidoActual);
  const nuevaidentificacion = prompt("Editar correo:", identificacionActual);
  const nuevadireccion = prompt("Editar correo:", direccionActual);


  if (nuevoNombre && nuevoapellido && nuevaidentificacion && nuevadireccion) {
    fetch(`${api_URL}${id_empleado}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ nombre: nuevoNombre, apellido: nuevoapellido, identificacion: identificacionActual, direccion: direccionActual })
    })
      .then(res => {
        if (!res.ok) throw new Error("Error al editar empleados");
        return res.json();
      })
      .then(() => {
        cargarEmpleados();
      })
      .catch(error => console.error(error));
  }
}

// Mostrar los clientes al cargar la página
cargarEmpleados();