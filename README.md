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

6. Instalar `cabal`

    `sudo apt install cabal-install`

7. Instalar el paquete `haskell-src-exts` para `ghc`

    `cabal install --lib haskell-src-exts`

### INSTRUCCIONES

...

(Para ejecutar con https)

7. Cambiar el valor de la variable de entorno PUERTO_INICIAL en el archivo `.env` por 443.

8. Instalar y configurar NGINX.

    * Agregar la siguiente regla en el archivo `/etc/nginx/sites-enabled/defaul`:

    ```nginx
    server {
        listen 443 ssl;
        server_name robotutor.exp.dc.uba.ar;

        location / {
            proxy_pass http://robotutor.exp.dc.uba.ar:8060/;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }

        # HSTS
        add_header Strict-Transport-Security "max-age=31536000";
        # CSP
        add_header Content-Security-Policy "default-src 'self';";
    }
    ```

9. Generar un certificado ssl y agregar las rutas al certificado y a la clave como valores de las variables de entorno CERT y KEY, respectivamente, en el archivo `.env`. Deberían agregarse automáticamente las siguientes líneas dentro de la regla creada en el paso anterior:
    ```nginx
    ssl_certificate /etc/letsencrypt/live/robotutor.exp.dc.uba.ar/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/robotutor.exp.dc.uba.ar/privkey.pem; # managed by Certbot
    ```