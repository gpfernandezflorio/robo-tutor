### REQUISITOS
1. Instalar `nvm`.

    `wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash`

2. Instalar la versión 17.9.1 de `Node`.

    `nvm install 17.9.1`

3. Instalar `pip`

    `sudo apt install python3-pip`

4. Instalar `dotenv`

    `pip install --break-system-packages load_dotenv`

5. Instalar `ghci`

    `sudo apt install ghc`

### INSTRUCCIONES
1. Clonar este repositorio.

  `git clone https://github.com/gpfernandezflorio/robo-tutor.git`

2. Sacarle permisos globales

  `chmod -R o-r robo-tutor`

3. Crear la carpeta rtTest para ejecutar el código.

  `mkdir /rtTest`

4. Linkear los fuentes de Gobstones y el parser de Haskell

  `ln -s servidor/gobstones-lang /rtTest/gbs`

  `cp servidor/parser.hs /rtTest/parser.hs`

5. Crear el usuario rtTest para ejecutar el código.

  `sudo useradd -m rtTest`

  `sudo passwd -d rtTest`

6. Crear la carpeta jail para ejecutar el código.

  `mkdir /rtTest/jail`

  `sudo chmod 777 /rtTest/jail`

(Para ejecutar con https)

7. Cambiar el valor de la variable de entorno PUERTO_INICIAL en el archivo `.env` por 443.

8. Generar un certificado ssl y agregar las rutas al certificado y a la clave como valores de las variables de entorno CERT y KEY, respectivamente, en el archivo `.env`.
