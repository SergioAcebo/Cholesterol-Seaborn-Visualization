import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/VORPC/Documents/Prácticas/Ejercicios/Ejercicios Tema 4/Ejercicio 4.5.csv")

#1.- Elabora un countplot que divida a los pacientes en función de su IMC_CAT
sns.countplot(data=df, x="IMC_CAT", hue="IMC_CAT", palette="colorblind", legend= False)
plt.title("Distribución de pacientes según su IMC")
plt.xlabel("Categoría de IMC")
plt.ylabel("Frecuencia")
plt.show()


#2.- Elabora un histograma para dividir a los pacientes con diabetes en función de su edad
diabeticos = df[df["Diabetes"]=="SI"]
sns.histplot(data=diabeticos, x="Edad", bins=range(40,90,5), kde= False, color="skyblue")
plt.title("Distribución por edad de pacientes diabéticos")
plt.xlabel("Edad")
plt.xticks(np.arange(40,91,5))
plt.ylabel("Frecuencia")
plt.show()


#3.- Elabora un counplot para dividir a los pacientes en hombres y mujeres y clasificarlos según su IMC_CAT
hombres = df[df["Sexo"]=="M"]
mujeres = df[df["Sexo"]=="F"]
fig, axs= plt.subplots(1,2, figsize=(14,5))

sns.countplot(data=hombres, x="IMC_CAT", hue="IMC_CAT", palette="deep", legend=False, ax=axs[0])
axs[0].set_title("Distribución de pacientes masculinos según su IMC")
axs[0].set_xlabel("Categorías de IMC")
axs[0].set_ylabel("Frecuencia")
axs[0].set_yticks(np.arange(0,20,1))

sns.countplot(data=mujeres, x="IMC_CAT", hue="IMC_CAT", palette="deep", legend=False, ax=axs[1])
axs[1].set_title("Distribución de pacientes femeninos según su IMC")
axs[1].set_xlabel("Categorías de IMC")
axs[1].set_ylabel("Frecuencia")
axs[1].set_yticks(np.arange(0,20,1))

plt.tight_layout()
plt.show()


#4.- Barplot para relacionar las personas que padecen diabetes y que padecen obesidad
datos_agrupados = df.groupby(["Diabetes","Obesidad"]).size().reset_index(name = "Total")
sns.barplot(data=datos_agrupados, x="Diabetes", y="Total", hue="Obesidad", palette="colorblind", legend=True)
plt.title("Pacientes con y sin Diabetes agrupados por Obesidad")
plt.yticks(np.arange(0,23,1))
plt.show()


#5.-Escribe un código que devuelva 2 subplots que relacionen los niveles de triglicéridos y de colesterol con la obesidad
fig, axs =plt.subplots(1,2, figsize = (14,5))

sns.barplot(data=df, x="IMC_CAT", y="Colesterol", hue="IMC_CAT", palette="muted", errorbar= "sd", err_kws={"linewidth":2}, capsize=0.3, ax=axs[0]) #No olvides los ejes
axs[0].set_title("Relación entre IMC y Colesterol")                           #err_kws grosor errorbar // capsize tamaño de las barras horizontales
axs[0].set_xlabel("Categorías de IMC")
axs[0].set_ylabel("Nivel de Colesterol  en sangre (mg/dl)")

sns.barplot(data=df, x="IMC_CAT", y="Trigliceridos", hue="IMC_CAT", palette="muted", errorbar= "sd", err_kws={"linewidth":2}, capsize= 0.3, ax=axs[1]) #ci = intervalo de confianza, sd= desviación estandar
axs[1].set_title("Relación entre IMC y Triglicéridos")
axs[1].set_xlabel("Categorías de IMC")
axs[1].set_ylabel("Nivel de triglicéridos en sangre (mg/dl)")

plt.tight_layout()
plt.show()


#6.- Elabora un código que devuelva 3 subplots que relacionen los niveles de triglicéridos, de colesterol y de glucosa con la diabetes
fig,axs=plt.subplots(1,3, figsize=(14,5))

sns.barplot(data=df, x="Diabetes", y="Colesterol", hue="Diabetes", palette="Set1", legend= False, errorbar= "sd", err_kws={"linewidth":1.5}, capsize= 0.4, ax=axs[0])
axs[0].set_title("Relación Colesterol y la Diabetes")
axs[0].set_xlabel("¿Padecen diabetes tipo 2?")
axs[0].set_ylabel("Nivel de Colesterol en sangre (mg/dl)")

sns.barplot(data=df, x="Diabetes", y="Trigliceridos", hue="Diabetes", palette="Set1", legend=False, errorbar="sd", err_kws={"linewidth":1.5}, capsize= 0.3, ax=axs[1])
axs[1].set_title("Relación Triglicéridos y la Diabetes")
axs[1].set_xlabel("¿Padecen diabetes tipo 2?")
axs[1].set_ylabel("Nivel de Triglicéridos en sangre (mg/dl)")

