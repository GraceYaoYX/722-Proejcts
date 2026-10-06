import numpy as np
from starter import ZONES, TIME_BLOCKS, COSTS, PROMISE, delivery_times


def calculate_late_cost(costs):
    """Calculate the total cost of one late order."""
    return (
        costs["refund"]
        + costs["churn_orders"] * costs["margin"]
    )


def best_promise(zone, time_block, promises, costs):
    """Return the best promise and its four-week net profit."""

    if len(promises) == 0:
        raise ValueError("The list of promises cannot be empty.")

    margin = costs["margin"]
    late_cost = calculate_late_cost(costs)

    recommended_promise = None
    highest_profit = float("-inf")

    for promise in sorted(promises):
        times = delivery_times(
            zone, time_block, promise, seed=1
        )

        number_of_orders = len(times)
        number_of_late_orders = np.sum(times > promise)

        net_profit = (
            number_of_orders * margin
            - number_of_late_orders * late_cost
        )

        if net_profit > highest_profit:
            highest_profit = net_profit
            recommended_promise = promise

    return recommended_promise, highest_profit