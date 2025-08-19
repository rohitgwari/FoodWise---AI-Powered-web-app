
import streamlit as st
import pandas as pd
import math

st.set_page_config(page_title="FoodWise", page_icon="🍲", layout="wide")

# ---------------------- THEME / STYLE ----------------------
st.markdown(
    """
    <style>
    .foodwise-hero h1 { color:#FF6F61; font-size: 3rem; margin-bottom:0; }
    .foodwise-hero h3 { color:#22C55E; font-weight:600; margin-top:0.25rem; }
    .foodwise-hero p { font-size:1.05rem; opacity:0.9; }
    .stButton>button {
        background:#FF6F61; color:white; border-radius:12px; padding:0.6rem 1rem;
        border:0; font-weight:600;
    }
    .stTextInput>div>div>input, .stNumberInput>div>div>input, textarea {
        border:2px solid #22C55E; border-radius:10px;
    }
    .pill { display:inline-block; padding:6px 10px; border-radius:999px; background:#F1F5F9; margin-right:8px; font-size:0.85rem;}
    </style>
    """, unsafe_allow_html=True
)

# ---------------------- HEADER ----------------------
st.markdown('<div class="foodwise-hero" style="text-align:center; padding: 10px 0 20px 0;">'
            '<h1>🍲 FoodWise</h1>'
            '<h3>AI‑Powered Food Waste Reduction & Sharing</h3>'
            '<p>Turn leftovers into recipes, plan meals precisely, and share surplus with your community.</p>'
            '</div>', unsafe_allow_html=True)

# ---------------------- NAV TABS ----------------------
tabs = st.tabs(["🏠 Home", "🥘 Recipes", "📅 Planner", "🤝 Sharing Hub"])

# ---------------------- HOME ----------------------
with tabs[0]:
    c1, c2 = st.columns([1,1])
    with c1:
        st.subheader("Why FoodWise?")
        st.write("- Many people overcook or leave ingredients unused.\n"
                 "- FoodWise helps convert leftovers into meals, estimate portions, and share surplus easily.")
        st.subheader("Key Features")
        st.markdown("• **Leftover Recipe Generator**\n\n"
                    "• **Smart Food Planner**\n\n"
                    "• **Food Sharing Hub**")
        st.caption("Built with Streamlit · SQLite · Optional APIs (Spoonacular/Edamam, Maps)")
    with c2:
        st.markdown("**Quick Start**")
        ingredients_quick = st.text_input("Enter leftovers (comma-separated)", key="home_ing")
        if st.button("Suggest 3 recipes", key="home_btn"):
            if ingredients_quick.strip():
                items = [x.strip() for x in ingredients_quick.split(",") if x.strip()]
                base = items[:3] if items else ["mixed veggies"]
                st.success("Here are some ideas:")
                st.write(f"1) {base[0].title()} Stir‑Fry")
                st.write(f"2) {base[0].title()} & {base[-1].title()} Fried Rice" if len(base)>1 else "2) Veggie Fried Rice")
                st.write(f"3) Hearty {base[0].title()} Soup")
            else:
                st.warning("Please enter at least one ingredient.")

# ---------------------- RECIPES ----------------------
with tabs[1]:
    st.subheader("Leftover Recipe Generator")
    c1, c2 = st.columns([2,1])
    with c1:
        ingredients = st.text_input("📝 Ingredients (comma-separated)", key="rec_ing")
        diet = st.selectbox("Diet preference", ["Any", "Vegetarian", "Vegan", "Egg‑free"])
        time_limit = st.slider("Max cooking time (minutes)", 10, 120, 30)
        difficulty = st.select_slider("Difficulty", ["Easy", "Medium", "Hard"], value="Easy")
        if st.button("🔍 Generate Recipes", key="rec_btn"):
            if ingredients.strip():
                items = [x.strip() for x in ingredients.split(",") if x.strip()]
                base = items[:2] if items else ["veggies"]
                tag = "" if diet=="Any" else f" · {diet}"
                st.success("Suggested recipes")
                st.markdown(f"- **{base[0].title()} Quick Stir‑Fry** ({difficulty}{tag}, ≤{time_limit}m)")
                st.markdown(f"- **{base[0].title()} {base[-1].title()} Wraps** ({difficulty}{tag}, ≤{time_limit}m)")
                st.markdown(f"- **{base[0].title()} One‑Pot Soup** ({difficulty}{tag}, ≤{time_limit}m)")
            else:
                st.warning("Enter at least one ingredient.")
    with c2:
        st.info("Tip: You can later plug an API (e.g., Spoonacular) or an LLM to fetch real recipes.")

# ---------------------- PLANNER ----------------------
with tabs[2]:
    st.subheader("Smart Food Planner")
    st.caption("Estimate ingredient quantities based on number of people.")
    dish = st.text_input("Dish name", value="Veg Fried Rice")
    people = st.number_input("Number of people", 1, 100, 4, step=1)
    # Simple baseline per‑person grams (demo values)
    baseline = {
        "rice (g)": 90, "mixed veggies (g)": 120, "oil (tbsp)": 0.75, "spices (tsp)": 1.0, "salt (tsp)": 0.5
    }
    if st.button("Calculate quantities", key="plan_btn"):
        rows = []
        for k, v in baseline.items():
            qty = v * people
            rows.append({"ingredient": k, "per_person": v, "total_for_group": round(qty, 2)})
        df = pd.DataFrame(rows)
        st.write(f"**Plan for:** {people} people · **Dish:** {dish}")
        st.dataframe(df, use_container_width=True)
        st.caption("Adjust baseline amounts as needed for your recipes.")

# ---------------------- SHARING HUB ----------------------
with tabs[3]:
    st.subheader("Share, Sell, or Donate Surplus")
    mode = st.radio("Action", ["Donate", "Sell"], horizontal=True)
    colA, colB = st.columns(2)
    with colA:
        item = st.text_input("Item name", value="Cooked rice (sealed)")
        qty = st.text_input("Quantity / units", value="2 boxes")
        location = st.text_input("Location / Area", value="Campus Block A")
        contact = st.text_input("Contact (phone/email)", value="example@iitj.ac.in")
    with colB:
        notes = st.text_area("Notes (expiry, dietary info)")
        price = None
        if mode == "Sell":
            price = st.number_input("Price (₹)", min_value=0, value=50, step=5)
    if "shared_items" not in st.session_state:
        st.session_state.shared_items = []

    if st.button("Add listing", key="share_btn"):
        st.session_state.shared_items.append({
            "mode": mode, "item": item, "qty": qty, "location": location,
            "contact": contact, "price": price if mode=="Sell" else "—", "notes": notes
        })
        st.success("Listing added ✅")

    if st.session_state.shared_items:
        st.write("### Current Listings")
        st.dataframe(pd.DataFrame(st.session_state.shared_items), use_container_width=True)
        st.caption("For production, save to a database (e.g., SQLite/Google Sheet) and add maps/filters.")