sns.barplot(data=df, x="Diabetes", y="Glucosa", hue="Diabetes", palette= "Set1", legend= False, errorbar="sd", err_kws={"linewidth":1.5}, capsize= 0.3, ax=axs[2])
axs[2].set_title("Relación Glucosa y la Diabetes")
axs[2].set_xlabel("¿Padecen diabetes tipo 2?")
axs[2].set_ylabel("Nivel de Glucosa en sangre (mg/dl)")

plt.tight_layout()
plt.show()


#7.- Elabora un código que devuelva 6 subplots con boxplots que relacionen la expresión de los 6 genes en pacientes con obesidad
fig,axs= plt.subplots(1,6, figsize=(25,16), constrained_layout = True) #Mejor que tight_layout() con tantos datos
plt.title("Relación entre los genes diana y la obesidad")

sns.boxplot(data=df, x="Obesidad", y="INSA", hue="Obesidad", legend= True, ax=axs[0])
axs[0].set_xlabel("¿Padece obesidad?")
axs[0].set_ylabel("Expresión INSA")

sns.boxplot(data=df, x="Obesidad", y="SLC2A2", hue="Obesidad", legend= True, ax=axs[1])
axs[1].set_xlabel("¿Padece obesidad?")
axs[1].set_ylabel("Expresión SLC2A2")

sns.boxplot(data=df, x="Obesidad", y="PEPCK", hue="Obesidad", legend= True, ax=axs[2])
axs[2].set_xlabel("¿Padece obesidad?")
axs[2].set_ylabel("Expresión PEPCK")

sns.boxplot(data=df, x="Obesidad", y="FTO", hue="Obesidad", legend= True, ax=axs[3])
axs[3].set_xlabel("¿Padece obesidad?")
axs[3].set_ylabel("Expresión FTO")

sns.boxplot(data=df, x="Obesidad", y="MC4R", hue="Obesidad", legend= True, ax=axs[4])
axs[4].set_xlabel("¿Padece obesidad?")
axs[4].set_ylabel("Expresión MC4R")

sns.boxplot(data=df, x="Obesidad", y="FADS1", hue="Obesidad", legend= True, ax=axs[5])
axs[5].set_xlabel("¿Padece obesidad?")
axs[5].set_ylabel("Expresión FADS1")

plt.show()


#8.- Repite el ejercicio anterior con pacientes con diabetes
fig,axs= plt.subplots(1,6, figsize=(25,16), constrained_layout = True) #Mejor que tight_layout() con tantos datos
plt.title("Relación entre los genes diana y la Diabetes")

sns.boxplot(data=df, x="Diabetes", y="INSA", hue="Diabetes", legend= True, ax=axs[0])
axs[0].set_xlabel("¿Padece Diabetes?")
axs[0].set_ylabel("Expresión INSA")

sns.boxplot(data=df, x="Diabetes", y="SLC2A2", hue="Diabetes", legend= True, ax=axs[1])
axs[1].set_xlabel("¿Padece Diabetes?")
axs[1].set_ylabel("Expresión SLC2A2")

sns.boxplot(data=df, x="Diabetes", y="PEPCK", hue="Diabetes", legend= True, ax=axs[2])
axs[2].set_xlabel("¿Padece Diabetes?")
axs[2].set_ylabel("Expresión PEPCK")

sns.boxplot(data=df, x="Diabetes", y="FTO", hue="Diabetes", legend= True, ax=axs[3])
axs[3].set_xlabel("¿Padece Diabetes?")
axs[3].set_ylabel("Expresión FTO")

sns.boxplot(data=df, x="Diabetes", y="MC4R", hue="Diabetes", legend= True, ax=axs[4])
axs[4].set_xlabel("¿Padece Diabetes?")
axs[4].set_ylabel("Expresión MC4R")

sns.boxplot(data=df, x="Diabetes", y="FADS1", hue="Diabetes", legend= True, ax=axs[5])
axs[5].set_xlabel("¿Padece Diabetes?")
axs[5].set_ylabel("Expresión FADS1")

plt.show()


#9.-Elabora un Heatmap que correlacione los genes INSA, GLUT2 y PEPCK
plt.figure(figsize=(8,6))
corr=df[["INSA", "SLC2A2", "PEPCK"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.show()

#10.-Elabora un Heatmap que correlacione los genes FTO, MC4R, FADS1
plt.figure(figsize=(8,6))
corr=df[["FTO", "MC4R", "FADS1"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.show()

#11.- #11.- Elabora un clustermap que correlacione la expresión de los 6 genes
plt.figure(figsize=(8,6))
corr=df[["INSA", "SLC2A2", "PEPCK", "FTO", "MC4R", "FADS1"]].corr()
sns.clustermap(corr, annot = True, cmap = "coolwarm", fmt=".2f")
plt.show()