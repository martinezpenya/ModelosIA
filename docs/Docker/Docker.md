#  Introducción a docker

## Generalidades

### Imprescindibles

- [¿Qué es docker? Imagen vs contenedor](https://www.youtube.com/watch?v=FAJ1o3hb35s) 
  
    [![¿Qué es docker? Imagen vs contenedor](https://img.youtube.com/vi/FAJ1o3hb35s/0.jpg)](https://youtu.be/BbA5dpS4CcI?si=FAJ1o3hb35s)
    <p><iframe width="560" height="315" src="https://www.youtube.com/embed/FAJ1o3hb35s?si=byaWLqYMVSlPFpIx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></p>
    
- [Curso de docker](https://youtu.be/4Dko5W96WHg?si=Ri9RgyfLWxbs0DY9&t=86)
  
    [![Curso de docker](https://img.youtube.com/vi/4Dko5W96WHg/0.jpg)](https://youtu.be/4Dko5W96WHg)
    <p><iframe width="560" height="315" src="https://www.youtube.com/embed/4Dko5W96WHg?si=TJyuhtQHMZg7GIt4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></p>
    
- [Creación de imágenes](https://www.youtube.com/watch?v=A8oXDTDhZWU)
  
    [![Creación de imágenes](https://img.youtube.com/vi/A8oXDTDhZWU/0.jpg)](https://youtu.be/A8oXDTDhZWU)
    <p><iframe width="560" height="315" src="https://www.youtube.com/embed/A8oXDTDhZWU?si=oPFtXsMsEeUI-T9o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></p>
    
### Arquitectura
![Arquitectura1](<assets/docker.png>)
![Arquitectura2](<assets/docker1.png>)
![Arquitectura3](<assets/docker2.png>)

### Instalación en Ubuntu

[https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-es](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-es)

Requisitos previos:

- **apt-transport-https:** permite que el administrador de paquetes transfiera datos a través de https
- **ca-certificates:** permite que el navegador web y el sistema verifiquen los certificados de seguridad
- **curl:** transfiere datos (similar a wget)
- **software-properties-common:** agrega scripts para administrar el software

```bash
sudo apt-get install  curl apt-transport-https ca-certificates software-properties-common
```

Agregamos repositorio

```bash
# Primero clave GPG
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

sudo apt update

sudo apt install docker-ce

sudo systemctl status docker
```

Por defecto, el comando docker solo puede ser ejecutado por el usuario root o un usuario del grupo docker, que se crea automáticamente durante el proceso de instalación de Docker.

Para evitar escribir sudo al ejecutar el comando docker, agregue su nombre de usuario al grupo docker:

```bash
sudo usermod -aG docker ${USER}

# Cerramos y abrimos sesión de nuevo o ejecutamos
su - ${USER}

# Confirmamos los grupos de nuestro usuario
id -nG
```

## Uso

### Comandos básicos

#### Gestión de imagenes

```bash
docker image
docker history
docker inspect
docker save/load
docker rmi
```

#### Gestión de contenedores

```bash
docker attach
docker exec
docker inspect
docker kill
docker logs
docker pause/unpause
docker port
docker ps
docker rename
docker start/stop/restart
docker rm
docker run
docker stats
docker top
docker update
```

#### Ejemplo

```bash
# Ver los contenedores que tenemos
docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

# Ver las imagenes que tenemos
docker images
REPOSITORY                             TAG       IMAGE ID       CREATED        SIZE

# Crear un contenedor con una imagen básica de debian
# Como no tenemos ninguna imagen de debian, la descarga y la ejecuta
docker run debian
# Intentamos ver el contenedor en ejecución, no aparece nada porque ya se ha cerrado
docker ps
# Podemos verlo con
docker ps -a
CONTAINER ID   IMAGE     COMMAND       CREATED              STATUS                          PORTS     NAMES
09b14daab800   debian    "bash"        2 seconds ago        Exited (0) 1 second ago                   pensive_wozniak

# Ejecutar un comando en un contenedor
docker run debian /bin/echo "Hello World"
Hello World

# Información
docker inspect debian
```

### Crear contenedor interactivo y con nombre.

[https://jolthgs.wordpress.com/2019/09/25/create-a-debian-container-in-docker-for-development/](https://jolthgs.wordpress.com/2019/09/25/create-a-debian-container-in-docker-for-development/)

Para que docker no se invente un nombre como “pensive_wozniak” (comando anterior) podemos definir el nombre que queremos.

Utilizaremos una de las imágenes de: [https://hub.docker.com/_/debian/tags](https://hub.docker.com/_/debian/tags)

```bash
# Obtenemos la imagen, en el apartado aterior la hemos ejecutado directamente con "run", esto
# la obtiene implícitamente. En este caso la vamos a descargar.
docker pull debian:10-slim

# --name
# -h hostname que tendrá el contenedor
# -e codificación de caracteres
# -it modo interactivo
# /bin/bash -l  la shell que se ejecutará
docker run --name debian-mini -h equipo1 -e LANG=C.UTF-8 -it debian:10-slim /bin/bash -l

--- Estamos dentro del contenedor ---
# Una vez dentro del contenedor podemos actualizarlo e instalar los paquetes que creamos necesarios
apt update && apt upgrade --yes && apt install sudo locales --yes
# Configurar timezone
dpkg-reconfigure tzdata

# Vamos a nuestra home y creamos un archivo
cd
echo "hola" > prueba.txt

# Salimos del contenedor
exit (o control + d)

--- Ahora volvemos a la consola de nuestro equipo ---
docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

docker ps -a
CONTAINER ID   IMAGE            COMMAND          CREATED          STATUS                      PORTS     NAMES
97d8dc048093   debian:10-slim   "/bin/bash -l"   2 minutes ago    Exited (0) 24 seconds ago             debian-mini
```

### Imágenes

Es un instalador donde podemos incorporar nuestra aplicación. Es el punto de inicio para crear contenedores.
Hay imágenes oficiales de por ejemplo Ubuntu, Apache, etc, que fueron creadas por sus creadores oficiales.

Página oficial para imágenes: [https://hub.docker.com](https://hub.docker.com) 

Vamos a utilizar la siguiente imagen para pruebas:

[https://hub.docker.com/_/hello-world](https://hub.docker.com/_/hello-world)

Para ejecutar este contenedor “hello-word” escribimos en la terminal:

```bash
docker run hello-world
```

Una vez ejecutado, ya dispondremos de la imagen descargada, podemos ver todas las imágenes que tenemos descargadas con:

```bash
docker images

REPOSITORY                              TAG           IMAGE ID       CREATED        SIZE
hello-world                             latest        ee301c921b8a   9 months ago   9.14kB
```

Desde la página web de docker hub, podemos ver diferentes versiones de la misma imagen en la pestaña “TAGS”

![Tags](<assets/docker6.jpg>)

Podemos descargar una imagen específica y ejecutarla:

```bash
docker run hello-world:linux

docker images
REPOSITORY                              TAG           IMAGE ID       CREATED        SIZE
hello-world                             latest        ee301c921b8a   9 months ago   9.14kB
hello-world                             linux         ee301c921b8a   9 months ago   9.14kB

docker run hello-world:linux
```

Para eliminar una imagen utilizamos el parámetro `rmi` por ejemplo:

```bash
docker pull alpine

docker images
REPOSITORY                              TAG           IMAGE ID       CREATED        SIZE
alpine                                  latest        ace17d5d883e   3 weeks ago    7.73MB
hello-world                             latest        ee301c921b8a   9 months ago   9.14kB
hello-world                             linux         ee301c921b8a   9 months ago   9.14kB

# Eliminamos, opción 1
docker rmi ace17d5d883e

# Eliminamos, opción 2
docker rmi alpine

# Eliminamos, opción 3
docker rmi ace1
```

También se pueden buscar imágenes desde consola.

```bash
docker search ubuntu

NAME                             DESCRIPTION                                     STARS     OFFICIAL
ubuntu                           Ubuntu is a Debian-based Linux operating sys…   16888     [OK]
websphere-liberty                WebSphere Liberty multi-architecture images …   298       [OK]
open-liberty                     Open Liberty multi-architecture images based…   64        [OK]
neurodebian                      NeuroDebian provides neuroscience research s…   106       [OK]
ubuntu-debootstrap               DEPRECATED; use "ubuntu" instead                52        [OK]
ubuntu-upstart                   DEPRECATED, as is Upstart (find other proces…   115       [OK]
ubuntu/nginx                     Nginx, a high-performance reverse proxy & we…   112
ubuntu/squid                     Squid is a caching proxy for the Web. Long-t…   83
ubuntu/cortex                    Cortex provides storage for Prometheus. Long…   4
ubuntu/prometheus                Prometheus is a systems and service monitori…   56
ubuntu/apache2                   Apache, a secure & extensible open-source HT…   70
...
```

### Volúmenes

Los volúmenes sirven para almacenar información de manera persistente en uno o varios contenedores. Es útil para que los archivos ya estén integrados en el propio contenedor y podamos disponer de dichos archivos en diferentes contenedores diferentes.

También nos permiten compartir archivos con el contenedor. Modificarlos en local y que se modifiquen en el contenedor.

#### Operaciones con volúmenes

```bash
# Ver disponibles
docker volume ls
DRIVER    VOLUME NAME

# Creamos un volumen
docker volume create almacen
almacen

docker volume ls
DRIVER    VOLUME NAME
local     almacen

docker volume inspect almacen
[
    {
        "CreatedAt": "2024-02-20T11:10:58Z",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/almacen/_data",
        "Name": "almacen",
        "Options": null,
        "Scope": "local"
    }
]

# Lo borramos
docker volume rm almacen
```

#### Ejemplo: compartir volúmenes con host

```bash
# Creamos un punto de montaje
docker run --rm -it -v /tmp/puntomontaje:/home ubuntu
```

#### Ejemplo: compartir volúmenes con contenedores

Vamos a crear un volumen para compartir archivos entre nuestro sistema de ficheros local y 2 contenedores (ubuntu y fedora).

```bash
docker volume create almacen

# Descargamos la imagen de ubuntu
docker pull ubuntu
# Descargamos la imagen de fedora
docker pull fedora

docker images
REPOSITORY                             TAG       IMAGE ID       CREATED        SIZE
ubuntu                                 latest    a50ab9f16797   7 days ago     69.2MB
fedora                                 latest    46243415778a   2 months ago   259MB

## Creamos un contenedor, modo interactivo
docker run --rm -it -v almacen:/home ubuntu
# dentro del contenedor
cd /home
touch prueba.txt
exit # -> Salimos del contenedor

## Creamos otro contenedor, modo interactivo
docker run --rm -it -v almacen:/home fedora
# dentro del contenedor
cd /home
ls -> existe el archivo prueba.txt
```

### Diferencias docker-compose vs DockerFile

[https://blog.elhacker.net/2022/01/gestion-contenedores-dockerfile-y-docker-compose.html](https://blog.elhacker.net/2022/01/gestion-contenedores-dockerfile-y-docker-compose.html)

#### Docker Compose

Docker Compose es una herramienta que permite simplificar el uso de Docker. A partir de archivos YAML es mas sencillo crear contenedores, conectarlos, habilitar puertos, volúmenes, etc.

Con Compose puedes crear diferentes contenedores y al mismo tiempo, en cada contenedor, diferentes servicios, unirlos a un volúmen común, iniciarlos y apagarlos, etc. Es un componente fundamental para poder construir aplicaciones y microservicios

**Parámetros docker-compose.yml**

- *“**version** ‘3’*: Los archivos docker-compose.yml son versionados, lo que significa que es muy importante indicar la versión de las instrucciones que queremos darle. A medida de que Docker evoluciona, habrá nuevas versiones, pero de todos modos, siempre hay compatibilidad hacia atrás, al indicar la versión
- *“**build** .”*: Se utiliza para indicar donde está el Dockerfile que queremos utilizar para crear el contenedor. Al definier “.” automáticamente considerará el Dockerfile existente en directorio actual.
- *“**command**”*: Una vez creado el contenedor, aqui lanzamos el comando que permite ejecutar Jekyll, en modo servidor. El comando “–host 0.0.0.0” sirve para mapear el contenedor al sistema operativo host
- *“**ports**”*: mapeamos los puertos locales, por ejemplo 4000 (webserver jekyll) y 35729 (livereload) al servidor host. Esto permite que accediendo a Localhost:4000 podamos probar el sitio generador por Jekyll
- *“**volumes**”*: lo que hacemos es mapear el directorio local se mapee directamente con el /directoriox, lugar donde hemos creado la aplicación. De este modo, cualquier cambio en el directorio local en el host, se hará de inmediato en el contenedor.

![comandos docker](<assets/docker7.jpg>)

Ejemplo, creación contenedor con wordpress:

```bash
mkdir /tmp/wp
cd /tmp/wp

nano docker-compose.yml
```

```bash
version: '3' #Utilizamos la versión 3

## Nos saltamos la sección network 

services:
    db:
        image: mariadb:10.3.9
        volumes:
            - data:/var/lib/mysql
        environment:
            - MYSQL_ROOT_PASSWORD=secret
            - MYSQL_DATABASE=wordpress
            - MYSQL_USER=manager
            - MYSQL_PASSWORD=secret
            ## Equivalente a
			## docker run -d --name wordpress-db \
       		## --mount source=wordpress-db,target=/var/lib/mysql \
        	## -e MYSQL_ROOT_PASSWORD=secret \
        	## -e MYSQL_DATABASE=wordpress \
        	## -e MYSQL_USER=manager \
        	## -e MYSQL_PASSWORD=secret mariadb:10.3.9

    web:
        image: wordpress:4.9.8
        depends_on:
            - db
        volumes:
            - ./target:/var/www/html
        environment:
            - WORDPRESS_DB_USER=manager
            - WORDPRESS_DB_PASSWORD=secret
            - WORDPRESS_DB_HOST=db
        ports:
            - 8080:80
            ## Equivalente a
            ## docker run -d --name wordpress \
		    ## --link wordpress-db:mysql \
		    ## --mount type=bind,source="$(pwd)"/target,target=/var/www/html \
		    ## -e WORDPRESS_DB_USER=manager \
		    ## -e WORDPRESS_DB_PASSWORD=secret \
		    ## -p 8080:80 \
		    ## wordpress:4.9.8

volumes:
    data: # creción de volumen, compose añade un prefijo por lo que se llamará worpdress_data
```

```bash
# Levantamos la aplicación
docker-compose up -d
# El parámetro -d es similar al de docker run: nos permite levantar los servicios en segundo plano.

docker-compose ps
## docker-compose ps solo muestra información de los servicios que se define en docker-compose.yaml, mientras que docker muestra todos.

# Detener servicios
docker-compose stop

# Borrar
docker-compose down

# Borrar volúmenes
docker-compose down -v
```

Cuando creamos contenedores con `docker` sin indicar un nombre, por defecto asigna uno aleatorio; mientras que en *Compose* el prefijo es el nombre del directorio y el sufijo el nombre del servicio: **wordpress_db_1**. El número indica el número de instancia. Es posible levantar más de una instancia de un mismo servicio.

Equivalencia de parámetros

| **parámetro *Docker***            | **parámetro *Composer*** |
| --------------------------------- | ------------------------ |
| `--mount`                         | `volumes`                |
| `-e`                              | `environment`            |
| `-p,--publish`                    | `ports`                  |
| se escribe el nombre de la imágen | `image`                  |

Si reiniciamos el ordenador, los contenedores estarán detenidos (stop), podremos reiniciarlos con `docker start` o `docker-compose start`. Este es el comportamiento predeterminado y el que nos interesa en un entorno de desarrollo.

Sin embargo, en otros entornos, o para casos concretos, igual queremos que un contenedor tenga el mismo estado en el que estaba antes de reiniciar la máquina (iniciado o parado).

Para eso usaremos el parámetro `restart`. En el caso de la base de datos de nuestro ejemplo, la configuración quedaría como:

```dockerfile hl_lines="4"
services:
    db:
        image: mariadb:10.3.9
        restart: unless-stopped
        volumes:
            - data:/var/lib/mysql
        environment:
            - MYSQL_ROOT_PASSWORD=secret
            - MYSQL_DATABASE=wordpress
            - MYSQL_USER=manager
            - MYSQL_PASSWORD=secret
```

Otros valores son: `no` (por defecto), `always` y `on-failure`.

#### DockerFile

**Ejemplo básico**

Nos ubicamos en la carpeta donde vayamos a trabajar con la imagen, por ejemplo voy a crear un directorio llamado `docker-images`.

Y creamos una archivo `Dockerfile` con un editor de texto.

```bash
FROM ubuntu
RUN apt update
RUN apt install python 3 -y
RUN apt install netris -y
```

Creamos la imagen según las órdenes anteriores:

```bash
docker build -t python-ubuntu .
```

***Hay un error en el Dockerfile, corregir y volver a ejecutar el build.***

Ya tenemos una imagen de ubuntu pero con python3 instalado:

```bash
docker run -it python-ubuntu

python3

Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Una vez salimos podemos ver todas las “capas” de la imagen:

```bash
docker history -H python-ubuntu

IMAGE          CREATED         CREATED BY                                      SIZE      COMMENT
78732fd773c4   2 minutes ago   RUN /bin/sh -c apt install netris # buildkit    1MB       buildkit.dockerfile.v0
<missing>      2 minutes ago   RUN /bin/sh -c apt install python3 -y # buil…   29.5MB    buildkit.dockerfile.v0
<missing>      3 minutes ago   RUN /bin/sh -c apt update # buildkit            45.1MB    buildkit.dockerfile.v0
<missing>      3 weeks ago     /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B
<missing>      3 weeks ago     /bin/sh -c #(nop) ADD file:8d91b8bd386e0cc34…   69.2MB
<missing>      3 weeks ago     /bin/sh -c #(nop)  LABEL org.opencontainers.…   0B
<missing>      3 weeks ago     /bin/sh -c #(nop)  LABEL org.opencontainers.…   0B
<missing>      3 weeks ago     /bin/sh -c #(nop)  ARG LAUNCHPAD_BUILD_ARCH     0B
<missing>      3 weeks ago     /bin/sh -c #(nop)  ARG RELEASE                  0B
```

### Creación de imágenes propias

Para construir una imagen, se crea un `Dockerfile` con las instrucciones que especifican lo que va a ir en el entorno, dentro del contenedor (redes, volúmenes, puertos al exterior, archivos que se incluyen.

- Indica cómo y con qué construir la imagen.
- Podemos utilizar la imagen en tantos contenedores como queramos.

![Crear imagenes propias](<assets/docker8.jpg>)

El `DockerFile` nos permitirá definir las funciones básicas del contenedor.

Todo `Dockerfile` debe terminar en un comando `CMD` o en un `ENTRYPOINT`, pero en este caso, no lo utilizamos, ya que lanzaremos un comando directamente desde la receta de DockerCompose. Es decir, este `Dockerfile` se utiliza solamente para construir el contenedor y configurarlo. No es auto-ejecutable.

#### `FROM`

Imagen del sistema operativo donde va a correr el contenedor.

!!! tip 
    Las versiones “Alpine linux” ocupan muy poco espacio.

#### `RUN`

El comando **`RUN`** se ejecuta cuando se está construyendo una imagen personalizada para realizar una acción, creando una capa nueva. Este comando tiene el siguiente formato:

```dockerfile
RUN comando
```

```dockerfile
RUN [“ejecutable”, “parametro1”, …]
```

Ejemplo en windows:

```dockerfile
RUN [“Powershell”, “Get-Services”, “*”]
```



#### `COPY`

Sirve para copiar archivos desde nuestra máquina al contenedor. Podemos pasar un documento de texto de la máquina anfitrión al conenedor de python-ubuntu.

```dockerfile
FROM ....
RUN ....
RUN ....
COPY prueba.txt /
```

***Volvemos a construir la imagen y accedemos a ella para buscar el archivo.***

#### `ENV`

Podemos crear una variable y enviarla a nuestro contenedor, en mi caso por ejemplo voy a definir una variable llamada contenido que va a ir dirigida a un bloc de notas que está dentro del contenedor:

```dockerfile
....
ENV NUEVO_PATH /etc
```

Una vez regenerado la imagen y dentro del contenedor:

```bash
echo $NUEVO_PATH
/etc
```

Podemos combinar RUN con ENV

```dockerfile
ENV NUEVO_PATH /etc
RUN echo $NUEVO_PATH > /prueba.txt
```

#### `WORKDIR`

Nos situamos en un directorio determinado, nos puede ayudar en la copia de ficheros.

```dockerfile
.....
WORKDIR /home
COPY prueba.txt .  # Lo copia en /home
```

#### `EXPOSE`

Permite exponer los puertos que queramos

#### `LABEL`

Creamos etiquetas, por ejemplo:

```dockerfile
FROM ubuntu
LABEL version=1.0
LABEL autor=JosepGarcia
.....
```

#### `USER`

Sirve para establecer el usuario, debe existir. (Por defecto se utiliza root).

```dockerfile
....
RUN echo $(whoami) > /tmp/usuarioantes.txt

RUN useradd -m josepgarcia
USER josepgarcia
WORKDIR /home/josepgarcia
RUN echo $(whoami) > /tmp/usuarioahora.txt
```

#### `CMD`

Ejecuta comandos una vez se ha inicializado el conenedor (RUN se utiliza para crear la imagen de un contenedor).

```dockerfile
## Ejecutamos el comando top cuando se inicie el contenedor
.....
CMD top
```

#### `IGNORE`

Sirve para ignorar aquello que tengamos en nuestro directorio actual.

Por ejemplo:

Creamos una imagen que copie todo nuestro directorio actual al contenedor.

```bash
ls
Dockerfile  prueba.txt
```

contenido de Dockerfile:

```dockerfile
...
COPY . /tmp
...
```

Ahora le decimos que copie todo menos el archivo `Dockerfile`, para ello creamos un fichero llamado `.dockerignore` con el siguiente contenido

```bash
Dockerfile
```

### Guardar estado de los contenedores

https://www.baeldung.com/ops/docker-save-container-state

## Casos de uso

### Compatibilidad de código entre diferentes versiones de un lenguaje

```bash
mkdir /tmp/php
cd /tmp/php
```

Crear el siguiente archivo (test.php)

```php
<?php
// Funciona bien en php5 ya que list hace la asignación desde el último al primero
// En PHP 5, list() asigna los valores empezando desde el parámetro más a la derecha. En PHP 7, list() empieza desde el parámetro más a la izquierda.
// https://www.php.net/manual/es/function.list.php
$info = array('cafeína','marrón', 'café');

// Enumerar todas las variables
list($datos[], $datos[], $datos[]) = $info;
echo "El $datos[0] es $datos[1] y la $datos[2] lo hace especial.\n";
```

A continuación vamos a crear dos contenedores que sirva este código usando imágenes distintas , para cada versión de PHP y usando puertos distintos para acceder a cada versión de la aplicación:

```bash

docker run -d -p 8081:80 --name php56 -v /tmp/php:/var/www/html:ro php:5.6-apache
## Accedemos al contenedor: docker exec -it eb326ffd1b66 /bin/bash
## Ejecutamos test.php

**docker run -d -p 8082:80 --name php74 -v /tmp/php:/var/www/html:ro php:7.4-apache**
## Ejecutamos test.php desde web
## http://localhost:8082/test.php
```

### Crear una imagen de un repositorio de github

Ejemplo repositorio:

[https://github.com/k4m4/kickthemout](https://github.com/k4m4/kickthemout)

```bash
FROM ubuntu:focal

RUN apt update -y && apt upgrade -y && apt install python3 -y
RUN apt install -y git
RUN apt install -y python3-pip
RUN git clone https://github.com/k4m4/kickthemout.git

WORKDIR /kickthemout

RUN pip3 install -r requirements.txt

CMD python3 kickthemout.py
```

### Aplicación de python dentro de un contenedor

### Crear una imagen personalizada

[https://jolthgs.wordpress.com/2019/09/25/create-a-debian-container-in-docker-for-development/](https://jolthgs.wordpress.com/2019/09/25/create-a-debian-container-in-docker-for-development/)

Para crear una imagen personalizada utilizaremos el contenedor que habíamos creado en el punto 1, con una debian actualizada y con un fichero de texto prueba.txt

```bash
# Iniciamos el contenedor
docker start debian-mini

docker ps
CONTAINER ID   IMAGE            COMMAND          CREATED          STATUS         PORTS     NAMES
97d8dc048093   debian:10-slim   "/bin/bash -l"   10 minutes ago   Up 2 seconds             debian-mini

# Entramos en el contenedor iniciado
docker exec -it debian-mini bash

# Instalamos paquetes
apt install netris sl ninvaders

# ¿Dónde están?
find / -name ninvaders

ls /usr/games

# Salimos
control + d

# Nuestra imagen
docker image ls
REPOSITORY                             TAG       IMAGE ID       CREATED        SIZE
debian                                 10-slim   6016bddc4bad   9 days ago     63.5MB

```

## Copias de seguridad

### Copias de contenedores

Ya estén encendidos o apagados, podemos realizar respaldos de seguridad de los contenedores. Utilizando la opción “*export*” empaquetará el contenido, generando un fichero con extensión “.*tar*” de la siguiente manera:

```bash
docker export -o fichero-resultante.tar nombre-contenedor
```

o

```bash
docker export nombre-contenedor > fichero-resultante.tar
```

### **Restauración de copias de seguridad de contenedores**

Hay que tener en cuenta, antes de nada, que no es posible restaurar el contenedor directamente, de forma automática. En cambio, sí podemos crear una imagen, a partir de un respaldo de un contenedor, mediante el parámetro “*import*” de la siguiente manera:

```bash
docker import fichero-backup.tar nombre-nueva-imagen
```



### **Copias de imágenes**

Aunque no tiene mucho sentido por que se bajan muy rápido, también tenemos la posibilidad de realizar copias de seguridad de imágenes. El proceso se realiza al utilizar el parámetro ‘*save*‘, que empaquetará el contenido y generará un fichero con extensión “*tar*“, así:

```bash
docker save nombre_imagen > imagen.tar
```

o

```bash
docker save -o imagen.tar nombre_imagen
```

### **Restaurar copias de seguridad de imágenes**

Con el parámetro ‘load’, podemos restaurar copias de seguridad en formato ‘.tar’ y de esta manera recuperar la imagen.

```bash
docker load -i fichero.tar
```

## Contenedores ejemplo

### Monitorización y Gestión

- **[Netdata](https://github.com/netdata/netdata)** - Monitorización de sistemas en tiempo real con dashboard web completo
- **[Glances](https://nicolargo.github.io/glances/)** - Monitorización del sistema via web que muestra información de CPU, memoria, red y procesos
- **[Portainer](https://www.portainer.io/)** - Interfaz web para gestionar y administrar contenedores Docker
- **[Uptime Kuma](https://github.com/louislam/uptime-kuma)** - Monitor de disponibilidad para verificar el estado de contenedores y servicios

### Proxy y Red

- **[Nginx Proxy Manager](https://nginxproxymanager.com/)** - Proxy inverso con interfaz web para gestionar hosts virtuales y certificados SSL/TLS
- **[Acestream](https://acestream.org/)** - Motor P2P para streaming de video, útil para integrar canales en Jellyfin
- **[Libreddit](https://github.com/spikecodes/libreddit)** - Interfaz alternativa para Reddit libre de publicidad y tracking (modo lectura)
- **[Invidious](https://github.com/iv-org/invidious)** - Interfaz alternativa para YouTube que respeta la privacidad

### Multimedia y Entretenimiento

- **[Jellyfin](https://jellyfin.org/)** - Servidor multimedia libre para organizar y streaming de películas, series y música
- **[Soulseek](https://www.slsknet.org/)** - Cliente para la red P2P Soulseek especializada en compartir música
- **[youtube-dl](https://github.com/ytdl-org/youtube-dl)** - Herramienta para descargar videos y audio de YouTube y otros sitios
- **[Photoprism](https://www.photoprism.app/)** - Servicio de gestión y visualización de fotos personales con funciones de IA

### Productividad y Organización

- **[Nextcloud](https://nextcloud.com/)** - Plataforma de colaboración y almacenamiento en la nube auto-alojado
- **[Linkding](https://github.com/sissbruecker/linkding)** - Marcador social para guardar y organizar enlaces web
- **[GitBucket](https://gitbucket.github.io/)** - Plataforma Git auto-alojada similar a GitHub
- **[SearXNG](https://github.com/searxng/searxng)** - Metabuscador privado que agrega resultados de múltiples motores de búsqueda

### Seguridad y Contraseñas

- **[Vaultwarden](https://github.com/dani-garcia/vaultwarden)** - Implementación alternativa del gestor de contraseñas Bitwarden, más ligera y eficiente

### Automatización del Hogar

- **[Home Assistant](https://www.home-assistant.io/)** - Plataforma de domótica de código abierto para automatizar y controlar dispositivos del hogar
- **[Homebridge](https://homebridge.io/)** - Puente que permite integrar dispositivos no compatibles con el ecosistema Apple HomeKit
- **[Camera.UI](https://github.com/camera-ui/camera-ui)** - Aplicación para gestionar y visualizar cámaras de seguridad con integración HomeKit

### Utilidades y Mantenimiento

- **[Homepage](https://github.com/gethomepage/homepage)** - Dashboard personalizable como página de inicio para acceder a todos los servicios
- **[Watchtower](https://containrrr.dev/watchtower/)** - Servicio que actualiza automáticamente los contenedores Docker cuando hay nuevas versiones disponibles

## Ejercicios

### **Ejercicio1**

Modificar Dockerfile para que el usuario creado anteriormente pueda ejectuar sudo.

### Python

Crea 2 contenedores, uno con python 3.11 y otro con python 3.9

```bash
docker run -d --name python3.11 -v /tmp/php:/app python:3.11
```