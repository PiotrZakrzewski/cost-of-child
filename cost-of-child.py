import streamlit as st
import pandas as pd
import numpy as np

st.title('Cost of having a child')
st.caption('[Source Code](https://github.com/PiotrZakrzewski/cost-of-child)')
st.markdown('''
Interactive demonstration of how the cost of having a child differs between developing 
and developed countries. Inspired by video from [Economics Explained](https://www.youtube.com/watch?v=YYvLEbC3kn8&t=76s)''')

st.image("cost-of-childcare-illustration.png")

col1, col2 = st.columns(2)

with col1:
    st.header("A)Developed Country")
    median_annual_gross_salary_A = st.slider("Median annual gross salary [A]", 0, 100000, 30000, format="%d $")
    child_care_A = st.slider("Years child needs care [A]", 0, 18, 18, format="%d years")
    reduction_A = st.slider("Reduction in income [%] during taking care of child [A]", 0, 100, 20, format="%d %%")
    paid_education_duration_A = st.slider("Years in paid education [A]", 0, 10, 5, format="%d years")
    education_cost_A = st.slider("Cost of education [A] per year", 0, 100000, 5000, format="%d $")

with col2:
    st.header("B)Developing Country")
    median_annual_gross_salary_B = st.slider("Median annual gross salary [B]", 0, 100000, 3000, format="%d $")
    child_care_B = st.slider("Years child needs care [B]", 0, 18, 12, format="%d years")
    reduction_B = st.slider("Reduction in income [%] during taking care of child [B]", 0, 100, 20, format="%d %%")
    paid_education_duration_B = st.slider("Years in paid education [B]", 0, 10, 0, format="%d years")
    education_cost_B = st.slider("Cost of education [B] per year", 0, 100000, 0, format="%d $")

def cumulative_cost(salary, reduction, child_care, edu_duration, edu_cost):
    cumulative = []
    current = 0
    for _ in range(child_care):
        current += salary * (reduction/100)
        cumulative.append(current)
    for _ in range(edu_duration):
        current += edu_cost
        cumulative.append(current)
    last_added = cumulative[-1]
    while len(cumulative) < 28:
        cumulative.append(last_added)
    return cumulative
A = cumulative_cost(median_annual_gross_salary_A, reduction_A, child_care_A, paid_education_duration_A, education_cost_A)
B = cumulative_cost(median_annual_gross_salary_B, reduction_B, child_care_B, paid_education_duration_B, education_cost_B)
st.markdown('''
## Cumulative cost of having a child
First the opportunity cost of foregone income, then the cost of education.
Developed vs developing country (see legend).
''')
chart_data = pd.DataFrame(
    np.array([A, B]).T,
    columns=['Developed', 'Developing'])

st.area_chart(chart_data)