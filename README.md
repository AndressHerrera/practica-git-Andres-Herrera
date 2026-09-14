Andres Manuel Herrera Compean
2630420

Practica: Creación y sincronización de repositorios con Git y GitHub

OBJETIVO
Crear un repositorio local utilizando Git, sincronizarlo con un repositorio remoto en GitHub y comprobar el flujo de trabajo en ambos sentidos:
Repositorio local → GitHub
GitHub → Repositorio local

Descripción del procedimiento realizado: 
1-Crear la carpeta del proyecto
Se creó una carpeta local en el Escritorio llamada practica-git-Andres-Herrera, destinada a contener los archivos del repositorio.
2-Inicializar el repositorio local
Dentro de esa carpeta se ejecutó git init, lo que convirtió la carpeta en un repositorio Git, generando la subcarpeta oculta .git que da seguimiento a los cambios.
3-Configurar exclusiones con .gitignore
Se creó un archivo .gitignore con la línea .ssh/, para excluir del control de versiones la carpeta que contiene las llaves SSH, evitando que credenciales privadas se suban al repositorio.
4-Agregar los archivos del proyecto
Se colocaron dentro de la carpeta los archivos correspondientes a la tarea (README.md y datos.txt).
5-Vincular el repositorio remoto
Se ejecutó git remote add origin seguido de la URL del repositorio creado previamente en GitHub, estableciendo la conexión entre el repositorio local y el remoto.
6-Preparar los cambios (staging)
Se usó git add README.md datos.txt .gitignore para marcar los archivos como listos para ser confirmados.
7-Confirmar los cambios (commit)
Se ejecutó git commit -m "primer commit" para guardar una instantánea de los cambios preparados, junto con un mensaje descriptivo.
8-Subir los cambios a GitHub (push)
Finalmente se ejecutó git push -u origin main, subiendo los archivos al repositorio remoto y estableciendo el seguimiento entre la rama local main y la rama main de origin.

Comandos de Git utilizados
git init
git status
git remote add origin <url>
git remote -v
git add <archivo>
git commit -m "mensaje"
git branch -M main
git push
git pull

Explicación breve de la función de cada comando

git init: inicializa un repositorio Git dentro de la carpeta actual, creando la subcarpeta oculta .git que almacena todo el historial de versiones.
git status: muestra el estado actual del repositorio — qué archivos han cambiado, cuáles están preparados para el commit y cuáles aún no están siendo rastreados por Git.
git remote add origin <url>: establece la conexión entre el repositorio local y un repositorio remoto (en este caso, uno alojado en GitHub), identificándolo con el nombre origin.
git remote -v: muestra las URLs de los repositorios remotos configurados, permitiendo verificar que la conexión (origin) apunte a la dirección correcta tanto para descarga como para subida.
git add <archivo>: mueve los cambios de un archivo al área de preparación (staging area), marcándolos como listos para ser incluidos en el siguiente commit.
git commit -m "mensaje": guarda una instantánea permanente de los cambios preparados, junto con un mensaje descriptivo de lo que se modificó.
git branch -M main: renombra la rama actual a main, asegurando que coincida con el nombre de la rama principal del repositorio remoto.
git push: envía los commits guardados localmente hacia el repositorio remoto en GitHub.
git pull: descarga y combina en el repositorio local los cambios que existan en el repositorio remoto.

Cómo se creó el repositorio local

Cree una carpeta en el equipo destinada a contener el proyecto. Dentro de esa carpeta se ejecutó el comando git init, lo cual convirtió la carpeta en un repositorio Git, habilitando el seguimiento de cambios en los archivos que se agregaran posteriormente.

Cómo se vinculó el repositorio local con GitHub

Cree un repositorio vacío en GitHub, obteniendo su URL de conexión. Con el repositorio local ya inicializado, se ejecutó git remote add origin <url>, indicándole a Git la dirección remota hacia la cual se enviarían los cambios. Esta conexión se verificó con git remote -v, confirmando la URL tanto para descarga (fetch) como para subida (push).

Sincronización Local → GitHub

Los archivos del proyecto se agregaron al área de preparación con git add, y se confirmaron con git commit -m "mensaje", generando así un registro de los cambios. Posteriormente, con git push -u origin main, esos commits se enviaron al repositorio remoto en GitHub, quedando disponibles y visibles en línea. el indicador -u establece además el seguimiento entre la rama local main y la rama main del remoto, de modo que en subidas futuras basta con escribir git push.

Sincronización GitHub → Local

En caso de que existan cambios realizados directamente en GitHub o desde otro equipo, estos se pueden traer al repositorio local mediante el comando git pull origin main. este comando descarga los cambios remotos y los combina automáticamente con el contenido local, manteniendo ambas copias sincronizadas.

Descripción de los archivos contenidos en el repositorio
README.md: archivo de descripción del proyecto, en formato Markdown.
datos.txt: archivo de texto plano utilizado como parte de la práctica.
.gitignore: archivo de configuración que le indica a Git qué carpetas o archivos debe ignorar; en este caso, excluye la carpeta .ssh/ para evitar exponer las llaves de acceso SSH del usuario.

CONCLUSION PERSONAL: 
Con esta tarea reforce lo aprendido en clase ya que no tuve que hacer nada que no haya hecho en clase, me quedo mas claro el funcionamiento de los comandos de git y al momento de escribir codigos los tendre guardados en github.En general, esta práctica me ayudó a entender mejor cómo se organiza un proyecto con control de versiones y por qué es tan usado en el desarrollo de software: permite tener un historial de cambios, trabajar de forma ordenada y sincronizar el trabajo entre distintos equipos sin perder información.
