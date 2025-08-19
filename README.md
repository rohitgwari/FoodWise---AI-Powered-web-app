FoodWise – AI-Powered Food Waste Reduction & Sharing Platform
📌 Problem Statement

Every day, households, hostels, and restaurants throw away large amounts of edible food — either because they overestimated the quantity needed, or they didn’t know what to do with leftovers.
This leads to food waste, economic loss, and hunger in communities.

💡 Solution Overview

FoodWise is an AI-driven web app that helps users minimize food waste by:

🥘 Leftover Recipe Generator – Suggests creative recipes using available leftover ingredients.

📅 Smart Food Planner – Calculates the right ingredient quantities based on the number of people, reducing overcooking.

🤝 Food Sharing Hub – Connects people with surplus food to neighbors, NGOs, or communities, with options for donation or discount selling.

🔑 Key Features
1. Leftover Recipe Generator

Input ingredients manually or via voice/text.

AI/Recipe API recommends possible dishes.

Filters by time, diet (veg/vegan/etc.), and difficulty.

2. Smart Food Planner

Input dish + number of people.

AI/logic estimates exact ingredient quantities.

Generates shopping lists with precise amounts.

3. Food Sharing Hub

Sell sealed ingredient packs at discounts.

Donate opened but safe food to NGOs/communities.

Location-based matching via Google Maps API / Folium.

Optional: Assign delivery to local volunteers or delivery partners.

⚙️ Tech Stack

Frontend/UI: Streamlit (quick build, clean UI)

Backend/Database: SQLite for user & food data

APIs: Spoonacular/Edamam (recipes), Google Maps API (location matching)

AI Components:

NLP ingredient matching for recipe search

Quantity estimation algorithm for food planning

🌍 Impact

🏠 Households: Save money, reduce waste

👨‍👩‍👧‍👦 Communities: Connect surplus food with those in need

🌱 Environment: Lower food wastage & landfill load

🚀 Getting Started
1. Clone Repository
git clone https://github.com/your-username/FoodWise.git
cd FoodWise

2. Install Dependencies
pip install -r requirements.txt

3. Run App
streamlit run FoodWise.py
