import numpy as np
import random
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import urllib.parse

visibility = False

def inputs(program):
    has_error = False
    if program == "Single_Server":
        data_array= np.zeros(13, dtype=object)
        data_array[0] = st.sidebar.number_input("Number of Customers", min_value=1, value=10)
        if data_array[0] < 1:
            st.error("The number of simulations must be a positive integer.⚠️")
            has_error = True
        col1, col2 = st.sidebar.columns(2)
        with col1:data_array[1] = st.number_input("Min Service Time", min_value=1, value=2)
        with col2:data_array[2] = st.number_input("Max Service Time", min_value=1, value=5)
        if data_array[1] >= data_array[2]:
            st.error("The service time range must be valid (start must be less than end)⚠️.")
            has_error = True
        col1, col2 = st.sidebar.columns(2)
        with col1:data_array[3] = st.number_input("Min Interarrival Time", min_value=1, value=1)
        with col2:data_array[4] = st.number_input("Max Interarrival Time", min_value=1, value=4)
        if data_array[3] >= data_array[4]:
            st.error("The interarrival time range must be valid (start must be less than end)⚠️.")
            has_error = True
        EquivalentProbabilities = st.sidebar.checkbox("Use Equivalent Probabilities (Service Times Only)", value=True)
        data_array[12] = EquivalentProbabilities
        if not EquivalentProbabilities:
            data_array[5] = st.sidebar.text_input("Equivalent Service Times (space-separated)", "2 3 4 5")
        Auto_generate = st.sidebar.checkbox("Auto-generate Random Numbers", value=True)
        data_array[11] = Auto_generate
        if not Auto_generate:
            data_array[6] = st.sidebar.text_input("Service Random Numbers (space-separated)", "12 23 34")
            data_array[7] = st.sidebar.text_input("Arrival Random Numbers (space-separated)", "45 56 67")
            rand_values_service = list(map(int,data_array[6].split()))
            rand_values_arrival = list(map(int,data_array[7].split()))
            if not rand_values_service or not rand_values_arrival:
                st.error("Random numbers must be entered when auto randoms are disabled.")
                has_error = True
        EqualProbabilities = st.sidebar.checkbox("Use Equal Probabilities", value=True)
        data_array[10] = EqualProbabilities
        if not EqualProbabilities:
            data_array[8] =  st.sidebar.text_input("Service Probabilities (space-separated)", "0.2 0.5 0.3")
            data_array[9] =  st.sidebar.text_input("Interarrival Probabilities (space-separated)", "0.3 0.4 0.3")
            prob_Service = list(map(float,data_array[8].split()))
            prob_Interarrival = list(map(float,data_array[9].split()))
            if abs(sum(prob_Service) - 1) > 0.01:
                st.error("The sum of service probabilities must equal 1.⚠️")
                has_error = True
            if abs(sum(prob_Interarrival) - 1) > 0.01:
                st.error("The sum of Interarrival probabilities must equal 1.⚠️")
                has_error = True
            if not prob_Service or not prob_Interarrival:
                st.error("Probabilities must be entered when equal probability is disabled.⚠️")
                has_error = True
            if len(prob_Service) != (data_array[2]-data_array[1]+1):
                st.error("Probabilities must be entered equal to Service probability length.⚠️")
                has_error = True
            if len(prob_Interarrival) !=(data_array[4]-data_array[3]+1):
                st.error("Probabilities must be entered equal to Interarrival probability length.⚠️")
                has_error = True
    
    elif program == "Double_Server":

        data_array= np.zeros(17, dtype=object)
        data_array[0] = st.sidebar.number_input("Number of simulations", min_value=1, value=10)
        if data_array[0] < 1:
            st.error("The number of simulations must be a positive integer.⚠️")
            has_error = True
        col1, col2 = st.sidebar.columns(2)
        with col1:data_array[1] = st.number_input("Min Master Service Time", min_value=1, value=2)
        with col2:data_array[2] = st.number_input("Max Master Service Time", min_value=1, value=5)
        col1, col2 = st.sidebar.columns(2)
        with col1:data_array[3] = st.number_input("Min Slave Service Time", min_value=1, value=3)
        with col2:data_array[4] = st.number_input("Max Slave Service Time", min_value=1, value=6)
        if data_array[1] >= data_array[2]:
            st.error("The Master service time range must be valid (start must be less than end)⚠️.")
            has_error = True
        if data_array[3] >= data_array[4]:
            st.error("The Slave service time range must be valid (start must be less than end)⚠️.")
            has_error = True
        col1, col2 = st.sidebar.columns(2)
        with col1:data_array[5] = st.number_input("Min Interarrival Time", min_value=1, value=1)
        with col2:data_array[6] = st.number_input("Max Interarrival Time", min_value=1, value=4)
        if data_array[5] >= data_array[6]:
            st.error("The interarrival time range must be valid (start must be less than end)⚠️.")
            has_error = True

        EquivalentProbabilities = st.sidebar.checkbox("Use Equivalent Probabilities (Service Times Only)", value=True)
        data_array[16] = EquivalentProbabilities
        if not EquivalentProbabilities:
            data_array[7] = st.sidebar.text_input("Equivalent Master Service Times (space-separated)", "2 3 4 5")
            data_array[8] = st.sidebar.text_input("Equivalent Slave Service Times (space-separated)", "8 3 2 5")
        Auto_generate = st.sidebar.checkbox("Auto-generate Random Numbers", value=True)
        data_array[15] = Auto_generate
        if not Auto_generate:
            data_array[9] = st.sidebar.text_input("Service Random Numbers (space-separated)", "95 21 51 92 89 38 13 61 50 49 ")
            data_array[10] = st.sidebar.text_input("Arrival Random Numbers (space-separated)", "26 98 90 26 42 74 80 68 22")
            rand_values_service = list(map(int,data_array[9].split()))
            rand_values_arrival = list(map(int,data_array[10].split()))
            if not rand_values_service or not rand_values_arrival:
                st.error("Random numbers must be entered when auto randoms are disabled.")
                has_error = True
        EqualProbabilities = st.sidebar.checkbox("Use Equal Probabilities", value=True)
        data_array[14] = EqualProbabilities
        if not EqualProbabilities:
            data_array[11] =  st.sidebar.text_input("Master Service Probabilities (space-separated)", "0.30 0.28 0.25 0.17")
            data_array[12] =  st.sidebar.text_input("Slave Service Probabilities (space-separated)", "0.35 0.25 0.20 0.20")
            data_array[13] =  st.sidebar.text_input("Interarrival Probabilities (space-separated)", "0.25 0.40 0.20 0.15")
            prob_Master_Service = list(map(float,data_array[11].split()))
            prob_Slave_Service = list(map(float,data_array[12].split()))
            prob_Interarrival = list(map(float,data_array[13].split()))
            if abs(sum(prob_Master_Service) - 1) > 0.01:
                st.error("The sum of Master service probabilities must equal 1.⚠️")
                has_error = True
            if abs(sum(prob_Slave_Service) - 1) > 0.01:
                st.error("The sum of Slave service probabilities must equal 1.⚠️")
                has_error = True
            if abs(sum(prob_Interarrival) - 1) > 0.01:
                st.error("The sum of Interarrival probabilities must equal 1.⚠️")
                has_error = True
            if not prob_Master_Service or not prob_Interarrival or not prob_Slave_Service:
                st.error("Probabilities must be entered when equal probability is disabled.⚠️")
                has_error = True
            if len(prob_Slave_Service) != (data_array[4]-data_array[3]+1):
                st.error("Probabilities must be entered equal to Service probability length.⚠️")
                has_error = True
            if len(prob_Master_Service) != (data_array[2]-data_array[1]+1):
                st.error("Probabilities must be entered equal to Service probability length.⚠️")
                has_error = True
            if len(prob_Interarrival) !=(data_array[6]-data_array[5]+1):
                st.error("Probabilities must be entered equal to Interarrival probability length.⚠️")
                has_error = True
    
    elif program == "Inventory_Daily_Management":
        data_array = np.zeros(17, dtype=object)
        data_array[0] = st.sidebar.number_input("Number of Days (simulation)", min_value=1, value=10)
        if data_array[0] < 1:
            st.error("The number of simulations must be a positive integer.⚠️")
            has_error = True
            
        col1, col2 = st.sidebar.columns(2)
        with col1:data_array[1] = st.number_input("Min Daily Demand (units)", min_value=1, value=3)
        with col2:data_array[2] = st.number_input("Max Daily Demand (units)", min_value=1, value=6)
        if data_array[1] >= data_array[2]:
            st.error("The daily demand range must be valid (start must be less than end)⚠️.")
            has_error = True

        col1, col2 = st.sidebar.columns(2)
        with col1:data_array[3] = st.number_input("Min Lead Time (Days)", min_value=1, value=2)
        with col2:data_array[4] = st.number_input("Max Lead Time (Days)", min_value=1, value=4)
        if data_array[3] >= data_array[4]:
            st.error("The lead time range must be valid (start must be less than end)⚠️.")
            has_error = True

        EqualProbabilities = st.sidebar.checkbox("Use Equal Probabilities", value=False)
        data_array[10] = EqualProbabilities
        if not EqualProbabilities:
            data_array[8] =  st.sidebar.text_input("Demand Probabilities (space-separated)", "0.15 0.30 0.35 0.20")
            data_array[9] =  st.sidebar.text_input("Lead Time Probabilities (space-separated)", "0.2 0.6 0.2")
            prob_Demand = list(map(float,data_array[8].split()))
            prob_LeadTime = list(map(float,data_array[9].split()))
            if abs(sum(prob_Demand) - 1) > 0.01:
                st.error("The sum of Demand probabilities must equal 1.⚠️")
                has_error = True
            if abs(sum(prob_LeadTime) - 1) > 0.01:
                st.error("The sum of Lead Time probabilities must equal 1.⚠️")
                has_error = True
            if not prob_Demand or not prob_LeadTime:
                st.error("Probabilities must be entered when equal probability is disabled.⚠️")
                has_error = True
            if len(prob_Demand) != (data_array[2]-data_array[1]+1):
                st.error("Probabilities must be entered equal to Demand probability length.⚠️")
                has_error = True
            if len(prob_LeadTime) !=(data_array[4]-data_array[3]+1):
                st.error("Probabilities must be entered equal to Lead Time probability length.⚠️")
                has_error = True
 
        Auto_generate = st.sidebar.checkbox("Auto-generate Random Numbers", value=False)
        data_array[7] = Auto_generate
        if not Auto_generate:
            data_array[5] = st.sidebar.text_input("Demand Random Numbers (space-separated)", "64 33 18 94 78 17 54 09 28 72")
            data_array[6] = st.sidebar.text_input("Lead time Random Numbers (space-separated)", "5 1 9 4")
            rand_values_Demand = list(map(int,data_array[5].split()))
            rand_values_LeadTime = list(map(int,data_array[6].split()))
            if not rand_values_Demand or not rand_values_LeadTime:
                st.error("Random numbers must be entered when auto randoms are disabled.")
                has_error = True
        st.sidebar.markdown("---")
        st.sidebar.markdown("### Reorder Point one (RP1)")
        col1, col2 = st.sidebar.columns(2)
        with col1:data_array[11] = st.number_input("Min Inventory (unit)", min_value=1, value=10, key="RP1_1")
        with col2:data_array[12] = st.number_input("Recharge unit Number", min_value=1, value=15 ,key="RP1_2")
        if data_array[11] < 0:
            st.error("The Inventory Level must be a positive integer.⚠️")
            has_error = True
        if data_array[12] < 0:
            st.error("The Recharge unit Number must be a positive integer.⚠️")
            has_error = True
        st.sidebar.markdown("---")
        st.sidebar.markdown("### Reorder Point two (RP2)")
        col1, col2 = st.sidebar.columns(2)
        with col1:data_array[13] = st.number_input("Min Inventory (unit)", min_value=1, value=5 , key="RP2_1")
        with col2:data_array[14] = st.number_input("Recharge unit Number", min_value=1, value=15 , key="RP2_2")
        if data_array[13] < 0:
            st.error("The Inventory Level must be a positive integer.⚠️")
            has_error = True
        if data_array[14] < 0:
            st.error("The Recharge unit Number must be a positive integer.⚠️")
            has_error = True

        st.sidebar.markdown("---")
        st.sidebar.markdown("### Pre-Settings")
        data_array[15] = st.sidebar.number_input("Initial Inventory Level (unit)", min_value=1, value=10)
        if data_array[15] < 0:
            st.error("The Initial Inventory Level must be a positive integer.⚠️")
            has_error = True
        Shortage_case = st.sidebar.checkbox("Shortage In Demand Is Lost Forever", value=False)
        data_array[16] = Shortage_case
        if Shortage_case:
            st.sidebar.markdown("**Note:** The shortage in demand : lost forever.")
        else:
            st.sidebar.markdown("**Note:** The shortage in demand : backordered.")
    
    elif program == "Inventory_Cycle_Management":
        data_array = np.zeros(17, dtype=object)
        data_array[0] = st.sidebar.number_input("Number of Cycles (simulation)", min_value=1, value=5)
        if data_array[0] < 1:
            st.error("The number of simulations must be a positive integer.⚠️")
            has_error = True
            
        col1, col2 = st.sidebar.columns(2)
        with col1:data_array[1] = st.number_input("Min Daily Demand (units)", min_value=0, value=0)
        with col2:data_array[2] = st.number_input("Max Daily Demand (units)", min_value=0, value=4)
        if data_array[1] >= data_array[2]:
            st.error("The daily demand range must be valid (start must be less than end)⚠️.")
            has_error = True

        col1, col2 = st.sidebar.columns(2)
        with col1:data_array[3] = st.number_input("Min Lead Time (Days)", min_value=0, value=1)
        with col2:data_array[4] = st.number_input("Max Lead Time (Days)", min_value=0, value=3)
        if data_array[3] >= data_array[4]:
            st.error("The lead time range must be valid (start must be less than end)⚠️.")
            has_error = True

        EqualProbabilities = st.sidebar.checkbox("Use Equal Probabilities", value=False)
        data_array[10] = EqualProbabilities
        if not EqualProbabilities:
            data_array[8] =  st.sidebar.text_input("Demand Probabilities (space-separated)", "0.10 0.25 0.35 0.21 0.09")
            data_array[9] =  st.sidebar.text_input("Lead Time Probabilities (space-separated)", "0.6 0.3 0.1")
            prob_Demand = list(map(float,data_array[8].split()))
            prob_LeadTime = list(map(float,data_array[9].split()))
            if abs(sum(prob_Demand) - 1) > 0.01:
                st.error("The sum of Demand probabilities must equal 1.⚠️")
                has_error = True
            if abs(sum(prob_LeadTime) - 1) > 0.01:
                st.error("The sum of Lead Time probabilities must equal 1.⚠️")
                has_error = True
            if not prob_Demand or not prob_LeadTime:
                st.error("Probabilities must be entered when equal probability is disabled.⚠️")
                has_error = True
            if len(prob_Demand) != (data_array[2]-data_array[1]+1):
                st.error("Probabilities must be entered equal to Demand probability length.⚠️")
                has_error = True
            if len(prob_LeadTime) !=(data_array[4]-data_array[3]+1):
                st.error("Probabilities must be entered equal to Lead Time probability length.⚠️")
                has_error = True
 
        Auto_generate = st.sidebar.checkbox("Auto-generate Random Numbers", value=False)
        data_array[7] = Auto_generate
        if not Auto_generate:
            data_array[5] = st.sidebar.text_input("Demand Random Numbers (space-separated)", "24 35 65 81 54 03 87 27 73 70 47 45 48 17 09 42 87 26 36 40 07 63 19 88 94")
            data_array[6] = st.sidebar.text_input("Lead time Random Numbers (space-separated)", "5 0 3 4 8")
            rand_values_Demand = list(map(int,data_array[5].split()))
            rand_values_LeadTime = list(map(int,data_array[6].split()))
            if not rand_values_Demand or not rand_values_LeadTime:
                st.error("Random numbers must be entered when auto randoms are disabled.")
                has_error = True
        st.sidebar.markdown("---")
        
        st.sidebar.markdown("### Inventory Data ")
        data_array[11] = st.sidebar.number_input("Stander Inventory Level M (unit)", min_value=1, value=11)
        data_array[12] = st.sidebar.number_input("Periodic length N (day)", min_value=1, value=5)
        if data_array[11] < 0:
            st.error("The Stander Level must be a positive integer.⚠️")
            has_error = True
        if data_array[12] < 0:
            st.error("The Periodic unit Number must be a positive integer.⚠️")
            has_error = True

        st.sidebar.markdown("---")
        st.sidebar.markdown("### Initial Settings")
        data_array[13] = st.sidebar.number_input("Previous Reordering (unit)", min_value=1, value=8 )
        data_array[14] = st.sidebar.number_input("After (days)", min_value=1, value=2 )
        if data_array[13] < 0:
            st.error("The Inventory Level must be a positive integer.⚠️")
            has_error = True
        if data_array[14] < 0:
            st.error("The Recharge unit Number must be a positive integer.⚠️")
            has_error = True

        data_array[15] = st.sidebar.number_input("Starting quantity (unit)", min_value=1, value=3)
        if data_array[15] < 0:
            st.error("The start Inventory Level must be a positive integer.⚠️")
            has_error = True
        Shortage_case = st.sidebar.checkbox("Shortage In Demand Is Resumed", value=True)
        data_array[16] = Shortage_case
        if not Shortage_case:
            st.sidebar.markdown("**Note:** The shortage in demand : lost forever.")
        else:
            st.sidebar.markdown("**Note:** The shortage in demand : backordered.")        

    elif program == "Gambing_Game":
        data_array= np.zeros(10, dtype=object)
        Head = "Head"
        Tail = "Tail"
        data_array[0] = st.sidebar.number_input("Number of Trails (game play)", min_value=1, value=7)
        if data_array[0] <= 1:
            st.error("The number of simulations must be a positive integer.⚠️")
            has_error = True
        data_array[1] = st.sidebar.number_input("Cost Of One Flip ($) :", min_value=1, value=1)
        data_array[2] = st.sidebar.number_input("Win Cost ($) :", min_value=1, value=8)
        Auto_rand = st.sidebar.checkbox("Use Auto Randoms (H/T)", value=True)
        data_array[5] = Auto_rand
        if not Auto_rand:
            data_array[4] = st.sidebar.text_input("Enter Random Numbers (space-separated)", "2 3 4 5") 
            rand_values = list(map(int,data_array[4].split()))
            for i in range(len(rand_values)):
                if rand_values[i] < 0 or rand_values[i] > 9:
                    st.error(f"The random value at index {i} is invalid: {rand_values[i]} ⚠️ Must be between 0 and 9.")
                    has_error = True
            if  not rand_values:
                st.error("Th Randoms must be Entered ⚠️.")
                has_error = True

        if data_array[1] <= 0:
            st.error("The Win Cost must be valid (start must be 1)⚠️.")
            has_error = True   
        if data_array[2] <= 0:
            st.error("The Cost Of One Flip must be valid (start must be 1)⚠️.")
            has_error = True   
        st.sidebar.markdown("---")
        st.sidebar.markdown("### 🎰 Game Conditions ")   
        data_array[3] = st.sidebar.number_input("Difference Between (H/T):", min_value=1, value=3) 
        if data_array[3] <= 0:
            st.error("The Difference Between (H/T) must be a positive integer.⚠️")
            has_error = True
        data_array[6] = st.sidebar.selectbox("Upper Pound (5 - 9) :", [Head, Tail], index=1)
        data_array[7] = st.sidebar.number_input("Max Trails in One Game :", min_value=1, value=100)
    

        Initial_cost = st.sidebar.checkbox("Don't Use Initial Cost", value=True)
        data_array[9] = Initial_cost
        if not Initial_cost:
            data_array[8] = st.sidebar.text_input("Enter Inital Cost ($) :", "2000") 
            if not data_array[8]:
                st.error("The cost must be Entered ⚠️.")
                has_error = True



        st.sidebar.markdown("---")
    
    elif program == "Hinge_Assembly":
        data_array= np.zeros(11, dtype=object)
        data_array[0] = st.sidebar.number_input("Number of Trails (Assembly)", min_value=1, value=20)
        if data_array[0] <= 1:
            st.error("The number of simulations must be a positive integer.⚠️")
            has_error = True

        st.sidebar.markdown("---")
        st.sidebar.markdown("### 🌒 Assembled Parts (A + B + C) ")  
        col1, col2  = st.sidebar.columns(2)
        with col1:data_array[1] = st.number_input("A Size:", min_value=1.0, value=2.0)
        with col2:data_array[2] = st.number_input("± A Ratio", min_value=0.0001, value=0.05, max_value=0.9999)        
        col1, col2 = st.sidebar.columns(2)
        with col1:data_array[3] = st.number_input("B Size:", min_value=1.0, value=2.0)
        with col2:data_array[4] = st.number_input("± B Ratio", min_value=0.0001, value=0.05 , max_value=0.9999)  
        col1, col2 = st.sidebar.columns(2)
        with col1:data_array[5] = st.number_input("C Size:", min_value=1.0, value=30.0)
        with col2:data_array[6] = st.number_input("± C Ratio", min_value=0.0001, value=0.5 , max_value=0.9999)  
        st.sidebar.markdown("---")
        st.sidebar.markdown("### 🌖 General Part (D) ")   
        col1, col2  = st.sidebar.columns(2)
        with col1:data_array[7] = st.number_input("D Size:", min_value=1.0, value=34.5)
        with col2:data_array[8] = st.number_input("± D Ratio", min_value=0.0001, value=0.5, max_value=0.9999) 
        st.sidebar.markdown("---")
        Auto_rand = st.sidebar.checkbox("Use Auto Randoms", value=True)
        data_array[10] = Auto_rand
        if not Auto_rand:
            data_array[9] = st.sidebar.text_input("Enter Integer Random (space-separated)", "44 56 32 12 23 45 67 89 90 11 22 33 44 55 66 77 23 45 67 89") 
            rand_values = list(map(int,data_array[9].split()))
            for i in range(len(rand_values)):
                if rand_values[i] < 0 or rand_values[i] > 99:
                    st.error(f"The random value at index {i} is invalid: {rand_values[i]} ⚠️ Must be between 0 and 99.")
                    has_error = True
            if len(rand_values) != data_array[0]*4:
                st.error(f"The random values must be equal to the number of trails * number of part (4) .⚠️")
                has_error = True
            if  not rand_values:
                st.error("Th Randoms must be Entered ⚠️.")
                has_error = True
        if data_array[1] + data_array[3] + data_array[5] > (data_array[7] - data_array[8]):
            st.error("Can't Assembled : Shape(a+b+c) > Shape(d).⚠️")
            has_error = True
      
    else:
        st.error("Invalid program selected.")
        has_error = True
        data_array = None
    return data_array, has_error

