# 🛍️ ShopSmart - Customer Segmentation & Products Recommendation

ShopSmart is an end-to-end customer segmentation project that utilizes unsupervised learning to cluster customer behaviors from transaction data. The goal is to help e-commerce businesses personalize marketing, identify loyalty tiers, and improve decision-making.

---

## Project Overview

This notebook explores a real-world e-commerce dataset, applying preprocessing, outlier removal, dimensionality reduction (PCA), and clustering (KMeans). The clusters are interpreted with visual aids like radar charts and PCA projections for actionable insights.

---

## Dataset Description

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
   - Filtered non-positive quantities/prices  
   - Handled missing `CustomerID`  & `Description`
     <img width="1300" height="417" alt="image" src="https://github.com/user-attachments/assets/38192a7f-bb3c-4d86-904b-4f993abe7b07" />
     
   - Removed cancellations & duplicates  
   - Scaled features using `StandardScaler`


2. **Feature Engineering**
   
   1. RFM (Recency, Frequency, Monetary) Features
      - Recency (R):
      
         Days_Since_Last_Purchase: Days since last purchase (lower = more recent engagement).
      
      - Frequency (F):
      
         Total_Transactions: Total transactions per customer.
         
         Total_Products_Purchased: Total quantity of products purchased.
      
      - Monetary (M):
      
         Total_Spend: Total money spent by the customer.
         
         Average_Transaction_Value: Mean transaction value (Total_Spend / Total_Transactions).
      
   2. Product Diversity
         Unique_Products_Purchased: Count of distinct products bought.
      
   3. Behavioral Features
         Average_Days_Between_Purchases: Avg. days between purchases.
      
         Day_Of_Week: Preferred shopping day (0=Monday, 6=Sunday).
      
         Hour: Preferred shopping hour (24h format).
      
   4. Geographic Features
         Is_UK: Binary (1 if UK-based, 0 otherwise).
      
   5. Cancellation Insights
         Cancellation_Frequency: Total canceled transactions.
      
         Cancellation_Rate: Canceled transactions ratio (Cancellation_Frequency /          Total_Transactions).
      
   6. Seasonality & Trends
         Monthly_Spending_Mean: Avg. monthly spend.
      
         Monthly_Spending_Std: Volatility in monthly spend.
      
         Spending_Trend: Spending trend slope (+=increasing, -=decreasing).
         
3. **Outlier Detection**  
   - Used `IsolationForest` to remove noisy data
     <img width="1015" height="406" alt="image" src="https://github.com/user-attachments/assets/5c6f72d0-a3db-49c8-8e51-57e7f9dec678" />

4. **Correlation Analysis**
   <img width="1190" height="1100" alt="image" src="https://github.com/user-attachments/assets/bfc7e668-b2a4-4877-9de5-ddb827f7bea1" />
   Looking at the heatmap, we can see that there are some pairs of variables that have high       correlations, for instance:
   
   - Monthly_Spending_Mean and Average_Transaction_Value
   - Total_Spend and Total_Products_Purchased
   - Total_Transactions and Total_Spend
   - Cancellation_Rate and Cancellation_Frequency
   - Total_Transactions and Total_Products_Purchased

4. **Dimensionality Reduction**  
   - Applied **PCA** to project data into fewer dimensions for visualization & clustering
     
    <img width="1636" height="874" alt="image" src="https://github.com/user-attachments/assets/4431f4ea-dda5-4d9b-a5de-468837c585ae" />
   
   - From the plot, we can see that the increase in cumulative variance starts to slow down after the 6th component (which captures about 81% of the total variance).


5. **Clustering**  
   - Determined optimal `k` using **Elbow Method** and **Silhouette Score**
   - Elbow Graph
     
    <img width="1039" height="483" alt="image" src="https://github.com/user-attachments/assets/76507e72-c43f-4b5e-b804-c609c82aebcb" />

    - Silhouette Graph
      <img width="1951" height="3001" alt="image" src="https://github.com/user-attachments/assets/9d1aaf3b-66f2-47aa-b627-cce71134c8ea" />

   - Applied **K-Means** clustering on PCA-transformed data

