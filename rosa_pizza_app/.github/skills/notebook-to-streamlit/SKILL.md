---
name: notebook-to-streamlit
description: Build a Streamlit app using the Rosa's Pizza notebook analysis.
---

# Notebook to Streamlit

## Read the notebook
Find and read the project's .ipynb file before building the app.
Reuse the cost calculation and best-promise functions from Part II.

## Preserve the calculation logic
- Import ZONES, TIME_BLOCKS, COSTS, PROMISE, and delivery_times
  from the official starter package.
- Do not recreate or modify the starter code.
- Generate delivery data separately for each candidate promise.
- An order is late when its delivery time exceeds the promise.
- Late cost = refund + churn * profit margin.
- Net profit = number of orders * profit margin
  - number of late orders * late cost.
- Use the costs entered by the user.
- Preserve the notebook's seed and tie-breaking rule.

## Build the interface
- Provide dropdown menus for zone and time block.
- Allow users to set the minimum and maximum promised times.
- Generate candidate promises in five-minute increments.
- Allow users to adjust profit margin, churn, and refund.
- Use COSTS for the default cost values.
- Calculate after the user clicks a button.
- Display the recommended promise and four-week net profit.
- Reject invalid ranges and negative costs.
- Suggest expanding the range if the best promise is at its upper limit.

## Organize the project
- Put reusable calculation functions in logic.py.
- Put the Streamlit interface in app.py.
- List dependencies in requirements.txt, including:
  git+https://github.com/zhouy185/rosa-starter.git
- Explain installation and execution in README.md.

## Verify the app
Compare the app and notebook using the same zone, time block,
candidate promises, costs, and seed. Their results should match.