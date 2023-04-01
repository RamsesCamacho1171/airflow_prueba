# Docker

La tecnología Docker utiliza el kernel de Linux y sus funciones, como los grupos de control y los espacios de nombre, para dividir los procesos y ejecutarlos de manera independiente. El propósito de los contenedores es ejecutar varios procesos y aplicaciones por separado para que se pueda aprovechar mejor la infraestructura y, al mismo tiempo, conservar la seguridad que se obtendría con los sistemas individuales.

Las herramientas de los contenedores, como Docker, proporcionan un modelo de implementación basado en imágenes. Esto permite compartir fácilmente una aplicación o un conjunto de servicios, con todas las dependencias en varios entornos. Docker también automatiza la implementación de las aplicaciones (o los conjuntos de procesos que las constituyen) en el entorno de contenedores.

Estas herramientas están diseñadas a partir de los contenedores de Linux, por eso la tecnología Docker es sencilla y única. Además, ofrecen a los usuarios acceso sin precedentes a las aplicaciones, la posibilidad de realizar implementaciones en poco tiempo y el control sobre las versiones y su distribución.

# contenedor

Un contenedor de Linux® (Linux container) es un conjunto de uno o más procesos separados del resto del sistema. Todos los archivos que se necesitan para ejecutarlos provienen de una imagen diferente, lo cual significa que los contenedores de Linux se pueden trasladar desde la etapa de desarrollo hasta la de prueba y producción, sin perder uniformidad.

# Diferencia entre los contenedores y la virtualización

¿Los contenedores son simplemente una virtualización? No exactamente, considérelo más como un complemento. A continuación, encontrará una forma sencilla de comprenderlos:

- La virtualización permite que sus SO (Windows o Linux) se ejecuten simultáneamente en un solo sistema de hardware.
- Los contenedores comparten el mismo kernel del sistema operativo y separan los procesos de las aplicaciones del resto del sistema. Por ejemplo, los sistemas Linux ARM ejecutan contenedores de Linux para ARM; los sistemas Linux x86 ejecutan contenedores de Linux para x86; y los sistemas Windows x86 ejecutan contenedores de Windows para x86. Los contenedores de Linux son muy portátiles, pero deben ser compatibles con el sistema subyacente.

# Comandos

Para vizualizar imagenes listadas:

```
docker images
```

si necesitamos ayuda podemos usar el comando help

```
docker --help
```

y sale toda la listota

```
Usage:  docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Options:
      --config string      Location of client config files (default "/home/desarrollo/.docker")
  -c, --context string     Name of the context to use to connect to the daemon (overrides DOCKER_HOST env var and default context set with "docker context use")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket(s) to connect to
  -l, --log-level string   Set the logging level ("debug"|"info"|"warn"|"error"|"fatal") (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default "/home/desarrollo/.docker/ca.pem")
      --tlscert string     Path to TLS certificate file (default "/home/desarrollo/.docker/cert.pem")
      --tlskey string      Path to TLS key file (default "/home/desarrollo/.docker/key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Management Commands:
  app*        Docker App (Docker Inc., v0.9.1-beta3)
  builder     Manage builds
  buildx*     Docker Buildx (Docker Inc., v0.10.0-docker)
  compose*    Docker Compose (Docker Inc., v2.15.1)
  config      Manage Docker configs
  container   Manage containers
  context     Manage contexts
  image       Manage images
  manifest    Manage Docker image manifests and manifest lists
  network     Manage networks
  node        Manage Swarm nodes
  plugin      Manage plugins
  scan*       Docker Scan (Docker Inc., v0.23.0)
  secret      Manage Docker secrets
  service     Manage services
  stack       Manage Docker stacks
  swarm       Manage Swarm
  system      Manage Docker
  trust       Manage trust on Docker images
  volume      Manage volumes

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  build       Build an image from a Dockerfile
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  events      Get real time events from the server
  exec        Run a command in a running container
  export      Export a container's filesystem as a tar archive
  history     Show the history of an image
  images      List images
  import      Import the contents from a tarball to create a filesystem image
  info        Display system-wide information
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  login       Log in to a Docker registry
  logout      Log out from a Docker registry
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  ps          List containers
  pull        Pull an image or a repository from a registry
  push        Push an image or a repository to a registry
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  run         Run a command in a new container
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  search      Search the Docker Hub for images
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  version     Show the Docker version information
  wait        Block until one or more containers stop, then print their exit codes

Run 'docker COMMAND --help' for more information on a command.

To get more help with docker, check out our guides at https://docs.docker.com/go/guides/

```

para mas especifico pones docker **comando** --help y pos ya sale

# Crear contenedores

La forma mas basica de crear un contenedor es:

```
docker run ubuntu
```

eso creara un contenedor de ubuntu pero no lo inicia y si no tienes la imagen la va a descargar por ti del docker hub

```
https://hub.docker.com/
```

si solo quisieras bajar una imagen se utiliza:

```
docker pull **nombre de la imagen** -> docker pull mysql
```

el nombre y las versiones de las imagenes estan dentro de la informaciond de la imagen de docker hub

