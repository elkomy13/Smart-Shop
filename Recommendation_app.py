import streamlit as st
import pandas as pd

# Load your preprocessed data
@st.cache_data
def load_data():
    # Replace with your actual data loading logic
    customer_data = pd.read_csv("customer_data_with_recommendations.csv")
    top_products = pd.read_csv("top_products_per_cluster.csv")
    return customer_data, top_products

customer_data, top_products = load_data()

# App title
st.title("Customer Product Recommendations")

# Step 1: User selects a customer
customer_id = st.selectbox(
    "Select Customer ID",
    customer_data["CustomerID"].unique()
)

# Step 2: Display customer cluster and segment name
customer_cluster = customer_data[customer_data["CustomerID"] == customer_id]["cluster"].values[0]
cluster_names = {
    0: "Occasional Bargain Hunters",
    1: "Loyal Regulars",
    2: "High-Risk Big Spenders"
}
st.subheader(f"Customer Segment: **{cluster_names[customer_cluster]}**")

# Step 3: Show recommendations
st.header("Recommended Products")
recommendations = customer_data[customer_data["CustomerID"] == customer_id][[
    "Rec1_Description", "Rec2_Description", "Rec3_Description"
]].values.flatten()

for i, product in enumerate(recommendations, 1):
    st.write(f"{i}. {product}")

# Step 4: Show top products in the cluster (visualization)
st.header(f"Top 10 Products for {cluster_names[customer_cluster]}")
cluster_top_products = top_products[top_products["cluster"] == customer_cluster]
st.bar_chart(cluster_top_products.set_index("Description")["Quantity"])