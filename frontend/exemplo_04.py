# poetry add streamlit pandas

import streamlit as st
import pandas as pd
import subprocess
import os

# Função para carregar os dados do arquivo CSV
def load_data():
    df = pd.read_csv("execution_logs.log")
    return df

# Função para executar o script Python
def run_python_script():
    print(os.getcwd())
    os.chdir("./pipeline/")
    print(os.getcwd())
    subprocess.run(["python", "pipeline.py"])
    os.chdir("/home/oliveiraphm/jornada/workshop_ao_vivo_airflow/frontend")
    print(os.getcwd())
# Layout do aplicativo Streamlit
def main():
    st.title("Visualização de Logs e Execução de Scripts")
    os.chdir("/home/oliveiraphm/jornada/workshop_ao_vivo_airflow/frontend")
    st.image("pics/elyflow.png")

    # Carregar os dados do arquivo CSV
    df = load_data()

    # Exibir os dados na interface do Streamlit
    st.write("Logs de Execução:", df)

    # Botão para atualizar os dados
    if st.button("Atualizar Dados"):
        df = load_data()
        st.write("Dados Atualizados com Sucesso!")

    # Botão para executar o script Python
    if st.button("Executar Script Python"):
        run_python_script()
        st.write("Script Python executado com sucesso!")

if __name__ == "__main__":
    main()