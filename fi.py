import numpy as np
import random
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
    else:
        st.error("Invalid program selected.")
        has_error = True
        data_array = None
    return data_array, has_error

def data_labeled():
    # Get the input data from session state 00000000000000000000000000000000000
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
    


def RandomNum(MaxNumRange):
   return int(random.uniform(1, MaxNumRange))
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
                    ProbArryLeadTime[i, 3] = ProbArryLeadTime[i, 3]/ 10
                    ProbArryLeadTime[i, 4] = ProbArryLeadTime[i, 4]/ 10

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
                        xl = RandomNum(9)
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

    except Exception as e:
        st.error(f"An error occurred while calculating statistics: {e}")

def Graphics(program):
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
        st.button("📈 Inventory Cycle Management", on_click=lambda: go_to(""),disabled=True)
    st.markdown("---")
    st.markdown("#### 🏓 Game Modules:")    
    col1, col2 = st.columns(2)
    with col1:
        st.button("💰 Gambing Game", on_click=lambda: go_to(""),disabled=True)
    with col2:
        st.button("🧩 A Hinge Assembly", on_click=lambda: go_to(""),disabled=True)  
    st.markdown("---")    
    st.markdown("#### 🗞️ Dealer Modules:")    
    col1, col2 = st.columns(2)
    with col1:
        st.button("📰 News Dealer's", on_click=lambda: go_to(""),disabled=True)      
    st.markdown("---")
    with st.expander("ℹ️ About the App", expanded=False):
        st.markdown(
            "This web application is designed to simulate various operational models, "
            "providing insights into system performance and behavior. "
            "Explore the modules to understand how different parameters affect the system."
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


st.markdown(
    """
    <footer style='text-align: center; margin-top: 50px;'>
        <hr>
        <p style='font-size: 14px; color: gray;'>Powered by Osama Khaled Mohamed | osamakhaled117@gmail.com | 01201360725</p>
    </footer>
    """,
    unsafe_allow_html=True
)
