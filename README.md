## 🎥 Demo Video
https://youtu.be/_CsxOXUDYhc


📑 District Consumer Court Case Tracker (FastAPI)
📌 Introduction

  This project is a FastAPI backend that fetches case data directly from the Jagriti portal (https://e-jagriti.gov.in
  ) for District Consumer Courts (DCDRC).
  
  The backend replicates Jagriti’s search flow:
  
      Accepts state name, commission name, and search value as inputs.
      
      Maps them to internal IDs required by Jagriti’s backend.
      
      Fetches and formats case data into a clean JSON response.
      
      Supports multiple search endpoints like by-case-number, by-complainant, by-respondent, etc.
      
      Provides supporting endpoints for states and commissions.
      
      Restricts results to Daily Orders and defaults to Case Filing Date filtering.

⚡ Tech Stack

      Language: Python 3.10+
      
      Framework: FastAPI
      
      Server: Uvicorn
      
      Data Handling: Custom scraper/parser for Jagriti API responses



⚙️ Local Setup


1. Clone the repository
        git clone https://github.com/<your-username>/district-court-tracker.git
        cd district-court-tracker


2. Create & activate a virtual environment
        python -m venv .venv
        source .venv/bin/activate   # Linux/Mac
        .venv\Scripts\activate      # Windows


3. Install dependencies

    Option A – Install from requirements.txt
    
    pip install -r requirements.txt


    Option B – Install manually (recommended for local setup)(RECOMMENDED)
    
    pip install "fastapi[standard]"
    pip install uvicorn
    pip install httpx beautifulsoup4 lxml


4. Run the server
    uvicorn main:app --reload

🚀 API Endpoints
🔹 Supporting Endpoints

    GET /states → Returns list of states with their internal IDs.
    
    GET /commissions/{state_id} → Returns commissions for a given state.

🔹 Case Search Endpoints

    Each accepts JSON body or query params:
    
    {
      "state": "KARNATAKA",
      "commission": "Bangalore 1st & Rural Additional",
      "search_value": "Reddy"
    }


Available routes:
      
      POST /cases/by-case-number
      
      POST /cases/by-complainant
      
      POST /cases/by-respondent
      
      POST /cases/by-complainant-advocate
      
      POST /cases/by-respondent-advocate
      
      POST /cases/by-industry-type
      
      POST /cases/by-judge


📊 Features

      Fetches real-time case data from Jagriti (no mock data).
      
      Provides state & commission mapping endpoints.
      
      Restricts results to Daily Orders.
      
      Defaults to Case Filing Date filtering.
      
      Supports sorting & filtering (custom enhancements added).
      
      Separation of concerns: routes, models, and services are cleanly organized.

🛠️ Development Notes

      Inspect Jagriti portal network requests to extract correct state/commission IDs.
      
      Handle Captcha gracefully if required.
      
      Extendable for other courts/commissions in future.



