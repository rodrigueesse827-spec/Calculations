import math
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Mechanical Engineering Calculator", page_icon="⚙️", layout="wide"
)

# Standard gravity
G = 9.81


def main():
  st.title("⚙️ Mechanical Engineering Calculator")
  st.markdown(
      "A comprehensive, modular web application for mechanical engineering"
      " calculations built with Streamlit."
  )

  # Sidebar Navigation
  st.sidebar.title("Navigation")
  module = st.sidebar.selectbox(
      "Select Engineering Module",
      [
          "1. Mechanics",
          "2. Strength of Materials",
          "3. Thermodynamics",
          "4. Fluid Mechanics",
          "5. Thermal Engineering",
          "6. Machine Design",
      ],
  )

  st.sidebar.markdown("---")
  st.sidebar.info(
      "Tip: Adjust the inputs in real-time to instantly recalculate results!"
  )

  # ============================================================
  # 1. MECHANICS
  # ============================================================
  if module == "1. Mechanics":
    st.header("1. Mechanics")
    calc_type = st.selectbox(
        "Choose Calculation", ["Force", "Work", "Power", "Kinetic Energy"]
    )

    if calc_type == "Force":
      st.subheader("Force (F = m * a)")
      col1, col2 = st.columns(2)
      with col1:
        m = st.number_input("Mass (kg)", min_value=0.001, value=10.0, step=0.1)
      with col2:
        a = st.number_input(
            "Acceleration (m/s^2)", value=9.81, step=0.1, format="%.4f"
        )

      if st.button("Calculate Force"):
        F = m * a
        st.success(f"**Force = {F:.4f} N**")

    elif calc_type == "Work":
      st.subheader("Work (W = F * d * cos(theta))")
      col1, col2, col3 = st.columns(3)
      with col1:
        F = st.number_input("Force (N)", min_value=0.0, value=50.0, step=1.0)
      with col2:
        d = st.number_input(
            "Distance travelled (m)", min_value=0.001, value=5.0, step=0.1
        )
      with col3:
        theta = st.number_input(
            "Angle (degrees)", value=0.0, step=1.0, format="%.2f"
        )

      if st.button("Calculate Work"):
        W = F * d * math.cos(math.radians(theta))
        st.success(f"**Work = {W:.4f} J**")

    elif calc_type == "Power":
      st.subheader("Power (P = W / t)")
      col1, col2 = st.columns(2)
      with col1:
        W_val = st.number_input(
            "Work done (J)", min_value=0.001, value=1000.0, step=10.0
        )
      with col2:
        t = st.number_input(
            "Time taken (s)", min_value=0.001, value=10.0, step=0.1
        )

      if st.button("Calculate Power"):
        P = W_val / t
        st.success(f"**Power = {P:.4f} W**")

    elif calc_type == "Kinetic Energy":
      st.subheader("Kinetic Energy (KE = 1/2 * m * v^2)")
      col1, col2 = st.columns(2)
      with col1:
        m = st.number_input("Mass (kg)", min_value=0.001, value=100.0, step=1.0)
      with col2:
        v = st.number_input("Velocity (m/s)", value=20.0, step=0.5)

      if st.button("Calculate Kinetic Energy"):
        KE = 0.5 * m * (v**2)
        st.success(f"**Kinetic Energy = {KE:.4f} J**")

  # ============================================================
  # 2. STRENGTH OF MATERIALS
  # ============================================================
  elif module == "2. Strength of Materials":
    st.header("2. Strength of Materials")
    calc_type = st.selectbox(
        "Choose Calculation", ["Stress", "Strain", "Young's Modulus"]
    )

    if calc_type == "Stress":
      st.subheader("Stress (sigma = F / A)")
      col1, col2 = st.columns(2)
      with col1:
        F = st.number_input(
            "Axial Force (N)", min_value=0.001, value=5000.0, step=100.0
        )
      with col2:
        A = st.number_input(
            "Cross-sectional Area (m^2)",
            min_value=1e-9,
            value=0.0001,
            format="%.6f",
        )

      if st.button("Calculate Stress"):
        sigma = F / A
        st.success(
            f"**Stress = {sigma:.4f} Pa** ({sigma / 1e6:.4f} MPa)"
        )

    elif calc_type == "Strain":
      st.subheader("Strain (epsilon = dL / L)")
      col1, col2 = st.columns(2)
      with col1:
        dL = st.number_input(
            "Change in length (m)", value=0.002, step=0.0001, format="%.5f"
        )
      with col2:
        L = st.number_input(
            "Original length (m)", min_value=0.001, value=1.0, step=0.01
        )

      if st.button("Calculate Strain"):
        epsilon = dL / L
        st.success(f"**Strain = {epsilon:.6f}** (dimensionless)")

    elif calc_type == "Young's Modulus":
      st.subheader("Young's Modulus (E = sigma / epsilon)")
      col1, col2 = st.columns(2)
      with col1:
        sigma = st.number_input(
            "Stress (Pa)", min_value=1.0, value=2e8, step=1e6
        )
      with col2:
        epsilon = st.number_input(
            "Strain (dimensionless)",
            min_value=1e-9,
            value=0.001,
            format="%.6f",
        )

      if st.button("Calculate Young's Modulus"):
        E = sigma / epsilon
        st.success(
            f"**Young's Modulus = {E:.4e} Pa** ({E / 1e9:.4f} GPa)"
        )

  # ============================================================
  # 3. THERMODYNAMICS
  # ============================================================
  elif module == "3. Thermodynamics":
    st.header("3. Thermodynamics")
    calc_type = st.selectbox(
        "Choose Calculation",
        ["Heat Transfer", "Work Done by a Gas", "Thermal Efficiency"],
    )

    if calc_type == "Heat Transfer":
      st.subheader("Heat Transfer (Q = m * c * dT)")
      col1, col2, col3 = st.columns(3)
      with col1:
        m = st.number_input("Mass (kg)", min_value=0.001, value=2.0, step=0.1)
      with col2:
        c = st.number_input(
            "Specific heat capacity (J/kg.K)",
            min_value=0.001,
            value=4184.0,
            step=10.0,
        )
      with col3:
        dT = st.number_input("Temperature change (K)", value=25.0, step=0.5)

      if st.button("Calculate Heat Transfer"):
        Q = m * c * dT
        st.success(f"**Heat Transfer = {Q:.4f} J**")

    elif calc_type == "Work Done by a Gas":
      st.subheader("Work Done by a Gas (W = P * dV)")
      col1, col2 = st.columns(2)
      with col1:
        P = st.number_input(
            "Pressure (Pa)", min_value=0.001, value=101325.0, step=100.0
        )
      with col2:
        dV = st.number_input("Change in volume (m^3)", value=0.5, step=0.01)

      if st.button("Calculate Work Done"):
        W = P * dV
        st.success(f"**Work Done = {W:.4f} J**")

    elif calc_type == "Thermal Efficiency":
      st.subheader("Thermal Efficiency (eta = W_net / Q_in)")
      col1, col2 = st.columns(2)
      with col1:
        W_net = st.number_input(
            "Net work output (J)", min_value=0.001, value=500.0, step=10.0
        )
      with col2:
        Q_in = st.number_input(
            "Heat supplied (J)", min_value=0.001, value=1500.0, step=10.0
        )

      if st.button("Calculate Efficiency"):
        eta = W_net / Q_in
        st.success(
            f"**Thermal Efficiency = {eta:.4f}** ({eta * 100:.2f} %)"
        )

  # ============================================================
  # 4. FLUID MECHANICS
  # ============================================================
  elif module == "4. Fluid Mechanics":
    st.header("4. Fluid Mechanics")
    calc_type = st.selectbox(
        "Choose Calculation",
        [
            "Hydrostatic Pressure",
            "Reynolds Number",
            "Flow Velocity",
            "Discharge",
        ],
    )

    if calc_type == "Hydrostatic Pressure":
      st.subheader("Hydrostatic Pressure (P = rho * g * h)")
      col1, col2 = st.columns(2)
      with col1:
        rho = st.number_input(
            "Fluid density (kg/m^3)", min_value=0.001, value=1000.0, step=10.0
        )
      with col2:
        h = st.number_input(
            "Depth / height (m)", min_value=0.001, value=10.0, step=0.5
        )

      if st.button("Calculate Pressure"):
        P = rho * G * h
        st.success(
            f"**Pressure = {P:.4f} Pa** ({P / 1000:.4f} kPa)"
        )

    elif calc_type == "Reynolds Number":
      st.subheader("Reynolds Number (Re = rho * v * D / mu)")
      col1, col2 = st.columns(2)
      with col1:
        rho = st.number_input(
            "Fluid density (kg/m^3)", min_value=0.001, value=998.0, step=10.0
        )
        v = st.number_input(
            "Flow velocity (m/s)", min_value=0.001, value=1.5, step=0.1
        )
      with col2:
        D = st.number_input(
            "Pipe diameter (m)", min_value=0.001, value=0.05, step=0.005
        )
        mu = st.number_input(
            "Dynamic viscosity (Pa.s)",
            min_value=1e-6,
            value=0.001,
            format="%.6f",
        )

      if st.button("Calculate Reynolds Number"):
        Re = (rho * v * D) / mu
        st.success(f"**Reynolds Number = {Re:.2f}** (dimensionless)")
        if Re < 2300:
          st.info("-> Flow regime: **LAMINAR**")
        elif Re > 4000:
          st.warning("-> Flow regime: **TURBULENT**")
        else:
          st.info("-> Flow regime: **TRANSITIONAL**")

    elif calc_type == "Flow Velocity":
      st.subheader("Flow Velocity (v = Q / A)")
      col1, col2 = st.columns(2)
      with col1:
        Q = st.number_input(
            "Volumetric flow rate (m^3/s)", min_value=0.0001, value=0.05, step=0.01
        )
      with col2:
        A = st.number_input(
            "Cross-sectional area (m^2)",
            min_value=1e-6,
            value=0.01,
            format="%.4f",
        )

      if st.button("Calculate Velocity"):
        v = Q / A
        st.success(f"**Flow Velocity = {v:.4f} m/s**")

    elif calc_type == "Discharge":
      st.subheader("Discharge (Q = A * v)")
      col1, col2 = st.columns(2)
      with col1:
        A = st.number_input(
            "Cross-sectional area (m^2)",
            min_value=1e-6,
            value=0.01,
            format="%.4f",
        )
      with col2:
        v = st.number_input("Flow velocity (m/s)", min_value=0.0, value=2.0, step=0.1)

      if st.button("Calculate Discharge"):
        Q = A * v
        st.success(
            f"**Discharge = {Q:.4f} m^3/s** ({Q * 1000:.4f} L/s)"
        )

  # ============================================================
  # 5. THERMAL ENGINEERING
  # ============================================================
  elif module == "5. Thermal Engineering":
    st.header("5. Thermal Engineering")
    calc_type = st.selectbox(
        "Choose Calculation",
        ["Heat Conduction", "Coefficient of Performance (COP)", "Heat-Engine Efficiency"],
    )

    if calc_type == "Heat Conduction":
      st.subheader("Heat Conduction (Fourier's Law)")
      col1, col2 = st.columns(2)
      with col1:
        k = st.number_input(
            "Thermal conductivity (W/m.K)", min_value=0.001, value=0.8, step=0.1
        )
        A = st.number_input(
            "Cross-sectional area (m^2)", min_value=0.0001, value=2.0, step=0.1
        )
      with col2:
        dT = st.number_input(
            "Temperature difference (K)", min_value=0.0, value=30.0, step=1.0
        )
        L = st.number_input(
            "Wall thickness (m)", min_value=0.0001, value=0.1, step=0.01
        )

      if st.button("Calculate Heat Conduction"):
        Q = (k * A * dT) / L
        st.success(f"**Heat Conduction Rate = {Q:.4f} W**")

    elif calc_type == "Coefficient of Performance (COP)":
      st.subheader("Coefficient of Performance (COP)")
      device = st.radio("Select Device", ["Refrigerator", "Heat Pump"])
      col1, col2 = st.columns(2)
      with col1:
        Q_val = st.number_input(
            "Heat moved (Qc or Qh)", min_value=0.001, value=1000.0, step=10.0
        )
      with col2:
        W = st.number_input(
            "Compressor work input (W)", min_value=0.001, value=250.0, step=10.0
        )

      if st.button("Calculate COP"):
        COP = Q_val / W
        st.success(f"**{device} COP = {COP:.4f}** (dimensionless)")

    elif calc_type == "Heat-Engine Efficiency":
      st.subheader("Heat-Engine Efficiency (eta = 1 - Qc/Qh)")
      col1, col2 = st.columns(2)
      with col1:
        Qh = st.number_input(
            "Heat supplied by hot reservoir, Qh (J)",
            min_value=0.001,
            value=2000.0,
            step=10.0,
        )
      with col2:
        Qc = st.number_input(
            "Heat rejected to cold reservoir, Qc (J)",
            min_value=0.0,
            value=1200.0,
            step=10.0,
        )

      if st.button("Calculate Heat-Engine Efficiency"):
        if Qc >= Qh:
          st.error("Error: Qc cannot be greater than or equal to Qh.")
        else:
          eta = 1 - (Qc / Qh)
          st.success(
              f"**Heat-Engine Efficiency = {eta:.4f}** ({eta * 100:.2f} %)"
          )

  # ============================================================
  # 6. MACHINE DESIGN
  # ============================================================
  elif module == "6. Machine Design":
    st.header("6. Machine Design")
    calc_type = st.selectbox(
        "Choose Calculation", ["Torque", "Shaft Power", "Shaft Diameter"]
    )

    if calc_type == "Torque":
      st.subheader("Torque (T = F * r)")
      col1, col2 = st.columns(2)
      with col1:
        F = st.number_input("Applied force (N)", min_value=0.0, value=150.0, step=1.0)
      with col2:
        r = st.number_input(
            "Radius / lever arm (m)", min_value=0.0001, value=0.5, step=0.05
        )

      if st.button("Calculate Torque"):
        T = F * r
        st.success(f"**Torque = {T:.4f} N.m**")

    elif calc_type == "Shaft Power":
      st.subheader("Shaft Power (P = 2 * pi * N * T / 60)")
      col1, col2 = st.columns(2)
      with col1:
        N = st.number_input(
            "Rotational speed (RPM)", min_value=0.0, value=1500.0, step=10.0
        )
      with col2:
        T = st.number_input(
            "Torque (N.m)", min_value=0.0, value=50.0, step=1.0
        )

      if st.button("Calculate Shaft Power"):
        P = (2 * math.pi * N * T) / 60
        st.success(
            f"**Shaft Power = {P:.4f} W** ({P / 1000:.4f} kW)"
        )

    elif calc_type == "Shaft Diameter":
      st.subheader("Shaft Diameter (d = (16*T / (pi*tau_allow))^(1/3))")
      col1, col2 = st.columns(2)
      with col1:
        T = st.number_input(
            "Torque to transmit (N.m)", min_value=0.001, value=200.0, step=5.0
        )
      with col2:
        tau = st.number_input(
            "Allowable shear stress (Pa)",
            min_value=1.0,
            value=50e6,
            step=1e6,
            format="%.2e",
        )

      if st.button("Calculate Shaft Diameter"):
        d = ((16 * T) / (math.pi * tau)) ** (1 / 3)
        st.success(
            f"**Minimum Shaft Diameter = {d:.6f} m** ({d * 1000:.3f} mm)"
        )


if __name__ == "__main__":
  main()
