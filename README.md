## TFM-K-School

# Financial Product Sales Forecast Model

1. STRUCTURE OF THE REPOSITORY

2. MOTIVATION
I have been working in banking sector for 23 years.  During these years I have gone through all possible categories within a private network office open to consumers.  From cash desk salesman, table salesman to office management.  Banks, understood as simple mediators or channelers of wealth between the different actors in society, have changed. They have undergone a transformation, have evolved and have adapted to all times, economic circumstances and customer's way of thinking.  As a result of the various economic crises experienced, the reduction of interest rates and therefore the profits obtained by these concepts, the pure business of collecting and lending money has ceased to be the only motivation for this business.  The sale of other financial products such as investment funds, pension plans and risk insurance, among others, have managed to capture all the importance. The bank has specialized in this type of products, directing all its power and commercial strategy to the sale of these products by means of the specialized advice to its clients on the part of the employees of the branches.

3. OBJECTIVES AND CHOICE OF MODEL
The Funds, Plans and Insurance of Risk commercialized in banking offices as well as their maintenance in portfolio during 5 years on average, are of great importance within the account of results of an office and by extension of a bank.   In this scenario and through a set of data belonging to 450,000 customers I wanted to develop a predictive model of purchase of these financial products.  A predictive classification model that helps the entire commercial force of the branches to orient the commercialization, to optimize the times, methodologies and systems used. All this in pursuit of greater sales success and customer satisfaction.

4. DATA 
The data comes from the sum of different data sets obtained directly from the financial institution. ALL DATA HAS BEEN ANONYMIZED. NAMES AND NUMBER OF INTERNAL CLIENTS HAVE BEEN REMOVED, NUMBER AND SPECIFICATIONS OF AREA AND OFFICE ADDRESSES HAVE BEEN REMOVED AND FINALLY NUMBER OF ASSIGNMENT AND NAME OF COMMERCIAL MANAGER HAVE BEEN REMOVED.  All these data have been assigned a fictitious identification number, leaving only the data of holding or not holding product by customers.

5. EXPLANING DATA SET
DZ
Identificación Dirección de Zona a la que pertenece la oficina.
Una Dirección de Zona engloba varias oficinas
•	11 Direcciones de Zona
OFICINA
Numero de Oficina / Sucursal de banco
PERSONA
Numero de cliente
EDAD
Edad del cliente
ESTA_CARTERIZADO
Identifica si el cliente pertenece o no a una cartera.
CARTERA_PATRON
Tipo de cartera a la que pertenece el cliente.
•	Asesoramiento Financiero
•	Tutela = Familiar de cliente Asesoramiento Financiero
CLIENTE_BBP
Cliente con saldos superiores a 500.000€ identificado como colectivo Banca Privadal.  	
GESTOR
Numero identificación del gestor/ Asesor Financiero de la sucursal
TIP_GESTOR
Tipo de gestor
CODIGO_CARTERA
Numero identificación cartera a la que pertenece el cliente.
MARCA_AF_CCTE
Identifica tipo de gestor
•	AF- Asesor Financiero (Oficina)
•	CCTE – Gestor Online	
MARCA_BANCA_PERSONAL
Cliente perteneciente a cartera Asesoramiento Financiero e  identificado como colectivo Banca Personal.  	
SEGMENTO_RECORRIDO
Identifica el potencial recorrido del cliente para una mayor vinculación.
•	Alto Recorrido
•	Medio Recorrido
•	Bajo Recorrido
SEGMENTO_VALOR
Valor del cliente
CAMINO_DIGITAL 
Se diferencian 4 tipo de clientes según la utilización de canales digitales. 
•	Comprador
•	Consultivo
•	Transaccional
•	Poco uso.
DIGITAL_3_MESES
Identifica si el cliente ha utilizado medios digitales durante los últimos 3 meses.
LP_DOMIC_INGRESOS
Tiene o no tiene ingresos domiciliados
LP_OFIC_INTERNET
Tiene o no tiene servicio internet
LP_REC_LTGA_OTR
Tiene o no tiene recibos domiciliados
LP_SEG_ACCIDENT
Tiene o no tiene seguro accidentes contratado
LP_SEG_AUTO
Tiene o no tiene seguro automóvil contratado
LP_SEG_MEDICOS
Tiene o no tiene seguro salud privado contratado
LP_SEG_MULTIRRIES
Tiene o no tiene seguro hogar contratado
LP_SEG_VIDA
Tiene o no tiene seguro vida contratado
LP_TARJ_CREDITO
Tiene o no tiene tarjeta crédito pago fin de mes contratada
LP_TARJ_REVOLVING
Tiene o no tiene tarjeta crédito pago fraccionado contratada
SF_AH_CAPTACION_TT
Saldo en cuenta de ahorro
SF_FINANCIACION_TT
Importe financiación en activo. 
SF_FONDOS_INVER
Saldo en Fondo de Inversion
SF_PLAN_PENSION
Saldo Plan de Pension



6. VISUALIZATION