def data_labeled():
    if program == "Inventory_Daily_Management":
        days = st.session_state.input_data_array[0]
    elif program == "Gambing_Game":
        Game_cycle = st.session_state.input_data_array[0]
        Flip_Cost = st.session_state.input_data_array[1]
        Win_Cost = st.session_state.input_data_array[2]
        Game_Condition = st.session_state.input_data_array[3]
        Rand_Values = st.session_state.input_data_array[4]
        Auto_rand = st.session_state.input_data_array[5]
        Upper_Pound = st.session_state.input_data_array[6]
        Max_Trails = st.session_state.input_data_array[7]
        Inital_cost = st.session_state.input_data_array[8]
        initial_cost_case = st.session_state.input_data_array[9]
    elif program == "Hinge_Assembly":
        assembly = st.session_state.input_data_array[0]
        A_size = st.session_state.input_data_array[1]
        A_ratio = st.session_state.input_data_array[2]
        B_size = st.session_state.input_data_array[3]
        B_ratio = st.session_state.input_data_array[4]
        C_size = st.session_state.input_data_array[5]
        C_ratio = st.session_state.input_data_array[6]
        D_size = st.session_state.input_data_array[7]
        D_ratio = st.session_state.input_data_array[8]
        Auto_rand = st.session_state.input_data_array[10]
        rand_values = st.session_state.input_data_array[9]


def RandomNum(MaxNumRange):
   return int(random.uniform(0, MaxNumRange))
def GetProbabilities(var_data):
    probabilities = np.array(list(map(float,var_data.split())))
    return probabilities
def GetRandomNumbers(var_data):
    probabilities = np.array(list(map(int,var_data.split())))
    return probabilities


def CalculateProbability(StartRange, EndRange, ProbabilityCase, ProbValues=None):
    ProbabilityArry = np.zeros((EndRange - StartRange + 1, 5), dtype=float)
    CumulativeProb = 0

    for i in range(StartRange, EndRange + 1):
        ProbabilityArry[i - StartRange, 0] = i

    if ProbabilityCase:
        ProbValue = 1 / (EndRange - StartRange + 1)
        for i in range(StartRange, EndRange + 1):
            ProbabilityArry[i - StartRange, 1] = ProbValue    
    else:
        for i in range(StartRange, EndRange + 1):
            ProbabilityArry[i - StartRange, 1] = ProbValues[i - StartRange]

    for i in range(StartRange, EndRange + 1):
        CumulativeProb += ProbabilityArry[i - StartRange, 1]
        ProbabilityArry[i - StartRange, 2] = CumulativeProb 

    for i in range(StartRange, EndRange + 1):
        index = i - StartRange
        if index == 0:
            ProbabilityArry[index, 3] = 0
        else: 
            ProbabilityArry[index, 3] = (round(ProbabilityArry[index - 1, 2] * 100))
        ProbabilityArry[index, 4] = (round((ProbabilityArry[index, 2] * 100) - 1))
    
    return ProbabilityArry

def CalRandomTime(RandNum, StartR, EndR, ProbyCase, ProbValues):
    CheckArry = CalculateProbability(StartR, EndR, ProbyCase, ProbValues)
    
    for i in range(StartR, EndR + 1):
        if (CheckArry[i - StartR, 4] >= RandNum) and (CheckArry[i - StartR, 3] <= RandNum): 
            return CheckArry[i - StartR, 0]

