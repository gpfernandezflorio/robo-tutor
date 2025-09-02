### REQUISITOS
1. Instalar `nvm`.

    `wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash`

2. Instalar la versión 17.9.1 de `Node`.

    `nvm install 17.9.1`

3. Instalar `pip`

    `sudo apt install python3-pip`

4. Instalar `dotenv`

    `pip install --break-system-packages load_dotenv`

### INSTRUCCIONES
1. Clonar este repositorio.

2. Actualizar el valor de la variable de entorno UID en el archivo `.env` con el uid de usuario (sin permisos de administrador). Generalmente es el 1000. Se puede obtener ejecutando el comando `id` en una terminal.

(Para ejecutar con https)

3. Cambiar el valor de la variable de entorno PUERTO_INICIAL en el archivo `.env` por 443.

4. Generar un certificado ssl y agregar las rutas al certificado y a la clave como valores de las variables de entorno CERT y KEY, respectivamente, en el archivo `.env`.