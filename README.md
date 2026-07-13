

```markdown
# 🏺 Craft Mich - Desarrollo Web Integral (UTM)

Bienvenido al repositorio oficial de **Craft Mich**, el catálogo digital de artesanías de Michoacán. Este proyecto está desarrollado en Django como parte de la **Etapa 3: Diseño y Desarrollo**.

---

## 👥 Roles y Responsabilidades del Equipo

Para cumplir con los criterios de evaluación y asegurar que todos los integrantes tengan responsabilidades asignadas, nos dividiremos el desarrollo de la siguiente manera:

*   **Cristopher (Líder de Proyecto / @Cris786-code):** Inicialización del entorno, configuración del repositorio en GitHub, estructura base de Django y control de versiones.
*   **Mariana:** Diseño y desarrollo del Frontend. Creación de la plantilla global (`base.html`) y las vistas del catálogo (`index.html`, `catalogo.html`, `nosotros.html`) alineadas con los Mockups originales.
*   **Emiliano:** Configuración de la persistencia de datos. Creación de los modelos en `models.py` (Categorías, Productos, Reseñas y Estados/Municipios).
*   **Héctor:** Configuración y personalización del Panel de Administración de Django (`admin.py`), carga de datos iniciales de prueba (artesanías de barro, textil y cerámica) y optimización de filtros.

---

## 🚀 Guía de Inicio Rápido para el Equipo

### 1. Cómo clonar el repositorio (Solo la primera vez)
Abran la terminal en su computadora, naveguen hasta la carpeta donde guardan sus proyectos escolares y ejecuten:
```bash
git clone [https://github.com/Cris786-code/craft-mich.git](https://github.com/Cris786-code/craft-mich.git)
cd craft-mich

```

### 2. Configurar el Entorno Virtual

Para trabajar de forma aislada sin romper nada, sigan estos pasos en su terminal:

* **Crear el entorno virtual:**
```bash
python -m venv venv

```


* **Activar el entorno:**
* *En Windows (PowerShell):* `.\venv\Scripts\Activate.ps1`
* *En Windows (CMD):* `.\venv\Scripts\activate.bat`
* *En Linux/Mac/Project IDX:* `source venv/bin/activate`


* **Instalar Django:**
```bash
pip install django

```



### 3. Levantar el Servidor de Pruebas

Una vez instalado, verifiquen que todo funcione corriendo el proyecto de forma local:

```bash
python manage.py migrate
python manage.py runserver

```

Abran su navegador en `http://127.0.0.1:8000/` para ver el sitio.

---

## 🛠️ Cómo mandar actualizaciones a GitHub (Reglas de Oro)

Para cumplir estrictamente con el requerimiento de **"Incluir en las actualizaciones el nombre del responsable del cambio"**, cada vez que terminen una tarea sigan este flujo de comandos:

1. **Bajar cambios de los demás (Para evitar conflictos):**
```bash
git pull origin main

```


2. **Preparar tus archivos modificados:**
```bash
git add .

```


3. **Hacer el Commit con tu NOMBRE entre corchetes (OBLIGATORIO):**
* *Ejemplo si eres Mariana:* `git commit -m "[Mariana] Creadas las plantillas del catálogo y barra de navegación"`
* *Ejemplo si eres Emiliano:* `git commit -m "[Emiliano] Agregados los modelos de Barro, Textil y Cerámica"`
* *Ejemplo si eres Héctor:* `git commit -m "[Héctor] Filtros por municipio listos en el Django Admin"`


4. **Subir tus cambios a la nube:**
```bash
git push origin main

```



---

## 📸 Recordatorio para el Reporte Final (Capturas de Pantalla)

Antes de enviar la tarea, cada integrante debe asegurarse de tener:

1. Una captura de pantalla de su propia terminal ejecutando el comando `git commit` donde aparezca su nombre.
2. Una captura de la lista de Commits en la web de GitHub para demostrar la participación de todos.

```

---

### ¿Cómo subir este README a tu GitHub de una vez?
Crea el archivo `README.md` en tu IDE, pega el código anterior, guarda y ejecuta estos comandos en tu terminal:

```bash
git add README.md
git commit -m "[Cris] Agregado el archivo README explicativo con roles del equipo"
git push origin main

```