def ProbabilityTable(program):
        try:
            if program == "Single_Server":    
                SimulateNumber = st.session_state.input_data_array[0] 
                StartRangeServiceTime = st.session_state.input_data_array[1] 
                EndRangeServiceTime = st.session_state.input_data_array[2] 
                StartRangeInterArrivalTime = st.session_state.input_data_array[3]
                EndRangeInterArrivalTime = st.session_state.input_data_array[4]
                EqualProbabilityNumbers = st.session_state.input_data_array[5] 
                probservice = st.session_state.input_data_array[8]
                probInterarrival = st.session_state.input_data_array[9]
                ProbabilityCase = st.session_state.input_data_array[10]
                EquivalentCase = st.session_state.input_data_array[12]

                
                headers = ["Service Time", "Probability", "Cumulative", "Start Range", "End Range"] 
                if not ProbabilityCase:
                    ProbValuesServiceTime = GetProbabilities(probservice)
                    ProbValuesInterArrivalTime = GetProbabilities(probInterarrival)
                else: 
                    ProbValuesServiceTime = ProbValuesInterArrivalTime = None

                ProbArryServiceTime = CalculateProbability(StartRangeServiceTime, EndRangeServiceTime, ProbabilityCase, ProbValuesServiceTime)
                ProbArryInterArrivalTime = CalculateProbability(StartRangeInterArrivalTime, EndRangeInterArrivalTime, ProbabilityCase, ProbValuesInterArrivalTime)
                if not EquivalentCase:
                    Val = GetRandomNumbers(EqualProbabilityNumbers)
                    probVall = [val for val in Val if StartRangeServiceTime <= val <= EndRangeServiceTime]
                    df_service_equal = pd.DataFrame(probVall, columns=headers[0:1])
                # Convert to DataFrames
                df_service = pd.DataFrame(ProbArryServiceTime, columns=headers)
                df_interarrival = pd.DataFrame(ProbArryInterArrivalTime, columns=headers)

                # Format service DataFrame
                df_service["Service Time"] = df_service["Service Time"].astype(int)
                df_service["Start Range"] = df_service["Start Range"].astype(int)
                df_service["End Range"] = df_service["End Range"].astype(int)
                df_service["Probability"] = df_service["Probability"].map("{:.2f}".format)
                df_service["Cumulative"] = df_service["Cumulative"].map("{:.2f}".format)

                # Format interarrival DataFrame
                df_interarrival["Service Time"] = df_interarrival["Service Time"].astype(int)
                df_interarrival["Start Range"] = df_interarrival["Start Range"].astype(int)
                df_interarrival["End Range"] = df_interarrival["End Range"].astype(int)
                df_interarrival["Probability"] = df_interarrival["Probability"].map("{:.2f}".format)
                df_interarrival["Cumulative"] = df_interarrival["Cumulative"].map("{:.2f}".format)

                # Display Service Time Table
                st.subheader("⌛ Service Time Probability Array")
                if EquivalentCase:
                    st.dataframe(df_service)
                else:
                    st.dataframe(df_service_equal)
                st.markdown("-----")

                # Display Inter Arrival Time Table
                st.subheader("⏱️ Inter Arrival Time Probability Array")
                st.dataframe(df_interarrival)
            elif program == "Double_Server":

                StartRangeMasterServiceTime = st.session_state.input_data_array[1] 
                EndRangeMasterServiceTime = st.session_state.input_data_array[2] 
                StartRangeMSlaveServiceTime = st.session_state.input_data_array[3] 
                EndRangeSlaveServiceTime = st.session_state.input_data_array[4] 
                StartRangeInterArrivalTime = st.session_state.input_data_array[5]
                EndRangeInterArrivalTime = st.session_state.input_data_array[6]
                EqualProbabilityMasterNumbers = st.session_state.input_data_array[7]
                EqualProbabilitySlaveNumbers = st.session_state.input_data_array[8]
                probMasterService = st.session_state.input_data_array[11]
                probSlaveService = st.session_state.input_data_array[12]
                probInterarrival = st.session_state.input_data_array[13]
                ProbabilityCase = st.session_state.input_data_array[14]
                EquivalentCase = st.session_state.input_data_array[16]

                headers = ["Service Time", "Probability", "Cumulative", "Start Range", "End Range"] 
                if not ProbabilityCase:
                    ProbValuesMasterServiceTime = GetProbabilities(probMasterService)
                    ProbValuesSlaveServiceTime = GetProbabilities(probSlaveService)
                    ProbValuesInterArrivalTime = GetProbabilities(probInterarrival)
                else: 
                    ProbValuesMasterServiceTime = ProbValuesSlaveServiceTime = ProbValuesInterArrivalTime = None

                ProbArryMasterServiceTime = CalculateProbability(StartRangeMasterServiceTime, EndRangeMasterServiceTime, ProbabilityCase, ProbValuesMasterServiceTime)
                ProbArrySlaveServiceTime = CalculateProbability(StartRangeMSlaveServiceTime, EndRangeSlaveServiceTime, ProbabilityCase, ProbValuesSlaveServiceTime)
                ProbArryInterArrivalTime = CalculateProbability(StartRangeInterArrivalTime, EndRangeInterArrivalTime, ProbabilityCase, ProbValuesInterArrivalTime)
                if not EquivalentCase:
                    probValM = GetRandomNumbers(EqualProbabilityMasterNumbers)
                    probValMaster = [val for val in probValM if StartRangeMasterServiceTime <= val <= EndRangeMasterServiceTime]
                    probVals = GetRandomNumbers(EqualProbabilitySlaveNumbers)
                    probValSlave = [val for val in probVals if StartRangeMSlaveServiceTime <= val <= EndRangeSlaveServiceTime]
                    df_service_equal_master = pd.DataFrame(probValMaster, columns=headers[0:1])
                    df_service_equal_slave = pd.DataFrame(probValSlave, columns=headers[0:1])
                # Convert to DataFrames
                df_service_Master = pd.DataFrame(ProbArryMasterServiceTime, columns=headers)
                df_service_Slave = pd.DataFrame(ProbArrySlaveServiceTime, columns=headers)
                df_interarrival = pd.DataFrame(ProbArryInterArrivalTime, columns=headers)

                # Format service DataFrame
                df_service_Master["Service Time"] = df_service_Master["Service Time"].astype(int)
                df_service_Master["Start Range"] = df_service_Master["Start Range"].astype(int)
                df_service_Master["End Range"] = df_service_Master["End Range"].astype(int)
                df_service_Master["Probability"] = df_service_Master["Probability"].map("{:.2f}".format)
                df_service_Master["Cumulative"] = df_service_Master["Cumulative"].map("{:.2f}".format)

                # Format service DataFrame
                df_service_Slave ["Service Time"] = df_service_Slave ["Service Time"].astype(int)
                df_service_Slave ["Start Range"] = df_service_Slave ["Start Range"].astype(int)
                df_service_Slave ["End Range"] = df_service_Slave ["End Range"].astype(int)
                df_service_Slave ["Probability"] = df_service_Slave ["Probability"].map("{:.2f}".format)
                df_service_Slave ["Cumulative"] = df_service_Slave ["Cumulative"].map("{:.2f}".format)

                # Format interarrival DataFrame
                df_interarrival["Service Time"] = df_interarrival["Service Time"].astype(int)
                df_interarrival["Start Range"] = df_interarrival["Start Range"].astype(int)
                df_interarrival["End Range"] = df_interarrival["End Range"].astype(int)
                df_interarrival["Probability"] = df_interarrival["Probability"].map("{:.2f}".format)
                df_interarrival["Cumulative"] = df_interarrival["Cumulative"].map("{:.2f}".format)

                # Display Service Time Table
                st.subheader("🥇 Master Service Time Probability ")
                if EquivalentCase:
                    st.dataframe(df_service_Master)
                else:
                    st.dataframe(df_service_equal_master)
                st.markdown("-----")

                st.subheader("🥈 Slave Service Time Probability ")
                if EquivalentCase:
                    st.dataframe(df_service_Slave)
                else:
                    st.dataframe(df_service_equal_slave)
                st.markdown("-----")

                # Display Inter Arrival Time Table
                st.subheader("⏱️ Inter Arrival Time Probability ")
                st.dataframe(df_interarrival)
            elif program == "Inventory_Daily_Management":


                start_range_demand = st.session_state.input_data_array[1]
                end_range_demand = st.session_state.input_data_array[2]

                start_range_lead_time = st.session_state.input_data_array[3]
                end_range_lead_time = st.session_state.input_data_array[4]
                
                demand_probabilities = st.session_state.input_data_array[8]
                lead_time_probabilities = st.session_state.input_data_array[9]
                
                eqaul_probabilities = st.session_state.input_data_array[10]

                headers_demand = ["Demand", "Probability", "Cumulative", "Start Range", "End Range"]
                headers_leadtime = ["Lead Time", "Probability", "Cumulative", "Start Range", "End Range"]
                
                if not eqaul_probabilities:
                    ProbValuesDemandTime = GetProbabilities(demand_probabilities)
                    ProbValuesLeadTime = GetProbabilities(lead_time_probabilities)
                else: 
                    ProbValuesDemandTime = ProbValuesLeadTime = None

                ProbArryDemandTime = CalculateProbability(start_range_demand, end_range_demand, eqaul_probabilities, ProbValuesDemandTime)
                ProbArryLeadTime = CalculateProbability(start_range_lead_time, end_range_lead_time, eqaul_probabilities, ProbValuesLeadTime)
                for i in range( end_range_lead_time - start_range_lead_time  + 1):
                    ProbArryLeadTime[i, 3] = int(ProbArryLeadTime[i, 3]/ 10)
                    ProbArryLeadTime[i, 4] = int(ProbArryLeadTime[i, 4]/ 10)

                # Convert to DataFrames
                df_demand = pd.DataFrame(ProbArryDemandTime, columns=headers_demand)
                df_leadtime = pd.DataFrame(ProbArryLeadTime, columns=headers_leadtime)

                # Format demand DataFrame
                df_demand["Demand"] = df_demand["Demand"].astype(int)
                df_demand["Start Range"] = df_demand["Start Range"].astype(int)
                df_demand["End Range"] = df_demand["End Range"].astype(int)
                df_demand["Probability"] = df_demand["Probability"].map("{:.2f}".format)
                df_demand["Cumulative"] = df_demand["Cumulative"].map("{:.2f}".format)

                # Format lead time DataFrame
                df_leadtime["Lead Time"] = df_leadtime["Lead Time"].astype(int)
                df_leadtime["Start Range"] = df_leadtime["Start Range"].astype(int)
                df_leadtime["End Range"] = df_leadtime["End Range"].astype(int)
                df_leadtime["Probability"] = df_leadtime["Probability"].map("{:.2f}".format)
                df_leadtime["Cumulative"] = df_leadtime["Cumulative"].map("{:.2f}".format)

                # Display Demand Table
                st.subheader("📦 Daily Demand Probability Array")
                st.dataframe(df_demand)
                st.markdown("-----")


                # Display Lead Time Table
                st.subheader("⏲️ Lead Time Probability Array")
                st.dataframe(df_leadtime)
            elif program == "Inventory_Cycle_Management":
                start_range_demand = st.session_state.input_data_array[1]
                end_range_demand = st.session_state.input_data_array[2]

                start_range_lead_time = st.session_state.input_data_array[3]
                end_range_lead_time = st.session_state.input_data_array[4]
                
                demand_probabilities = st.session_state.input_data_array[8]
                lead_time_probabilities = st.session_state.input_data_array[9]
                
                eqaul_probabilities = st.session_state.input_data_array[10]

                headers_demand = ["Demand", "Probability", "Cumulative", "Start Range", "End Range"]
                headers_leadtime = ["Lead Time", "Probability", "Cumulative", "Start Range", "End Range"]
                
                if not eqaul_probabilities:
                    ProbValuesDemandTime = GetProbabilities(demand_probabilities)
                    ProbValuesLeadTime = GetProbabilities(lead_time_probabilities)
                else: 
                    ProbValuesDemandTime = ProbValuesLeadTime = None

                ProbArryDemandTime = CalculateProbability(start_range_demand, end_range_demand, eqaul_probabilities, ProbValuesDemandTime)
                ProbArryLeadTime = CalculateProbability(start_range_lead_time, end_range_lead_time, eqaul_probabilities, ProbValuesLeadTime)
                for i in range( end_range_lead_time - start_range_lead_time  + 1):
                    ProbArryLeadTime[i, 3] = int(ProbArryLeadTime[i, 3]/ 10)
                    ProbArryLeadTime[i, 4] = int(ProbArryLeadTime[i, 4]/ 10)

                # Convert to DataFrames
                df_demand = pd.DataFrame(ProbArryDemandTime, columns=headers_demand)
                df_leadtime = pd.DataFrame(ProbArryLeadTime, columns=headers_leadtime)

                # Format demand DataFrame
                df_demand["Demand"] = df_demand["Demand"].astype(int)
                df_demand["Start Range"] = df_demand["Start Range"].astype(int)
                df_demand["End Range"] = df_demand["End Range"].astype(int)
                df_demand["Probability"] = df_demand["Probability"].map("{:.2f}".format)
                df_demand["Cumulative"] = df_demand["Cumulative"].map("{:.2f}".format)
        
                st.subheader("📦 Daily Demand Probability Array")
                st.dataframe(df_demand)
                st.markdown("-----")


                # Display Lead Time Table
                st.subheader("⏲️ Lead Time Probability Array")
                st.dataframe(df_leadtime)
            elif program == "Hinge_Assembly":

                A_size = st.session_state.input_data_array[1]
                A_ratio = st.session_state.input_data_array[2]
                B_size = st.session_state.input_data_array[3]
                B_ratio = st.session_state.input_data_array[4]
                C_size = st.session_state.input_data_array[5]
                C_ratio = st.session_state.input_data_array[6]
                D_size = st.session_state.input_data_array[7]
                D_ratio = st.session_state.input_data_array[8]

                st.subheader("🔑 Assembly Parts Equations:")
                st.latex(fr"A_{{part}} = {A_size} ± {A_ratio}")
                st.latex(fr"B_{{part}} = {B_size} ± {B_ratio}")
                st.latex(fr"C_{{part}} = {C_size} ± {C_ratio}")
                st.latex(fr"D_{{part}} = {D_size} ± {D_ratio}")
                st.markdown("-----")

                headers = ["Part", "Minmum", "Maximum"]
                part_ranges = {
                    "A": (A_size - A_ratio, A_size + A_ratio),
                    "B": (B_size - B_ratio, B_size + B_ratio),
                    "C": (C_size - C_ratio, C_size + C_ratio),
                    "D": (D_size - D_ratio, D_size + D_ratio),
                }

                # تحويلها لقائمة لسهولة تحويلها لجدول
                rows = [[part, min_val, max_val] for part, (min_val, max_val) in part_ranges.items()]


                df_Assembly = pd.DataFrame(rows, columns=headers)
                st.subheader("📦 Assembly Parts Table")
                st.dataframe(df_Assembly)   
            else:
                st.error("Invalid program selected.")                
        except Exception as e:
            st.error(f"An error occurred while generating table: {e}")

