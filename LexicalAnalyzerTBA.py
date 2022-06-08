import streamlit as st
import string
import pandas as pd

st.write("""
# Aplikasi Lexical Analyzer  TBA 
Dibuat oleh **Nuril Febri Setiyawan (1301218594)**
dan **Syahrul Ramadhani (1301218584)**""")
st.subheader("Daftar Kata yang tersedia: ")
d={'Kata':['ammak','mangge','andi','bayao','es','anganre','asare','angnginung','sapatu','jekne']}
df = pd.DataFrame(
    pd.DataFrame(data=d)
)

st.table(df)


sentence = st.text_input("Masukkan Kata: ", placeholder='Masukkan Kata')
cari=st.button('Cari')
if cari:
    input_string = sentence.lower()+ '#'

    alphabet_list = list (string.ascii_lowercase)
    state_list = ['q0','q1','q2','q3','q4',"q5",'q6','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16'
    ,'q17','q18','q19','q20','q21','q22','q23','q24','q25','q26','q27','q28','q29','q30','q31','q32']

    transition_table = {}

    for state in state_list:
        for alphabet in alphabet_list:
            transition_table[(state,alphabet)]= 'error'
            transition_table[(state,'#')] = 'error'
            transition_table[(state, ' ')]= 'error'
        transition_table['q0', ' ']='q0'

    #andi
    transition_table [('q0', 'a')] = 'q1'
    transition_table [('q1', 'n')] = 'q2'
    transition_table [('q2', 'd')] = 'q3'
    transition_table [('q3', 'i')] = 'q4'
    transition_table [('q4', ' ')] = 'q32'
    transition_table [('q4', '#')] = 'accept'
    transition_table [('q32', ' ')] = 'q32'
    transition_table [('q32', '#')] = 'accept'

    transition_table [('q32', 'a')] = 'q1'

    #asare
    transition_table [('q0', 'a')] = 'q1'
    transition_table [('q1', 's')] = 'q15'
    transition_table [('q15', 'a')] = 'q6'
    transition_table [('q6', 'r')] = 'q8'
    transition_table [('q8', 'e')] = 'q9'
    transition_table [('q9', ' ')] = 'q32'
    transition_table [('q9', '#')] = 'accept'
    transition_table [('q32', ' ')] = 'q32'
    transition_table [('q32', '#')] = 'accept'

    transition_table [('q32', 'a')] = 'q1'

    #es
    transition_table [('q0', 'e')] = 'q30'
    transition_table [('q30', 's')] = 'q31'
    transition_table [('q31', ' ')] = 'q32'
    transition_table [('q31', '#')] = 'accept'
    transition_table [('q32', ' ')] = 'q32'
    transition_table [('q32', '#')] = 'accept'

    transition_table [('q32', 'e')] = 'q30'

    #angnginung
    transition_table [('q0', 'a')] = 'q1'
    transition_table [('q1', 'n')] = 'q2'
    transition_table [('q2', 'g')] = 'q5'
    transition_table [('q5', 'n')] = 'q2'
    transition_table [('q2', 'g')] = 'q5'
    transition_table [('q5', 'i')] = 'q4'
    transition_table [('q4', 'n')] = 'q7'
    transition_table [('q7', 'u')] = 'q10'
    transition_table [('q10', 'n')] = 'q11'
    transition_table [('q11', 'g')] = 'q12'
    transition_table [('q12', ' ')] = 'q32'
    transition_table [('q12', '#')] = 'accept'
    transition_table [('q32', ' ')] = 'q32'
    transition_table [('q32', '#')] = 'accept'

    transition_table [('q32', 'a')] = 'q1'

    #sapatu
    transition_table [('q0', 's')] = 'q20'
    transition_table [('q20', 'a')] = 'q17'
    transition_table [('q17', 'p')] = 'q21'
    transition_table [('q21', 'a')] = 'q6'
    transition_table [('q6', 't')] = 'q22'
    transition_table [('q22', 'u')] = 'q23'
    transition_table [('q23', ' ')] = 'q32'
    transition_table [('q23', '#')] = 'accept'
    transition_table [('q32', ' ')] = 'q32'
    transition_table [('q32', '#')] = 'accept'

    transition_table [('q32', 's')] = 'q20'

    #jekne
    transition_table [('q0', 'j')] = 'q28'
    transition_table [('q28', 'e')] = 'q27'
    transition_table [('q27', 'k')] = 'q14'
    transition_table [('q14', 'n')] = 'q29'
    transition_table [('q29', 'e')] = 'q30'
    transition_table [('q30', ' ')] = 'q32'
    transition_table [('q30', '#')] = 'accept'
    transition_table [('q32', ' ')] = 'q32'
    transition_table [('q32', '#')] = 'accept'

    transition_table [('q32', 'j')] = 'q28'

    #ammak
    transition_table [('q0', 'a')] = 'q1'
    transition_table [('q1', 'm')] = 'q13'
    transition_table [('q13', 'm')] = 'q13'
    transition_table [('q13', 'a')] = 'q6'
    transition_table [('q6', 'k')] = 'q14'
    transition_table [('q14', ' ')] = 'q32'
    transition_table [('q14', '#')] = 'accept'
    transition_table [('q32', ' ')] = 'q32'
    transition_table [('q32', '#')] = 'accept'

    transition_table [('q32', 'a')] = 'q1'

    #mangge
    transition_table [('q0', 'm')] = 'q24'
    transition_table [('q24', 'a')] = 'q17'
    transition_table [('q17', 'n')] = 'q25'
    transition_table [('q25', 'g')] = 'q26'
    transition_table [('q26', 'g')] = 'q26'
    transition_table [('q26', 'e')] = 'q27'
    transition_table [('q27', ' ')] = 'q32'
    transition_table [('q27', '#')] = 'accept'
    transition_table [('q32', ' ')] = 'q32'
    transition_table [('q32', '#')] = 'accept'

    transition_table [('q32', 'm')] = 'q24'

    #bayao
    transition_table [('q0', 'b')] = 'q16'
    transition_table [('q16', 'a')] = 'q17'
    transition_table [('q17', 'y')] = 'q18'
    transition_table [('q18', 'a')] = 'q6'
    transition_table [('q6', 'o')] = 'q19'
    transition_table [('q19', ' ')] = 'q32'
    transition_table [('q19', '#')] = 'accept'
    transition_table [('q32', ' ')] = 'q32'
    transition_table [('q32', '#')] = 'accept'

    transition_table [('q32', 'b')] = 'q16'

    #anganre
    transition_table [('q0', 'a')] = 'q1'
    transition_table [('q1', 'n')] = 'q2'
    transition_table [('q2', 'g')] = 'q5'
    transition_table [('q5', 'a')] = 'q6'
    transition_table [('q6', 'n')] = 'q7'
    transition_table [('q7', 'r')] = 'q8'
    transition_table [('q8', 'e')] = 'q9'
    transition_table [('q9', ' ')] = 'q32'
    transition_table [('q9', '#')] = 'accept'
    transition_table [('q32', ' ')] = 'q32'
    transition_table [('q32', '#')] = 'accept'

    transition_table [('q32', 'a')] = 'q1'

    #Lexical Analisis
    idx_char = 0 #huruf yg pertama kali di proses adalah huruf yg paling kiri
    state = 'q0'
    current_token = ''

    #Proses 1/1 hurufnya
    while state !='accept':
        current_char = input_string [idx_char]
        current_token += current_char
        state = transition_table [(state, current_char)]

        if state=='q32':
            st.write('current token : ', current_token, 'VALID')
            current_token=''
            
        if state == 'error':
            st.write('error')
            break;
        idx_char = idx_char + 1

    if state == 'accept':
        st.write('Semua Token Diinput : ', sentence, 'VALID')