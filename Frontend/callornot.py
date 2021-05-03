import pickle
import streamlit as st

st.markdown("<h1 style='text-align: center; color: black;'>Call Or Not</h1>", unsafe_allow_html=True)

st.image('./imagenhogar.png')
st.subheader("Por favor, rellena el Cuestionario")

 
# Cargamos el modelo
pickle_in = open('clfforest_gs.pkl', 'rb') 
clasificador = pickle.load(pickle_in)

# Definimos la función que realizará la predicción a partir de los datos que introduzcamos en el cuestionario.  
def prediccion (edad, marca_bp, seg_valor, seg_recorrido, marca_ccte, camino_digital,
              saldo_ffii, saldo_plp, lp_dom_ingresos, lp_rbos,
              lp_seg_vida ,lp_seg_auto ,lp_seg_acc, lp_tjta_cto, lp_tjt_rev,
              saldo_captacion, saldo_financiacion ):   
    
     
    
    #Nº1--------------------------------------
    edad == edad
    
    #Nª2--------------------------------------
    if marca_bp == "NO":
        marca_bp = 0
    else:
        marca_bp = 1
        
    #Nª3--------------------------------------    
    if seg_valor ==   "ALTO":
        seg_valor = 0
    elif seg_valor == "MEDIO":
        seg_valor = 2
    else:
        seg_valor = 1  
        
    #Nª4--------------------------------------
    if seg_recorrido ==   "ALTO":
        seg_recorrido = 0
    elif seg_recorrido == "MEDIO":
        seg_recorrido = 2
    elif seg_recorrido == "BAJO":
        seg_recorrido = 1   
    else:
        seg_recorrido = 3
        
    #Nª5--------------------------------------    
    if marca_ccte ==   "AF":
        marca_ccte = 0
    elif marca_ccte == "CCTE":
        marca_ccte = 2
    else:
        marca_ccte = 1 
    
    #Nª6--------------------------------------    
    if camino_digital ==   "SIN USO":
        camino_digital = 3
    elif camino_digital == "CONSULTIVO":
        camino_digital = 1
    elif camino_digital == "TRANSACCIONAL":
        camino_digital = 4
    elif camino_digital == "POCO USO":
        camino_digital = 2
    else:
        camino_digital = 0
        
    #Nª7--------------------------------------    
    if saldo_ffii == "NO":
        saldo_ffii = 0
    else:
        saldo_ffii = 1
        
    #Nª8--------------------------------------    
    if saldo_plp == "NO":
        saldo_plp = 0
    else:
        saldo_plp = 1
        
    #Nª9--------------------------------------    
    if lp_dom_ingresos == "NO":
        lp_dom_ingresos = 0
    else:
        lp_dom_ingresos = 1

    #Nª10--------------------------------------    
    if lp_rbos == "NO":
        lp_rbos = 0
    else:
        lp_rbos = 1

    #Nª11--------------------------------------    
    if lp_seg_vida == "NO":
        lp_seg_vida = 0
    else:
        lp_seg_vida = 1
    
    #Nª12--------------------------------------    
    if lp_seg_auto == "NO":
        lp_seg_auto = 0
    else:
        lp_seg_auto = 1
        
    #Nª13--------------------------------------    
    if lp_seg_acc == "NO":
        lp_seg_acc = 0
    else:
        lp_seg_acc = 1
    
    #Nª14--------------------------------------    
    if lp_tjta_cto == "NO":
        lp_tjta_cto = 0
    else:
        lp_tjta_cto = 1

    #Nª15--------------------------------------    
    if lp_tjt_rev == "NO":
        lp_tjt_rev = 0
    else:
        lp_tjt_rev = 1
        
    #Nª16--------------------------------------    
    saldo_captacion == saldo_captacion
    
    #Nª17--------------------------------------    
    saldo_financiacion == saldo_financiacion

        
    # Predicciones 
    prediccion = clasificador.predict( 
        [[edad, marca_bp, seg_valor, seg_recorrido, marca_ccte,
         camino_digital,saldo_ffii,saldo_plp,lp_dom_ingresos,
         lp_rbos,lp_seg_vida,lp_seg_auto,lp_seg_acc,lp_tjta_cto,
         lp_tjt_rev,saldo_captacion,saldo_financiacion]])
     
    if prediccion == 0:
        pred = 'NO LLAMES'
    else:
        pred = 'LLAMA'
    return pred


# Definicion del Cuestionario
edad = st.slider('Edad del Cliente', min_value=25, max_value=90)
#edad = st.number_input('Edad del Cliente')

saldo_captacion = st.number_input('Saldo en Cuenta del Cliente')
saldo_financiacion = st.number_input('Financiacion del Cliente')

seg_valor = st.selectbox('Segmento Valor', ['ALTO','MEDIO','BAJO'])
seg_recorrido = st.selectbox('Recorrido cliente',['ALTO ', 'MEDIO ', 'BAJO ','NO CALCULADO']) 
marca_ccte = st.selectbox('Tipo de Gestor',['ASESOR EN OFICINA', 'ASESOR EN INTERNET', 'SIN ASESOR'])
camino_digital = st.selectbox('Para que usa la APP internet',['COMPRADOR', 'CONSULTIVO', 'TRANSACCIONAL', 'POCO USO','SIN USO'])

marca_bp = st.radio('Es cliente Banca Personal', ['SI','NO'])
saldo_ffii = st.radio('Tiene Fondos de Inversion', ['SI','NO'])
saldo_plp = st.radio('Tiene Plan de Pension', ['SI','NO'])
lp_dom_ingresos = st.radio('Tiene domiciliados la nomina', ['SI','NO'])
lp_rbos = st.radio('Tiene domiciliados los recibos', ['SI','NO'])
lp_seg_vida = st.radio('Tiene seguro de vida', ['SI','NO'])
lp_seg_auto = st.radio('Tiene seguro de coche', ['SI','NO'])
lp_seg_acc = st.radio('Tiene seguro de accidentes', ['SI','NO'])
lp_tjta_cto = st.radio('Tiene tarjeta de credito', ['SI','NO'])
lp_tjt_rev = st.radio('Tiene revolving', ['SI','NO'])


# Prediccion Final.
if st.button("Prediccion"): 
        result = prediccion(edad, marca_bp, seg_valor, seg_recorrido, marca_ccte,
                 camino_digital,saldo_ffii,saldo_plp,lp_dom_ingresos,
                 lp_rbos,lp_seg_vida,lp_seg_auto,lp_seg_acc,lp_tjta_cto,
                 lp_tjt_rev,saldo_captacion,saldo_financiacion) 
        st.success('Resultado * {}'.format(result))
        
        