def TableData(program):
    try:
        if program == "Single_Server":
            SimulateNumber = st.session_state.input_data_array[0] 
            StartRangeServiceTime = st.session_state.input_data_array[1] 
            EndRangeServiceTime = st.session_state.input_data_array[2] 
            StartRangeInterArrivalTime = st.session_state.input_data_array[3]
            EndRangeInterArrivalTime = st.session_state.input_data_array[4]
            EqualProbabilityNumbers = st.session_state.input_data_array[5] 
            ServiceRandomNumbers = st.session_state.input_data_array[6]
            ArrivalRandomNumbers = st.session_state.input_data_array[7]
            ServiceProbabilities = st.session_state.input_data_array[8] 
            InterarrivalProbabilities = st.session_state.input_data_array[9]
            EquivalentCase = st.session_state.input_data_array[12]
            ProbabilityCase = st.session_state.input_data_array[10]
            RandomCase = st.session_state.input_data_array[11]
            TableArry = np.zeros((SimulateNumber + 1, 11), dtype=int)
            InterArrivalTime = 0

            if not ProbabilityCase:
                ProbValuesServiceTime = GetProbabilities(ServiceProbabilities)
                ProbValuesInterArrivalTime = GetProbabilities(InterarrivalProbabilities)
            else:
                ProbValuesServiceTime = ProbValuesInterArrivalTime = None

            if not RandomCase:
                RandValuesServiceTime = GetRandomNumbers(ServiceRandomNumbers)
                RandValuesInterArrivalTime = GetRandomNumbers(ArrivalRandomNumbers)
            else:
                RandValuesServiceTime = RandValuesInterArrivalTime = None

            if not EquivalentCase:
                Vall = GetRandomNumbers(EqualProbabilityNumbers)
                probVal = [val for val in Vall if StartRangeServiceTime <= val <= EndRangeServiceTime]
            else:
                probVal = None

            for i in range(SimulateNumber):
                TableArry[i, 0] = i + 1

                if RandomCase:
                    TableArry[i + 1, 1] = RandomNum(99)
                    TableArry[i + 1, 2] = CalRandomTime(TableArry[i + 1, 1], StartRangeInterArrivalTime, EndRangeInterArrivalTime, ProbabilityCase, ProbValuesInterArrivalTime)
                else:
                    TableArry[i + 1, 1] = RandValuesInterArrivalTime[i] if i < len(RandValuesInterArrivalTime) else RandValuesInterArrivalTime[i % len(RandValuesInterArrivalTime)]
                    TableArry[i + 1, 2] = CalRandomTime(TableArry[i + 1, 1], StartRangeInterArrivalTime, EndRangeInterArrivalTime, ProbabilityCase, ProbValuesInterArrivalTime)

                if RandomCase and EquivalentCase:
                    TableArry[i, 4] = RandomNum(99)
                    TableArry[i, 5] = CalRandomTime(TableArry[i, 4], StartRangeServiceTime, EndRangeServiceTime, ProbabilityCase, ProbValuesServiceTime)
                if not RandomCase and EquivalentCase:
                    TableArry[i, 4] = RandValuesServiceTime[i] if i < len(RandValuesServiceTime) else RandValuesServiceTime[i % len(RandValuesServiceTime)]
                    TableArry[i, 5] = CalRandomTime(TableArry[i, 4], StartRangeServiceTime, EndRangeServiceTime, ProbabilityCase, ProbValuesServiceTime)
                if RandomCase and not EquivalentCase:
                    TableArry[i, 4] = 0
                    TableArry[i, 5] = (probVal[i] if i < len(probVal) else probVal[i % len(probVal)]) 
                if not RandomCase and not EquivalentCase:
                    TableArry[i, 4] = 0
                    TableArry[i, 5] = (probVal[i] if i < len(probVal) else probVal[i % len(probVal)])

                InterArrivalTime += TableArry[i + 1, 2]
                TableArry[i + 1, 3] = InterArrivalTime  

                if TableArry[i - 1, 8] >= TableArry[i, 3]:
                    TableArry[i, 6] = TableArry[i - 1, 8] 
                else:
                    TableArry[i, 6] = TableArry[i, 3]

                TableArry[i, 8] = TableArry[i, 5] + TableArry[i, 6]

                TableArry[i, 7] = TableArry[i, 6] - TableArry[i, 3]

                TableArry[i, 9] = TableArry[i, 5] + TableArry[i, 7]

                TableArry[i, 10] = TableArry[i, 6] - TableArry[i - 1, 8]

            TableArry[SimulateNumber] = np.sum(TableArry[:SimulateNumber], axis=0)

            TotalWhosWaitInQueue = np.count_nonzero(TableArry[:SimulateNumber, 7])
            st.session_state.output_data_Table = TableArry
            st.session_state.TotalWhosWaitInQueue = TotalWhosWaitInQueue
            st.session_state.program_type = "single_server"

            return TableArry, TotalWhosWaitInQueue,"single_server"
        elif program == "Double_Server":
            SimulateNumber = st.session_state.input_data_array[0]
            StartRangeMasterServiceTime = st.session_state.input_data_array[1] 
            EndRangeMasterServiceTime = st.session_state.input_data_array[2] 
            StartRangeMSlaveServiceTime = st.session_state.input_data_array[3] 
            EndRangeSlaveServiceTime = st.session_state.input_data_array[4] 
            StartRangeInterArrivalTime = st.session_state.input_data_array[5]
            EndRangeInterArrivalTime = st.session_state.input_data_array[6]
            EqualProbabilityMasterNumbers = st.session_state.input_data_array[7]
            EqualProbabilitySlaveNumbers = st.session_state.input_data_array[8]
            ServiceRandomNumbers = st.session_state.input_data_array[9]
            ArrivalRandomNumbers = st.session_state.input_data_array[10]
            probMasterService = st.session_state.input_data_array[11]
            probSlaveService = st.session_state.input_data_array[12]
            probInterarrival = st.session_state.input_data_array[13]
            ProbabilityCase = st.session_state.input_data_array[14]
            RandomCase = st.session_state.input_data_array[15]
            EquivalentCase = st.session_state.input_data_array[16]

            TableArry = np.zeros((SimulateNumber+2, 17), dtype=int)
            InterArrivalTime = 0

            if not ProbabilityCase:
                ProbValuesMasterServiceTime = GetProbabilities(probMasterService)
                ProbValuesSlaveServiceTime = GetProbabilities(probSlaveService)
                ProbValuesInterArrivalTime = GetProbabilities(probInterarrival)
            else: 
                ProbValuesMasterServiceTime = ProbValuesSlaveServiceTime = ProbValuesInterArrivalTime = None

            ProbArryMasterServiceTime = CalculateProbability(StartRangeMasterServiceTime, EndRangeMasterServiceTime, ProbabilityCase, ProbValuesMasterServiceTime)
            ProbArrySlaveServiceTime = CalculateProbability(StartRangeMSlaveServiceTime, EndRangeSlaveServiceTime, ProbabilityCase, ProbValuesSlaveServiceTime)
            ProbArryInterArrivalTime = CalculateProbability(StartRangeInterArrivalTime, EndRangeInterArrivalTime, ProbabilityCase, ProbValuesInterArrivalTime)
            
            if not EquivalentCase:
                probValM = GetRandomNumbers(EqualProbabilityMasterNumbers)
                probValMaster = [val for val in probValM if StartRangeMasterServiceTime <= val <= EndRangeMasterServiceTime]
                probVals = GetRandomNumbers(EqualProbabilitySlaveNumbers)
                probValSlave = [val for val in probVals if StartRangeMSlaveServiceTime <= val <= EndRangeSlaveServiceTime]
            else:
                probValMaster = probValSlave = None

            if not RandomCase:
                RandValuesServiceTime = GetRandomNumbers(ServiceRandomNumbers)
                RandValuesInterArrivalTime = GetRandomNumbers(ArrivalRandomNumbers)
            else:
                RandValuesServiceTime = RandValuesInterArrivalTime = None
            for i in range(1,SimulateNumber+1):
                
                TableArry[i,0] = i

                if  RandomCase:
                    TableArry[i+1,1] = RandomNum(99)
                    TableArry[i+1,2] = CalRandomTime(TableArry[i+1,1],StartRangeInterArrivalTime,EndRangeInterArrivalTime,ProbabilityCase,ProbValuesInterArrivalTime)
                else:
                    TableArry[i+1,1] = RandValuesInterArrivalTime[i-1] if i<= len(RandValuesInterArrivalTime) else RandValuesInterArrivalTime[i%(len(RandValuesInterArrivalTime))]
                    TableArry[i+1,2] = CalRandomTime(TableArry[i+1,1],StartRangeInterArrivalTime,EndRangeInterArrivalTime,ProbabilityCase,ProbValuesInterArrivalTime)
                
                InterArrivalTime += TableArry[i+1,2]
                TableArry[i+1,3] =  InterArrivalTime  

                if RandomCase:
                    TableArry[i,4] = RandomNum(99)
                    TableArry[i,5] = CalRandomTime(TableArry[i,4],StartRangeMasterServiceTime,EndRangeMasterServiceTime,ProbabilityCase,ProbValuesMasterServiceTime)
                    TableArry[i,6] = CalRandomTime(TableArry[i,4],StartRangeMSlaveServiceTime,EndRangeSlaveServiceTime,ProbabilityCase,ProbValuesSlaveServiceTime)
                else:
                    TableArry[i,4] = RandValuesServiceTime[i-1] if i<= len(RandValuesServiceTime) else RandValuesServiceTime[i%(len(RandValuesServiceTime))]
                    TableArry[i,5] = CalRandomTime(TableArry[i,4],StartRangeMasterServiceTime,EndRangeMasterServiceTime,ProbabilityCase,ProbValuesMasterServiceTime)
                    TableArry[i,6] = CalRandomTime(TableArry[i,4],StartRangeMSlaveServiceTime,EndRangeSlaveServiceTime,ProbabilityCase,ProbValuesSlaveServiceTime)

            for i in range(1, SimulateNumber+1):
                #if arr >= STXE(i-1) and STYE(i-1) !=0: WILL FILL X
                if TableArry[i,3] >= TableArry[i-1,9] and TableArry[i-1,9] !=0:
                    TableArry[i,7] = TableArry[i,3]
                    TableArry[i,8] = TableArry[i,5] # STX = STx
                    TableArry[i,9] = TableArry[i,7] + TableArry[i,8] # STXE = STX + STXB
                
                #if arr < STXE(i-1) and STYE(i-1) !=0: WILL FILL Y
                if TableArry[i,3] < TableArry[i-1,9] and TableArry[i-1,9] == TableArry[i-2,12]:
                    TableArry[i,7] = TableArry[i-1,9]
                    TableArry[i,8] = TableArry[i,5] # STX = STx
                    TableArry[i,9] = TableArry[i,7] + TableArry[i,8] # STXE = STX + STXB

                elif TableArry[i,3] < TableArry[i-1,9] and TableArry[i-1,9] !=0:

                    if TableArry[i-1,12] !=0:   
                        TableArry[i,10] = TableArry[i,3]
                        TableArry[i,11] = TableArry[i,6]
                        TableArry[i,12] = TableArry[i,10] + TableArry[i,11] # STYE = STY + STYB
                    elif TableArry[i-1,12] ==0: 
                        tempp = TableArry[i,3]
                        for j in range(i-1,0,-1):
                            if TableArry[j,12] != 0:
                                tempp = TableArry[j,12] 
                                break
                        TableArry[i,10] = max(tempp, TableArry[i,3])# STXB = AT
                        TableArry[i,11] = TableArry[i,6] # STX = STx
                        TableArry[i,12] = TableArry[i,10] + TableArry[i,11]               
                
                
                #if arr >= STXE(i-1) and STYE(i-1) == 0:
                if TableArry[i,3] >= TableArry[i-1,9] and TableArry[i-1,9] == 0:
                    tempp = TableArry[i,3]
                    for j in range(i-1,0,-1):
                        if TableArry[j,9] != 0:
                            tempp = TableArry[j,9] 
                            break
                    TableArry[i,7] = max(tempp, TableArry[i,3])# STXB = AT
                    TableArry[i,8] = TableArry[i,5] # STX = STx
                    TableArry[i,9] = TableArry[i,7] + TableArry[i,8] # STXE = STX + STXB
                
                TableArry[i,13] = TableArry[i,7] - TableArry[i,3] if TableArry[i,10] == 0 else TableArry[i,10] - TableArry[i,3] #QU = STYB - AT or STXB - AT
                TableArry[i,14] = TableArry[i,13] + TableArry[i,8]+ TableArry[i,11]# TS = QU + STX + STY

            for i in range( 1 , SimulateNumber+1):  
                if TableArry[i,7] != 0:
                    if TableArry[i-1,9] != 0 :
                        TableArry[i,15] = TableArry[i,7] - TableArry[i-1,9] #IDLEX  =  STXB(I) - STXE(I-1)
                    else :
                        tempp = 0
                        for j in range(i-1,0,-1):
                            if TableArry[j,9] != 0:
                                tempp = TableArry[j,9] 
                                break            
                        TableArry[i,15] = TableArry[i,7] - tempp #IDLEX  =  STXB(I) - STXE(I-1)
                if TableArry[i,10] != 0:
                    if TableArry[i-1,12] != 0:
                        TableArry[i,16] = TableArry[i,10] - TableArry[i-1,12] #IDLEX  =  STXB(I) - STXE(I-1)
                    else :
                        tempp = 0
                        for j in range(i-1,0,-1):
                            if TableArry[j,12] != 0:
                                tempp = TableArry[j,12] 
                                break            
                        TableArry[i,16] = TableArry[i,10] - tempp #IDLEX  =  STXB(I) - STXE(I-1)
            TableArry[SimulateNumber+1] = np.sum(TableArry[:SimulateNumber], axis=0)
            TotalWhosWaitInQueue = np.count_nonzero(TableArry[:SimulateNumber, 13])
            st.session_state.output_data_Table = TableArry
            st.session_state.TotalWhosWaitInQueue = TotalWhosWaitInQueue
            st.session_state.program_type = "Double_server"
            return TableArry, TotalWhosWaitInQueue,"Double_server"
        elif program == "Inventory_Daily_Management":

            days = st.session_state.input_data_array[0]
            start_range_demand = st.session_state.input_data_array[1]
            end_range_demand = st.session_state.input_data_array[2]
            start_range_lead_time = st.session_state.input_data_array[3]
            end_range_lead_time = st.session_state.input_data_array[4]
            demand_random_numbers = st.session_state.input_data_array[5]
            lead_time_random_numbers = st.session_state.input_data_array[6]
            demand_probabilities = st.session_state.input_data_array[8]
            lead_time_probabilities = st.session_state.input_data_array[9]
            eqaul_probabilities = st.session_state.input_data_array[10]
            auto_random_generate = st.session_state.input_data_array[7]
            reorder_point_1_limit = st.session_state.input_data_array[11]
            reorder_point_1_recharge = st.session_state.input_data_array[12]
            reorder_point_2_limit = st.session_state.input_data_array[13]
            reorder_point_2_recharge = st.session_state.input_data_array[14]
            initial_inventory = st.session_state.input_data_array[15]
            shortage_case = st.session_state.input_data_array[16]

            TableArry = np.zeros((days, 14), dtype=int)

            Cumulative_demand = 0 
            Cumulative_stock = 0
            cumulative_shortage = 0
            backup = 0 
            temp = 0             
            Pickup_lead_time = []

            if not eqaul_probabilities:
                ProbValuesDemandTime = GetProbabilities(demand_probabilities)
                ProbValuesLeadTimeTime = GetProbabilities(lead_time_probabilities)
            else: 
                ProbValuesDemandTime = ProbValuesLeadTimeTime = None

            
            ProbArryLeadTimeTime = CalculateProbability(start_range_lead_time, end_range_lead_time, eqaul_probabilities, ProbValuesLeadTimeTime)
            for i in range( end_range_lead_time - start_range_lead_time  + 1):
                ProbArryLeadTimeTime[i, 3] = ProbArryLeadTimeTime[i, 3]/ 10
                ProbArryLeadTimeTime[i, 4] = ProbArryLeadTimeTime[i, 4]/ 10
            
            if not auto_random_generate:
                RandValuesDemandTime = GetRandomNumbers(demand_random_numbers)
                RandValuesLeadTimeTime = GetRandomNumbers(lead_time_random_numbers)
            else:
                RandValuesDemandTime = RandValuesLeadTimeTime = None

            if not auto_random_generate:
                range_length = end_range_lead_time - start_range_lead_time + 1
                for x in range(len(RandValuesLeadTimeTime)):
                    for i in range(len(RandValuesLeadTimeTime)):
                        idx = i % range_length  
                        if (ProbArryLeadTimeTime[idx, 4] >= RandValuesLeadTimeTime[x]) and (ProbArryLeadTimeTime[idx, 3] <= RandValuesLeadTimeTime[x]):
                            Pickup_lead_time.append(ProbArryLeadTimeTime[idx, 0]) 
                            break
            else:
                for x in range(days):
                    for i in range(days):
                        idx = i % len(ProbArryLeadTimeTime) 
                        xl = RandomNum(10)
                        if (ProbArryLeadTimeTime[idx, 4] >= xl) and (ProbArryLeadTimeTime[idx, 3] <= xl):
                            Pickup_lead_time.append(ProbArryLeadTimeTime[idx, 0]) 
                            break

                
                    

               


            for i in range(days):

                TableArry[i,0] = i + 1 # Day

                if TableArry[i,0] == 1:
                    TableArry[i,1] = initial_inventory
                else:

                    if not shortage_case:                                                                  #
                        if TableArry[i,0] == TableArry[i-1,4] and TableArry[i,0] == TableArry[i-1,6]  :
                            TableArry[i,1] = reorder_point_1_recharge + reorder_point_2_recharge + backup   
                        elif TableArry[i,0] == TableArry[i-1,4]  :
                            TableArry[i,1] =  reorder_point_1_recharge  + backup 
                        elif TableArry[i,0] == TableArry[i-1,6]  :
                            TableArry[i,1] =  reorder_point_2_recharge + backup
                        else :
                            if TableArry[i-1,1] >= TableArry[i-1,8] :
                                TableArry[i,1] = TableArry[i-1,1] - TableArry[i-1,8] 
                            else :
                                TableArry[i,1] = 0

                    else:
                        if TableArry[i,0] == TableArry[i-1,4] and TableArry[i,0] == TableArry[i-1,6] :
                            TableArry[i,1] = reorder_point_1_recharge + reorder_point_2_recharge  + TableArry[i-1,1]-  TableArry[i-1,8] if TableArry[i-1,10] == 0 else reorder_point_2_recharge + reorder_point_1_recharge
                        elif TableArry[i,0] == TableArry[i-1,4]  :
                            TableArry[i,1] = reorder_point_1_recharge + TableArry[i-1,1] -  TableArry[i-1,8]  if TableArry[i-1,10] == 0 else reorder_point_1_recharge
                        elif TableArry[i,0] == TableArry[i-1,6]  :
                            TableArry[i,1] = reorder_point_2_recharge + TableArry[i-1,1] -  TableArry[i-1,8] if TableArry[i-1,10] == 0 else reorder_point_2_recharge
                        else :
                            TableArry[i,1] = TableArry[i-1,1] - TableArry[i-1,8] if TableArry[i-1,1] >= TableArry[i-1,8] else 0




                Cumulative_stock += TableArry[i,1] 
                TableArry[i,2] = Cumulative_stock # Cumulative stock

                if auto_random_generate:
                    TableArry[i,7] = RandomNum(99)
                    TableArry[i,8] = CalRandomTime(TableArry[i,7],start_range_demand,end_range_demand,eqaul_probabilities,ProbValuesDemandTime)
                else:
                    TableArry[i,7] = RandValuesDemandTime[i] if i < len(RandValuesDemandTime) else RandValuesDemandTime[i % len(RandValuesDemandTime)]
                    TableArry[i,8] = CalRandomTime(TableArry[i,7],start_range_demand,end_range_demand,eqaul_probabilities,ProbValuesDemandTime)

                Cumulative_demand += TableArry[i,8] 
                TableArry[i,9] = Cumulative_demand # Cumulative demand  

                if TableArry[i,1] <= reorder_point_1_limit:
                    TableArry[i,3] = reorder_point_1_recharge 
                else:
                    TableArry[i,3]=0
                if  TableArry[i-1,4] > TableArry[i,0] :
                    TableArry[i,3] = reorder_point_1_recharge

                if TableArry[i,3] != 0:

                    if TableArry[i,0] != 1 and TableArry[i-1,4] != 0 and TableArry[i-1,4] > TableArry[i,0] :
                        TableArry[i,4] = TableArry[i-1,4] 
                        TableArry[i,12] = TableArry[i-1,12]
                    else:
                        if temp < len(Pickup_lead_time):
                            TableArry[i,4] = TableArry[i,0] + Pickup_lead_time[temp]   
                            TableArry[i,12] = Pickup_lead_time[temp]     
                            temp += 1  
                        else:
                            temp = temp % len(Pickup_lead_time)
                            TableArry[i,4] = TableArry[i,0] + Pickup_lead_time[temp]
                            TableArry[i,12] = Pickup_lead_time[temp]
                            temp += 1
                else:
                    TableArry[i,4] = 0


                if TableArry[i,1] <= reorder_point_2_limit :
                    TableArry[i,5] = reorder_point_2_recharge
                else:
                    TableArry[i,5] = 0   
                if  TableArry[i-1,6] > TableArry[i,0] :
                    TableArry[i,5] = reorder_point_2_recharge
 
                if TableArry[i,5] != 0:

                    if TableArry[i,0] != 1 and TableArry[i-1,6] != 0 and TableArry[i-1,6] > TableArry[i,0] :
                        TableArry[i,6] = TableArry[i-1,6] 
                        TableArry[i,13] = TableArry[i-1,13]
                    else:
                        if temp < len(Pickup_lead_time):
                            TableArry[i,6] = TableArry[i,0] + Pickup_lead_time[temp]
                            TableArry[i,13] = Pickup_lead_time[temp]                            
                            temp += 1  
                        else:
                            temp = temp % len(Pickup_lead_time)
                            TableArry[i,6] = TableArry[i,0] + Pickup_lead_time[temp]
                            TableArry[i,13] = Pickup_lead_time[temp]
                            temp += 1
                else:
                    TableArry[i,6] = 0  

                if TableArry[i,1] < TableArry[i,8]:
                    backup += (TableArry[i,1] - TableArry[i,8])
                else:
                    backup = 0
                TableArry[i,10] = backup # Shortage 


                if TableArry[i,1] < TableArry[i,8]:
                    TableArry[i,10] =abs(TableArry[i,1] - TableArry[i,8])
                cumulative_shortage += TableArry[i,10]
                TableArry[i,11] = cumulative_shortage # Cumulative shortage




            TotalWhosWaitInQueue = 0#np.count_nonzero(TableArry[:days, 7])
            st.session_state.output_data_Table = TableArry
            st.session_state.TotalWhosWaitInQueue = TotalWhosWaitInQueue
            st.session_state.program_type = "Inventory_Daily_Management"
            return TableArry, TotalWhosWaitInQueue,"Inventory_Daily_Management"
        elif program == "Inventory_Cycle_Management":

            cycle_simulation = st.session_state.input_data_array[0]
            start_range_demand = st.session_state.input_data_array[1]
            end_range_demand = st.session_state.input_data_array[2]
            start_range_lead_time = st.session_state.input_data_array[3]
            end_range_lead_time = st.session_state.input_data_array[4]
            demand_random_numbers = st.session_state.input_data_array[5]
            lead_time_random_numbers = st.session_state.input_data_array[6]
            demand_probabilities = st.session_state.input_data_array[8]
            lead_time_probabilities = st.session_state.input_data_array[9]
            eqaul_probabilities = st.session_state.input_data_array[10]
            auto_random_generate = st.session_state.input_data_array[7]
            standard_inventory_level_m = st.session_state.input_data_array[11]
            periodic_length_n = st.session_state.input_data_array[12]
            previous_reordering = st.session_state.input_data_array[13]
            after_days = st.session_state.input_data_array[14]
            starting_quantity = st.session_state.input_data_array[15]
            shortage_case = st.session_state.input_data_array[16]

            table_length = cycle_simulation * periodic_length_n + 1       

            TableArry = np.zeros((table_length, 11), dtype=int)
            day_counter = 0
            Cumulative_demand = 0 
            Cumulative_stock = 0
            cumulative_shortage = 0
            backup = 0 
            temp = 0             
            Pickup_lead_time = []
            Pickup_lead_time_rand = []
            cumulative_cycle = 1

            if not eqaul_probabilities:
                ProbValuesDemandTime = GetProbabilities(demand_probabilities)
                ProbValuesLeadTimeTime = GetProbabilities(lead_time_probabilities)
            else: 
                ProbValuesDemandTime = ProbValuesLeadTimeTime = None

            
            ProbArryLeadTimeTime = CalculateProbability(start_range_lead_time, end_range_lead_time, eqaul_probabilities, ProbValuesLeadTimeTime)
            for i in range( end_range_lead_time - start_range_lead_time  + 1):
                ProbArryLeadTimeTime[i, 3] = ProbArryLeadTimeTime[i, 3]/ 10
                ProbArryLeadTimeTime[i, 4] = ProbArryLeadTimeTime[i, 4]/ 10
            
            if not auto_random_generate:
                RandValuesDemandTime = GetRandomNumbers(demand_random_numbers)
                RandValuesLeadTimeTime = GetRandomNumbers(lead_time_random_numbers)
            else:
                RandValuesDemandTime = None
                RandValuesLeadTimeTime = Pickup_lead_time_rand

            if not auto_random_generate:
                range_length = end_range_lead_time - start_range_lead_time + 1
                for x in range(len(RandValuesLeadTimeTime)):
                    for i in range(len(RandValuesLeadTimeTime)):
                        idx = i % range_length  
                        if (ProbArryLeadTimeTime[idx, 4] >= RandValuesLeadTimeTime[x]) and (ProbArryLeadTimeTime[idx, 3] <= RandValuesLeadTimeTime[x]):
                            Pickup_lead_time.append(ProbArryLeadTimeTime[idx, 0]) 
                            break
            else:
                for x in range(table_length):
                    for i in range(table_length):
                        idx = i % len(ProbArryLeadTimeTime) 
                        xl = RandomNum(10)
                        if (ProbArryLeadTimeTime[idx, 4] >= xl) and (ProbArryLeadTimeTime[idx, 3] <= xl):
                            Pickup_lead_time_rand.append(xl) 
                            Pickup_lead_time.append(ProbArryLeadTimeTime[idx, 0]) 
                            break

            for i in range(table_length):
                #days 1-5
                TableArry[i,1] = i % periodic_length_n + 1 
                #cycle 1-5
                TableArry[i,0] = cumulative_cycle
                if TableArry[i,1] == periodic_length_n:
                    cumulative_cycle += 1
                #random number for demand
                if auto_random_generate:
                    TableArry[i,2] = RandomNum(99)
                    TableArry[i,4] = CalRandomTime(TableArry[i,2],start_range_demand,end_range_demand,eqaul_probabilities,ProbValuesDemandTime)
                else:
                    TableArry[i,2] = RandValuesDemandTime[i] if i < len(RandValuesDemandTime) else RandValuesDemandTime[i % len(RandValuesDemandTime)]
                    TableArry[i,4] = CalRandomTime(TableArry[i,2],start_range_demand,end_range_demand,eqaul_probabilities,ProbValuesDemandTime)

                if i == 0:
                    TableArry[i,3] = starting_quantity
                else:
                    if TableArry[i,1] == (after_days + 1) % periodic_length_n :
                        if shortage_case:
                            TableArry[i,3] = TableArry[i-1,5] + previous_reordering - backup if backup <= TableArry[i-1,5] + previous_reordering else 0
                            backup = 0
                        else:
                            TableArry[i,3] = TableArry[i-1,5] + previous_reordering 
                            backup = 0
                    else:
                       TableArry[i,3] = TableArry[i-1,5] 

                if TableArry[i,3] <= TableArry[i,4] :
                    TableArry[i,5] =0 
                    TableArry[i,6] = abs(TableArry[i,3] - TableArry[i,4]) # Shortage
                    backup += TableArry[i,6]
                else:
                    TableArry[i,5] = TableArry[i,3] - TableArry[i,4] # Ending Inventory

                cumulative_shortage += TableArry[i,6]
                TableArry[i,7] = cumulative_shortage # Cumulative shortage
                if TableArry[i,1] == periodic_length_n:
                    TableArry[i,8] = standard_inventory_level_m - TableArry[i,5] - backup  # Order Quantity
                    previous_reordering = TableArry[i,8]
                    
                    valid_temp = temp % len(RandValuesLeadTimeTime) if len(RandValuesLeadTimeTime) > 0 else 0
                    TableArry[i,9] = RandValuesLeadTimeTime[valid_temp]
                    
                    valid_temp_pickup = temp % len(Pickup_lead_time) if len(Pickup_lead_time) > 0 else 0
                    TableArry[i,10] = Pickup_lead_time[valid_temp_pickup]
                    
                    after_days = Pickup_lead_time[valid_temp_pickup] + periodic_length_n
                    temp += 1
                    

            TableArry[table_length-1] = np.sum(TableArry[:table_length-1], axis=0)
            TotalWhosWaitInQueue = 0
            st.session_state.output_data_Table = TableArry
            st.session_state.TotalWhosWaitInQueue = TotalWhosWaitInQueue
            st.session_state.program_type = "Inventory_Cycle_Management"
            return TableArry, TotalWhosWaitInQueue,"Inventory_Cycle_Management"              
        elif program == "Gambing_Game":
            Game_cycle = st.session_state.input_data_array[0]
            Flip_Cost = st.session_state.input_data_array[1]
            Win_Cost = st.session_state.input_data_array[2]
            Game_Condition = st.session_state.input_data_array[3]
            Values = st.session_state.input_data_array[4]
            Auto_rand = st.session_state.input_data_array[5]
            if not Auto_rand:
                Rand_Values = list(map(int,Values.split()))
            Upper_Pound = st.session_state.input_data_array[6] 
            Max_trails = st.session_state.input_data_array[7]
            st.title("🎰 Gambling Game Simulation")
            all_game_dataframes = []
            Initial_cost = st.session_state.input_data_array[8]
            initial_case = st.session_state.input_data_array[9]

            if not initial_case :
                initial_cost = int(Initial_cost)
                    
                for i in range(Game_cycle):
                    results = []
                    heads = 0
                    tails = 0
                    trial = 0

                    while abs(heads - tails) < Game_Condition and trial < Max_trails and initial_cost > 0 :
                        trial += 1
                        if Auto_rand:
                            rand = RandomNum(10)
                        else:
                            rand = Rand_Values[trial - 1] if trial - 1 < len(Rand_Values) else Rand_Values[(trial - 1) % len(Rand_Values)]
                        if rand < 5:
                            result = "Tail" if Upper_Pound == "Head" else "Head"  # عكس القيمة
                        else:
                            result = Upper_Pound  

                        if result == "Head":
                            heads += 1
                        else:
                            tails += 1
                        if abs(heads - tails) < Game_Condition and trial < Max_trails:
                            Payment = 0
                            Win =0
                        else:

                            if trial >= Max_trails:
                                Payment = Max_trails * Flip_Cost
                                Win = 0
                            else:
                                Payment = trial * Flip_Cost
                                Win = Win_Cost

                        row = [trial ,rand, result, heads, tails ,Payment,Win]
                        results.append(row)

                    balance = Win - Payment

                    initial_cost += balance

                    if initial_cost < 0:
                        st.error(f"💔 You lost! all money $")
                        if trial == 1:
                            row = [0 ,0, 0, 0, 0 ,0,0]
                            results.append(row)
                        break    
                    columns = ["Trial","Random", "Result", "Heads", "Tails", "Payment", "Win"]
                    df = pd.DataFrame(results, columns=columns)
                    all_game_dataframes.append(df)
                    st.subheader(f"🕹️ Game {i+1} Results:")    
                    with st.expander(f"📊 Game {i+1} Summary (Finished in {trial} trials with {balance} $) "):
                        st.dataframe(df)
                        if balance > 0:
                            st.success(f"🏆 You won! Final Balance: {balance}$")
                        else:   
                            st.error(f"💔 You lost! Final Balance: {balance}$")
            else:
                    
                for i in range(Game_cycle):
                    results = []
                    heads = 0
                    tails = 0
                    trial = 0

                    while abs(heads - tails) < Game_Condition and trial < Max_trails :
                        trial += 1
                        if Auto_rand:
                            rand = RandomNum(10)
                        else:
                            rand = Rand_Values[trial - 1] if trial - 1 < len(Rand_Values) else Rand_Values[(trial - 1) % len(Rand_Values)]
                        if rand < 5:
                            result = "Tail" if Upper_Pound == "Head" else "Head"  # عكس القيمة
                        else:
                            result = Upper_Pound  

                        if result == "Head":
                            heads += 1
                        else:
                            tails += 1
                        if abs(heads - tails) < Game_Condition and trial < Max_trails:
                            Payment = 0
                            Win =0
                        else:

                            if trial >= Max_trails:
                                Payment = Max_trails * Flip_Cost
                                Win = 0
                            else:
                                Payment = trial * Flip_Cost
                                Win = Win_Cost
                        row = [trial ,rand, result, heads, tails ,Payment,Win]
                        results.append(row)
                    balance = Win - Payment
                    columns = ["Trial","Random", "Result", "Heads", "Tails", "Payment", "Win"]
                    df = pd.DataFrame(results, columns=columns)
                    all_game_dataframes.append(df)
                    st.subheader(f"🕹️ Game {i+1} Results:")    
                    with st.expander(f"📊 Game {i+1} Summary (Finished in {trial} trials with {balance} $) "):
                        st.dataframe(df)
                        if balance > 0:
                            st.success(f"🏆 You won! Final Balance: {balance}$")
                        else:   
                            st.error(f"💔 You lost! Final Balance: {balance}$")



            TableArry_list = [df.to_numpy() for df in all_game_dataframes]
            TableArry = pd.concat(all_game_dataframes, keys=[f"Game {i+1}" for i in range(Game_cycle)])
            TableArry = TableArry.reset_index(level=0).rename(columns={"level_0": "Game"})
            TotalWhosWaitInQueue = 0
            st.session_state.output_data_Table = TableArry
            st.session_state.TotalWhosWaitInQueue = TotalWhosWaitInQueue
            st.session_state.program_type = "Gambing_Game"
            return TableArry, TotalWhosWaitInQueue,"Gambing_Game"     
        elif program == "Hinge_Assembly":

            assembly = st.session_state.input_data_array[0]
            A_size = st.session_state.input_data_array[1]
            A_ratio = st.session_state.input_data_array[2]
            B_size = st.session_state.input_data_array[3]
            B_ratio = st.session_state.input_data_array[4]
            C_size = st.session_state.input_data_array[5]
            C_ratio = st.session_state.input_data_array[6]
            D_size = st.session_state.input_data_array[7]
            D_ratio = st.session_state.input_data_array[8]
            Auto_rand = st.session_state.input_data_array[10]
            randd = st.session_state.input_data_array[9]
            if not Auto_rand :
                rand_values = list(map(int,randd.split())) 

            TableArry = np.zeros((assembly, 11), dtype=object)
            def calculation(type,rand):
                if type == "A":
                    if A_size > 0 and A_size <= 9:
                        size = 0.1
                        return (A_size - A_ratio) + size * rand
                    elif A_size > 9 and A_size <= 99:
                        size = 1
                        return (A_size - A_ratio) + size * rand
                elif type == "B":
                    if B_size > 0 and B_size <= 9:
                        size = 0.1
                        return (B_size - B_ratio) + size * rand
                    elif B_size > 9 and B_size <= 99:
                        size = 1
                        return (B_size - B_ratio) + size * rand
                elif type == "C":
                    if C_size > 0 and C_size <= 9:
                        size = 0.1
                        return (C_size - C_ratio) + size * rand
                    elif C_size > 9 and C_size <= 99:
                        size = 1
                        return (C_size - C_ratio) + size * rand
                elif type == "D":
                    if D_size > 0 and D_size <= 9:
                        size = 0.1
                        return (D_size - D_ratio) + size * rand
                    elif D_size > 9 and D_size <= 99:
                        size = 1
                        return (D_size - D_ratio) + size * rand
                else:
                    st.error("Invalid type.")



            for i in range(assembly):
                TableArry[i,0] = i + 1
                if Auto_rand:
                    TableArry[i,1] = "{:.2f}".format(RandomNum(99) / 100)
                    TableArry[i,3] = "{:.2f}".format(RandomNum(99) / 100)
                    TableArry[i,5] = "{:.2f}".format(RandomNum(99) / 100)
                    TableArry[i,8] = "{:.2f}".format(RandomNum(99) / 100)  
                else:
                    rand_len = len(rand_values)
                    TableArry[i,1] = "{:.2f}".format(rand_values[(4 * i) % rand_len] / 100)
                    TableArry[i,3] = "{:.2f}".format(rand_values[(4 * i + 1) % rand_len] / 100)
                    TableArry[i,5] = "{:.2f}".format(rand_values[(4 * i + 2) % rand_len] / 100)
                    TableArry[i,8] = "{:.2f}".format(rand_values[(4 * i + 3) % rand_len] / 100)
                TableArry[i,2] = "{:.2f}".format(calculation("A",float(TableArry[i,1])))
                TableArry[i,4] = "{:.2f}".format(calculation("B",float(TableArry[i,3])))
                TableArry[i,6] = "{:.2f}".format(calculation("C",float(TableArry[i,5])))
                TableArry[i,7] = "{:.2f}".format(float(TableArry[i,2]) +float( TableArry[i,4] )+float( TableArry[i,6]))
                TableArry[i,9] = "{:.2f}".format(calculation("D",float(TableArry[i,8])))
                if float(TableArry[i,7]) > float(TableArry[i,9]):
                    TableArry[i,10] = "-"
                else:
                    TableArry[i,10] = "+"
            
            TotalWhosWaitInQueue = 0
            st.session_state.output_data_Table = TableArry
            st.session_state.TotalWhosWaitInQueue = TotalWhosWaitInQueue
            st.session_state.program_type = "Hinge_Assembly"
            return TableArry, TotalWhosWaitInQueue,"Hinge_Assembly"                    
        else:
            st.error("Invalid program selected.")
    except Exception as e:
        st.error(f"An error occurred while generating table data: {e}")


