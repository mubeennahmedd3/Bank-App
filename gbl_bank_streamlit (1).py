import streamlit as st
import streamlit.components.v1 as components

# ==========================================
# PAGE CONFIG (Full-Width Modern Web App)
# ==========================================
st.set_page_config(
    page_title="Gareeb Bank Limited (GBL) - Digital Banking",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# INJECT TAILWIND CSS, GOOGLE FONTS & CUSTOM UI STYLING
# ==========================================
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        /* Hide default Streamlit chrome for pure custom HTML-like interface */
        #MainMenu, footer, header {visibility: hidden;}
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 2rem !important;
            max-width: 960px !important;
            font-family: 'Inter', sans-serif;
        }
        body, .stApp {
            background-color: #f8fafc;
            color: #1e293b;
            font-family: 'Inter', sans-serif;
        }

        /* Top Dark Emerald Navigation Bar */
        .gbl-navbar {
            background-color: #022c22;
            color: white;
            padding: 16px 24px;
            border-radius: 0 0 22px 22px;
            box-shadow: 0 10px 25px -5px rgba(2, 44, 34, 0.25);
            border-bottom: 1px solid #065f46;
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 28px;
        }
        .gbl-logo-box {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .gbl-icon {
            width: 42px;
            height: 42px;
            border-radius: 12px;
            background: linear-gradient(135deg, #10b981, #047857);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
            color: white;
            box-shadow: 0 4px 10px rgba(16, 185, 129, 0.3);
        }
        .gbl-badge-gold {
            font-size: 10px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            padding: 2px 8px;
            border-radius: 999px;
            background: rgba(245, 158, 11, 0.18);
            color: #fbbf24;
            border: 1px solid rgba(245, 158, 11, 0.35);
        }
        .gbl-user-pill {
            background: rgba(6, 95, 70, 0.85);
            border: 1px solid #047857;
            padding: 6px 14px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 600;
            color: #d1fae5;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        /* Hero Banner Card */
        .gbl-hero {
            background: linear-gradient(135deg, #064e3b 0%, #022c22 55%, #0f172a 100%);
            padding: 34px 36px;
            border-radius: 24px;
            color: white;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
            margin-bottom: 24px;
        }
        .gbl-pill-tag {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 4px 12px;
            border-radius: 999px;
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.15);
            font-size: 12px;
            font-weight: 600;
            color: #fbbf24;
            margin-bottom: 12px;
            font-family: 'JetBrains Mono', monospace;
        }

        /* Option Cards */
        .option-card {
            background: #ffffff;
            border: 2px solid #e2e8f0;
            border-radius: 20px;
            padding: 22px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.04);
            margin-bottom: 10px;
            min-height: 175px;
        }
        .option-card-green { border-top: 5px solid #047857; }
        .option-card-gold  { border-top: 5px solid #f59e0b; }
        .option-card-red   { border-top: 5px solid #e11d48; }

        .press-badge {
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            font-weight: 700;
            padding: 4px 10px;
            border-radius: 999px;
            display: inline-block;
            margin-bottom: 12px;
        }

        /* Dashboard Balance Card */
        .dash-card {
            background: linear-gradient(135deg, #022c22 0%, #064e3b 50%, #065f46 100%);
            border-radius: 24px;
            padding: 28px 32px;
            color: white;
            box-shadow: 0 20px 25px -5px rgba(2, 44, 34, 0.25);
            margin-bottom: 22px;
        }
        .balance-amount {
            font-family: 'JetBrains Mono', monospace;
            font-size: 2.6rem;
            font-weight: 800;
            color: #ffffff;
            letter-spacing: -0.02em;
        }

        /* Statement Entry Cards */
        .stmt-item {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 16px;
            padding: 14px 16px;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 1px 3px rgba(0,0,0,0.03);
        }
        .stmt-text {
            font-family: 'JetBrains Mono', monospace;
            font-size: 13px;
            font-weight: 600;
            color: #1e293b;
        }
        .tag-sent {
            background: #fef3c7;
            color: #92400e;
            font-size: 10px;
            font-weight: 700;
            padding: 2px 8px;
            border-radius: 6px;
            text-transform: uppercase;
            margin-left: 8px;
        }
        .tag-recv {
            background: #d1fae5;
            color: #065f46;
            font-size: 10px;
            font-weight: 700;
            padding: 2px 8px;
            border-radius: 6px;
            text-transform: uppercase;
            margin-left: 8px;
        }
        .tag-with {
            background: #ffe4e6;
            color: #9f1239;
            font-size: 10px;
            font-weight: 700;
            padding: 2px 8px;
            border-radius: 6px;
            text-transform: uppercase;
            margin-left: 8px;
        }

        /* Style Streamlit buttons to match HTML rounded UI */
        div.stButton > button {
            border-radius: 12px !important;
            font-weight: 700 !important;
            padding: 0.55rem 1.1rem !important;
            transition: all 0.2s ease !important;
        }
        div.stButton > button[kind="primary"] {
            background-color: #047857 !important;
            border-color: #047857 !important;
            color: white !important;
        }
        div.stButton > button[kind="primary"]:hover {
            background-color: #065f46 !important;
            border-color: #065f46 !important;
        }
        /* Style Tabs */
        button[data-baseweb="tab"] {
            font-weight: 700 !important;
            font-size: 13px !important;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# DATABASE (data_base.py)
# ==========================================
DEFAULT_ACCOUNTS = {
    "4210112345671": {
        "name": "Zeeshan Ali",
        "balance": 25000,
        "statments": ["Your first deposite is: 25000"],
        "pin": "1234",
        "acc_status": "active"
    },
    "4210198765432": {
        "name": "Ali Khan",
        "balance": 15000,
        "statments": ["Your first deposite is: 15000"],
        "pin": "4321",
        "acc_status": "active"
    }
}

if "accounts" not in st.session_state:
    st.session_state.accounts = {
        k: {
            "name": v["name"],
            "balance": v["balance"],
            "statments": list(v["statments"]),
            "pin": v["pin"],
            "acc_status": v["acc_status"]
        }
        for k, v in DEFAULT_ACCOUNTS.items()
    }

if "view" not in st.session_state:
    st.session_state.view = "menu"

if "current_cnic" not in st.session_state:
    st.session_state.current_cnic = None

if "pin_attempts" not in st.session_state:
    st.session_state.pin_attempts = {}


def navigate_to(view_name):
    st.session_state.view = view_name
    st.rerun()


accounts = st.session_state.accounts
active_user = accounts.get(st.session_state.current_cnic) if st.session_state.current_cnic else None

# ==========================================
# TOP NAVIGATION BAR (Matches HTML Header)
# ==========================================
user_badge_html = ""
if active_user:
    user_badge_html = f"""
        <div class="gbl-user-pill">
            <span style="width:8px; height:8px; background:#34d399; border-radius:50%; display:inline-block;"></span>
            <span>{active_user['name']} ({st.session_state.current_cnic})</span>
        </div>
    """

st.markdown(f"""
    <div class="gbl-navbar">
        <div class="gbl-logo-box">
            <div class="gbl-icon"><i class="fa-solid fa-landmark"></i></div>
            <div>
                <div style="display:flex; align-items:center; gap:8px;">
                    <span style="font-weight:800; font-size:20px; letter-spacing:-0.02em;">GBL</span>
                    <span class="gbl-badge-gold">Limited</span>
                </div>
                <div style="font-size:12px; color:rgba(209, 250, 229, 0.8);">
                    Gareeb Bank Limited &bull; Apna Bank
                </div>
            </div>
        </div>
        {user_badge_html}
    </div>
""", unsafe_allow_html=True)


# ==========================================
# VIEW 1: MAIN WELCOME MENU (bank.py Loop)
# ==========================================
if st.session_state.view == "menu":
    st.markdown("""
        <div class="gbl-hero">
            <div class="gbl-pill-tag">
                <i class="fa-solid fa-terminal"></i>
                <span>bank.py &bull; 13-Digit CNIC Banking Portal</span>
            </div>
            <h1 style="margin:0 0 8px 0; font-size:2rem; font-weight:800; color:white;">
                Welcome to Gareeb Bank Limited (GBL)
            </h1>
            <p style="margin:0; color:rgba(209, 250, 229, 0.85); font-size:0.95rem; line-height:1.5;">
                Har aam aadmi ka bharosa. Choose your option below to open a new 13-digit CNIC account, access your dashboard, or exit the portal.
            </p>
        </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
            <div class="option-card option-card-green">
                <span class="press-badge" style="background:#022c22; color:white;">Press (1)</span>
                <h3 style="margin:0 0 6px 0; font-size:1.15rem; font-weight:800; color:#0f172a;">Create Account</h3>
                <p style="margin:0; font-size:0.85rem; color:#64748b; line-height:1.45;">
                    13-digit CNIC aur 4-digit PIN ke sath naya GBL account kholein.
                </p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Open Create Account →", key="btn_opt1", type="primary", use_container_width=True):
            navigate_to("create")

    with c2:
        st.markdown("""
            <div class="option-card option-card-gold">
                <span class="press-badge" style="background:#1e293b; color:white;">Press (2)</span>
                <h3 style="margin:0 0 6px 0; font-size:1.15rem; font-weight:800; color:#0f172a;">Login Account</h3>
                <p style="margin:0; font-size:0.85rem; color:#64748b; line-height:1.45;">
                    Apne 13-digit CNIC aur PIN se login karein (3 ghalat attempts par block).
                </p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Open Login Account →", key="btn_opt2", use_container_width=True):
            navigate_to("login")

    with c3:
        st.markdown("""
            <div class="option-card option-card-red">
                <span class="press-badge" style="background:#ffe4e6; color:#9f1239;">Press (0)</span>
                <h3 style="margin:0 0 6px 0; font-size:1.15rem; font-weight:800; color:#0f172a;">Exit Application</h3>
                <p style="margin:0; font-size:0.85rem; color:#64748b; line-height:1.45;">
                    Banking session mehfooz tareeqay se band karein aur bahar niklein.
                </p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Exit Application →", key="btn_opt0", use_container_width=True):
            navigate_to("exit")

    # Quick CLI Simulator Bar (Matches HTML bottom bar)
    st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)
    with st.container(border=True):
        cli_l, cli_m, cli_r = st.columns([3, 1.5, 1])
        with cli_l:
          
        with cli_m:
            cli_choice = st.text_input("CLI", placeholder="1, 2 or 0", max_chars=2, label_visibility="collapsed")
        with cli_r:
            if st.button("Run", use_container_width=True):
                val = cli_choice.strip()
                if val == "1":
                    navigate_to("create")
                elif val == "2":
                    navigate_to("login")
                elif val == "0":
                    navigate_to("exit")
                else:
                    st.error("*********** Invalid Choice ************* (Enter 1, 2, or 0)")


# ==========================================
# VIEW 2: CREATE ACCOUNT (first_interface.py)
# ==========================================
elif st.session_state.view == "create":
    top_l, top_r = st.columns([4, 1])
    with top_l:
        st.markdown("### Open New GBL Account")
        st.caption("`first_interface.py • create_account()`")
    with top_r:
        if st.button("← Menu", use_container_width=True):
            navigate_to("menu")

    with st.container(border=True):
        with st.form("create_form"):
            name = st.text_input("Full Name (Account Holder)", placeholder="e.g. Muhammad Ahmed").strip().capitalize()
            cnic = st.text_input("13-Digit CNIC Number (Without Dashes)", max_chars=13, placeholder="e.g. 4210155667788").strip()
            first_deposite = st.number_input("First Deposit (PKR)", min_value=0, step=500, value=1000)

            p1, p2 = st.columns(2)
            with p1:
                pin = st.text_input("Create 4-Digit PIN", type="password", max_chars=4, placeholder="••••").strip()
            with p2:
                c_pin = st.text_input("Confirm 4-Digit PIN", type="password", max_chars=4, placeholder="••••").strip()

            submit_create = st.form_submit_button("Create GBL Account", type="primary", use_container_width=True)

            if submit_create:
                if not name:
                    st.error("Please enter your full name.")
                elif cnic in accounts:
                    st.error("*********** CNIC is already exist *************")
                elif not (len(cnic) == 13 and cnic.isdigit()):
                    st.error("*********** Invalid CNIC (must be 13 digits) *************")
                elif first_deposite <= 0:
                    st.error("*********** Invalid Amount (must be in positive) *************")
                elif not (len(pin) == 4 and pin.isdigit()):
                    st.error("*********** Invalid PIN (must be in 4 digits) *************")
                elif c_pin != pin:
                    st.error("*********** Confirmation PIN is not matched *************")
                else:
                    accounts[cnic] = {
                        "name": name,
                        "balance": int(first_deposite),
                        "statments": [f"Your first deposite is: {int(first_deposite)}"],
                        "pin": pin,
                        "acc_status": "active"
                    }
                    st.success(f"Account Created Successfully! Holder: **{name}** | CNIC: `{cnic}` | Balance: **Rs. {int(first_deposite):,}**")


# ==========================================
# VIEW 3: LOGIN ACCOUNT (first_interface.py)
# ==========================================
elif st.session_state.view == "login":
    top_l, top_r = st.columns([4, 1])
    with top_l:
        st.markdown("### Welcome Back to GBL Bank")
        st.caption("`first_interface.py • login_account()`")
    with top_r:
        if st.button("← Menu", use_container_width=True):
            navigate_to("menu")

    with st.container(border=True):
        with st.form("login_form"):
            cnic = st.text_input("13-Digit CNIC Number", max_chars=13, placeholder="e.g. 4210112345671").strip()
            pin = st.text_input("4-Digit Security PIN", type="password", max_chars=4, placeholder="••••").strip()
            login_submit = st.form_submit_button("Access Dashboard", type="primary", use_container_width=True)

            if login_submit:
                if cnic not in accounts:
                    st.error("*********** Account does not found *************")
                elif accounts[cnic]["acc_status"] != "active":
                    st.error("*********** Account is temporary block (visit our branch) *************")
                elif pin == accounts[cnic]["pin"]:
                    st.session_state.pin_attempts[cnic] = 0
                    st.session_state.current_cnic = cnic
                    navigate_to("dashboard")
                else:
                    attempts = st.session_state.pin_attempts.get(cnic, 0) + 1
                    st.session_state.pin_attempts[cnic] = attempts
                    if attempts >= 3:
                        accounts[cnic]["acc_status"] = "unactive"
                        st.error("*********** Account is temporary block (visit our branch) *************")
                    else:
                        st.warning(f"*********** Invalid PIN (Attempts left: {3 - attempts}) *************")

        st.markdown("---")
        st.caption("INSTANT TEST ACCOUNTS (1-CLICK LOGIN):")
        t1, t2 = st.columns(2)
        with t1:
            if st.button("⚡ Login: Zeeshan Ali (4210112345671)", use_container_width=True):
                accounts["4210112345671"]["acc_status"] = "active"
                st.session_state.pin_attempts["4210112345671"] = 0
                st.session_state.current_cnic = "4210112345671"
                navigate_to("dashboard")
        with t2:
            if st.button("⚡ Login: Ali Khan (4210198765432)", use_container_width=True):
                accounts["4210198765432"]["acc_status"] = "active"
                st.session_state.pin_attempts["4210198765432"] = 0
                st.session_state.current_cnic = "4210198765432"
                navigate_to("dashboard")


# ==========================================
# VIEW 4: LOGGED-IN BANKING DASHBOARD
# ==========================================
elif st.session_state.view == "dashboard":
    cnic = st.session_state.current_cnic
    if not cnic or cnic not in accounts:
        navigate_to("menu")

    user = accounts[cnic]

    # Top Account Balance Card (Matches HTML Gradient Card)
    st.markdown(f"""
        <div class="dash-card">
            <div style="display:flex; justify-content:space-between; align-items:flex-start; border-bottom:1px solid rgba(255,255,255,0.15); padding-bottom:18px; margin-bottom:18px;">
                <div>
                    <div style="font-size:12px; color:#a7f3d0; font-family:'JetBrains Mono', monospace; margin-bottom:6px;">
                        <span style="background:rgba(16,185,129,0.2); padding:3px 10px; border-radius:999px; border:1px solid rgba(52,211,153,0.3);">{cnic}</span>
                        &nbsp;&bull;&nbsp; Status: <strong>{user['acc_status'].upper()}</strong>
                    </div>
                    <h2 style="margin:0; font-size:1.85rem; font-weight:800; color:white;">{user['name']}</h2>
                </div>
            </div>
            <div>
                <div style="font-size:11px; text-transform:uppercase; letter-spacing:0.08em; color:rgba(209,250,229,0.75); font-weight:700;">
                    (4) Show Balance &bull; Available Current Balance
                </div>
                <div style="margin-top:4px;">
                    <span style="font-size:1.25rem; font-weight:700; color:#fbbf24;">Rs.</span>
                    <span class="balance-amount">{user['balance']:,}</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    _, logout_col = st.columns([4, 1.3])
    with logout_col:
        if st.button("Press (0): Logout", use_container_width=True):
            st.session_state.current_cnic = None
            navigate_to("menu")

    # Two-Column Layout: Left = Operations, Right = Bank Statement
    left_col, right_col = st.columns([1.05, 1.15], gap="large")

    with left_col:
        with st.container(border=True):
            st.markdown("#### Banking Menu Options")
            tab_w, tab_d, tab_t, tab_p = st.tabs([
                "(1) Withdraw",
                "(2) Deposit",
                "(3) Transfer",
                "(6) PIN"
            ])

            # (1) Withdraw
            with tab_w:
                with st.form("withdraw_form"):
                    w_amt = st.number_input("Withdraw Amount (Rs.)", min_value=0, step=500, key="w_input")
                    if st.form_submit_button("Confirm Withdraw", type="primary", use_container_width=True):
                        if w_amt > 0 and w_amt <= user["balance"]:
                            user["balance"] -= int(w_amt)
                            user["statments"].append(f"Amount Withdrawn: {int(w_amt)}")
                            st.success("*********** Withdraw successfully *************")
                            st.rerun()
                        else:
                            st.error("*********** Invalid Amount *************")

            # (2) Deposit
            with tab_d:
                with st.form("deposit_form"):
                    d_amt = st.number_input("Deposit Amount (Rs.)", min_value=0, step=500, key="d_input")
                    if st.form_submit_button("Confirm Deposit", type="primary", use_container_width=True):
                        if d_amt > 0:
                            user["balance"] += int(d_amt)
                            user["statments"].append(f"Amount Deposite: {int(d_amt)}")
                            st.success("*********** Deposite successfully *************")
                            st.rerun()
                        else:
                            st.error("*********** Invalid Amount *************")

            # (3) Fund Transfer (Live Beneficiary Verification + Name in Statement)
            with tab_t:
                bene_cnic = st.text_input("Beneficiary 13-Digit CNIC", max_chars=13, placeholder="e.g. 4210198765432").strip()
                if bene_cnic == cnic:
                    st.error("Cannot transfer to your own CNIC")
                elif bene_cnic in accounts:
                    st.success(f"Verified Recipient: **{accounts[bene_cnic]['name']}**")
                elif len(bene_cnic) > 0:
                    st.caption("Recipient Name: Enter valid 13-digit CNIC")

                t_amt = st.number_input("Transfer Amount (Rs.)", min_value=0, step=500, key="t_input")
                if st.button("Send Funds Instantly", type="primary", use_container_width=True):
                    if bene_cnic == cnic:
                        st.error("Cannot transfer funds to your own account.")
                    elif bene_cnic not in accounts:
                        st.error("*********** Beneficiary does not found *************")
                    elif t_amt > 0 and t_amt <= user["balance"]:
                        amt_int = int(t_amt)
                        receiver = accounts[bene_cnic]

                        user["balance"] -= amt_int
                        receiver["balance"] += amt_int

                        user["statments"].append(
                            f"Fund transfer to {receiver['name']} ({bene_cnic}): Rs. {amt_int}"
                        )
                        receiver["statments"].append(
                            f"Fund received from {user['name']} ({cnic}): Rs. {amt_int}"
                        )
                        st.success(f"Fund Transferred to {receiver['name']}!")
                        st.rerun()
                    else:
                        st.error("*********** Invalid Amount *************")

            # (6) PIN Change
            with tab_p:
                with st.form("pin_form"):
                    cur_pin = st.text_input("Current 4-Digit PIN", type="password", max_chars=4).strip()
                    new_pin = st.text_input("New 4-Digit PIN", type="password", max_chars=4).strip()
                    conf_pin = st.text_input("Confirm New PIN", type="password", max_chars=4).strip()

                    if st.form_submit_button("Update Security PIN", type="primary", use_container_width=True):
                        if cur_pin != user["pin"]:
                            st.error("********** Invalid PIN *************")
                        elif not (len(new_pin) == 4 and new_pin.isdigit()):
                            st.error("*********** Invalid PIN (must be in 4 digits) *************")
                        elif conf_pin != new_pin:
                            st.error("*********** Confirmation PIN is not matched *************")
                        else:
                            user["pin"] = new_pin
                            st.success("********** PIN update successfully *************")

    # Right Column: (5) Bank Statement
    with right_col:
        with st.container(border=True):
            st.markdown(f"#### (5) Bank Statement &nbsp; `({len(user['statments'])} entries)`")
            if not user["statments"]:
                st.info("No statement entries recorded yet.")
            else:
                for idx, entry in enumerate(reversed(user["statments"])):
                    low = entry.lower()
                    tag_html = ""
                    if "fund transfer to" in low:
                        tag_html = '<span class="tag-sent">Transfer Sent</span>'
                    elif "fund received from" in low:
                        tag_html = '<span class="tag-recv">Transfer Received</span>'
                    elif "withdrawn" in low:
                        tag_html = '<span class="tag-with">Withdrawn</span>'

                    entry_num = len(user["statments"]) - idx
                    st.markdown(f"""
                        <div class="stmt-item">
                            <div>
                                <span class="stmt-text">{entry}</span>
                                {tag_html}
                            </div>
                            <span style="font-family:'JetBrains Mono', monospace; font-size:11px; color:#94a3b8;">#{entry_num}</span>
                        </div>
                    """, unsafe_allow_html=True)


# ==========================================
# VIEW 5: EXIT SCREEN (choice == "0")
# ==========================================
elif st.session_state.view == "exit":
    st.markdown("""
        <div style="background:white; border:1px solid #e2e8f0; border-radius:24px; padding:42px 28px; text-align:center; box-shadow:0 10px 25px -5px rgba(0,0,0,0.06);">
            <div style="font-family:'JetBrains Mono', monospace; color:#94a3b8; font-size:12px; margin-bottom:8px;">
                ==============================
            </div>
            <h2 style="margin:0; font-size:1.85rem; font-weight:800; color:#0f172a;">
                Thanks for using GBL Bank
            </h2>
            <div style="font-family:'JetBrains Mono', monospace; color:#94a3b8; font-size:12px; margin-top:8px; margin-bottom:20px;">
                ==============================
            </div>
            <p style="color:#475569; font-size:0.95rem; max-width:440px; margin:0 auto 24px auto;">
                Apka session mehfooz tareeqay se khatam ho chuka hai. Gareeb Bank Limited (GBL) ka intikhab karne ka shukriya!
            </p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)
    _, btn_c, _ = st.columns([1.2, 1.5, 1.2])
    with btn_c:
        if st.button("↻ Restart GBL Application", type="primary", use_container_width=True):
            navigate_to("menu")
