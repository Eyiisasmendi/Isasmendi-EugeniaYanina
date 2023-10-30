<h1 align="center"> 👩‍💻 Isasmendi, Eugenia Yanina <h1>
<p>📁Repositorio para desarrollo del Proyecto Final de Digitalers</p>
<div align="center">
  <a href="https://github.com/isasmendi"><img src="img/icons-sport.png"></a>
</div>
<br>
<h1 align="center"> Sistema de Administración de Canchas : La Esquina 🥅⚽🦶 <h1>
<h2>Sobre el Projeto:</h2>
Es una aplicación web para poder administrar los turnos de canchas segun el deporte, diseñado para ayudar a los propietarios de instalaciones deportivas a gestionar con o sin reservas de manera eficiente.
<h2>Caracteristicas Funcionales:</h2>
<ul>
  <li><b>Registro de usuarios: </b> Lleva un registro de los datos de los usuarios tanto como administrador,empleado e cliente segun eso es el acceso al sistema.</li>

  <li><b>Registro de clientes: </b> Lleva un registro de los datos de los clientes y sus reservas e ingreso </li>

  <li><b>Registro de equipo: </b>Permite a los administradores registrar información detallada sobre los equipos que utilizan las canchas, incluyendo datos de jugadores y estadísticas de los partidos.</li>

  <li>Registro de Canchas: </b>Facilita el registro detallado de las canchas disponibles, incluyendo información sobre el tipo de superficie, dimensiones, y precio. </li>

  <li>Calendario Visual: </b> Visualiza los horarios de las canchas en un calendario</li>
  
  <li><b> Gestión de Notificaciones: </b> Envía recordatorios y confirmaciones de reservas a los clientes por correo electrónico o mensajes de texto, whatsApp.</li>
</ul>
<h2>Modelo de Tabla:</h2>
<br>

## Registro de Usuario

| Campo              | Descripción                                            |
| ------------------ | ------------------------------------------------------ |
| id                 | Identificador único del usuario.                       |
| nombre             | Nombre del usuario.                                    |
| rol                | Rol del usuario (administrador, empleado, cliente).    |
| correo_electrónico | Correo electrónico del usuario.                        |
| contraseña         | Contraseña (generalmente almacenada de manera segura). |

## Registro de Clientes

| Campo              | Descripción                                                    |
| ------------------ | -------------------------------------------------------------- |
| id                 | Identificador único del cliente.                               |
| nombre             | Nombre del cliente.                                            |
| teléfono           | Número de teléfono del cliente.                                |
| correo_electrónico | Correo electrónico del cliente.                                |
| socio              | Indicador de si el cliente es socio (para aplicar descuentos). |

## Registro de Reservas

| Campo      | Descripción                                                  |
| ---------- | ------------------------------------------------------------ |
| id         | Identificador único de la reserva.                           |
| cliente_id | ID del cliente que hizo la reserva.                          |
| cancha_id  | ID de la cancha reservada.                                   |
| equipo_id  | ID del equipo (si es una reserva para un partido de equipo). |
| fecha      | Fecha y hora de la reserva.                                  |
| descuento  | Descuento aplicado a la reserva (si el cliente es socio).    |
| estado     | Estado de la reserva (confirmada, pendiente, cancelada).     |

## Registro de Cancha

| Campo              | Descripción                                                          |
| -------------------| -------------------------------------------------------------------- |
| id                 | Identificador único de la cancha.                                    |
| nombre             | Nombre o número de la cancha.                                        |
| categoría_cancha_id| Categoría de la cancha (fútbol, rugby, béisbol, hockey y tenis).     |
| tipo_superficie    | Tipo de superficie de la cancha (césped sintético, tierra, cemento). |
| medida_campo       | Dimensiones de cancha segun deporte                                  |
| precio             | Tarifa por el uso de la cancha.                                      |

## Registro de Equipos

| Campo                | Descripción                                                              |
| -------------------- | ------------------------------------------------------------------------ |
| id                   | Identificador único del equipo.                                          |
| nombre               | Nombre del equipo.                                                       |
| contacto             | Información de contacto (capitán u otra persona de contacto). |
| jugadores            | Datos de los miembros del equipo                                         |
| estadísticas_partido | Datos PJ:partidos jugados, PG:partidos ganados, PE:partidos empatados.   |
| estadísticas_goles   | Datos GC = Goles Contras, DG = Diferencias de Goles                      |
| fecha_creación       | Fecha de creación del equipo.                                            |

## Registro de Categoria de Cancha

| Campo  | Descripción                                             |
| ------ | ------------------------------------------------------- |
| id     | Identificador único de categoria.                      |
| nombre | Nombre de categoria( 1-fútbol,2-rugby,3-béisbol,4-hockey, 5-tenis). |     |


#Acceso del sistema:
----

*`Nombre de Usuario: super `
*`Correo electronico: super@admin.com `
*`Password: superadmin123 `

----

#Autor

----------------------
* [@Eyiisasmendi] (https://github.com/Eyiisasmendi)