def TablePrinter():
    if "output_data_Table" in st.session_state:
        try:
            if st.session_state.program_type == "single_server":    
                TableArry = st.session_state.output_data_Table
                SimulateNumber = st.session_state.input_data_array[0]


                df_table = pd.DataFrame(TableArry[:-1], columns=["NO", "RAT", "IAT", "AT", "RST", "ST", "STB", "QU", "STE", "TS", "IDLE"])
                total_row = {
                    "NO": SimulateNumber,
                    "RAT": "",  # Leave blank
                    "IAT": "",
                    "AT": TableArry[SimulateNumber, 3],
                    "RST": "",
                    "ST": TableArry[SimulateNumber, 5],
                    "STB": "",
                    "QU": TableArry[SimulateNumber, 7],
                    "STE": "",
                    "TS": TableArry[SimulateNumber, 9],
                    "IDLE": TableArry[SimulateNumber, 10]
                }

                df_total = pd.DataFrame([total_row])
                st.markdown("### 🗃️ TABLE DATA:")
                st.dataframe(df_table, use_container_width=True)

                st.markdown("### 📑TOTAL DATA:")
                st.dataframe(df_total, use_container_width=True)
            elif st.session_state.program_type == "Double_server":

                TableArry = st.session_state.output_data_Table
                SimulateNumber = st.session_state.input_data_array[0]


                df_table = pd.DataFrame(TableArry[1:-1], columns= ["NO", "RAT", "IAT", "AT", "RST", "STx", "STy", "STXB", "STX", "STXE", "STYB", "STY", "STYE", "QU", "TS", "IDLEX", "IDLEY"])
                total_row = {
                    "NO": SimulateNumber,
                    "RAT": "",  # Leave blank
                    "IAT": "",
                    "AT": TableArry[SimulateNumber+1, 3],
                    "RST": "",
                    "STx": TableArry[SimulateNumber+1, 5],
                    "STy": TableArry[SimulateNumber+1, 6],
                    "STXB": "",
                    "STX": TableArry[SimulateNumber+1, 8],
                    "STXE": "",
                    "STYB": "",
                    "STY": TableArry[SimulateNumber+1, 11],
                    "STYE": "",
                    "QU": TableArry[SimulateNumber+1, 13],
                    "TS": TableArry[SimulateNumber+1, 14],
                    "IDLEX": TableArry[SimulateNumber+1, 15],
                    "IDLEY": TableArry[SimulateNumber+1, 16]
                }


                df_total = pd.DataFrame([total_row])
                st.markdown("### 🗃️ TABLE DATA:")
                st.dataframe(df_table, use_container_width=True)

                st.markdown("### 📑TOTAL DATA:")
                st.dataframe(df_total, use_container_width=True)                
            elif st.session_state.program_type == "Inventory_Daily_Management":
                table_data = st.session_state.output_data_Table
                days = st.session_state.input_data_array[0]
                
                df_table = pd.DataFrame(table_data, columns=["Day", "Stk", "CStk", "Ord1", "Due1", "Ord2", "Due2","R-dmd", "Dmd", "C-dmd", "Short", "CShort","LT 1","LT 2"])
                                                      #columns=[" 0 ", " 1 ", " 2  ",  " 3 ", "  4 ", " 5  ", "  6 ","  7  ", " 8 ", "  9  ", " 1 0 ", "  11 "," 12 "," 13 "])
                total_row = {
                    "Day": days,
                    "Stk": "",
                    "CStk": table_data[days-1, 2],
                    "Ord1": "",
                    "Due1": "",
                    "Ord2": "",
                    "Due2": "",
                    "R-dmd":"",
                    "Dmd": "",
                    "C-dmd": table_data[days-1, 9],
                    "Short": "",
                    "CShort": table_data[days-1, 11],
                    "LT 1": "",
                    "LT 2": ""
                }
                df_total = pd.DataFrame([total_row])
                st.markdown("### 🗃️ TABLE DATA:")
                st.dataframe(df_table, use_container_width=True)
                st.markdown("-----")
                st.markdown("### 📑TOTAL DATA:")
                st.dataframe(df_total, use_container_width=True)
            elif st.session_state.program_type == "Inventory_Cycle_Management":
                table_data = st.session_state.output_data_Table
                cycle_simulation = st.session_state.input_data_array[0]
                periodic_length_n = st.session_state.input_data_array[12]
                table_length = cycle_simulation * periodic_length_n + 1
                
                df_table = pd.DataFrame(table_data[:-1], columns=["Cyl","Day", "R-dmd", "B-Inv", "Dmd", "E-Inv", "Short", "C-sh","Ord-Q", "R-LT", "LOD-T"])
                                                    #columns=[" 0 ", " 1 ", " 2  ",  " 3 ", "  4 ", " 5  ", "  6 ","   7  ", " 8 ", "  9  ", " 1 0 ",
                total_row = {
                    "Cyl": cycle_simulation,
                    "Day": table_length-1,
                    "R-dmd": "",
                    "B-Inv":"",
                    "Dmd": table_data[ table_length-1,4],
                    "E-Inv":table_data[ table_length-1,5],
                    "Short": "",
                    "C-sh":"",
                    "Ord-Q":table_data[ table_length-1,8],
                    "R-LT":"",
                    "LOD-T": ""
                }
                df_total = pd.DataFrame([total_row])
                st.markdown("### 🗃️ TABLE DATA:")
                st.dataframe(df_table, use_container_width=True)
                st.markdown("-----")
                st.markdown("### 📑TOTAL DATA:")
                st.dataframe(df_total, use_container_width=True)
            elif st.session_state.program_type == "Gambing_Game":
                df_table = st.session_state.output_data_Table 
                table_data = st.session_state.output_data_Table
                Game_cycle = st.session_state.input_data_array[0]
                Flip_Cost = st.session_state.input_data_array[1]
                total_win = table_data["Win"].sum()
                total_payment = table_data["Payment"].sum()
                intial_cost =int( st.session_state.input_data_array[8])
                heads = 0
                tails = 0
                Trail = total_payment/Flip_Cost
                itrator = round(Trail)
                for i in range(itrator):
                    if df_table.iloc[i]["Result"] == "Head":
                        heads += 1
                    else:
                        tails += 1
                
                df_table = pd.DataFrame(table_data, columns=["Game","Trial", "Random", "Result", "Heads", "Tails", "Payment", "Win"])

                total_row = {
                    "Game":df_table["Game"].iloc[itrator-1][5] ,
                    "Trial": Trail,
                    "Heads": heads,
                    "Tails": tails,
                    "Payment": total_payment,
                    "Win": total_win,
                    "Balance": intial_cost+ total_win - total_payment,
                }
                df_total = pd.DataFrame([total_row])
                st.subheader("🎰 Tablel Simulation")
                st.dataframe(df_table, use_container_width=True)
                st.markdown("-----")
                st.subheader("📑Total Simulation")
                st.dataframe(df_total, use_container_width=True)
            elif st.session_state.program_type == "Hinge_Assembly":
                table_data = st.session_state.output_data_Table
                assembly = st.session_state.input_data_array[0]

                multi_index = pd.MultiIndex.from_tuples([
                    ("Index", "i"),
                    ("A Part Size", "Rand-A"),
                    ("A Part Size", "A"),
                    ("B Part Size", "Rand-B"),
                    ("B Part Size", "B"),
                    ("C Part Size", "Rand-C"),
                    ("C Part Size", "C"),
                    ( "Total","A+B+C"),
                    ("D Part Size", "Rand-D"),
                    ("D Part Size", "D"),
                    ("Results", "Sine"),
                ])


                df_table = pd.DataFrame(table_data, columns=multi_index)
                
                def highlight_sine_column(row):
                    color = ''
                    if row[("Results", "Sine")] == "-":
                        color = 'background-color:#a20909'
                    elif row[("Results", "Sine")] == "+":
                        color = 'background-color: #0c901c'
                    else:
                        color = 'background-color: #08154d'

                    return [color if col == ("Results", "Sine") else '' for col in row.index]

                styled_table = df_table.style.apply(highlight_sine_column, axis=1)

                st.markdown("### 🗃️ TABLE DATA:")
                #st.dataframe(df_table, use_container_width=True)
                st.dataframe(styled_table, use_container_width=True)
            else:
                st.error("Invalid program selected.")
        except Exception as e:
            st.error(f"An error occurred while printing the table: {e}")