# Imagenes

Las imagenes de docker estan creadas en base de distintas imagenes (layers)
y estas imagenes son de solo lectura, es decir si nosotros tenemos la imagen de ubuntu, que en la fecha que escribo esto, su imagen solo contiene un layer que es de solo lectura y con todo eso pesa 124mb, si creamos 3 contenedores no tendriamos 372mb, solo tendriamos 124 porque todos los contenedores apuntan a la misma imagen.

Cada conetendor cuando se crea cuenta con un layer temporal donde se generaran nuestros cambios y asi le almacenaran las cosas que vayamos agregando y si llegaramos a borrar la imagen este layer temporal de muere (a menos de que lo persistamos dentro de otra imagen).

## creacion basica de imagen

regrasando al ejemplo de ubuntu, esta imagen viene casi sin nada instalado entonces si necesitaramos mas cosas tendriamos que instalarlas por nuestra propia cuenta.

por ejemplo el cambio mas basico seria realizar un apt-get update
que ya nos incrementaria la memoria del contenedor, para poder ver ese incremento usamos el comando:

```
docker ps -s
CONTAINER ID  IMAGE COMMAND  CREATED             STATUS         PORTS  NAMES        SIZE
a6c6cae99dc2  ubuntu "bash"  About an hour ago  Up 27 minutes          ubu1    46.4MB (virtual 124MB)
```

aqui podemos ver que nuestra imagen tiene un peso de 124mb, y el contenedor de 46mb con los cambios ya hechos.

un comando que podemos usar para ver que cambios se han hecho es

```
docker diff <contenedor>

A- nuevo
C- cambio
D- borrado
```

si quiseramos crear una iamgen rapida de este conetendor se haria con el siguiente comando:

```
docker commit <contenedor> <nombre_imagen> -> docker commit ubu1 mi_ubuntu
```

cuando creamos una nueva imagen se añaden mas layer, en este caso como ubuntu tenia 1, ahora se le añade el otro layer que teniamos para agregar mas cosas,
entonces cuando creemos nuevas imagenes basadas en esta, los contenedores apuntaran a esta. Cabe aclarar que el crear imagenes si hace que ocupemos mas espacio en memoria.

## dockerfile

Lo ideal para crear imagenes nuevas es utilizar un dockerfile, ya que si las creamos en consola no tendremos un control preciso de los cambios realizados, ademas no podremos contar con un control de versiones de nuestras imagenes.

un ejemplo sencillo es el siguiente:

```
FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3
```

este codigo se va a guardar dentro de un archivo llamado **Dockerfile** y los que nos esta indicando que de la imagen de ubuntu va a ejecutar los siguientes comandos:

- apt-get update
- apt-get install -y python3

estos comandos deben ser automaticos y ni interactivos.

Ahora para correr el documento utilizaremos el comando:

```
docker build -t imagen_python .
```

le estamos diciendo que cree una imagen con el nombre imagen_python y que busqie el archivo dockerfile en el directorio actual.

Para la creacion de la imagen creara un primer un contenedor que correra el primer run, luego lo borra y crea un segundo contenedor para el segundo,
entonces nuestra imagen tendria 3 layer, es como si hubiera hecho 2 commit.

ahora otro ejemplo:

```
FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3
RUN echo 1.0 >> /etc/version && apt-get install -y git \
    && apt-get install -y iputils-ping
```

lo que estamos haciendo es agrupar distintos comandos dentro del ultimo run ya que si los fueramos añadiendo cada uno en un run tendria muchas capas inecesarias
entonces podemos anidar varias tareas en un mismo run.

lo que nos indican los caracteres es:

    * && indica la separacion entre cada instruccion
    * \ nos indica un salto de linea

## CMD

Solo puede existir un cmd en un docker file que es para ejecutar comandos.
Ejecutan una shell (bin/bash)

ejemplo:

```
FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3
RUN echo 1.0 >> /etc/version && apt-get install -y git \
    && apt-get install -y iputils-ping
CMD echo "bienvenido papu"
```

en este caso tenemos lo mismo del ejemplo anterior, pero añadimos el cmd, lo que indica que ejecutara el comando que mostrara el "bienvenido papu".

este comando se ejecuta creando una shell

otro ejemplo

```
FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3
RUN echo 1.0 >> /etc/version && apt-get install -y git \
    && apt-get install -y iputils-ping
CMD ["echo","Hola bebe"]
```

en este caso la unica diferencia es que a la hora de ejecutar no depende de una shell

por lo que entendi es que ejecuta directamente el comando y no atravez de una bash

otro ejemplo:

```
FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3
RUN echo 1.0 >> /etc/version && apt-get install -y git \
    && apt-get install -y iputils-ping
CMD /bin/bash
```

lo que tenemos aqui es que le estamos indicando que cuando ejecutemos el contenedor nos corra la bash, pero esto en teoria esta mal.

con el comando docker image history **<nombre:imagen>** podemos ver los cambios de nuestras imagenes, veamos el cambio de la imagen creada:

