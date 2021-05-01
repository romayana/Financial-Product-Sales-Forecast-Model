# **Modelo Previsión Ventas Productos Financieros**

### **1. Motivación Personal**

Desde 1998 hasta la actualidad, he desarrollado mi vida profesional en una entidad financiera, principalmente en Banca de particulares. Durante estos 23 años he pasado por todas las categorías laborales posibles dentro de una oficina comercial abierta al consumidor.  Desde comercial de caja y de mesa,  a subdirector y director de oficina. En 2018, motivado por la búsqueda de nuevas habilidades, reciclaje laboral y personal, la adaptación a la nueva realidad de transformación digital y la necesidad de construir un plan alternativo debido a las inciertas perspectivas laborales,  huyendo de mi zona de confort decido cursar un Master en Bussines Analytics con la intención de aprender nuevas formas de análisis de negocio y poder ponerlas en práctica.   Durante el curso me doy cuenta que aun sin ninguna base de programación o informática, estadística o matemáticas, procediendo de una licenciatura de letras, había encontrado una motivación, una nueva parcela de estudio y un nuevo reto.  Decido continuar la formación con el **Master en Data Science de K-School**, recomendado por un antiguo profesor y siempre avisado de la dificultad técnica del mismo.  El resultado lo puedo definir en una frase.  **Intenso pero muy satisfecho y con ganas de continuar mi formación.**</p>


### **2. Datos**

Los datos con los que vamos a trabajar proceden de la suma de diferentes conjuntos de datos obtenidos directamente de la entidad financiera. TODOS LOS DATOS HAN SIDO ANONIMIZADOS. SE HAN ELIMINADO LOS NOMBRES Y EL NÚMERO DE CLIENTES INTERNOS, SE HAN ELIMINADO EL NÚMERO Y LAS ESPECIFICACIONES DE LAS DIRECCIONES DE ÁREA Y DE OFICINA Y, POR ÚLTIMO, SE HAN ELIMINADO LOS NOMBRES DE LOS ASESORES COMERCIALES. A todos estos datos se les ha asignado un número de identificación ficticio, quedando únicamente los datos de tenencia o no de producto por parte de los clientes.


### **3. Objetivos**

Los Seguros de Riesgo comercializados en las oficinas bancarias, así como su mantenimiento en cartera durante 5 años de media, son de gran importancia dentro de la cuenta de resultados de una oficina y por extensión de un banco. En este escenario y a través de un conjunto de datos pertenecientes a 450.000 clientes he querido desarrollar un modelo predictivo de compra de estos productos financieros concretando en los Seguros del Hogar.

### **4. Finalidad**

Generar un modelo predictivo de clasificación que ayude a toda la fuerza comercial de las sucursales a orientar la comercialización, a optimizar los tiempos, metodologías y sistemas utilizados. Todo ello en busca de un mayor éxito de ventas y satisfacción de los clientes

### **5. Importancia del problema a resolver**

La generación de comisiones es fundamental para la cuenta de resultados de la oficina y del banco.  Los seguros de hogar se quedan en cartera durante un periodo medio de 5 años. Cada seguro de hogar contratado deja una comisión directa del 15 %.  Esto sobre un seguro de hogar de prima media de 300€ supone 45€ de comisión anual.   Nuestra base de datos correspondiente únicamente a 162 oficinas y 450.000 clientes podría llegar a generar unas comisiones anuales de más de 17mm€ en caso de que todos los clientes que no disponen de seguro de hogar lo contratasen.  Solo con esta cifra y extrapolándola a un colectivo de clientes totales de 3 – 4 millones de clientes,  queda más que explicado la evidente y clara la necesidad de identificar potenciales clientes que sean susceptibles de contratar el seguro de hogar.  

### **6. Informacion del Repositorio**

El repositorio se estructura en   7 carpetas y 4 archivos. ( Según posición en repositorio )

Carpeta 1 – Códigos Python Limpieza y Unión 

Carpeta 2 – Códigos Python EDA Análisis Exploratorio

Carpeta 3 – Frontend.  Aplicación creada para nuestro modelo (APP CallorNot.)

Carpeta 4 – Imágenes .png guardadas de cada una de las gráficas construidas

Carpeta 5 – Memoria. Notebooks memoria & codigo y memoria simplificada.

Carpeta 6 – Códigos Python Modelos clasificación utilizados.

Carpeta 7 – Códigos Python Preprocesado

Archivo 1 – archivo .gitignore.  Archivos descartados en las actualizaciones del repositorio

Archivo 2 – Diccionario e información del significado de las variables

Archivo 3 – Memoria TFM. Documento word Memoria.

Archivo 4 – Readme con primera información del Trabajo y comunicación de expectativas


### **7. Requisitos Tecnicos**

Para ejecutar el código es necesario tener instalado Python versión 3.8 así como distintos paquetes o librerías.  Se recomienda tener instalada la Suite Anaconda donde se encontrarán preinstalados la mayoría de los paquetes y librerías que son necesarias. Adicionalmente sera necesaria la instalacion de los siguientes librerias:

•	Imbalanced learn - pip install imbalanced learn

•	pydotplus - pip install pydotplus

•	streamlit - pip install setreamlit

### **8. Guia y ejecución**

Paso 1. Clonar repositorio GitHub https://github.com/romayana/Financial-Product-Sales-Forecast-Model.git en carpeta local elegida.

Paso 2. Descargar base de datos:
A pesar de haberse Anonimizado toda la base de datos, se ha decidido que la misma no estará disponible en el repositorio de GitHub.  Para acceder a la base de datos ubicada en el Google Drive del propietario del TFM,   se tendrá que solicitar permiso y acceso a la misma  dirigiendo correo electrónico a manuelgonzalezprados@gmail.com el cual previa valoración de los fines y objetivos perseguidos podrá compartir el enlace con la persona solicitante.

Paso 3. Una vez compartido el acceso,  descargar y ubicar la carpeta entera llamada Origin_Data en la carpeta carpeta local donde se ha clonado el repositorio.

Paso 4. Ejecutar código con la siguiente secuencia y orden. Los archivos csv se irán guardando en cada una de las carpetas.

1º Carpeta Cleanning & Merging
 - _merging_data,ipynb 
 - _cleanning_data.ipynb

2º Carpeta Exploratory Data Analysis
 -	EDA.ipynb

3º Carpeta Preprocessing
 -	Preprocessing.ipynb

4º Carpeta Models
 -	Ejecutar los modelos.

5º Carpeta Frontend
 - Aplicación Callornot


