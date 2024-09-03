

## ¡Contribuir al Proyecto!

Hola a todos/as,

Quiero invitarlos a que formen parte activa del proyecto en el que hemos estado trabajando. Hacer un fork del repositorio y subir sus propios cambios es una excelente manera de poner en práctica lo que hemos aprendido, experimentar con nuevas ideas y colaborar con sus compañeros/as. Además, es una oportunidad para mejorar sus habilidades en Git y GitHub, herramientas fundamentales en el mundo IT.

### ¿Por qué hacer un fork?

1. **Aprendizaje Activo**: Poner en práctica lo que aprenden en clase y experimentar con el código.
2. **Colaboración**: Trabajar en equipo y aprender a manejar contribuciones de múltiples desarrolladores.
3. **Portafolio**: Tener un historial de contribuciones que pueden mostrar en sus futuros portafolios.
4. **Feedback**: Recibir retroalimentación sobre su código para mejorar continuamente.

### ¿Cómo hacer un fork y contribuir?

#### 1. Crear un fork del repositorio

1. **Iniciar sesión en GitHub**: Asegúrense de estar logueados en GitHub.
2. **Ir al repositorio**: Visiten el repositorio del proyecto en GitHub.
3. **Hacer fork**: Hagan clic en el botón "Fork" en la parte superior derecha de la página del repositorio. Esto creará una copia del repositorio en su cuenta de GitHub.

#### 2. Clonar el fork a su máquina local

1. **Clonar el repositorio**: En su cuenta de GitHub, naveguen a su fork del proyecto y copien la URL del repositorio (botón "Code" y luego copiar la URL).
2. **Abrir terminal o Git Bash**: En su computadora, abran una terminal o Git Bash.
3. **Ejecutar comando de clonación**: Ejecuten el siguiente comando reemplazando `URL_DEL_REPOSITORIO` con la URL que copiaron:
   ```bash
   git clone URL_DEL_REPOSITORIO
   ```
4. **Navegar al directorio del proyecto**: 
   ```bash
   cd nombre-del-repositorio
   ```

#### 3. Crear una nueva rama para sus cambios

1. **Crear una rama**: Antes de hacer cualquier cambio, creen una nueva rama para mantener sus cambios organizados:
   ```bash
   git checkout -b nombre-de-la-rama
   ```

#### 4. Realizar cambios y hacer commits

1. **Realizar cambios**: Hagan los cambios en el código que desean.
2. **Agregar cambios**: Añadan los cambios al área de preparación:
   ```bash
   git add .
   ```
3. **Hacer commit**: Realicen un commit con un mensaje descriptivo:
   ```bash
   git commit -m "Descripción de los cambios realizados"
   ```

#### 5. Enviar los cambios a GitHub

1. **Enviar cambios**: Suban su rama con los cambios a su fork en GitHub:
   ```bash
   git push origin nombre-de-la-rama
   ```

#### 6. Crear un Pull Request

1. **Ir a GitHub**: En su repositorio fork en GitHub, verán un mensaje para crear un Pull Request (PR) para la nueva rama que acaban de subir.
2. **Crear PR**: Hagan clic en "Compare & pull request" y llenen los detalles del PR, explicando qué cambios hicieron y por qué.
3. **Enviar PR**: Hagan clic en "Create pull request".

¡Y eso es todo! Una vez que envíen su Pull Request, lo revisaré y si todo está bien, lo fusionaremos con el repositorio principal.

### ¡A trabajar!

