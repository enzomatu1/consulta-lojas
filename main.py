import streamlit as st
import csv 
import re

st.title("Consulta lojas")

def gerarEmail(VD):
    with open("relacao.csv", newline="", encoding="utf-8") as f:
            leitor = csv.reader(f)
            for linha in leitor:
                if VD == linha[2]:
                    return("@"+linha[41]+", Olá loja tudo bem?\nPor favor, liberem o acesso para que o(s) técnicos possa(m) melhorar link de internet em sua loja. Abaixo, informo os dados dos técnicos para validação.")
def buscaVD(VD):
        ggl = ""
        with open("relacao.csv", newline="", encoding="utf-8") as f:
            leitor = csv.reader(f)
            for linha in leitor:
                if VD == linha[2]:
                    st.write("\n*VD:",linha[2],"\nNome da loja:",linha[6],"\nRegião da loja:", linha[8],"\nHorário de funcionamento:",linha[45])
                    st.write("*Endereço:", linha[15],"\nTelefone 1:", linha[38],"\nTelefone 2:", linha[39],"\nCelular:", linha[40],"\nE-Mail:", linha[41])
                    st.write("*Estado:", linha[18],"\nGR:", linha[11],"\nGGL:", linha[10])
                    ggl = linha[10]
                    with open("GGL.csv", newline="", encoding="utf-8") as f:
                        leitor = csv.reader(f)
                        for i in leitor:
                            if ggl == i[0]:
                                st.write("*Número ggl:", i[1])
                    with open("designacao.csv", newline="", encoding="utf-8") as f:
                        leitor = csv.reader(f)
                        for j in leitor:
                            if VD == j[2]:
                                st.write("*Desginação:", j[6], j[5], j[4])
                        st.write("__________________________________________________________________________________________________________________________")
                        st.write('\n')

            if ggl == "":
                st.write("\nVD não encontrado\n")

def buscaDesignacao(designacao):
    with open("designacao.csv", newline="", encoding="utf-8") as f:
        leitor = csv.reader(f)
        for linha in leitor:
                limpo = re.sub(r'[^A-Za-z0-9]', '', linha[6])
                if designacao == limpo:
                    VD = linha[2]
                    buscaVD(VD)

def buscaEndereco(ende):
    with open("relacao.csv", newline="", encoding="utf-8") as f:
        leitor = csv.reader(f)
        for linha in leitor:
            if ende.upper().strip() in linha[15].upper().strip():
                buscaVD(linha[2])

# -------------------------
# STREAMLIT MENU (replaces input())
# -------------------------

opcao = st.selectbox(
    "O que quer procurar?",
    ("Selecionar...", "VD", "Designação", "Endereço","Gerar E-Mail")
)

if opcao == "VD":
    VD = st.text_input("Qual o VD da loja?")
    if st.button("Buscar VD"):
        buscaVD(VD)

elif opcao == "Designação":
    des = st.text_input("Qual a designação da loja? (XXX/XX/XXXXX ou com _)")
    if st.button("Buscar Designação"):
        des = des.upper()
        des = re.sub(r'[^A-Za-z0-9]', '', des)
        buscaDesignacao(des)

elif opcao == "Endereço":
    ende = st.text_input("Qual o endereço da loja? (não precisa colocar inteiro)")
    if st.button("Buscar Endereço"):
        buscaEndereco(ende)

elif opcao == "Gerar E-Mail":
    VD = st.text_input("Qual o VD da loja?")
    if st.button("Buscar VD"):
        st.code(gerarEmail(VD))