def Statistics(program):
    try:
        st.subheader("📄 Data Report")
        if program_type == "single_server":
            SumSimulate = st.session_state.input_data_array[0]
            TableArry = st.session_state.output_data_Table
            SumArrivalTime = TableArry[SumSimulate, 3]
            SumQueueTime = TableArry[SumSimulate, 7]
            NumWhosWait = st.session_state.TotalWhosWaitInQueue
            SumServiceTime = TableArry[SumSimulate, 5] 
            SumIdleTime = TableArry[SumSimulate, 10]
            SumTimeInSystem = TableArry[SumSimulate, 9]
            data = {
                "Statistic": [
                    "Probability Idle Server",
                    "Average Service Time (Min)",
                    "Average Time Customer Spends In System (Min)",
                    "Average Waiting Time (Min)",
                    "Average Time Between Arrivals (Min)",
                    "Average Waiting Time Between Whos WAIT (Min)"
                ],
                "Value": [
                    SumIdleTime / SumArrivalTime if SumArrivalTime != 0 else 0.00,
                    SumServiceTime / SumSimulate if SumSimulate != 0 else 0.00,
                    SumTimeInSystem / SumSimulate if SumSimulate != 0 else 0.00,
                    SumQueueTime / SumSimulate if SumSimulate != 0 else 0.00,
                    SumArrivalTime / (SumSimulate - 1) if SumSimulate > 1 else 0.000,
                    SumQueueTime / NumWhosWait if NumWhosWait != 0 else 0.000
                ]
            }
            df = pd.DataFrame(data, columns=["Statistic", "Value"])
            st.dataframe(df)
        elif program_type == "Double_server":

            SumSimulate = st.session_state.input_data_array[0]
            TableArry = st.session_state.output_data_Table

            SumArrivalTime = TableArry[SumSimulate+1, 3]
            SumQueueTime = TableArry[SumSimulate+1, 13]
            NumWhosWait = st.session_state.TotalWhosWaitInQueue
            SumServiceTimex = TableArry[SumSimulate+1, 8]
            SumServiceTimey = TableArry[SumSimulate+1, 11]
            SumIdleTimex = TableArry[SumSimulate+1, 15]
            SumIdleTimey = TableArry[SumSimulate+1, 16]
            SumTimeInSystem = TableArry[SumSimulate+1, 14]

            data = {
                "Statistic": [
                    "Probability Idle Server Master",
                    "Probability Idle Server Slave",
                    "Average Service Time Master (Min)",
                    "Average Service Time Slave (Min)",
                    "Average Time Customer Spends In System (Min)",
                    "Average Waiting Time (Min)",
                    "Average Time Between Arrivals (Min)",
                    "Average Waiting Time Between Whos WAIT (Min)"
                ],
                "Value": [
                    SumIdleTimex / SumArrivalTime if SumArrivalTime != 0 else 0.00,
                    SumIdleTimey / SumArrivalTime if SumArrivalTime != 0 else 0.00,
                    SumServiceTimex / SumSimulate if SumSimulate != 0 else 0.00,
                    SumServiceTimey / SumSimulate if SumSimulate != 0 else 0.00,
                    SumTimeInSystem / SumSimulate if SumSimulate != 0 else 0.00,
                    SumQueueTime / SumSimulate if SumSimulate != 0 else 0.00,
                    SumArrivalTime / (SumSimulate - 1) if SumSimulate > 1 else 0.000,
                    SumQueueTime / NumWhosWait if NumWhosWait != 0 else 0.000
                ]
            }
            df = pd.DataFrame(data, columns=["Statistic", "Value"])
            st.dataframe(df)
        elif program_type == "Inventory_Daily_Management":
            days = st.session_state.input_data_array[0]
            TableArry = st.session_state.output_data_Table
            SumStock = TableArry[days-1, 2]
            SumDemand = TableArry[days-1, 9]
            SumShortage = TableArry[days-1, 11]
            data = {
                "Statistic": [
                    "Average Stock (Units)",
                    "Average Demand (Units)",
                    "Average Shortage (Units)",
                    "Service Level (%)"
                ],
                "Value": [
                    round( SumStock / days,2) if days != 0 else 0.00,
                    round( SumDemand / days,2) if days != 0 else 0.00,
                    round( SumShortage / days,2) if days != 0 else 0.00,
                    round( (SumDemand - SumShortage) / SumDemand * 100 ,2)if SumDemand != 0 else 0.00
                ]
            }
            df = pd.DataFrame(data, columns=["Statistic", "Value"])
            st.dataframe(df)
        elif program_type == "Inventory_Cycle_Management":

            TableArry = st.session_state.output_data_Table
            cycle_simulation = st.session_state.input_data_array[0]
            periodic_length_n = st.session_state.input_data_array[12]
            table_length = cycle_simulation * periodic_length_n + 1
            data = {
                "Statistic": [
                    "Average Ending Inventory (Units)",
                    "Total Demand (Units)",
                    "Order Quantity (Units)"
                ],
                "Value": [
                    round(  TableArry[ table_length-1,5] /(table_length-1) ,2) if table_length != 0 else 0.00,
                    round( TableArry[ table_length-1,4],2) if table_length != 0 else 0.00,
                    round(  TableArry[ table_length-1,8],2) if table_length != 0 else 0.00,

                ]
            }
            df = pd.DataFrame(data, columns=["Statistic", "Value"])
            st.dataframe(df)


    except Exception as e:
        st.error(f"An error occurred while calculating statistics: {e}")

