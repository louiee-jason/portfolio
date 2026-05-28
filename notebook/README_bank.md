# Bank Customer Segmentation & Classification

## Overview
This project presents an end-to-end machine learning pipeline to segment banking customers and predict their behavioral profiles. By combining unsupervised learning (clustering) and supervised learning (classification), the project transforms unlabeled transactional data into actionable business insights.

## Problem Statement
Banks often lack labeled data to understand customer behavior, making it difficult to perform targeted marketing, risk profiling, and retention strategies.

This project addresses the problem by:
- Identifying customer segments using clustering
- Generating labels from cluster results
- Training classification models to predict customer segments

## Methodology

### 1. Data Preprocessing
- Handled missing values and duplicates
- Applied feature encoding (Label Encoding, One-Hot Encoding)
- Performed outlier treatment using IQR
- Scaled features using StandardScaler
- Conducted feature engineering through binning

### 2. Customer Segmentation
- Algorithm: K-Means Clustering
- Optimal clusters determined using Elbow Method and Silhouette Score
- PCA used for dimensionality reduction and visualization

### 3. Cluster Insights
- Segment 0: High-income customers with frequent transactions (high-value segment)
- Segment 1: Low activity customers with minimal transactions (low engagement)
- Segment 2: Moderate income with high credit usage (potential risk segment)

### 4. Classification Modeling
- Models: Decision Tree, Random Forest
- Evaluation metrics: Accuracy, Precision, Recall, F1-score
- Hyperparameter tuning using GridSearchCV

## Results
- Random Forest achieved strong performance in predicting customer segments
- Clustering-based labeling proved effective for training supervised models

## Business Impact
- Enables targeted marketing for high-value customers
- Helps identify risky customer segments with high credit usage
- Supports retention strategies for low-engagement users

## Tech Stack
Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
