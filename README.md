**Django Ecommerce**
*Tienda virtual*

## Pasos a seguir
    * Crear entorno virtual 
 > `python -m venv virtualenv_name`

    * Activar entorno virtual.
> `source virtualenv_name/Scripts/activate`

    * Instalar dependencias
> `pip install -r requirements.txt`

    * Crear migraciones
   > `python manage.py makemigrations`

    * Migrar a la BD
   > `python mange.py migrate`

    * Iniciar app
   > `python mange.py runserver`

       * Crear un superusuario
   > `python mange.py createsuperuser`


**Una tienda hecha con django. El admin podra agregar productos desde el panel, administrar usuarios, categorias, editar, en fin CRUD. **

**La pagina contiene un buscador donde por el nombre podra encontrar el producto solicitado.**

**El usuario logueado podra acceder al carrito, donde tendra un checkout de pagos. Tambien el usuario podra actualizar sus datos haciendo clic en su nombre en el navbar**

**Proximamente más opciones.**




# **Requirimientos**
* Python 3