def Graphics(program_type):
    if program_type == "single_server":
        try:
            st.subheader("📊 Customer Time Analysis")
            if "output_data_Table" in st.session_state and "TotalWhosWaitInQueue" in st.session_state:
                SimulateNumber = st.session_state.input_data_array[0]
                TotalWhosWaitInQueue = st.session_state.TotalWhosWaitInQueue
                TableArry = st.session_state.output_data_Table
                customer_ids = TableArry[:-1, 0] 
                waiting_times = TableArry[:-1, 7].astype(float)
                arrival_times = TableArry[:-1, 3].astype(float)
                service_start = TableArry[:-1, 6].astype(float)
                service_times = TableArry[:-1, 8].astype(float)
                time_system = TableArry[:-1, 9].astype(float)
                idle_times = TableArry[:-1, 10].astype(float)
                total_service_time = service_times.sum()
                total_idle_times = idle_times.sum()
                total_time_in_system = time_system.sum()

                ### Chart 1: Bar Chart – Waiting Time Per Customer
                fig1, ax1 = plt.subplots()
                ax1.bar(time_system, waiting_times, color='red')
                ax1.set_title("Waiting Time for Each Customer")
                ax1.set_xlabel("Time in System")
                ax1.set_ylabel("Waiting Time")
                ax1.grid(True, linestyle="--", alpha=0.9)
                ax1.set_ylim(0, len(waiting_times))  # Set y-axis limit from 0 to max waiting time + 5
                ax1.set_xlim(0, len(time_system))  # Set x-axis limit based on number of customers
                st.pyplot(fig1)

                ### Chart 2: Line Chart – Arrival vs. Service Start
                fig2, ax2 = plt.subplots()
                ax2.plot(customer_ids, arrival_times, label="Arrival Time", marker='o', color='blue')
                ax2.plot(customer_ids, service_start, label="Service Start Time", marker='x', color='orange')
                ax2.set_title("Arrival vs. Service Start Time")
                ax2.set_xlabel("Customer ID")
                ax2.set_ylabel("Time")
                ax2.legend()
                ax2.grid(True, linestyle="-", alpha=0.9)
                st.pyplot(fig2)

                ### Chart 3: Pie Chart – Server Utilization
                fig3, ax3 = plt.subplots()
                ax3.pie(
                    [(len(customer_ids) - 1), (len(customer_ids)) - TotalWhosWaitInQueue],
                    labels=["Customer waits", "Customer not waits"],
                    autopct='%1.1f%%',
                    colors=['green', 'gray'],
                    startangle=60
                )
                ax3.set_title("Server Utilization")
                st.pyplot(fig3)

                ### Chart 4: Summary Numbers
                st.markdown("### 🔍 Simulation Summary")
                col1, col2 = st.columns(2)
                col1.metric("Total Customers", len(customer_ids))
                col2.metric("Total Who Waited", TotalWhosWaitInQueue)
                col3, col4 = st.columns(2)
                col3.metric("Total Service Time", f"{total_service_time:.1f}")
                col4.metric("Idle Time", f"{total_idle_times:.1f}")
                col5, col6 = st.columns(2)
                col5.metric("Total Time in System", f"{total_time_in_system:.2f}")
                col6.metric("Average Waiting Time", f"{waiting_times.mean():.2f}")
                col7, col8 = st.columns(2)
                col7.metric("Average Service Time", f"{service_times.mean():.2f}")
                col8.metric("Average Time Between Arrivals", f"{arrival_times.mean():.2f}")
        except Exception as e:
            st.error(f"An error occurred while generating graphics: {e}")
    elif program_type == "Double_server":
        try:

            SimulateNumber = st.session_state.input_data_array[0]
            TotalWhosWaitInQueue = st.session_state.TotalWhosWaitInQueue
            TableArry = st.session_state.output_data_Table
            customer_ids = TableArry[1:-1, 0] 
            waiting_times = TableArry[1:-1, 13].astype(float)
            arrival_times = TableArry[1:-1, 3].astype(float)
            service_times_slave = TableArry[1:-1, 11].astype(float)
            times_master = TableArry[1:-1, 5]
            times_slave = TableArry[1:-1, 6]
            service_times_master = TableArry[1:-1, 8].astype(float)
            service_start_master = TableArry[1:-1, 7].astype(float)
            service_start_slave = TableArry[1:-1, 10].astype(float)
            time_system = TableArry[1:-1, 14].astype(float)
            idle_times_master = TableArry[1:-1, 15].astype(float)
            idle_times_slave = TableArry[1:-1, 16].astype(float)
            total_service_time_master = service_times_master.sum()
            total_service_time_slave = service_times_slave.sum()
            total_idle_times_master = idle_times_master.sum()
            total_idle_times_slave = idle_times_slave.sum()
            total_time_in_system = time_system.sum()
            master_job= np.count_nonzero(TableArry[:SimulateNumber+1, 8])
            slave_job= np.count_nonzero(TableArry[:SimulateNumber+1, 11])
            total_master= times_master.sum()
            total_slave= times_slave.sum()
            st.markdown("### 🔍 Simulation Summary")
            col1, col2 = st.columns(2)
            col1.metric("Total Customers", len(customer_ids))
            col2.metric("Total Who Waited", TotalWhosWaitInQueue)
            col3, col4 = st.columns(2)
            col3.metric("Total Service Time master", f"{total_service_time_master:.1f}")
            col4.metric("Idle Time master", f"{total_idle_times_master:.1f}")
            col3, col4 = st.columns(2)
            col3.metric("Total Service Time slave", f"{total_service_time_slave:.1f}")
            col4.metric("Idle Time slave", f"{total_idle_times_slave:.1f}")
            col5, col6 = st.columns(2)
            col5.metric("Total Time in System", f"{total_time_in_system:.2f}")
            col6.metric("Average Waiting Time", f"{waiting_times.mean():.2f}")
            col7, col8 = st.columns(2)
            col7.metric("Average Service Time master", f"{service_times_master.mean():.2f}")
            col8.metric("Average Service Time slave", f"{service_times_slave.mean():.2f}")
            col7, col8 = st.columns(2)
            col7.metric("Average Service Time", f"{total_service_time_master - total_service_time_slave :.2f}")
            col8.metric("Average Time Between Arrivals", f"{arrival_times.mean():.2f}")
            col7, col8 = st.columns(2)
            col7.metric("Master Service Time", total_master)
            col8.metric("Slave Service Time", total_slave)
            col7, col8 = st.columns(2)
            col7.metric("Master jobs", master_job )
            col8.metric("Slave jobs ", slave_job )
            ### Chart 1: Bar Chart – Waiting Time Per Customer
            st.subheader("📊 Customer Time Analysis")
            fig1, ax1 = plt.subplots()
            ax1.bar(time_system, waiting_times, color='red')
            ax1.set_title("Waiting Time for Each Customer")
            ax1.set_xlabel("Time in System")
            ax1.set_ylabel("Waiting Time")
            ax1.grid(True, linestyle="--", alpha=0.9)
            ax1.set_ylim(0, len(waiting_times))  # Set y-axis limit from 0 to max waiting time + 5
            ax1.set_xlim(0, len(time_system))  # Set x-axis limit based on number of customers
            st.pyplot(fig1)

            fig9, ax1 = plt.subplots()
            ax1.bar(times_master, customer_ids, color='red')
            ax1.bar(times_slave, customer_ids, color='blue')
            ax1.set_title("servers compared to each other")
            ax1.set_xlabel("Time")
            ax1.set_ylabel("customer ID")
            ax1.legend(["Master", "Slave"])
            ax1.grid(True, linestyle="--", alpha=0.9)
            st.pyplot(fig9)

            ### Chart 2: Line Chart – Arrival vs. Service Start
            fig2, ax2 = plt.subplots()
            ax2.plot(customer_ids, arrival_times, label="Arrival Time", marker='o', color='blue')
            ax2.plot(customer_ids, service_start_master, label="Service Start Time", marker='x', color='orange')
            ax2.set_title("Arrival Time vs. Service Start Master Time")
            ax2.set_xlabel("Customer ID")
            ax2.set_ylabel("Time")
            ax2.legend()
            ax2.grid(True, linestyle="-", alpha=0.9)
            st.pyplot(fig2)

            fig3, ax2 = plt.subplots()
            ax2.plot(customer_ids, arrival_times, label="Arrival Time", marker='o', color='blue')
            ax2.plot(customer_ids, service_start_slave, label="Service Start Time", marker='x', color='orange')
            ax2.set_title("Arrival Time vs. Service Start Master Time")
            ax2.set_xlabel("Customer ID")
            ax2.set_ylabel("Time")
            ax2.legend()
            ax2.grid(True, linestyle="-", alpha=0.9)
            st.pyplot(fig3)

            fig4, ax2 = plt.subplots()
            ax2.plot(customer_ids, arrival_times, label="Arrival Time", marker='o', color='blue')
            ax2.plot(customer_ids, service_times_master, label="Service Time", marker='x', color='orange')
            ax2.set_title("Arrival Time vs. Service Master Time")
            ax2.set_xlabel("Customer ID")
            ax2.set_ylabel("Time")
            ax2.legend()
            ax2.grid(True, linestyle="-", alpha=0.9)
            st.pyplot(fig4)

            fig5, ax2 = plt.subplots()
            ax2.plot(customer_ids, arrival_times, label="Arrival Time", marker='o', color='blue')
            ax2.plot(customer_ids, service_times_slave, label="ServiceTime", marker='x', color='orange')
            ax2.set_title("Arrival Time vs. Service Slave Time")
            ax2.set_xlabel("Customer ID")
            ax2.set_ylabel("Time")
            ax2.legend()
            ax2.grid(True, linestyle="-", alpha=0.9)
            st.pyplot(fig5)

            fig6, ax2 = plt.subplots()
            ax2.plot(customer_ids, service_times_master, label="ServiceTime master", marker='o', color='blue')
            ax2.plot(customer_ids, service_times_slave, label="ServiceTime slave", marker='x', color='orange')
            ax2.set_title("Service master Time vs. Service Slave Time")
            ax2.set_xlabel("Customer ID")
            ax2.set_ylabel("Time")
            ax2.legend()
            ax2.grid(True, linestyle="-", alpha=0.9)
            st.pyplot(fig6)

            ### Chart 3: Pie Chart – Server Utilization
            fig7, ax3 = plt.subplots()
            ax3.pie(
                [TotalWhosWaitInQueue, (len(customer_ids)) - TotalWhosWaitInQueue],
                labels=["Customer waits", "Customer not waits"],
                autopct='%1.1f%%',
                colors=[ 'red','green'],
                startangle=60
            )
            ax3.set_title("Server Utilization")
            st.pyplot(fig7)

        except Exception as e:
            st.error(f"An error occurred while generating graphics: {e}")
    elif program_type == "Inventory_Daily_Management":
        try:
            st.subheader("📊 Inventory Daily Management Analysis")
            TableArry = st.session_state.output_data_Table
            days = st.session_state.input_data_array[0]
            cumulative_stock = TableArry[:days, 2]
            cumulative_demand = TableArry[:days, 9]
            cumulative_shortage = TableArry[:days, 11]
            col1 , col2 = st.columns(2)
            col1.metric("Total Stock", cumulative_stock[-1])
            col2.metric("Total Demand", cumulative_demand[-1])
            col3 , col4 = st.columns(2)
            col3.metric("Total Shortage", cumulative_shortage[-1])
            col4.metric("Total Days", days)
            col5 , col6 = st.columns(2)
            col5.metric("Average Stock", cumulative_stock.mean())
            col6.metric("Average Demand", cumulative_demand.mean())
            col7 , col8 = st.columns(2)
            col7.metric("Average Shortage", cumulative_shortage.mean())
            col8.metric("Real payment",  cumulative_demand[-1] - cumulative_shortage[-1])

            fig8, ax8 = plt.subplots()
            ax8.plot(cumulative_stock, label="Stock", marker='o', color='blue')
            ax8.plot(cumulative_demand, label="Demand", marker='x', color='orange')
            ax8.plot(cumulative_shortage, label="Shortage", marker='x', color='red')
            ax8.set_title("Stock vs. Demand vs. Shortage")
            ax8.set_xlabel("Days")
            ax8.set_ylabel("Units")
            ax8.legend()
            ax8.grid(True, linestyle="-", alpha=0.9)
            st.pyplot(fig8)
        except Exception as e:
            st.error(f"An error occurred while generating graphics: {e}")
    elif program_type == "Inventory_Cycle_Management":
        try:
            st.subheader("📊 Inventory Daily Management Analysis")
            TableArry = st.session_state.output_data_Table
            cycle_simulation = st.session_state.input_data_array[0]
            periodic_length_n = st.session_state.input_data_array[12]
            table_length = cycle_simulation * periodic_length_n + 1
            cm_b =TableArry[:table_length, 3]
            cm_e =TableArry[:table_length, 5]
            cm_d =TableArry[:table_length, 4]
            col1 , col2 = st.columns(2)
            col1.metric("Total Days", table_length -1)
            col2.metric("Total cycles", cycle_simulation)
            col3 , col4 = st.columns(2)
            col3.metric("Total orders", TableArry[ table_length-1,8])
            col4.metric("Total demand",TableArry[ table_length-1,4])

            fig8, ax8 = plt.subplots()
            ax8.plot(cm_b, label="Stock", marker='o', color='blue')
            ax8.plot(cm_e, label="Demand", marker='x', color='orange')
            ax8.plot(cm_d, label="Shortage", marker='x', color='red')
            ax8.set_title("begin vs. end vs. demand")
            ax8.set_xlabel("Days")
            ax8.set_ylabel("Units")
            ax8.legend()
            ax8.grid(True, linestyle="-", alpha=0.9)
            st.pyplot(fig8)
        except Exception as e:
            st.error(f"An error occurred while generating graphics: {e}")
    elif program_type == "Hinge_Assembly":
        try:
            st.subheader("📊 Hinge Assembly Analysis")
            TableArry = st.session_state.output_data_Table
            assembly = st.session_state.input_data_array[0]
            cm_a =TableArry[:assembly, 2]
            cm_b =TableArry[:assembly, 4]
            cm_c =TableArry[:assembly, 6]
            cm_d =TableArry[:assembly, 9]
            total=TableArry[:assembly, 7]
            
            plus=0
            for i in range(assembly):
                if TableArry[i, 10] == "-": plus+=1
       
            col1  = st.columns(1)[0]
            col1.metric("Total Probability not assembled (%)", plus/assembly*100)
            col3 , col4 = st.columns(2)
            col3.metric("Total Assembled", assembly - plus)
            col4.metric("Total Not Assembled", plus)

            fig8, ax8 = plt.subplots()
            ax8.plot(cm_a, label="A Part Size", marker='o', color='blue')
            ax8.plot(cm_b, label="B Part Size", marker='x', color='orange')
            ax8.plot(cm_c, label="C Part Size", marker='o', color='red')
            ax8.set_title("A vs. B vs. C Part Size")
            ax8.set_xlabel("Assembly")
            ax8.set_ylabel("Units")
            ax8.legend()
            ax8.grid(True, linestyle="-", alpha=0.9)
            st.pyplot(fig8)
            fig9, ax9 = plt.subplots()
            ax9.plot(total, label="D Part Size", marker='o', color='blue')
            ax9.plot(cm_d, label="D Part Size", marker='x', color='orange')
            ax9.set_title("D Part Size")
            ax9.set_xlabel("Assembly")
            ax9.set_ylabel("Units")
            ax9.legend()
            ax9.grid(True, linestyle="-", alpha=0.9)
            st.pyplot(fig9)
        except Exception as e:
            st.error(f"An error occurred while generating graphics: {e}")

    elif program_type == "Gambing_Game_statistics": 
        try:    
            st.subheader("🧰 Data Entered ")
            Game_cycle = st.session_state.input_data_array[0]
            Flip_Cost = st.session_state.input_data_array[1]
            Win_Cost = st.session_state.input_data_array[2]
            Game_Condition = st.session_state.input_data_array[3]
            Rand_Values = st.session_state.input_data_array[4]
            Auto_rand = st.session_state.input_data_array[5]
            Upper_Pound = st.session_state.input_data_array[6] 
            Max_trails = st.session_state.input_data_array[7] 
            initial_cost = st.session_state.input_data_array[8]

            col1 , col2 = st.columns(2)
            col1.metric("Game Played", Game_cycle)
            col2.metric("Max trials/game", Max_trails)
            col3 , col4 = st.columns(2)
            col3.metric("Cost of Win", Win_Cost)
            col4.metric("Cost of Flip", Flip_Cost)
            col6 ,col7  = st.columns(2)
            col7.metric("Game Condition", Game_Condition)
            col6.metric("| Tail - Head | = ", Game_Condition)
            col8 ,col9 = st.columns(2)
            col8.metric("Upper Pound", Upper_Pound) 
            col9.metric("Initial Cost", initial_cost) 
        except Exception as e:
            st.error(f"An error occurred while generating graphics: {e}")
    elif program_type == "Gambing_Game_statistics_output": 
        try:    

            df_table = st.session_state.output_data_Table 
            table_data = st.session_state.output_data_Table
            Game_cycle = st.session_state.input_data_array[0]
            Flip_Cost = st.session_state.input_data_array[1]
            total_win = table_data["Win"].sum()
            total_payment = table_data["Payment"].sum()
            intial_cost =int( st.session_state.input_data_array[8])
            heads = 0
            tails = 0

            hamada = ""
            Trail = total_payment/Flip_Cost
            itrator = round(Trail)
            for i in range(itrator):
                if df_table.iloc[i]["Result"] == "Head":
                    heads += 1
                else:
                    tails += 1
            hamada2=int(df_table["Game"].iloc[itrator-1][5])
            if total_win - total_payment > 0 and Game_cycle == hamada2:
                hamada = "winner 🎉"
            elif total_win - total_payment < 0 or Game_cycle > hamada2 :
                hamada = "loser 💔"
            else:
                hamada = "draw 🙄"
            st.subheader("📑TOTAL Result")
            st.markdown("-----")
            st.title("You Are : "+ hamada)
            st.markdown("-----")
            col1 , col2 = st.columns(2)
            col1.metric("Game Played", hamada2)
            col2.metric("Total Trials", Trail)
            col3 , col4 = st.columns(2)
            col3.metric("Total Win", total_win)
            col4.metric("Total Payment", total_payment)
            col6 ,col7  = st.columns(2)
            col7.metric("Total Balance", intial_cost + total_win - total_payment)
            col6.metric("Total return cost", total_win - total_payment )
            col8 ,col9 = st.columns(2)
            col8.metric("Tail", tails) 
            col9.metric("Head", heads) 
            col10 ,col11 = st.columns(2)
            col10.metric("Avarage requirement flips played (flips)", Trail/hamada2)
            col11.metric("Avarage requirement flips Must played (flips)", Trail/Game_cycle)
        except Exception as e:
            st.error(f"An error occurred while generating graphics: {e}")
    elif program_type == "Gambing_Game_results":
        try:    
            df_table = st.session_state.output_data_Table 
            table_data = st.session_state.output_data_Table
            Game_cycle = st.session_state.input_data_array[0]
            Flip_Cost = st.session_state.input_data_array[1]
            total_win = table_data["Win"].sum()
            total_payment = table_data["Payment"].sum()
            intial_cost =int( st.session_state.input_data_array[8])
            heads = 0
            tails = 0
            hamada = ""
            Trail = total_payment/Flip_Cost
            itrator = round(Trail)
            for i in range(itrator):
                if df_table.iloc[i]["Result"] == "Head":
                    heads += 1
                else:
                    tails += 1
            hamada2=int(df_table["Game"].iloc[itrator-1][5])

            fig8, ax8 = plt.subplots()           
            ax8.plot(df_table["Game"], df_table["Payment"], label="Payment", marker='o', color='blue')
            ax8.plot(df_table["Game"], df_table["Win"], label="Win", marker='x', color='orange')
            ax8.set_title("Payment vs. Win")
            ax8.set_xlabel("Game")
            ax8.set_ylabel("Units")
            ax8.legend()
            ax8.grid(True, linestyle="-", alpha=0.9)
            st.pyplot(fig8)

            fig9, ax1 = plt.subplots()
            ax1.bar(df_table["Game"], df_table["Heads"], color='red')
            ax1.bar(df_table["Game"], df_table["Tails"], color='blue')
            ax1.set_title("Heads vs. Tails")
            ax1.set_xlabel("Game")
            ax1.set_ylabel("Units")
            ax1.legend(["Heads", "Tails"])
            ax1.grid(True, linestyle="--", alpha=0.9)
            st.pyplot(fig9)

            for i in range(hamada2):
                game_name = f"Game {i+1}"
                game_data = df_table[df_table["Game"] == game_name]

                if not game_data.empty:
                    fig, ax = plt.subplots()
                    ax.plot(game_data["Trial"], game_data["Heads"], label="Heads", marker='o', color='blue')
                    ax.plot(game_data["Trial"], game_data["Tails"], label="Tails", marker='x', color='orange')
                    ax.set_title(f"Heads vs. Tails - {game_name}")
                    ax.set_xlabel("Trial")
                    ax.set_ylabel("Count")
                    ax.legend()
                    ax.grid(True, linestyle="--", alpha=0.7)
                    st.pyplot(fig)
                else:
                    st.warning(f"No data found for {game_name}")


        except Exception as e:
            st.error(f"An error occurred while generating graphics: {e}")

    else:
        st.error("Invalid program type for graphics generation. Please check the program type.")

