# Monty Hall Simulation

# [monty_hall.py](monty_hall.py)
This file contains the logic for which the problem is based on. To run the simulation for a number set of trials, the following code can be used.
```
num_simulations = 1000
monty_hall = MontyHall()
results = monty_hall().run_simulation(num_simulations)
```
Which will return the number of times the participant won by changing doors.

# [app.py](app.py)
**Before you install streamlit** - It is recommended you follow the instructions on the streamlit website to install streamlit as it may require adding a path to PATH.
  
An interactice app can be used to visualize results of simulations. The requirements.txt file must be installed first, and it can be done by runnng the following command in the same directory as requirements.txt
```
pip3 install -r requirements.txt
```
Once requirements are installed, the app can be started by running the following command.
```
streamlit run app.py
```