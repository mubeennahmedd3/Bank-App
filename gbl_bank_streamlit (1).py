import streamlit as st

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

st.set_page_config(
    page_title="Gareeb Bank Limited (GBL)",
    page_icon="🏦",
    layout="centered"
)

# Custom CSS for clean banking UI
st.markdown("""
    <style>
        .main-header {
            background: linear-gradient(135deg, #064e3b 0%, #047857 100%);
            padding: 20px 24px;
            border-radius: 14px;
            color: white;
            margin-bottom: 20px;
        }
        .main-header h1 {
            margin: 0;
            font-size: 1.75rem;
            color: white;
        }
        .main-header p {
            margin: 4px 0 0 0;
            color: #a7f3d0;
            font-size: 0.9rem;
        }
        .balance-box {
            background-color: #ecfdf5;
            border: 1px solid #10b981;
            border-radius: 12px;
            padding: 16px 20px;
            margin-bottom: 16px;
        }
        .stmt-card {
            background-color: #f8fafc;
            border-left: 4px solid #047857;
            padding: 10px 14px;
            border-radius: 6px;
            margin-bottom: 8px;
            font-family: monospace;
            font-size: 0.9rem;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State
if "accounts" not in st.session_state:
    st.session_state.accounts = {k: {
        "name": v["name"],
        "balance": v["balance"],
        "statments": list(v["statments"]),
        "pin": v["pin"],
        "acc_status": v["acc_status"]
    } for k, v in DEFAULT_ACCOUNTS.items()}

if "view" not in st.session_state:
    st.session_state.view = "menu"  # menu | create | login | dashboard | exit

if "current_cnic" not in st.session_state:
    st.session_state.current_cnic = None

if "pin_attempts" not in st.session_state:
    st.session_state.pin_attempts = {}


def go_to(view_name):
    st.session_state.view = view_name
    st.rerun()


# Top Header
st.markdown("""
    <div class="main-header">
        <h1>🏦 Gareeb Bank Limited (GBL)</h1>
        <p>Apna Bank • Har Aam Aadmi Ka Bharosa</p>
    </div>
""", unsafe_allow_html=True)

accounts = st.session_state.accounts


# ==========================================
# VIEW 1: MAIN MENU (bank.py)
# ==========================================
if st.session_state.view == "menu":
    st.subheader("Main Menu — Choose Your Option (1, 2, 0)")
    st.caption("Test Accounts: CNIC `4210112345671` (PIN: `1234`) | CNIC `4210198765432` (PIN: `4321`)")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**Press (1)**")
        if st.button("Create Account", use_container_width=True, type="primary"):
            go_to("create")

    with col2:
        st.markdown("**Press (2)**")
        if st.button("Login Account", use_container_width=True):
            go_to("login")

    with col3:
        st.markdown("**Press (0)**")
        if st.button("Exit Application", use_container_width=True):
            go_to("exit")


# ==========================================
# VIEW 2: CREATE ACCOUNT (first_interface.py)
# ==========================================
elif st.session_state.view == "create":
    top_l, top_r = st.columns([3, 1])
    with top_l:
        st.subheader("Create New GBL Account")
    with top_r:
        if st.button("← Main Menu", use_container_width=True):
            go_to("menu")

    with st.form("create_account_form"):
        name = st.text_input("Full Name").strip().capitalize()
        cnic = st.text_input("13-Digit CNIC Number", max_chars=13).strip()
        first_deposite = st.number_input("First Deposit (Rs.)", min_value=0, step=100, value=1000)
        pin = st.text_input("Create 4-Digit PIN", type="password", max_chars=4).strip()
        c_pin = st.text_input("Confirm 4-Digit PIN", type="password", max_chars=4).strip()

        submitted = st.form_submit_button("Create Account", type="primary", use_container_width=True)

        if submitted:
            if not name:
                st.error("Please enter your full name.")
            elif cnic in accounts:
                st.error("CNIC is already exist!")
            elif not (len(cnic) == 13 and cnic.isdigit()):
                st.error("Invalid CNIC (must be 13 digits).")
            elif first_deposite <= 0:
                st.error("Invalid Amount (must be positive).")
            elif not (len(pin) == 4 and pin.isdigit()):
                st.error("Invalid PIN (must be 4 digits).")
            elif c_pin != pin:
                st.error("Confirmation PIN is not matched!")
            else:
                accounts[cnic] = {
                    "name": name,
                    "balance": int(first_deposite),
                    "statments": [f"Your first deposite is: {int(first_deposite)}"],
                    "pin": pin,
                    "acc_status": "active"
                }
                st.success(f"Account created successfully! Holder: {name} | CNIC: {cnic} | Balance: Rs. {int(first_deposite):,}")


# ==========================================
# VIEW 3: LOGIN ACCOUNT (first_interface.py)
# ==========================================
elif st.session_state.view == "login":
    top_l, top_r = st.columns([3, 1])
    with top_l:
        st.subheader("Welcome Back to GBL Bank")
    with top_r:
        if st.button("← Main Menu", use_container_width=True):
            go_to("menu")

    with st.form("login_form"):
        cnic = st.text_input("13-Digit CNIC Number", max_chars=13).strip()
        pin = st.text_input("4-Digit PIN", type="password", max_chars=4).strip()
        login_btn = st.form_submit_button("Login", type="primary", use_container_width=True)

        if login_btn:
            if cnic not in accounts:
                st.error("Account does not found!")
            elif accounts[cnic]["acc_status"] != "active":
                st.error("Account is temporary block (visit our branch).")
            elif pin == accounts[cnic]["pin"]:
                st.session_state.pin_attempts[cnic] = 0
                st.session_state.current_cnic = cnic
                st.session_state.view = "dashboard"
                st.rerun()
            else:
                attempts = st.session_state.pin_attempts.get(cnic, 0) + 1
                st.session_state.pin_attempts[cnic] = attempts
                if attempts >= 3:
                    accounts[cnic]["acc_status"] = "unactive"
                    st.error("Account is temporary block (visit our branch) after 3 invalid PIN attempts.")
                else:
                    st.warning(f"Invalid PIN! Remaining attempts: {3 - attempts}")


# ==========================================
# VIEW 4: DASHBOARD (login_menu.py & all_features.py)
# ==========================================
elif st.session_state.view == "dashboard":
    cnic = st.session_state.current_cnic
    if cnic not in accounts:
        go_to("menu")

    user = accounts[cnic]

    hdr_l, hdr_r = st.columns([3, 1])
    with hdr_l:
        st.markdown(f"""
            <div class="balance-box">
                <div style="font-size: 0.85rem; color: #047857; font-weight: 600;">
                    {user["name"]} • CNIC: {cnic} ({user["acc_status"].upper()})
                </div>
                <div style="font-size: 1.8rem; font-weight: 800; color: #064e3b; margin-top: 4px;">
                    Current Balance: Rs. {user["balance"]:,}
                </div>
            </div>
        """, unsafe_allow_html=True)
    with hdr_r:
        st.write("")
        if st.button("(0) Logout", use_container_width=True):
            st.session_state.current_cnic = None
            go_to("menu")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "(1) Withdraw",
        "(2) Deposit",
        "(3) Fund Transfer",
        "(4) Show Balance",
        "(5) Bank Statement",
        "(6) PIN Change"
    ])

    # (1) Withdraw Amount
    with tab1:
        st.markdown("#### Withdraw Amount")
        with st.form("withdraw_form"):
            w_amt = st.number_input("Enter your Amount (Rs.)", min_value=0, step=100, key="w_amt")
            if st.form_submit_button("Withdraw", type="primary"):
                if w_amt > 0 and w_amt <= user["balance"]:
                    user["balance"] -= int(w_amt)
                    user["statments"].append(f"Amount Withdrawn: {int(w_amt)}")
                    st.success("Withdraw successfully!")
                    st.rerun()
                else:
                    st.error("Invalid Amount or Insufficient Balance!")

    # (2) Deposit Amount
    with tab2:
        st.markdown("#### Deposit Amount")
        with st.form("deposit_form"):
            d_amt = st.number_input("Enter your Amount (Rs.)", min_value=0, step=100, key="d_amt")
            if st.form_submit_button("Deposit", type="primary"):
                if d_amt > 0:
                    user["balance"] += int(d_amt)
                    user["statments"].append(f"Amount Deposite: {int(d_amt)}")
                    st.success("Deposite successfully!")
                    st.rerun()
                else:
                    st.error("Invalid Amount!")

    # (3) Fund Transfer (Shows Recipient & Sender Name in Statement)
    with tab3:
        st.markdown("#### Fund Transfer")
        with st.form("transfer_form"):
            bene_cnic = st.text_input("Enter Beneficiary 13-Digit CNIC Number", max_chars=13).strip()
            t_amt = st.number_input("Enter Transfer Amount (Rs.)", min_value=0, step=100, key="t_amt")
            if st.form_submit_button("Transfer Funds", type="primary"):
                if bene_cnic == cnic:
                    st.error("Cannot transfer funds to your own account.")
                elif bene_cnic not in accounts:
                    st.error("Beneficiary does not found!")
                elif t_amt > 0 and t_amt <= user["balance"]:
                    amt_int = int(t_amt)
                    recipient_name = accounts[bene_cnic]["name"]
                    sender_name = user["name"]

                    user["balance"] -= amt_int
                    accounts[bene_cnic]["balance"] += amt_int

                    user["statments"].append(
                        f"Fund transfer to {recipient_name} ({bene_cnic}): Rs. {amt_int}"
                    )
                    accounts[bene_cnic]["statments"].append(
                        f"Fund received from {sender_name} ({cnic}): Rs. {amt_int}"
                    )
                    st.success(f"Fund Transferred successfully to {recipient_name}!")
                    st.rerun()
                else:
                    st.error("Invalid Amount or Insufficient Balance!")

    # (4) Show Balance
    with tab4:
        st.markdown("#### Current Balance")
        st.info(f"Your current balance is: **Rs. {user['balance']:,}**")

    # (5) Bank Statement
    with tab5:
        st.markdown("#### Bank Statement")
        if not user["statments"]:
            st.write("No statement entries found.")
        else:
            for item in reversed(user["statments"]):
                st.markdown(f'<div class="stmt-card">{item}</div>', unsafe_allow_html=True)

    # (6) PIN Change
    with tab6:
        st.markdown("#### Change PIN")
        with st.form("pin_change_form"):
            cur_pin = st.text_input("Enter your current PIN", type="password", max_chars=4).strip()
            new_pin = st.text_input("Create your New PIN", type="password", max_chars=4).strip()
            conf_pin = st.text_input("Confirm your PIN", type="password", max_chars=4).strip()

            if st.form_submit_button("Update PIN", type="primary"):
                if cur_pin != user["pin"]:
                    st.error("Invalid PIN!")
                elif not (len(new_pin) == 4 and new_pin.isdigit()):
                    st.error("Invalid PIN (must be in 4 digits).")
                elif conf_pin != new_pin:
                    st.error("Confirmation PIN is not matched!")
                else:
                    user["pin"] = new_pin
                    st.success("PIN updated successfully!")


# ==========================================
# VIEW 5: EXIT SCREEN (choice == "0")
# ==========================================
elif st.session_state.view == "exit":
    st.success("Thanks for using GBL Bank!")
    st.write("Apka session khatam ho chuka hai.")
    if st.button("Restart GBL Application", type="primary"):
        go_to("menu")
