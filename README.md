Caso de estudio para el parcial de ARQUITECTURA DE SOTFWARE primer corte

El diseño del sistema se basa en una arquitectura de microservicios para proporcionar flexibilidad y escalabilidad. Se equilibran requerimientos funcionales, como recomendaciones personalizadas, con imperativos no funcionales, como seguridad y escalabilidad. La presentación clara de beneficios y retroalimentación inmediata es una prioridad. La implementación sigue principios SOLID para garantizar un código mantenible y extensible, con un enfoque en la seguridad en cada etapa. Los microservicios seleccionados incluyen autenticación, gestión de usuarios y beneficios. La arquitectura se adapta a necesidades actuales y futuras, enfocándose en la usabilidad y seguridad.

*Microservicios: -Autenticación Este microservicio maneja la autenticación de usuarios y la autorización para acceder a recursos específicos. Puede emitir tokens de acceso y gestionar la seguridad. -Gestión de Usuarios: Encargado de la gestión de perfiles de usuario, información personal y funciones asociadas a la identidad del usuario.

-Gestión de Beneficios: Administra la lógica de negocio relacionada con los beneficios ofrecidos a los usuarios, como descuentos, recompensas o servicios específicos.


![Diagraama de Clases](https://github.com/DonadoM/Parcial/assets/156842239/8c427a1e-a331-476a-8179-61e2bbfd89b3)

Principio de Responsabilidad Única (SRP):

Cumplimiento: Cada clase y función tiene una única razón para cambiar. Por ejemplo, en la clase CredictCard, se encarga exclusivamente de representar una tarjeta de crédito. La clase get_current_user en el módulo auth_service_py tiene la responsabilidad de validar y devolver el usuario actual.

Principio Abierto/Cerrado (OCP):
Cumplimiento: El código parece estar abierto para extensiones sin necesidad de modificaciones. Por ejemplo, puedes agregar nuevos métodos de pago o beneficios sin cambiar el código existente.

Principio de Inversión de Dependencia (DIP):
Cumplimiento: Las dependencias se inyectan, lo que facilita la inversión de dependencias en algunas partes del código, como en get_current_user.


#NOTA: Los comentarios en el codigo fueron hechos por IA, estos mismmos fueron analizados y corroborados. Asimismo se empleo la guia PEP8 de python para mantener un estilo claro y con buen margen de presentaciòn. 
