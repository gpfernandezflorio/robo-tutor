# Crear el usuario que va a correr el servidor con permisos de administrados y asignarle una contraseña segura

  `sudo useradd -m rtServer`

  `sudo passwd rtServer`

  `sudo usermod -aG sudo rtServer`

  `su rtServer`

# Clonar el repositorio en su carpeta sin acceso por parte de otros usuarios

  `cd /rtServer`

  `git clone https://github.com/gpfernandezflorio/robo-tutor.git`

# Crear el usuario que va a correr los intentos enviados sin contraseña

  `sudo useradd rtTest`

  `sudo passwd -d rtTest`

# Crear la carpeta para correr los intentos enviados, con permiso de lectura

  `sudo mkdir /rtTest`

  `sudo chmod 755 /rtTest`

# Copiar los fuentes de Gobstones y el parser de Haskell

  `cp -r /rtServer/robo-tutor/servidor/gobstones-lang /rtTest/gbs`

  `cp /rtServer/robo-tutor/servidor/parser.hs /rtTest/parser.hs`

# Quitar acceso global al repositorio

  `chmod -R 770 /rtServer/robo-tutor`