# 🛍️ ShopSmart - Customer Segmentation & Behavior Profiling

ShopSmart is an end-to-end customer segmentation project that utilizes unsupervised learning to cluster customer behaviors from transaction data. The goal is to help e-commerce businesses personalize marketing, identify loyalty tiers, and improve decision-making.

---

## 🚀 Project Overview

This notebook explores a real-world e-commerce dataset, applying preprocessing, outlier removal, dimensionality reduction (PCA), and clustering (KMeans). The clusters are interpreted with visual aids like radar charts and PCA projections for actionable insights.

---

## 📦 Dataset Description

The dataset includes transactional data from an online retailer, with the following key columns:

- **InvoiceNo** → Unique transaction ID. Transactions starting with `C` indicate cancellations.  
- **StockCode** → Unique identifier for products.  
- **Description** → Product name.  
- **Quantity** → Number of units bought.  
- **InvoiceDate** → Timestamp of the transaction.  
- **UnitPrice** → Product price per unit.  
- **CustomerID** → Unique customer identifier.  
- **Country** → Customer location.

---

## ⚙️ Methodology

1. **Preprocessing**  
   - Removed cancellations & duplicates  
   - Filtered non-positive quantities/prices  
   - Handled missing `CustomerID`  
   - Scaled features using `StandardScaler`

2. **Outlier Detection**  
   - Used `IsolationForest` to remove noisy data

3. **Dimensionality Reduction**  
   - Applied **PCA** to project data into fewer dimensions for visualization & clustering

4. **Clustering**  
   - Determined optimal `k` using **Elbow Method** and **Silhouette Score**  
   - Applied **K-Means** clustering on PCA-transformed data

5. **Interpretation**  
   - Created **Radar Chart** to compare behavioral profiles  
   - Cluster distribution & feature breakdown for business actions

---

## 📈 Visualizations & Insights


### 1. 🧼 Missing Value plot
<img width="1621" height="520" alt="image" src="https://github.com/user-attachments/assets/c732d3c5-b737-4cfe-8521-11dc5b984dac" />

> Highlights missing `CustomerID` — which were either dropped or grouped under anonymous.

---

### 2. 🔎 Correlation Matrix  
<img width="743" height="684" alt="image" src="https://github.com/user-attachments/assets/7ab6358b-e767-4589-9059-d9d392be129e" />
> Helps detect redundant or strongly related features before PCA.

---

### 3. 📉 PCA - Explained Variance  
<img width="875" height="481" alt="image" src="https://github.com/user-attachments/assets/6dc391bb-7ef8-4cda-92ef-366e26bc2682" />
 
> First 2 components explain ~80% variance — ideal for visualization.

---

### 4. 🧭 PCA - 2D Projection  
<img width="988" height="460" alt="image" src="https://github.com/user-attachments/assets/2e109200-596b-4aaf-add3-0640c35c7ba6" />

> Reveals natural grouping potential before clustering.

---

### 5. 💡 Elbow Method  
![Uploading image.png…]()

> Shows inertia curve — elbow at `k=3` indicates optimal number of clusters.

---

### 6. 📐 Silhouette Scores  
![Silhouette](images/silhouette_score.png)  
> Validates that 3 clusters are distinct and not overlapping.

---

### 7. 🎯 KMeans Clustering  
![Clusters](images/kmeans_clusters.png)  
> Final cluster allocation in 2D PCA space.

---

### 8. 🕸️ Radar Chart - Cluster Profiles  
![Radar](images/radar_chart.png)  
> Cluster profiles based on features like `recency`, `frequency`, `monetary`.  
> - Cluster 0: Infrequent, low spenders  
> - Cluster 1: Loyal and frequent buyers  
> - Cluster 2: Frequent but low-value spenders  

> 💬 “Radar chart was extremely helpful to compare segment characteristics intuitively.”

---

### 9. 📊 Cluster Distribution  
![Cluster Histogram](images/cluster_histogram.png)  
> Bar chart showing the size of each segment. Useful for strategy scaling.

---

### 10. 📈 Feature Distribution by Cluster  
![Feature Clusters](images/feature_per_cluster.png)  
> Helps explain which behaviors dominate each group (e.g., spending, visit recency).

---

## 🧠 Cluster Summary & Business Implications

| Cluster | Description                  | Actionable Insight                  |
|---------|------------------------------|-------------------------------------|
| 0       | Low spend, infrequent buyers | Re-engage via promotions            |
| 1       | High spend, frequent         | Loyalty program, VIP marketing      |
| 2       | Frequent but low spenders    | Upsell or bundle products           |

---

## 📁 Project Structure

