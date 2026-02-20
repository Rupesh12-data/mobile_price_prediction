import streamlit as st
import numpy as np
import joblib

model = joblib.load("mobile_predict/mobile prerdict modelgbr.pkl")
st.title('Mobile Price Prediction ')

st.text('Select Your Requirement to Pridict Mobile Price ')

#'480p (640x480)' mapping imp natra string value janxa
resolution_map = {
    '': 0,
    '480p (640x480)': 480,
    '720p HD (1280x720)': 720,
    '1080p FHD (1920x1080)': 1080,
    '1440p QHD (2560x1440)': 1440,
    '2160p 4K UHD (3840x2160)': 2160,
    '4320p 8K (7680x4320)': 4320
}
re_display = list(resolution_map.keys())#display huni
re_selected = st.selectbox("Resolution", re_display)
re = resolution_map[re_selected]#model lai chayeko value

ppi_map = {
    '': 0,
    '150 PPI': 150,
    '200 PPI': 200,
    '250 PPI': 250,
    '300 PPI': 300,
    '350 PPI': 350,
    '400 PPI': 400,
    '450 PPI': 450,
    '500 PPI': 500,
    '550 PPI': 550,
    '600 PPI': 600
}
pp_display = list(ppi_map.keys())
pp_selected = st.selectbox("PPI (Pixel Density)", pp_display)
pp = ppi_map[pp_selected]

cpu_map = {
    '': 0,
    'Dual Core (2)': 2,
    'Quad Core (4)': 4,
    'Hexa Core (6)': 6,
    'Octa Core (8)': 8,
    'Deca Core (10)': 10
}
cp_display = list(cpu_map.keys())
cp_selected = st.selectbox("CPU Cores", cp_display)
cp = cpu_map[cp_selected]

internal_map = {
    '': 0,
    '8 GB': 8,
    '16 GB': 16,
    '32 GB': 32,
    '64 GB': 64,
    '128 GB': 128,
    '256 GB': 256,
    '512 GB': 512,
    '1 TB': 1024
}
In_display = list(internal_map.keys())
In_selected = st.selectbox("Internal Memory", In_display)
In = internal_map[In_selected]

# RAM - map to GB
ram_map = {
    '': 0,
    '1 GB': 1,
    '2 GB': 2,
    '3 GB': 3,
    '4 GB': 4,
    '6 GB': 6,
    '8 GB': 8,
    '12 GB': 12,
    '16 GB': 16,
    '18 GB': 18,
    '24 GB': 24
}
ra_display = list(ram_map.keys())
ra_selected = st.selectbox("RAM", ra_display)
ra = ram_map[ra_selected]

# Front Camera - map to MP
front_map = {
    '': 0,
    '0 MP (No Front Camera)': 0,
    '2 MP': 2,
    '5 MP': 5,
    '8 MP': 8,
    '13 MP': 13,
    '16 MP': 16,
    '20 MP': 20,
    '32 MP': 32,
    '40 MP': 40,
    '50 MP': 50
}
fr_display = list(front_map.keys())
fr_selected = st.selectbox("Front Camera", fr_display)
fr = front_map[fr_selected]

battery_map = {
    '': 0,
    '2000 mAh': 2000,
    '2500 mAh': 2500,
    '3000 mAh': 3000,
    '3500 mAh': 3500,
    '4000 mAh': 4000,
    '4500 mAh': 4500,
    '5000 mAh': 5000,
    '5500 mAh': 5500,
    '6000 mAh': 6000,
    '7000 mAh': 7000
}
ba_display = list(battery_map.keys())
ba_selected = st.selectbox("Battery Capacity", ba_display)
ba = battery_map[ba_selected]

thickness_map = {
    '': 0,
    '5.0 mm': 5.0,
    '5.5 mm': 5.5,
    '6.0 mm': 6.0,
    '6.5 mm': 6.5,
    '7.0 mm': 7.0,
    '7.5 mm': 7.5,
    '8.0 mm': 8.0,
    '8.5 mm': 8.5,
    '9.0 mm': 9.0,
    '10.0 mm': 10.0
}
th_display = list(thickness_map.keys())
th_selected = st.selectbox("Thickness", th_display)
th = thickness_map[th_selected]

rear_map = {
    '': 0,
    '2 MP': 2,
    '5 MP': 5,
    '8 MP': 8,
    '12 MP': 12,
    '13 MP': 13,
    '16 MP': 16,
    '20 MP': 20,
    '32 MP': 32,
    '48 MP': 48,
    '50 MP': 50,
    '64 MP': 64,
    '108 MP': 108,
    '200 MP': 200
}
rea_display = list(rear_map.keys())
rea_selected = st.selectbox("Rear Camera", rea_display)
rea = rear_map[rea_selected]

cpu_freq_map = {
    '': 0,
    '1.0 GHz': 1.0,
    '1.2 GHz': 1.2,
    '1.5 GHz': 1.5,
    '1.8 GHz': 1.8,
    '2.0 GHz': 2.0,
    '2.2 GHz': 2.2,
    '2.4 GHz': 2.4,
    '2.5 GHz': 2.5,
    '2.8 GHz': 2.8,
    '3.0 GHz': 3.0,
    '3.2 GHz': 3.2
}
cpf_display = list(cpu_freq_map.keys())
cpf_selected = st.selectbox("CPU Frequency", cpf_display)
cpf = cpu_freq_map[cpf_selected]

sa= st.number_input(
    "Sales (Number of Units Sold)",
    min_value=0,
    max_value=10000000,
    value=0,
    step=50
)

we = st.number_input(
    "Weight (grams)",
    min_value=0,
    max_value=500,
    value=0,
    step=5
)

if st.button("Predict Price"):
    if re == 0 or pp == 0 or cp == 0 or In == 0 or ra == 0 or fr == 0 or ba == 0 or th == 0 or rea == 0 or cpf == 0 or sa == 0 or we ==0:
        st.error("Please fill all the requirements !! ")
    else:
        st.success("All requirements submitted")
        
        input_data = np.array([[re, pp, cp, In, ra, fr, ba, th, rea, cpf,sa,we]])
        
        predict = model.predict(input_data)
        
        st.subheader("Predicted Mobile Price")
        st.write(f"Price: {predict[0]:.2f}")
        
        with st.expander("View Submitted Specifications"):
            st.write(f"**Resolution:** {re_selected}")
            st.write(f"**PPI:** {pp_selected}")
            st.write(f"**CPU Cores:** {cp_selected}")
            st.write(f"**Internal Memory:** {In_selected}")
            st.write(f"**RAM:** {ra_selected}")
            st.write(f"**Front Camera:** {fr_selected}")
            st.write(f"**Battery:** {ba_selected}")
            st.write(f"**Thickness:** {th_selected}")
            st.write(f"**Rear Camera:** {rea_selected}")
            st.write(f"**CPU Frequency:** {cpf_selected}")
            st.write(f"**Sales:** {sa}")
            st.write(f"**Weight:** {we}")
