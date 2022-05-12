import matplotlib.pyplot as plt
import streamlit as st
from monty_hall import MontyHall

st.markdown('# Monty Hall Simulation')
num_simulation = st.number_input('Times to run simulation', format='%i', value=0)

if num_simulation > 0:
    result = MontyHall().run_simulation(int(num_simulation))
    won_percent = round((result/num_simulation)*100, 2)
    lost_percent = 100 - won_percent
    f'''
    By switching doors, the contestant won {result} times or {won_percent}%
    '''
    fig, ax = plt.subplots()
    ax.pie([won_percent, lost_percent], labels=['Won', 'Lost'], autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')
    st.pyplot(fig)