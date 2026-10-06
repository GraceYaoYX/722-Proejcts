import streamlit as st

from logic import best_promise
from starter import ZONES, TIME_BLOCKS, COSTS, PROMISE


st.set_page_config(
    page_title="Rosa's Pizza",
    page_icon="🍕"
)

st.title("🍕 Rosa's Pizza Delivery Promise")
st.write(
    "Choose a zone, time block, and costs to find the "
    "delivery promise with the highest estimated net profit."
)
st.caption(
    f"Current delivery promise: {PROMISE} minutes. "
    "Results represent four weeks of simulated orders."
)

with st.form("promise_form"):
    st.subheader("Delivery area")

    zone = st.selectbox("Zone", ZONES)
    time_block = st.selectbox("Time block", TIME_BLOCKS)

    st.subheader("Promises to compare")

    minimum = st.number_input(
        "Minimum promise (minutes)",
        min_value=5,
        value=5,
        step=5
    )

    maximum = st.number_input(
        "Maximum promise (minutes)",
        min_value=5,
        value=90,
        step=5
    )

    st.caption("Promises are compared in 5-minute increments.")

    st.subheader("Costs")

    margin = st.number_input(
        "Profit margin per order ($)",
        min_value=0.0,
        value=float(COSTS["margin"]),
        step=0.50
    )

    churn = st.number_input(
        "Future orders lost per late order",
        min_value=0.0,
        value=float(COSTS["churn_orders"]),
        step=0.10
    )

    refund = st.number_input(
        "Refund per late order ($)",
        min_value=0.0,
        value=float(COSTS["refund"]),
        step=0.50
    )

    submitted = st.form_submit_button("Find best promise")

if submitted:
    if minimum > maximum:
        st.error(
            "The minimum promise must not exceed the maximum."
        )
    elif minimum % 5 != 0 or maximum % 5 != 0:
        st.error(
            "Please enter minimum and maximum promises "
            "that are multiples of 5."
        )
    else:
        promises = list(range(int(minimum), int(maximum) + 1, 5))

        user_costs = {
            "margin": margin,
            "churn_orders": churn,
            "refund": refund
        }

        with st.spinner("Comparing delivery promises..."):
            recommended, profit = best_promise(
                zone,
                time_block,
                promises,
                user_costs
            )

        st.subheader("Recommendation")

        st.metric(
            "Best delivery promise",
            f"{recommended} minutes"
        )

        st.metric(
            "Estimated four-week net profit",
            f"${profit:,.2f}"
        )

        st.write(f"Selected area: **{zone} — {time_block}**")

        if recommended == maximum:
            st.warning(
                "The best promise is at the upper limit. "
                "Try a larger maximum to check whether "
                "a longer promise is more profitable."
            )

        st.caption(
            "This is the best result among the tested promises. "
            "A fixed random seed of 1 makes results repeatable."
        )