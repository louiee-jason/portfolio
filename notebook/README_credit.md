# Credit Default Prediction

## Overview
This project builds a machine learning model to predict customer credit default risk using financial data. The goal is to help financial institutions identify high-risk customers and reduce potential losses.

## Problem
Banks need to identify customers who are likely to default, but financial datasets are often imbalanced and noisy.

## Methodology
- Data cleaning and preprocessing
- Feature engineering
- Handling class imbalance using Resampling Method
- Model training using:
  - Random Forest
- Evaluation using ROC-AUC, Precision, Recall, and F1-score

## Results
- Improved recall for default class, enabling better detection of high-risk customers
- Random Forest performed better in handling imbalanced data

## Key Insight
- Customers with higher credit utilization and lower income are more likely to default

## Business Impact
- Helps banks reduce financial risk
- Supports decision-making in credit approval

## Tech Stack
Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
