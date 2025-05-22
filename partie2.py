import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# importation des datasets depuis GitHub

# Titre de la page
st.title("Mini-projet Streamlit Partie 2")

st.header("Paramétrage et choix d'un dataset")

datasetname = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/dataset_names.txt")
selected_dataset = st.selectbox('Choisissez un dataset :', datasetname)
df = sns.load_dataset(selected_dataset)

st.dataframe(df)

# Choix des colonnes X et Y
column_names = df.columns.tolist()
x = st.selectbox("Choisissez une colonne X :", column_names)
y = st.selectbox("Choisissez une colonne Y :", column_names)

st.write('---')
st.header("Choix de la visualisation")
listvis = ["bar_chart", "line_chart", "scatter_chart"]
vis = st.selectbox("Choisissez un graphique :", listvis)

if vis == "bar_chart":
    st.bar_chart(data=df, x=x, y=y)
elif vis == "line_chart":
    st.line_chart(data=df, x=x, y=y)
else:
    st.scatter_chart(data=df, x=x, y=y)

st.header("Matrice de corrélation")

# --- Traitement des valeurs manquantes ---
# On repère les colonnes numériques
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

# On vérifie s'il y a des NA dans ces colonnes
null_counts = df[numeric_cols].isna().sum()
cols_with_na = null_counts[null_counts > 0].index.tolist()

if cols_with_na:
    # il y a au moins une colonne avec des nulls
    for col in cols_with_na:
        median_val = df[col].median()
        df[col].fillna(median_val, inplace=True)
    st.success(f"Remplacement des NaN par la médiane sur les colonnes : {', '.join(cols_with_na)}")
else:
    # pas de colonnes à traiter
    st.info("Il n'y a pas de valeurs manquantes dans les colonnes numériques.")

# --- Calcul de la matrice de corrélation ---
# on re-sélectionne les colonnes numériques (au cas où le type aurait changé)
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
df_corr = df[numeric_cols].corr()

# Affichage de la heatmap
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(df_corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
st.pyplot(fig)
