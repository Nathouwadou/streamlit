import streamlit as st
st.title("Quel homme êtes-vous ?")

taille = 0
poid =0
BF = 0
pilo =0

placeholder = st.empty()

with placeholder.container():
    age = st.number_input("Entrez votre age en année", value=None, placeholder="Age...")
    poid = st.number_input("Entrez votre poid en kilogramme", value=None, placeholder="Poid...")
    st.image('BF.png', width=330)
    BF = st.number_input("En vous aidant de la photo ci-dessus, entrez votre taux de masse grasse en pourcentage", value=None, placeholder="Body fat...")
    taille = st.number_input("Entrez votre taille en centimetre", value=None, placeholder="Taille...")
    pilo = st.number_input("Entrez votre pilosité sur une echelle de 0 à 100, 0 correspondant à une absence totale de poil et 100 à un corps entierement couvert de fourrure", value=None, placeholder="Pilosité...")
  

if st.button('Valider'):
    IMC = poid/(0.01*taille)**2
    twinkness = 190-age-3*IMC
    daddyness = age+0.8*pilo
    chadness = 4.5*IMC/(0.1*BF)
    placeholder.empty()
    if age>64:
        st.write('Vous êtes un boomer, il faut baisser les retraites géantes des boomers.')
    elif twinkness>=98 and chadness<=73:
        st.image('twink.png')
    elif twinkness>=98 and chadness>73:
        st.image('twunk.png')
    elif chadness >86 and daddyness<60:
        st.image('gigachad.png')
    elif chadness >86 and daddyness>=60:
        st.image('daddychad.png')
    elif chadness <=86 and daddyness>60 and IMC<24:
        st.image('daddy.png')
    elif chadness <=86 and daddyness>60 and IMC>=24:
        st.image('bears.png')
    elif daddyness>49 :
        st.image('bears.png')
    else :
        st.image('inclas.png')

  
