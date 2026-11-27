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
# CLEAN BANKING CSS WITH GRAPHICS & BADGES
# ==========================================
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
    <style>
        #MainMenu, footer, header {visibility: hidden;}
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 2.5rem !important;
            max-width: 940px !important;
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
            width: 42px;
            height: 42px;
            border-radius: 12px;
            background: linear-gradient(135deg, #10b981, #047857);
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 10px rgba(16, 185, 129, 0.25);
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
            padding: 6px 13px;
            border-radius: 999px;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        /* Welcome Hero with SVG Graphic */
        .welcome-banner {
            background: linear-gradient(135deg, #064e3b 0%, #022c22 100%);
            border-radius: 22px;
            padding: 30px 34px;
            color: white;
            margin-bottom: 22px;
            box-shadow: 0 12px 24px -6px rgba(2, 44, 34, 0.22);
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 20px;
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
            opacity: 0.92;
            max-width: 560px;
        }
        .hero-graphic {
            flex-shrink: 0;
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 18px;
            padding: 14px;
        }

        /* Action Cards on Home */
        .portal-card {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 18px;
            padding: 22px;
            box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
            margin-bottom: 10px;
            min-height: 162px;
        }
        .card-icon-wrap {
            width: 42px;
            height: 42px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 14px;
        }
        .icon-green {
            background: #ecfdf5;
            color: #047857;
            border: 1px solid #a7f3d0;
        }
        .icon-gold {
            background: #fffbeb;
            color: #b45309;
            border: 1px solid #fde68a;
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
            border-radius: 22px;
            padding: 26px 30px;
            color: white;
            box-shadow: 0 14px 28px -6px rgba(2, 44, 34, 0.25);
            margin-bottom: 18px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 20px;
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
            margin-top: 12px;
            padding-top: 12px;
            border-top: 1px solid rgba(255,255,255,0.14);
            display: flex;
            flex-wrap: wrap;
            gap: 22px;
        }
        .chip-visual {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.16);
            border-radius: 16px;
            padding: 14px;
            flex-shrink: 0;
        }

        /* Statement Rows with Direction Graphics */
        .tx-row {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 14px;
            padding: 12px 15px;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
        }
        .tx-left {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .tx-badge {
            width: 34px;
            height: 34px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'JetBrains Mono', monospace;
            font-weight: 800;
            font-size: 15px;
            flex-shrink: 0;
        }
        .tx-badge-credit {
            background: #ecfdf5;
            color: #059669;
            border: 1px solid #a7f3d0;
        }
        .tx-badge-debit {
            background: #fef2f2;
            color: #dc2626;
            border: 1px solid #fecaca;
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
            white-space: nowrap;
        }
        .tx-debit {
            font-family: 'JetBrains Mono', monospace;
            font-size: 13px;
            font-weight: 700;
            color: #dc2626;
            white-space: nowrap;
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
# SVG GRAPHIC SNIPPETS
# ==========================================
LOGO_SVG = """
<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M3 21h18"/><path d="M3 10h18"/><path d="M5 6l7-3 7 3"/><path d="M4 10v11"/><path d="M20 10v11"/><path d="M8 14v3"/><path d="M12 14v3"/><path d="M16 14v3"/>
</svg>
"""

SHIELD_SVG = """
<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
</svg>
"""

HERO_CARD_SVG = """
<svg width="112" height="72" viewBox="0 0 112 72" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="2" y="4" width="108" height="64" rx="10" fill="rgba(16,185,129,0.16)" stroke="#34d399" stroke-width="1.5"/>
    <rect x="14" y="16" width="24" height="17" rx="3.5" fill="#fbbf24" fill-opacity="0.85"/>
    <path d="M50 20C54 23 54 27 50 30" stroke="#a7f3d0" stroke-width="2" stroke-linecap="round"/>
    <path d="M56 17C62 22 62 28 56 33" stroke="#a7f3d0" stroke-width="2" stroke-linecap="round"/>
    <line x1="14" y1="47" x2="62" y2="47" stroke="#d1fae5" stroke-width="2.5" stroke-linecap="round" stroke-opacity="0.7"/>
    <circle cx="88" cy="47" r="8" fill="#10b981" fill-opacity="0.7"/>
    <circle cx="79" cy="47" r="8" fill="#fbbf24" fill-opacity="0.75"/>
</svg>
"""

USER_PLUS_SVG = """
<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><line x1="20" y1="8" x2="20" y2="14"/><line x1="17" y1="11" x2="23" y2="11"/>
</svg>
"""

LOGIN_KEY_SVG = """
<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"/><polyline points="10 17 15 12 10 7"/><line x1="15" y1="12" x2="3" y2="12"/>
</svg>
"""

WALLET_CHART_SVG = """
<svg width="86" height="64" viewBox="0 0 86 64" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="6" y="10" width="74" height="46" rx="10" fill="rgba(255,255,255,0.08)" stroke="#6ee7b7" stroke-width="1.4"/>
    <polyline points="18,42 33,31 46,37 66,20" stroke="#fbbf24" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="66" cy="20" r="3.5" fill="#34d399"/>
</svg>
"""

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
    f'<span class="secure-badge">{SHIELD_SVG} {current_user["name"]}</span>'
    if current_user else
    f'<span class="secure-badge">{SHIELD_SVG} Secured Banking</span>'
)

st.markdown(f"""
    <div class="bank-topbar">
        <div class="bank-brand">
            <div class="bank-logo">{LOGO_SVG}</div>
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
    st.markdown(f"""
        <div class="welcome-banner">
            <div>
                <h1>Welcome to Gareeb Bank Limited</h1>
                <p>Simple, fast, and reliable digital banking. Open an account with your 13-digit CNIC or sign in to manage your funds.</p>
            </div>
            <div class="hero-graphic">{HERO_CARD_SVG}</div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        st.markdown(f"""
            <div class="portal-card">
                <div class="card-icon-wrap icon-green">{USER_PLUS_SVG}</div>
                <h3>Open a New Account</h3>
                <p>Register instantly using your 13-digit CNIC number, set a 4-digit security PIN, and make your opening deposit.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Create Account", type="primary", use_container_width=True):
            go_page("register")

    with col2:
        st.markdown(f"""
            <div class="portal-card">
                <div class="card-icon-wrap icon-gold">{LOGIN_KEY_SVG}</div>
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

    # Account Summary Card with Graphic
    st.markdown(f"""
        <div class="account-card">
            <div style="flex-grow:1;">
                <div class="acc-label">Available Balance</div>
                <div class="acc-balance">Rs. {user['balance']:,}</div>
                <div class="acc-meta">
                    <span>Account Title: <strong>{user['name']}</strong></span>
                    <span>CNIC: <strong>{format_cnic(cnic)}</strong></span>
                </div>
            </div>
            <div class="chip-visual">{WALLET_CHART_SVG}</div>
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
                    badge_cls = "tx-badge-credit" if is_credit else "tx-badge-debit"
                    st.markdown(f"""
                        <div class="tx-row">
                            <div class="tx-left">
                                <div class="tx-badge {badge_cls}">{sign}</div>
                                <div>
                                    <div class="tx-title">{tx['title']}</div>
                                    <div class="tx-date">{tx['time']}</div>
                                </div>
                            </div>
                            <div class="{amt_cls}">{sign} Rs. {tx['amount']:,}</div>
                        </div>
                    """, unsafe_allow_html=True)