6. **Clustering Evaluation**
   - 3D Visualization of Top PCs
     
     <img width="647" height="581" alt="image" src="https://github.com/user-attachments/assets/f68a4da0-d645-4cf1-834e-7c0891dfe461" />
     
   - Cluster Distribution Visualization
     
     <img width="855" height="407" alt="image" src="https://github.com/user-attachments/assets/5409c9f5-0206-4ad5-9bee-1fab0139c4fd" />

   - Evaluation Metrics
  
     
        <img width="548" height="242" alt="image" src="https://github.com/user-attachments/assets/cca23bd3-079c-407f-82cc-515c2b8c9919" />

        1. **The Silhouette Score** of approximately 0.236, although not close to 1, still indicates a fair amount of separation between the clusters. It suggests that the clusters are somewhat distinct, but                   there might be slight overlaps between them. Generally, a score closer to 1 would be ideal, indicating more distinct and well-separated clusters.
        
        2. **The Calinski Harabasz Score** is 1257.17, which is considerably high, indicating that the clusters are well-defined. A higher score in this metric generally signals better cluster definitions, thus                implying that our clustering has managed to find substantial structure in the data.
      
        3. **The Davies Bouldin Score** of 1.37 is a reasonable score, indicating a moderate level of similarity between each cluster and its most similar one. A lower score is generally better as it indicates                less similarity between clusters, and thus, our score here suggests a decent separation between the clusters.

   - Created **Radar Chart** to compare behavioral profiles
     <img width="1989" height="524" alt="image" src="https://github.com/user-attachments/assets/f72a5360-1ebd-4889-9df0-e1e9ffbb0024" />
      1. Cluster 0 (Red Chart) Profile: Sporadic Shoppers with a Preference for Weekend Shopping

         Customers in this cluster tend to spend less, with a lower number of transactions and products purchased. They have a slight tendency to shop during the weekends, as indicated by the very high                    Day_of_Week value. Their spending trend is relatively stable but on the lower side, and they have a low monthly spending variation (low Monthly_Spending_Std). These customers have not engaged in many             cancellations, showing a low cancellation frequency and rate. The average transaction value is on the lower side, indicating that when they do shop, they tend to spend less per transaction.

      2. Cluster 1 (Green Chart): Profile: Infrequent Big Spenders with a High Spending Trend

         Customers in this cluster show a moderate level of spending, but their transactions are not very frequent, as indicated by the high Days_Since_Last_Purchase and Average_Days_Between_Purchases. They have          a very high spending trend, indicating that their spending has been increasing over time. These customers prefer shopping late in the day, as indicated by the high Hour value, and they mainly reside in            the UK. They have a tendency to cancel a moderate number of transactions, with a medium cancellation frequency and rate. Their average transaction value is relatively high, meaning that when they shop,          they tend to make substantial purchases.

      3. Cluster 2 (Blue Chart) Profile: Frequent High-Spenders with a High Rate of Cancellations

         Customers in this cluster are high spenders with a very high total spend, and they purchase a wide variety of unique products. They engage in frequent transactions, but also have a high cancellation             frequency and rate. These customers have a very low average time between purchases, and they tend to shop early in the day (low Hour value). Their monthly spending shows high variability, indicating that          their spending patterns might be less predictable compared to other clusters. Despite their high spending, they show a low spending trend, suggesting that their high spending levels might be decreasing            over time.
   
   7. **Recommendation System**
      - I am set to develop a recommendation system to enhance the online shopping experience. This system will suggest products to customers based on the purchasing patterns prevalent in their respective                clusters.
        
      - video demo:

         ![recommendation](https://github.com/user-attachments/assets/f0d47245-67e9-4028-8b79-fd902e46deb4)