def DownloadData(program):
    try:
        if program == "single_server":
            st.subheader("⬇️ Download All Simulation Data")           
            TableArry = st.session_state.output_data_Table
            df_simulation = pd.DataFrame(TableArry, columns=["NO", "RAT", "IAT", "AT", "RST", "ST", "STB", "QU", "STE", "TS", "IDLE"])

            # Calculate additional statistics if needed
            TotalWhosWaitInQueue = np.count_nonzero(TableArry[:-1, 7])
            SumArrivalTime = TableArry[:-1, 3].sum()
            SumServiceTime = TableArry[:-1, 5].sum()
            SumIdleTime = TableArry[:-1, 10].sum()
            SumQueueTime = TableArry[:-1, 7].sum()
            SumTimeInSystem = TableArry[:-1, 9].sum()
            
            # Prepare the summary statistics DataFrame
            df_statistics = pd.DataFrame({
                "Statistic": [
                    "Total Customers",
                    "Total Customers Who Waited",
                    "Total Arrival Time",
                    "Total Service Time",
                    "Total Idle Time",
                    "Total Time in System",
                    "Average Waiting Time",
                    "Average Service Time",
                    "Average Time Between Arrivals"
                ],
                "Value": [
                    len(TableArry) - 1,  # Assuming NO includes a header
                    TotalWhosWaitInQueue,
                    SumArrivalTime,
                    SumServiceTime,
                    SumIdleTime,
                    SumTimeInSystem,
                    TableArry[:-1, 7].mean(),
                    TableArry[:-1, 5].mean(),
                    TableArry[:-1, 3].mean()  # Assuming this is the interarrival time
                ]
            })
            
            # Combine both DataFrames for downloading
            df_combined = pd.concat([df_simulation, df_statistics], ignore_index=True)
            
            # Convert to CSV format
            csv = df_combined.to_csv(index=False).encode('utf-8')
            # Create a download button
            st.download_button(
                label="Download Data as CSV",
                data=csv,
                file_name="simulation_data.csv",
                mime="text/csv"
            )
        elif program == "Double_server":
            st.subheader("⬇️ Download All Simulation Data")
            TableArry = st.session_state.output_data_Table
            df_simulation = pd.DataFrame(TableArry[1:], columns=["NO", "RAT", "IAT", "AT", "RST", "STx", "STy", "STXB", "STX", "STXE", "STYB", "STY", "STYE", "QU", "TS", "IDLEX", "IDLEY"])
            
            TotalWhosWaitInQueue = np.count_nonzero(TableArry[1:-1, 13])
            SumArrivalTime = TableArry[1:-1, 3].sum()
            SumServiceTimeMaster = TableArry[1:-1, 8].sum() 
            SumServiceTimeSlave= TableArry[1:-1, 11].sum()
            SumIdleTimem = TableArry[1:-1, 15].sum() 
            SumIdleTimes = TableArry[1:-1, 16].sum()
            SumQueueTime = TableArry[1:-1, 13].sum()
            SumTimeInSystem = TableArry[1:-1, 14].sum()

            df_statistics = pd.DataFrame({
                "Statistic": [
                    "Total Customers",
                    "Total Customers Who Waited",
                    "Total Arrival Time",
                    "Total Service Time master",
                    "Total Service Time slave",
                    "Total Idle Time master",
                    "Total Idle Time slave",
                    "Total Time in System",
                    "Average Waiting Time",
                    "Average Service master Time",
                    "Average Service slave Time",
                    "Average Time Between Arrivals"
                ],
                "Value": [
                    len(TableArry) - 2,  # Assuming NO includes a header
                    TotalWhosWaitInQueue,
                    SumArrivalTime,
                    SumServiceTimeMaster,
                    SumServiceTimeSlave,
                    SumIdleTimem,
                    SumIdleTimes,
                    SumTimeInSystem,
                    TableArry[1:-1, 13].mean(),
                    TableArry[1:-1, 8].mean(),
                    TableArry[1:-1, 11].mean(),
                    TableArry[1:-1, 3].mean()  # Assuming this is the interarrival time
                ]
            })
            # Combine both DataFrames for downloading
            df_combined = pd.concat([df_simulation, df_statistics], ignore_index=True)
            
            # Convert to CSV format
            csv = df_combined.to_csv(index=False).encode('utf-8')
            # Create a download button
            st.download_button(
                label="Download Data as CSV",
                data=csv,
                file_name="simulation_data.csv",
                mime="text/csv"
            )
        elif program == "Inventory_Cycle_Management":
            st.subheader("⬇️ Download All Simulation Data")
            TableArry = st.session_state.output_data_Table
            df_simulation = pd.DataFrame(TableArry[:-1], columns=["Cyl","Day", "R-dmd", "B-Inv", "Dmd", "E-Inv", "Short", "C-sh","Ord-Q", "R-LT", "LOD-T"])
            
            # Calculate additional statistics if needed
            cycle_simulation = st.session_state.input_data_array[0]
            periodic_length_n = st.session_state.input_data_array[12]
            table_length = cycle_simulation * periodic_length_n + 1
            cm_b =TableArry[table_length-1, 3]
            cm_e =TableArry[table_length-1, 5]
            cm_d =TableArry[table_length-1, 4]

            df_statistics = pd.DataFrame({
                "Statistic": [
                    "Total Days",
                    "Total cycle",
                    "Total Demand",
                    "Total Shortage"
                ],
                "Value": [
                    table_length -1,
                    cycle_simulation,
                    cm_d,
                    TableArry[table_length-1, 6]
                ]
            })
            
            # Combine both DataFrames for downloading
            df_combined = pd.concat([df_simulation, df_statistics], ignore_index=True)
            
            # Convert to CSV format
            csv = df_combined.to_csv(index=False).encode('utf-8')
            # Create a download button
            st.download_button(
                label="Download Data as CSV",
                data=csv,
                file_name="simulation_data.csv",
                mime="text/csv"
            )
        elif program == "Inventory_Daily_Management":
            st.subheader("⬇️ Download All Simulation Data")
            TableArry = st.session_state.output_data_Table
            df_simulation = pd.DataFrame(TableArry, columns=["Day", "Stk", "CStk", "Ord1", "Due1", "Ord2", "Due2","R-dmd", "Dmd", "C-dmd", "Short", "CShort","LT 1","LT 2"])
            
            # Calculate additional statistics if needed
            days = st.session_state.input_data_array[0]
            SumStock = TableArry[days-1, 2]
            SumDemand = TableArry[days-1, 9]
            SumShortage = TableArry[days-1, 11]

            df_statistics = pd.DataFrame({
                "Statistic": [
                    "Total Days",
                    "Total Stock",
                    "Total Demand",
                    "Total Shortage",
                    "Average Stock",
                    "Average Demand",
                    "Average Shortage",
                    "Service Level (%)"
                ],
                "Value": [
                    days,
                    SumStock,
                    SumDemand,
                    SumShortage,
                    SumStock / days if days != 0 else 0.00,
                    SumDemand / days if days != 0 else 0.00,
                    SumShortage / days if days != 0 else 0.00,
                    (SumDemand - SumShortage) / SumDemand * 100 if SumDemand != 0 else 0.00
                ]
            })
            
            # Combine both DataFrames for downloading
            df_combined = pd.concat([df_simulation, df_statistics], ignore_index=True)
            
            # Convert to CSV format
            csv = df_combined.to_csv(index=False).encode('utf-8')
            # Create a download button
            st.download_button(
                label="Download Data as CSV",
                data=csv,
                file_name="simulation_data.csv",
                mime="text/csv"
            )
        elif program == "Gambing_Game":
            st.subheader("⬇️ Download All Simulation Data")
            TableArry = st.session_state.output_data_Table
            
            multi_index = pd.MultiIndex.from_tuples([
                ("Index", "i"),
                ("A Part Size", "Rand-A"),
                ("A Part Size", "A"),
                ("B Part Size", "Rand-B"),
                ("B Part Size", "B"),
                ("C Part Size", "Rand-C"),
                ("C Part Size", "C"),
                ( "Total","A+B+C"),
                ("D Part Size", "Rand-D"),
                ("D Part Size", "D"),
                ("Results", "Sine"),
            ])


            df_simulation = pd.DataFrame(TableArry, columns=multi_index)            

            csv = df_simulation.to_csv(index=False).encode('utf-8')

            st.download_button(
                label="Download Data as CSV",
                data=csv,
                file_name="simulation_data.csv",
                mime="text/csv"
            )
        elif program == "Hinge_Assembly":
            st.subheader("⬇️ Download All Simulation Data")
            TableArry = st.session_state.output_data_Table
            df_simulation = pd.DataFrame(TableArry, columns=["Assembly", "A Part Size", "B Part Size", "C Part Size", "D Part Size"])
            
            # Convert to CSV format
            csv = df_simulation.to_csv(index=False).encode('utf-8')
            # Create a download button
            st.download_button(
                label="Download Data as CSV",
                data=csv,
                file_name="simulation_data.csv",
                mime="text/csv"
            )
        else:
            st.error("Invalid program type for download data generation. Please check the program type.")
    except Exception as e:
        st.error(f"An error occurred while generating download data: {e}")


if "page" not in st.session_state:
    st.session_state.page = "main"

def go_to(page_name):
    st.session_state.page = page_name

if st.session_state.page == "main":
    st.title("🎯 Simulation Web App")
    st.markdown("### Welcome!")
    st.markdown(
        "This platform allows you to simulate a variety of operational models. "
        "Choose a module below to begin exploring system behaviors through simulation."
    )

    st.markdown("#### 🦸‍♂️ Available Simulation Modules:")
    st.markdown("---")
    st.markdown("#### 📡 Server Modules:")  
    col1, col2=st.columns(2)
    with col1:
        st.button("📦 Single Server Simulation", on_click=lambda: go_to("Single_Server"))
    with col2:
        st.button("🖥️ Double Server Simulation", on_click=lambda: go_to("Double_Server"))
    st.markdown("---")
    st.markdown("#### 🏬 Inventory Modules:")    
    col1, col2 = st.columns(2)
    with col1:
        st.button("📊 Inventory Daily Management", on_click=lambda: go_to("Inventory_Daily_Management"))
    with col2:
        st.button("📈 Inventory Cycle Management", on_click=lambda: go_to("Inventory_Cycle_Management"))
    st.markdown("---")
    st.markdown("#### 🏓 Game Modules:")    
    col1, col2 = st.columns(2)
    with col1:
        st.button("💰 Gambing Game", on_click=lambda: go_to("Gambing_Game"))
    with col2:
        st.button("🧩 A Hinge Assembly", on_click=lambda: go_to("Hinge_Assembly"))  
    st.markdown("---")    
    st.markdown("#### 🗞️ Dealer Modules:")    
    col1, col2 = st.columns(2)
    with col1:
        st.button("📰 News Dealer's", on_click=lambda: go_to(""),disabled=True)      
    st.markdown("---")
    with st.expander("ℹ️ About the App", expanded=False):
        st.markdown(
            "This web application is designed by Eng. Osama khaled to simulate various operational models, "
            "providing insights into system performance and behavior. "
            "Explore the modules to understand how different parameters affect the system."
        )
    phone_number = "201201360725" 
    message = "مرحبًا، أحتاج إلى مساعدة بخصوص مشروعك 🙏" 

    encoded_message = urllib.parse.quote(message)
    whatsapp_url = f"https://wa.me/{phone_number}?text={encoded_message}"

    st.markdown(
            f"""
            <a href="{whatsapp_url}" target="_blank">
                <button style="
                    background-color: #167514;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 8px;
                    font-size: 16px;
                    cursor: pointer;
                ">
                    💬 Connect What's app
                </button>
            </a>
            """,
            unsafe_allow_html=True
        )


elif st.session_state.page == "Single_Server":
    visibility = True
    st.title("📦 Single Server Simulation")
    st.markdown("*A single server queue simulation models the process of customers arriving at a service point, where they wait in line to be served by a single server, allowing analysis of performance metrics such as waiting times, service times, and system utilization.*")
    st.sidebar.title("Settings")
    data_array, has_error = inputs("Single_Server")
    st.session_state.input_data_array = data_array
    simulate_btn = st.sidebar.button("Run Simulation 📊", on_click=lambda:(simulate_btn==True), disabled=has_error)
    st.sidebar.button("🔙 Back" ,on_click=lambda:go_to("main"))
        
    if simulate_btn:
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["💡 Probabilities", "📈 Analysis", "📄 Data Report", "📊 Graphics", "⬇️ Download"])
        with tab1:
            ProbabilityTable("Single_Server")
        with tab2:
            table_data,TotalWhosWaitInQueue,program_type = TableData("Single_Server")
            TablePrinter()
        with tab3:
            Statistics("single_server")
        with tab4:
            Graphics("single_server")      
        with tab5:
            DownloadData("single_server")


elif st.session_state.page == "Double_Server":
    visibility = True
    st.title("💻🌐 Double Server Simulation")
    st.markdown("*A Double server queue simulation models the process of customers arriving at a service point, where they wait in line to be served by a Double server, allowing analysis of performance metrics such as waiting times, service times, and system utilization.*")
    st.sidebar.title("Settings")
    data_array, has_error = inputs("Double_Server")
    st.session_state.input_data_array = data_array
    simulate_btn = st.sidebar.button("Run Simulation 📊", on_click=lambda:(simulate_btn==True), disabled=has_error)
    st.sidebar.button("🔙 Back" ,on_click=lambda:go_to("main"))
    if simulate_btn:
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["💡 Probabilities", "📈 Analysis", "📄 Data Report", "📊 Graphics", "⬇️ Download"])
        with tab1:
            ProbabilityTable("Double_Server")   
        with tab2:
            table_data, TotalWhosWaitInQueue ,program_type  = TableData("Double_Server")
            TablePrinter()
        with tab3:
            Statistics("Double_server")
        with tab4:
            Graphics("Double_server")
        with tab5:
            DownloadData("Double_server")


elif st.session_state.page == "Inventory_Daily_Management":
    visibility = True
    st.title("📤 Inventory Daily Management")
    st.markdown(
        """
        **Manage and simulate inventory flow on a daily basis to monitor stock levels, optimize reordering,
        and evaluate overall system efficiency.**

        This module helps in modeling daily inventory scenarios using simulation, helping you make data-driven decisions 
        for supply chain and stock management.
        """ )    
    st.sidebar.title("Settings")
    data_array, has_error = inputs("Inventory_Daily_Management")
    st.session_state.input_data_array = data_array
    simulate_btn = st.sidebar.button("Run Simulation 📊", on_click=lambda:(simulate_btn==True), disabled=has_error)
    st.sidebar.button("🔙 Back" ,on_click=lambda:go_to("main"))
    if simulate_btn:
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["💡 Probabilities", "📈 Analysis", "📄 Data Report", "📊 Graphics", "⬇️ Download"])
        with tab1:
            ProbabilityTable("Inventory_Daily_Management")   
        with tab2:
            table_data, TotalWhosWaitInQueue ,program_type  = TableData("Inventory_Daily_Management")
            TablePrinter()
        with tab3:
            Statistics("Inventory_Daily_Management")
        with tab4:
            Graphics("Inventory_Daily_Management")
        with tab5:
            DownloadData("Inventory_Daily_Management")

elif st.session_state.page == "Inventory_Cycle_Management":
    visibility = True
    st.title("📦 Inventory Cycle Management")
    st.markdown(
        """
        **Manage and simulate inventory flow on a cycle basis to monitor stock levels, optimize reordering,
        and evaluate overall system efficiency.**

        This module helps in modeling cycle inventory scenarios using simulation, helping you make data-driven decisions 
        for supply chain and stock management.
        """ )    
    st.sidebar.title("Settings")
    data_array, has_error = inputs("Inventory_Cycle_Management")
    st.session_state.input_data_array = data_array
    simulate_btn = st.sidebar.button("Run Simulation 📊", on_click=lambda:(simulate_btn==True), disabled=has_error)
    st.sidebar.button("🔙 Back" ,on_click=lambda:go_to("main"))
    if simulate_btn:
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["💡 Probabilities", "📈 Analysis", "📄 Data Report", "📊 Graphics", "⬇️ Download"])
        with tab1:
            ProbabilityTable("Inventory_Cycle_Management")   
        with tab2:
            table_data, TotalWhosWaitInQueue ,program_type  = TableData("Inventory_Cycle_Management")
            TablePrinter()
        with tab3:
            Statistics("Inventory_Cycle_Management")
        with tab4:
            Graphics("Inventory_Cycle_Management")
        with tab5:
            DownloadData("Inventory_Cycle_Management")

elif st.session_state.page == "Gambing_Game":
    visibility = True
    st.title("💰 Gambing Game")
    st.markdown(
        """
        **Manage and simulate gambling scenarios to monitor stock levels, optimize reordering,
        and evaluate overall system efficiency.**

        This module helps in modeling gambling scenarios using simulation, helping you make data-driven decisions 
        for supply chain and stock management.
        """ )    
    st.sidebar.title(" 👨🏻‍🔧 Settings")
    data_array, has_error = inputs("Gambing_Game")
    st.session_state.input_data_array = data_array
    simulate_btn = st.sidebar.button("Run Simulation 📊", on_click=lambda:(simulate_btn==True), disabled=has_error)
    st.sidebar.button("🔙 Back" ,on_click=lambda:go_to("main"))
    if simulate_btn:
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["💡 Data Entered", "📈 Analysis", "📄 Statistics", "📊 Graphics", "⬇️ Download"])
        with tab1:
            Graphics("Gambing_Game_statistics")   
        with tab2:
            table_data, TotalWhosWaitInQueue ,program_type  = TableData("Gambing_Game")
            TablePrinter()
        with tab3:
            Graphics("Gambing_Game_statistics_output")
        with tab4:
            Graphics("Gambing_Game_results")
        with tab5:
            DownloadData("Gambing_Game")

elif st.session_state.page == "Hinge_Assembly":
    visibility = True
    st.title("🧩 A Hinge Assembly")
    st.markdown(
        """
        **Experience hinge assembly like never before simulate real-time scenarios to evaluate efficiency,
        track component usage, and achieve successful builds.**

        This simulation module is designed to reflect real-world assembly challenges, helping you make 
        smarter decisions in production, planning, and process optimization.
        """   )
    st.sidebar.title(" 👨🏻‍🔧 Settings")
    data_array, has_error = inputs("Hinge_Assembly")
    st.session_state.input_data_array = data_array
    simulate_btn = st.sidebar.button("Run Simulation 📊", on_click=lambda:(simulate_btn==True), disabled=has_error)
    st.sidebar.button("🔙 Back" ,on_click=lambda:go_to("main"))
    if simulate_btn:
        tab1, tab2, tab3, tab4 = st.tabs(["💡 Data Entered", "📈 Analysis", "📄 Statistics", "⬇️ Download"])
        with tab1:
            ProbabilityTable("Hinge_Assembly")  
        with tab2:
            table_data, TotalWhosWaitInQueue ,program_type  = TableData("Hinge_Assembly")
            TablePrinter()
        with tab3:
            Graphics("Hinge_Assembly")
        with tab4:
            DownloadData("Gambing_Game")
st.markdown(
    """
    <footer style='text-align: center; margin-top: 50px;'>
        <hr>
        <p style='font-size: 14px; color: gray;'>Powered by Osama Khaled Mohamed | osamakhaled117@gmail.com | 01201360725</p>
    </footer>
    """,
    unsafe_allow_html=True
)