```
docker image history image:v1
IMAGE          CREATED         CREATED BY                                      SIZE      COMMENT
9b96cfea49db   2 minutes ago   /bin/sh -c #(nop)  CMD ["/bin/sh" "-c" "/bin…   0B
640c5bd8e762   3 days ago      /bin/sh -c echo 1.0 >> /etc/version && apt-g…   75MB
c628dd3ecc13   4 days ago      /bin/sh -c apt-get install -y python3           30MB
c18bad246d1f   4 days ago      /bin/sh -c apt-get update                       42.4MB
6b7dfa7e8fdb   3 months ago    /bin/sh -c #(nop)  CMD ["bash"]                 0B
<missing>      3 months ago    /bin/sh -c #(nop) ADD file:481dd2da6de715252…   77.8MB
```

lo que hace el ultimo punto es llamar desde el /bin/bash -c a otra vez al /bin/bash, estamos llamando a una bash desde una shell y eso estaria mal. lo ideal habria sido ponerlo en formato json como el de la penultima linea.(en este caso funciona igual, pero en otro caso podria dar algun error)

entonces seria:

```
FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3
RUN echo 1.0 >> /etc/version && apt-get install -y git \
    && apt-get install -y iputils-ping
CMD ["/bin/bash"]


docker image history image:v1
IMAGE          CREATED         CREATED BY                                      SIZE      COMMENT
5853105f6e49   3 seconds ago   /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B
640c5bd8e762   3 days ago      /bin/sh -c echo 1.0 >> /etc/version && apt-g…   75MB
c628dd3ecc13   4 days ago      /bin/sh -c apt-get install -y python3           30MB
c18bad246d1f   4 days ago      /bin/sh -c apt-get update                       42.4MB
6b7dfa7e8fdb   3 months ago    /bin/sh -c #(nop)  CMD ["bash"]                 0B
<missing>      3 months ago    /bin/sh -c #(nop) ADD file:481dd2da6de715252…   77.8MB
```

## ENTRYPOINT

ejecuta algo cuando corremos el contendor al igual que el cmd, pero a diferencia de cmd nos permite "blindar" ese comando, es decir cuando se corra el contenedor se ejecute siempre. Con cmd no pasa eso.

**nota**
Si nostros ponemos a la hora de correr un contenedor= docker run -it --rm image:v2 ls
estariamos sustituyendo el comando que asignamos(en este caso bash) por ls:

```
docker run -it --rm image:v2 ls
bin   dev  home  lib32  libx32  mnt  proc  run   srv  tmp  var
boot  etc  lib   lib64  media   opt  root  sbin  sys  usr
```

Esto solo pasa cuando utilizamos cmd, con entrypoit no.

```
FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3
RUN echo 1.0 >> /etc/version && apt-get install -y git \
    && apt-get install -y iputils-ping
ENTRYPOINT ["/bin/bash"]

este solo se debe ejecuta en formato json. Se puede en formato shell, pero no lo hagas
```

**nota** puedes poner

```
docker rmi ==> docker image rm
```

ejecucion de contenedor sobrescribiendo:

```
docker run -it --rm image:v2 ls
/usr/bin/ls: /usr/bin/ls: cannot execute binary file
```

le esta concatenando el ls a nuestro comando ya predefinido

ejemplo:

```
FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3
RUN echo 1.0 >> /etc/version && apt-get install -y git \
    && apt-get install -y iputils-ping
ENTRYPOINT ["df"]
```

si corremos el contenedor y añadimos por ejemplo --help el resultado es:

```
docker run -it --rm image:v2 --help
Usage: df [OPTION]... [FILE]...
Show information about the file system on which each FILE resides,
or all file systems by default.

Mandatory arguments to long options are mandatory for short options too.
  -a, --all             include pseudo, duplicate, inaccessible file systems
  -B, --block-size=SIZE  scale sizes by SIZE before printing them; e.g.,
                           '-BM' prints sizes in units of 1,048,576 bytes;
                           see SIZE format below
  -h, --human-readable  print sizes in powers of 1024 (e.g., 1023M)
  -H, --si              print sizes in powers of 1000 (e.g., 1.1G)
  -i, --inodes          list inode information instead of block usage
  -k                    like --block-size=1K
  -l, --local           limit listing to local file systems
      --no-sync         do not invoke sync before getting usage info (default)
      --output[=FIELD_LIST]  use the output format defined by FIELD_LIST,
                               or print all fields if FIELD_LIST is omitted.
  -P, --portability     use the POSIX output format
      --sync            invoke sync before getting usage info
      --total           elide all entries insignificant to available space,
                          and produce a grand total
  -t, --type=TYPE       limit listing to file systems of type TYPE
  -T, --print-type      print file system type
  -x, --exclude-type=TYPE   limit listing to file systems not of type TYPE
  -v                    (ignored)
      --help     display this help and exit
      --version  output version information and exit
```

cocatena al df nuestro --help

```
docker run -it --rm image:v2 siuuu
df: siuuu: No such file or directory
```

Entonces con cmd podemos modificar ese comando de arranque, con entrypoint nos ata a ese comando.
