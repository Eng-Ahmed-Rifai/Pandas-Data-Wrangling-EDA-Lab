# 🧹 Pandas Data Wrangling & Exploratory Analysis Lab

**Author:** [Eng. Ahmed Rifai](https://github.com/Eng-Ahmed-Rifai)  
**Credential:** Coursera Certified Guided Project (`practical-data-wrangling-with-pandas`)  
**Live Interactive UI:** [Launch Data Wrangling Lab](index.html)

---

## 📌 Project Overview
Data wrangling and exploratory data analysis (EDA) constitute over 80% of real-world data science workflows. This repository demonstrates production-grade data cleansing, missing value imputation, outlier detection, and statistical correlation analysis on multi-decade global health metrics (WHO Life Expectancy dataset).

---

## 🛠️ Data Engineering Pipeline Stages
1. **Raw Ingestion & Schema Audit:** Profiling 2,938 rows $\times$ 21 variables with initial 18.2% missingness.
2. **Stratified Median Imputation:** Imputing missing values conditioned on macroeconomic status (`Developed` vs. `Developing`) to prevent information distortion.
3. **Robust Outlier Capping (Winsorization):** Applying Interquartile Range ($IQR \pm 1.5$) boundary clipping to protect downstream linear/gradient models from extreme skew.
4. **Exploratory Data Storytelling:** Interactive visualization of GDP per capita, adult mortality, and educational attainment correlations.

---

## 🎛️ Interactive Data Studio
Open `index.html` to explore:
- Step-by-step pipeline state visualizer.
- Global region and economic status dynamic filtering.
- Before-vs-after missing value comparison bar charts.
- Scatter plot trendlines illustrating income elasticity of life expectancy.

---

## 🚀 How to Run Locally
```bash
git clone https://github.com/Eng-Ahmed-Rifai/Pandas-Data-Wrangling-EDA-Lab.git
cd Pandas-Data-Wrangling-EDA-Lab
python -m venv .venv
source .venv/bin/activate  # Or .venv\Scripts\activate on Windows
pip install pandas numpy matplotlib seaborn
python train.py
```
