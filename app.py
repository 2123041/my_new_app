import streamlit as st

def knapsack(wt, val, W, n):
    if n == 0 or W == 0:
        return 0
    if wt[n-1] > W:
        return knapsack(wt, val, W, n-1)
    else:
        return max(val[n-1] + knapsack(wt, val, W-wt[n-1], n-1), knapsack(wt, val, W, n-1))

def main():
    st.title("Knapsack Problem")
    n = st.slider("Number of items", 1, 100, 1)
    wt = [st.number_input(f"Weight of item {i+1}") for i in range(n)]
    val = [st.number_input(f"Value of item {i+1}") for i in range(n)]
    W = st.number_input("Capacity of knapsack")
    if st.button("Solve"):
        result = knapsack(wt, val, W, n)
        st.success(f"Maximum value is {result}")

if __name__ == "__main__":
    main()
