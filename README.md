## FoodWise – AI-Powered Food Waste Reduction & Sharing Platform
#### Problem Statement

Every day, households, hostels, and restaurants throw away large amounts of edible food — either because they overestimated the quantity needed, or they didn’t know what to do with leftovers.
This leads to food waste, economic loss, and hunger in communities.

#### Solution Overview

FoodWise is an AI-driven web app that helps users minimize food waste by:

### Leftover Recipe Generator – Suggests creative recipes using available leftover ingredients.

### Smart Food Planner – Calculates the right ingredient quantities based on the number of people, reducing overcooking.

### Food Sharing Hub – Connects people with surplus food to neighbors, NGOs, or communities, with options for donation or discount selling.

#### Key Features
#### 1. Leftover Recipe Generator

Input ingredients manually or via voice/text.

AI/Recipe API recommends possible dishes.

Filters by time, diet (veg/vegan/etc.), and difficulty.

#### 2. Smart Food Planner

Input dish + number of people.

AI/logic estimates exact ingredient quantities.

Generates shopping lists with precise amounts.

#### 3. Food Sharing Hub

Sell sealed ingredient packs at discounts.

Donate opened but safe food to NGOs/communities.

Location-based matching via Google Maps API / Folium.

Optional: Assign delivery to local volunteers or delivery partners.

#### Tech Stack

Frontend/UI: Streamlit (clean UI with tabs and forms)

State Management: st.session_state for storing data during a session

#### Libraries:

pandas → for ingredient calculations and displaying tables

math (minor use for calculations)

#### Impact

 Households: Save money and reduce food waste by turning leftovers into new meals.

 Communities: Enable easy sharing of surplus food with neighbors or peers.

 Environment: Reduce landfill waste and promote sustainability through mindful cooking and sharing.


