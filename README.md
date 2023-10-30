<h1 align="center"> 👩‍💻 Isasmendi, Eugenia Yanina <h1>
<p>📁Repositorio para desarrollo del Proyecto Final de Digitalers</p>
<div align="center">
  <a href="https://github.com/isasmendi"><img src="img/icons-sport.png"></a>
</div>
<br>
<h1 align="center"> Sistema de Administración de Canchas : La Esquina 🥅⚽🦶 <h1>
<h2>Sobre el Projeto:</h2>
Es una aplicación web para poder administrar los turnos de canchas segun el deporte, diseñado para ayudar a los propietarios de instalaciones deportivas a gestionar sus reservas y horarios de manera eficiente.
<h2>Caracteristicas Funcionales:</h2>
<ul>
  <li><b>Registro de usuarios: </b> Lleva un registro de los datos de los usuarios tanto como administrador como empleado segun eso es el acceso al sistema.</li>

  <li><b>Registro de clientes: </b> Lleva un registro de los datos de los clientes y sus reservas.</li>

  <li><b>Registro de equipo: </b>Permite a los administradores registrar información detallada sobre los equipos que utilizan las canchas, incluyendo datos de contacto, jugadores, y estadísticas.</li>

  <li>Gestion de Reserva de cancha: </b>Permite a los administradores programar y gestionar reservas de canchas deportivas. </li>

  <li>Registro de Canchas: </b>Facilita el registro detallado de las canchas disponibles, incluyendo información sobre el tipo de superficie, dimensiones, y tarifas. </li>

  <li>Calendario Visual: </b> Visualiza los horarios de las canchas en un calendario</li>
  
  <li><b> Gestión de Notificaciones: </b> Envía recordatorios y confirmaciones de reservas a los clientes por correo electrónico o mensajes de texto, whatsApp.</li>
</ul>
<h2>Modelo de Tabla:</h2>
<br>

## Registro de Usuario
| Campo            | Descripción                                               |
|------------------|-----------------------------------------------------------|
| id               | Identificador único del usuario.                         |
| nombre           | Nombre del usuario.                                       |
| rol              | Rol del usuario (administrador, empleado, cliente).      |
| correo_electrónico | Correo electrónico del usuario.                        |
| contraseña       | Contraseña (generalmente almacenada de manera segura).   |

## Registro de Clientes
| Campo            | Descripción                                               |
|------------------|-----------------------------------------------------------|
| id               | Identificador único del cliente.                         |
| nombre           | Nombre del cliente.                                       |
| teléfono          | Número de teléfono del cliente.                           |
| correo_electrónico | Correo electrónico del cliente.                        |
| socio            | Indicador de si el cliente es socio (para aplicar descuentos). |

## Registro de Reservas
| Campo            | Descripción                                               |
|------------------|-----------------------------------------------------------|
| id               | Identificador único de la reserva.                       |
| cliente_id       | ID del cliente que hizo la reserva.                       |
| cancha_id        | ID de la cancha reservada.                                 |
| equipo_id        | ID del equipo (si es una reserva para un partido de equipo). |
| fecha            | Fecha y hora de la reserva.                               |
| descuento        | Descuento aplicado a la reserva (si el cliente es socio). |
| estado           | Estado de la reserva (confirmada, pendiente, cancelada).  |

## Registro de Cancha
| Campo            | Descripción                                               |
|------------------|-----------------------------------------------------------|
| id               | Identificador único de la cancha.                        |
| nombre           | Nombre o número de la cancha.                             |
| categoría        | Categoría de la cancha (según edades: infantil, juvenil, adulto). |
| tipo_superficie  | Tipo de superficie de la cancha (césped sintético, tierra, cemento). |
| precio           | Tarifa por el uso de la cancha.                           |
| correo_electrónico | Correo electrónico de la cancha (si es aplicable).      |
