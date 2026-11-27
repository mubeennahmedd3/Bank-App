import streamlit as st
from datetime import datetime

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Gareeb Bank Limited (GBL) | Online Banking",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# CLEAN REALISTIC BANKING CSS
# ==========================================
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
    <style>
        #MainMenu, footer, header {visibility: hidden;}
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 2.5rem !important;
            max-width: 920px !important;
            font-family: 'Inter', sans-serif;
        }
        body, .stApp {
            background-color: #f4f6f9;
            color: #0f172a;
            font-family: 'Inter', sans-serif;
        }

        /* Top Banking Header */
        .bank-topbar {
            background: #022c22;
            color: #ffffff;
            padding: 16px 26px;
            border-radius: 0 0 18px 18px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 6px 20px rgba(2, 44, 34, 0.18);
            margin-bottom: 26px;
        }
        .bank-brand {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .bank-logo {
            width: 40px;
            height: 40px;
            border-radius: 10px;
            background: linear-gradient(135deg, #10b981, #047857);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
            font-size: 16px;
            color: white;
        }
        .bank-title {
            font-size: 18px;
            font-weight: 800;
            letter-spacing: -0.02em;
            margin: 0;
            line-height: 1.2;
        }
        .bank-sub {
            font-size: 11px;
            color: #a7f3d0;
            margin: 0;
        }
        .secure-badge {
            background: rgba(16, 185, 129, 0.15);
            border: 1px solid rgba(52, 211, 153, 0.35);
            color: #6ee7b7;
            font-size: 11px;
            font-weight: 600;
            padding: 5px 12px;
            border-radius: 999px;
        }

        /* Welcome Hero */
        .welcome-banner {
            background: linear-gradient(135deg, #064e3b 0%, #022c22 100%);
            border-radius: 20px;
            padding: 32px 34px;
            color: white;
            margin-bottom: 22px;
            box-shadow: 0 12px 24px -6px rgba(2, 44, 34, 0.22);
        }
        .welcome-banner h1 {
            margin: 0 0 8px 0;
            font-size: 1.85rem;
            font-weight: 800;
            color: white;
        }
        .welcome-banner p {
            margin: 0;
            font-size: 0.95rem;
            color: #d1fae5;
            opacity: 0.9;
        }

        /* Action Cards on Home */
        .portal-card {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 16px;
            padding: 22px;
            box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
            margin-bottom: 10px;
            min-height: 145px;
        }
        .portal-card h3 {
            margin: 0 0 6px 0;
            font-size: 1.1rem;
            font-weight: 700;
            color: #0f172a;
        }
        .portal-card p {
            margin: 0;
            font-size: 0.86rem;
            color: #64748b;
            line-height: 1.45;
        }

        /* Account Card in Dashboard */
        .account-card {
            background: linear-gradient(135deg, #022c22 0%, #064e3b 60%, #065f46 100%);
            border-radius: 20px;
            padding: 26px 30px;
            color: white;
            box-shadow: 0 14px 28px -6px rgba(2, 44, 34, 0.25);
            margin-bottom: 20px;
        }
        .acc-label {
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: #a7f3d0;
            font-weight: 600;
        }
        .acc-balance {
            font-family: 'JetBrains Mono', monospace;
            font-size: 2.35rem;
            font-weight: 700;
            color: #ffffff;
            margin-top: 2px;
        }
        .acc-meta {
            font-family: 'JetBrains Mono', monospace;
            font-size: 12px;
            color: #d1fae5;
            margin-top: 10px;
            padding-top: 12px;
            border-top: 1px solid rgba(255,255,255,0.14);
            display: flex;
            justify-content: space-between;
        }

        /* Statement Rows */
        .tx-row {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 12px 15px;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .tx-title {
            font-size: 13px;
            font-weight: 600;
            color: #1e293b;
        }
        .tx-date {
            font-size: 11px;
            color: #94a3b8;
            font-family: 'JetBrains Mono', monospace;
            margin-top: 2px;
        }
        .tx-credit {
            font-family: 'JetBrains Mono', monospace;
            font-size: 13px;
            font-weight: 700;
            color: #059669;
        }
        .tx-debit {
            font-family: 'JetBrains Mono', monospace;
            font-size: 13px;
            font-weight: 700;
            color: #dc2626;
        }

        div.stButton > button {
            border-radius: 10px !important;
            font-weight: 600 !important;
            padding: 0.5rem 1rem !important;
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
    </style>
""", unsafe_allow_html=True)

# ==========================================
# SESSION DATABASE
# ==========================================
if "accounts" not in st.session_state:
    st.session_state.accounts = {}

if "page" not in st.session_state:
    st.session_state.page = "home"

if "active_cnic" not in st.session_state:
    st.session_state.active_cnic = None

if "pin_attempts" not in st.session_state:
    st.session_state.pin_attempts = {}


def go_page(name):
    st.session_state.page = name
    st.rerun()


def format_cnic(cnic_str):
    if len(cnic_str) == 13 and cnic_str.isdigit():
        return f"{cnic_str[:5]}-{cnic_str[5:12]}-{cnic_str[12]}"
    return cnic_str


def now_str():
    return datetime.now().strftime("%d %b %Y, %I:%M %p")


accounts = st.session_state.accounts
current_user = accounts.get(st.session_state.active_cnic) if st.session_state.active_cnic else None

# ==========================================
# TOP HEADER BAR
# ==========================================
right_badge = (
    f'<span class="secure-badge">Signed in: {current_user["name"]}</span>'
    if current_user else
    '<span class="secure-badge">256-Bit Secured Portal</span>'
)

st.markdown(f"""
    <div class="bank-topbar">
        <div class="bank-brand">
            <div class="bank-logo">GBL</div>
            <div>
                <p class="bank-title">Gareeb Bank Limited</p>
                <p class="bank-sub">Digital Banking Services &bull; Pakistan</p>
            </div>
        </div>
        {right_badge}
    </div>
""", unsafe_allow_html=True)


# ==========================================
# 1. HOME SCREEN
# ==========================================
if st.session_state.page == "home":
    st.markdown("""
        <div class="welcome-banner">
            <h1>Welcome to Gareeb Bank Limited</h1>
            <p>Simple, fast, and reliable digital banking. Open an account with your CNIC or sign in to manage your funds.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        st.markdown("""
            <div class="portal-card">
                <h3>Open a New Account</h3>
                <p>Register instantly using your 13-digit CNIC number, set a 4-digit security PIN, and make your opening deposit.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Create Account", type="primary", use_container_width=True):
            go_page("register")

    with col2:
        st.markdown("""
            <div class="portal-card">
                <h3>Customer Sign In</h3>
                <p>Access your account balance, transfer funds to other GBL members, view statements, or update your PIN.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Sign In to Account", use_container_width=True):
            go_page("login")


# ==========================================
# 2. CREATE ACCOUNT SCREEN
# ==========================================
elif st.session_state.page == "register":
    h_left, h_right = st.columns([4, 1])
    with h_left:
        st.subheader("Open New Bank Account")
    with h_right:
        if st.button("← Back", use_container_width=True):
            go_page("home")

    with st.container(border=True):
        with st.form("register_form"):
            full_name = st.text_input("Account Holder Full Name", placeholder="Enter your full name").strip().title()
            cnic_input = st.text_input("CNIC Number (13 digits without dashes)", max_chars=13, placeholder="e.g. 4210112345671").strip()
            opening_deposit = st.number_input("Initial Deposit Amount (PKR)", min_value=0, step=500, value=1000)

            p_col1, p_col2 = st.columns(2)
            with p_col1:
                pin_input = st.text_input("Create 4-Digit PIN", type="password", max_chars=4, placeholder="••••").strip()
            with p_col2:
                confirm_pin = st.text_input("Confirm 4-Digit PIN", type="password", max_chars=4, placeholder="••••").strip()

            submitted = st.form_submit_button("Open Account", type="primary", use_container_width=True)

            if submitted:
                if not full_name:
                    st.error("Please enter the account holder's full name.")
                elif cnic_input in accounts:
                    st.error("An account with this CNIC already exists.")
                elif not (len(cnic_input) == 13 and cnic_input.isdigit()):
                    st.error("Invalid CNIC. Please enter exactly 13 numeric digits.")
                elif opening_deposit <= 0:
                    st.error("Initial deposit must be greater than Rs. 0.")
                elif not (len(pin_input) == 4 and pin_input.isdigit()):
                    st.error("PIN must be exactly 4 numeric digits.")
                elif pin_input != confirm_pin:
                    st.error("PIN and Confirm PIN do not match.")
                else:
                    amt = int(opening_deposit)
                    accounts[cnic_input] = {
                        "name": full_name,
                        "balance": amt,
                        "pin": pin_input,
                        "acc_status": "active",
                        "statments": [
                            {
                                "title": "Opening Account Deposit",
                                "amount": amt,
                                "type": "credit",
                                "time": now_str()
                            }
                        ]
                    }
                    st.success(f"Account opened successfully for **{full_name}** ({format_cnic(cnic_input)}). You can now sign in.")


# ==========================================
# 3. LOGIN SCREEN
# ==========================================
elif st.session_state.page == "login":
    h_left, h_right = st.columns([4, 1])
    with h_left:
        st.subheader("Sign In to Online Banking")
    with h_right:
        if st.button("← Back", use_container_width=True):
            go_page("home")

    with st.container(border=True):
        with st.form("login_form"):
            cnic_login = st.text_input("CNIC Number (13 digits)", max_chars=13, placeholder="Enter your 13-digit CNIC").strip()
            pin_login = st.text_input("4-Digit PIN", type="password", max_chars=4, placeholder="••••").strip()
            login_submitted = st.form_submit_button("Sign In", type="primary", use_container_width=True)

            if login_submitted:
                if cnic_login not in accounts:
                    st.error("Account not found. Please check your CNIC or open a new account.")
                elif accounts[cnic_login]["acc_status"] != "active":
                    st.error("Your account has been temporarily blocked due to multiple invalid PIN attempts. Please visit your nearest GBL branch.")
                elif pin_login == accounts[cnic_login]["pin"]:
                    st.session_state.pin_attempts[cnic_login] = 0
                    st.session_state.active_cnic = cnic_login
                    go_page("dashboard")
                else:
                    tries = st.session_state.pin_attempts.get(cnic_login, 0) + 1
                    st.session_state.pin_attempts[cnic_login] = tries
                    if tries >= 3:
                        accounts[cnic_login]["acc_status"] = "unactive"
                        st.error("Account temporarily blocked after 3 incorrect PIN attempts. Please visit a GBL branch.")
                    else:
                        st.warning(f"Incorrect PIN. {3 - tries} attempt(s) remaining before account lock.")


# ==========================================
# 4. BANKING DASHBOARD
# ==========================================
elif st.session_state.page == "dashboard":
    cnic = st.session_state.active_cnic
    if not cnic or cnic not in accounts:
        go_page("home")

    user = accounts[cnic]

    # Account Summary Card
    st.markdown(f"""
        <div class="account-card">
            <div class="acc-label">Available Balance</div>
            <div class="acc-balance">Rs. {user['balance']:,}</div>
            <div class="acc-meta">
                <span>Account Title: <strong>{user['name']}</strong></span>
                <span>CNIC: <strong>{format_cnic(cnic)}</strong></span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    _, signout_col = st.columns([4.5, 1])
    with signout_col:
        if st.button("Sign Out", use_container_width=True):
            st.session_state.active_cnic = None
            go_page("home")

    left_col, right_col = st.columns([1.05, 1.15], gap="large")

    # Left: Banking Operations
    with left_col:
        with st.container(border=True):
            tab_transfer, tab_deposit, tab_withdraw, tab_pin = st.tabs([
                "Fund Transfer",
                "Deposit",
                "Withdraw",
                "Change PIN"
            ])

            # Fund Transfer (Includes Recipient & Sender Name in Statement)
            with tab_transfer:
                bene_cnic = st.text_input("Recipient CNIC (13 digits)", max_chars=13, placeholder="Enter beneficiary CNIC").strip()

                if bene_cnic:
                    if bene_cnic == cnic:
                        st.error("You cannot transfer funds to your own account.")
                    elif bene_cnic in accounts:
                        st.info(f"Recipient Name: **{accounts[bene_cnic]['name']}**")
                    elif len(bene_cnic) == 13:
                        st.warning("No GBL account found for this CNIC.")

                transfer_amt = st.number_input("Amount (PKR)", min_value=0, step=500, key="transfer_amt")
                if st.button("Transfer Money", type="primary", use_container_width=True):
                    if bene_cnic == cnic:
                        st.error("Self-transfer is not allowed.")
                    elif bene_cnic not in accounts:
                        st.error("Beneficiary account not found.")
                    elif transfer_amt <= 0 or transfer_amt > user["balance"]:
                        st.error("Invalid amount or insufficient balance.")
                    else:
                        amt = int(transfer_amt)
                        recipient = accounts[bene_cnic]

                        user["balance"] -= amt
                        recipient["balance"] += amt

                        user["statments"].append({
                            "title": f"Fund Transfer to {recipient['name']} ({format_cnic(bene_cnic)})",
                            "amount": amt,
                            "type": "debit",
                            "time": now_str()
                        })
                        recipient["statments"].append({
                            "title": f"Fund Received from {user['name']} ({format_cnic(cnic)})",
                            "amount": amt,
                            "type": "credit",
                            "time": now_str()
                        })
                        st.success(f"Rs. {amt:,} transferred to {recipient['name']}.")
                        st.rerun()

            # Deposit
            with tab_deposit:
                with st.form("deposit_form"):
                    dep_amt = st.number_input("Deposit Amount (PKR)", min_value=0, step=500, key="dep_amt")
                    if st.form_submit_button("Deposit Cash", type="primary", use_container_width=True):
                        if dep_amt <= 0:
                            st.error("Please enter a valid deposit amount.")
                        else:
                            amt = int(dep_amt)
                            user["balance"] += amt
                            user["statments"].append({
                                "title": "Cash Deposit",
                                "amount": amt,
                                "type": "credit",
                                "time": now_str()
                            })
                            st.success(f"Rs. {amt:,} deposited successfully.")
                            st.rerun()

            # Withdraw
            with tab_withdraw:
                with st.form("withdraw_form"):
                    with_amt = st.number_input("Withdraw Amount (PKR)", min_value=0, step=500, key="with_amt")
                    if st.form_submit_button("Withdraw Cash", type="primary", use_container_width=True):
                        if with_amt <= 0 or with_amt > user["balance"]:
                            st.error("Invalid amount or insufficient balance.")
                        else:
                            amt = int(with_amt)
                            user["balance"] -= amt
                            user["statments"].append({
                                "title": "Cash Withdrawal",
                                "amount": amt,
                                "type": "debit",
                                "time": now_str()
                            })
                            st.success(f"Rs. {amt:,} withdrawn successfully.")
                            st.rerun()

            # Change PIN
            with tab_pin:
                with st.form("change_pin_form"):
                    old_pin = st.text_input("Current PIN", type="password", max_chars=4).strip()
                    new_pin = st.text_input("New 4-Digit PIN", type="password", max_chars=4).strip()
                    conf_new_pin = st.text_input("Confirm New PIN", type="password", max_chars=4).strip()

                    if st.form_submit_button("Update PIN", type="primary", use_container_width=True):
                        if old_pin != user["pin"]:
                            st.error("Current PIN is incorrect.")
                        elif not (len(new_pin) == 4 and new_pin.isdigit()):
                            st.error("New PIN must be 4 numeric digits.")
                        elif new_pin != conf_new_pin:
                            st.error("New PIN confirmation does not match.")
                        else:
                            user["pin"] = new_pin
                            st.success("Your security PIN has been updated.")

    # Right: Account Statement
    with right_col:
        with st.container(border=True):
            st.markdown("#### Account Statement")
            tx_list = user["statments"]
            if not tx_list:
                st.info("No transactions yet.")
            else:
                for tx in reversed(tx_list):
                    is_credit = tx["type"] == "credit"
                    sign = "+" if is_credit else "-"
                    amt_cls = "tx-credit" if is_credit else "tx-debit"
                    st.markdown(f"""
                        <div class="tx-row">
                            <div>
                                <div class="tx-title">{tx['title']}</div>
                                <div class="tx-date">{tx['time']}</div>
                            </div>
                            <div class="{amt_cls}">{sign} Rs. {tx['amount']:,}</div>
                        </div>
                    """, unsafe_allow_html=True)
