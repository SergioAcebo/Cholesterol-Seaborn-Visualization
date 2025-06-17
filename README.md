# Biological Data Visualization with Seaborn
This repository contains data and scripts from a **fictitious exercise** developed during the *"Biological Data Analysis with Python"* course at the University of San Jorge.

The fictitious data file is named `patients.csv` and contains the following columns:

- `ID`
- `Sex`
- `Age`
- `Weight`
- `Height`
- `BMI`
- `BMI-CAT`
- `Obesity` (Does the patient have obesity?)
- `Diabetes` (Does the patient have diabetes?)
- `Blood glucose level (mg/dl)`
- `Blood cholesterol level (mg/dl)`
- `Blood triglyceride level (mg/dl)`
- `insa gene expression`
- `slc2a2 gene expression`
- `pepck gene expression`
- `fto gene expression`
- `mc4r gene expression`
- `fads1 gene expression`

**Important:** Please make sure to download the `patients.csv` file and save it in your `Downloads` folder so that the program can run correctly.

## Features

The program allows you to:

1. Generate a **countplot** dividing patients based on their BMI-CAT.
2. Generate a **histogram** dividing patients with diabetes based on their age.
3. Generate a **cluster plot** dividing obese patients based on their sex.
4. Generate a **bar plot** showing the relation between diabetes and obesity.
5. Generate **2 subplots** relating triglyceride and cholesterol levels with obesity.
6. Generate **3 subplots** relating triglyceride, cholesterol, and glucose levels with diabetes.
7. Generate **6 subplots** with **boxplots** showing the expression of 6 genes in obese patients.
8. Generate **6 subplots** with **boxplots** showing the expression of 6 genes in diabetic patients.
9. Generate a **heatmap** correlating the genes *insa*, *slc2a2*, and *pepck*.
10. Generate a **heatmap** correlating the genes *fto*, *mc4r*, and *fads1*.
11. Generate a **cluster map** correlating the expression of all 6 genes.

