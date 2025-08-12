# Comandos de git
A continuacion se listaran los comandos mas utiles y comunes para trabajar con git y github

1. Agregar elementos o archivos creados. El punto significa que sea agregaran todos los elementos creados, si se desea agregar uno solo se cambia el punto por el nombre del archivo
``` bash
git add .
```

2. Realizar un commit: sirve para agregar tu contenido con un mensaje descriptivo de la tarea realizada
``` bash
git commit -m "Actualizacion TP1"
```

3. Ver el estado de los archivos en el repositorio: muestra los cambios realizados y los archivos que están listos para ser añadidos o confirmados
``` bash
git status
```

4. Ver el historial de commits: muestra una lista de los commits realizados en el repositorio
``` bash
git log
```

5. Clonar un repositorio: copia un repositorio remoto a tu máquina local
``` bash
git clone <url-del-repositorio>
```

6. Actualizar el repositorio local con los cambios del repositorio remoto
``` bash
git pull
```

7. Subir los cambios locales al repositorio remoto
``` bash
git push
```

## Comandos para trabajar con ramas

1. Crear una nueva rama
``` bash
git branch <nombre-de-la-rama>
```

2. Cambiar a una rama existente
``` bash
git checkout <nombre-de-la-rama>
```

3. Crear y cambiar a una nueva rama en un solo paso
``` bash
git checkout -b <nombre-de-la-rama>
```

4. Listar todas las ramas
``` bash
git branch
```

5. Fusionar una rama con la rama actual
``` bash
git merge <nombre-de-la-rama>
```

6. Eliminar una rama
``` bash
git branch -d <nombre-de-la-rama>
```

## ¿Qué pasa cuando realizamos un push desde una rama?

Cuando realizamos un `git push` desde una rama, los cambios locales de esa rama se suben al repositorio remoto en la misma rama. Esto significa que los cambios estarán disponibles en GitHub (u otro servicio remoto) para que otros colaboradores puedan verlos o trabajar con ellos.

Si la rama no existe en el repositorio remoto, Git creará automáticamente esa rama en el remoto.

## ¿Qué pasa cuando se realiza una pull request?

Una pull request (PR) es una solicitud para fusionar los cambios de una rama en otra (generalmente en la rama principal, como `main` o `master`). Los pasos típicos son:

1. Crear una rama local y realizar los cambios necesarios.
2. Subir la rama al repositorio remoto con `git push`.
3. En GitHub, abrir una pull request desde la rama creada hacia la rama principal.
4. Los colaboradores revisan los cambios, sugieren modificaciones si es necesario, y finalmente aprueban la PR.
5. Una vez aprobada, la PR se fusiona en la rama principal.

## ¿Qué hacer cuando se elimina una rama en GitHub?

Cuando una pull request se fusiona y la rama asociada se elimina en GitHub, es importante limpiar las ramas locales para evitar confusión. Los pasos son:

1. Verificar que estás en otra rama (por ejemplo, `main`):
   ```bash
   git checkout main
   ```

2. Eliminar la rama local que ya no existe en el remoto:
   ```bash
   git branch -d <nombre-de-la-rama>
   ```

3. Actualizar las referencias remotas para eliminar las ramas que ya no existen en el remoto:
   ```bash
   git fetch --prune
   ```

Esto asegura que tu repositorio local esté sincronizado con el remoto y no contenga ramas obsoletas.

## ¿Cómo resolver conflictos de merge?

Cuando dos ramas tienen cambios en las mismas líneas de un archivo, Git genera un conflicto al intentar fusionarlas. Para resolverlo:

1. Realiza el merge que genera el conflicto:
   ```bash
   git merge <nombre-de-la-rama>
   ```

2. Git marcará los archivos en conflicto. Abre los archivos afectados y busca las marcas de conflicto (`<<<<<<<`, `=======`, `>>>>>>>`).

3. Edita los archivos para resolver los conflictos, eligiendo o combinando los cambios necesarios.

4. Una vez resueltos, añade los archivos al área de preparación:
   ```bash
   git add <archivo-en-conflicto>
   ```

5. Finaliza el merge con un commit:
   ```bash
   git commit
   ```

## Comandos para trabajar con etiquetas (tags)

Las etiquetas se utilizan para marcar puntos específicos en el historial de commits, como versiones de un proyecto.

1. Crear una etiqueta ligera:
   ```bash
   git tag <nombre-de-la-etiqueta>
   ```

2. Crear una etiqueta anotada (recomendada para incluir información adicional como mensajes):
   ```bash
   git tag -a <nombre-de-la-etiqueta> -m "Mensaje de la etiqueta"
   ```

3. Listar todas las etiquetas:
   ```bash
   git tag
   ```

4. Subir una etiqueta al repositorio remoto:
   ```bash
   git push origin <nombre-de-la-etiqueta>
   ```

5. Subir todas las etiquetas al repositorio remoto:
   ```bash
   git push --tags
   ```

6. Eliminar una etiqueta local:
   ```bash
   git tag -d <nombre-de-la-etiqueta>
   ```

7. Eliminar una etiqueta en el remoto:
   ```bash
   git push origin --delete <nombre-de-la-etiqueta>
   ```

