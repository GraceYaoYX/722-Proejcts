# Rosa's Pizza Delivery Promise App

A Streamlit app that helps Rosa select the delivery promise
with the highest estimated net profit for a chosen zone and time block.

## Features

- Select a delivery zone and time block.
- Set the minimum and maximum delivery promises.
- Compare promises in five-minute increments.
- Adjust profit margin, refund cost, and future orders lost per late order.
- Display the recommended promise and estimated four-week net profit.
- Suggest expanding the range when the recommendation reaches the upper limit.

## Calculation

For each candidate promise, the app generates delivery data using
the official rosa-starter package.

An order is late if its delivery time exceeds the promised time.

Cost per late order:

    refund + future orders lost per late order * profit margin

Estimated net profit:

    number of orders * profit margin
    - number of late orders * cost per late order

The app selects the candidate with the highest net profit.
If profits are equal, it selects the shorter promise.

A fixed random seed of 1 makes results repeatable.
Results represent four weeks of simulated orders and are subject
to simulation uncertainty.

## Project Files

- `722_A1.ipynb`: Assignment analysis and explanations.
- `logic.py`: Cost calculation and best-promise functions.
- `app.py`: Streamlit interface.
- `requirements.txt`: Python dependencies.
- `.github/skills/notebook-to-streamlit/SKILL.md`:
  Project skill for reusing the notebook logic in the app.

## Run Locally on Windows

Open a terminal in the project folder.

Create a virtual environment:

    py -m venv .venv

Install dependencies:

    .\.venv\Scripts\python.exe -m pip install -r requirements.txt

Start the app:

    .\.venv\Scripts\python.exe -m streamlit run app.py

Open the Local URL displayed in the terminal.

## Deployment

The app is intended to be deployed on Streamlit Community Cloud
from its GitHub repository, using `app.py` as the entry point.

Add the deployed app link here after deployment.

## AI Assistance

Codex assisted with reviewing the notebook logic and preparing
the Streamlit application. The project includes a
notebook-to-streamlit skill to guide reuse of the notebook logic.

The assignment notebook contains the detailed AI-use appendix.