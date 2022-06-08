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
    tokens = sentence.lower().split()
    tokens.append('EOS')

    #Symbol definition
    non_terminals=['S','NN','VB']
    terminals = ['ammak','mangge','andi','bayao','es','sapatu','jekne','anganre','asare','angnginung']

    #parse table definition
    parse_table={}
    parse_table[('S','ammak')] = ['NN','VB','NN']
    parse_table[('S','mangge')] = ['NN','VB','NN']
    parse_table[('S','andi')] = ['NN','VB','NN']
    parse_table[('S','bayao')] = ['NN','VB','NN']
    parse_table[('S','es')] = ['NN','VB','NN']
    parse_table[('S','sapatu')] = ['NN','VB','NN']
    parse_table[('S','jekne')] = ['NN','VB','NN']
    parse_table[('S','anganre')] = ['error']
    parse_table[('S','asare')] = ['error']
    parse_table[('S','angnginung')] = ['error']
    parse_table[('S','EOS')] = ['error']

    parse_table[('NN','ammak')] = ['ammak']
    parse_table[('NN','mangge')] = ['mangge']
    parse_table[('NN','andi')] = ['andi']
    parse_table[('NN','bayao')] = ['bayao']
    parse_table[('NN','es')] = ['es']
    parse_table[('NN','sapatu')] = ['sapatu']
    parse_table[('NN','jekne')] = ['jekne']
    parse_table[('NN','anganre')] = ['error']
    parse_table[('NN','asare')] = ['error']
    parse_table[('NN','angnginung')] = ['error']
    parse_table[('NN','EOS')] = ['error']

    parse_table[('VB','ammak')] = ['error']
    parse_table[('VB','mangge')] = ['error']
    parse_table[('VB','andi')] = ['error']
    parse_table[('VB','bayao')] = ['error']
    parse_table[('VB','es')] = ['error']
    parse_table[('VB','sapatu')] = ['error']
    parse_table[('VB','jekne')] = ['error']
    parse_table[('VB','anganre')] = ['anganre']
    parse_table[('VB','asare')] = ['asare']
    parse_table[('VB','angnginung')] = ['angnginung']
    parse_table[('VB','EOS')] = ['error']

    #stack initialisationg
    stack=[]
    stack.append('#')
    stack.append('S')

    #input reading initialisationg
    idx_token = 0
    symbol = tokens[idx_token]
    #parsing process
    while(len(stack)>0):
        top = stack[len(stack)-1]
        st.write('top = ',top)
        st.write('symbol = ',symbol)
        if top in terminals:
            st.write('Top adalah symbol terminal')
            if top==symbol:
                stack.pop()
                idx_token = idx_token +1
                symbol = tokens[idx_token]
                if symbol == 'EOS':
                    st.write ('isi stack: ',stack)
                    stack.pop()
            else:
                st.write('error')
                break;
        elif top in non_terminals:
            st.write('otp adalah simboo non-terminal')
            if parse_table[(top,symbol)][0]!='error':
                stack.pop()
                symbols_to_be_pushed = parse_table[(top,symbol)]
                for i in range(len(symbols_to_be_pushed)-1,-1,-1):
                    stack.append(symbols_to_be_pushed[i])
            else:
                st.write('error')
                st.write('error')
                break;
        else:
            st.write('error')
            break;
        st.write('isi stack:',stack)
        st.write()
    

    #conslusion
    st.write()
    if symbol =='EOS' and len(stack)==0:
        st.write('input string',sentence,'diterima, sesuai Grammar')
    else:
        st.write('Error, input string: ',sentence,'tidak diterima, tidak sesuai Grammar')