
from typing import Union
from routes.state import STATE_CODES
from fastapi import FastAPI
from pydantic import BaseModel
from utils import fetch_cases_for_commission
from typing import Optional

app = FastAPI()

class CaseRequest(BaseModel):
    state: str
    commission: str
    search_val: str
    case_number: Optional[str] = None
    complainant_name:Optional[str] = None
    respondent_name:Optional[str] = None
    complainant_advocate_name:Optional[str] = None
    case_type_name:Optional[str] = None
    commission_type_en:Optional[str] = None


# TO Get All Cases in State 
@app.post("/")
def get_case(req:CaseRequest):
    state = req.state
    commission = req.commission
    search_val = req.search_val

    print(state)
    
    cases = fetch_cases_for_commission(commission,search_val , state)
    return {"cases": cases}

@app.post("/")
def get_case(req:CaseRequest):
    state = req.state
    commission = req.commission
    search_val = req.search_val

    print(state)
    
    cases = fetch_cases_for_commission(commission,search_val , state)
    return {"cases": cases}


# Cases By Case Number 
@app.post("/cases/case-number")
def get_by_caseNumber(req:CaseRequest):

    case_number= req.case_number
    state = req.state
    commission = req.commission
    search_val = req.search_val

    cases = fetch_cases_for_commission(commission,search_val , state)  

    case_list = cases["cases"]
    case_obj = next((c for c in case_list if c.get("case_number") == case_number), None)

    print("case"+ case_number)

    if case_obj:
        return {"case": case_obj}
    else:
        return {"error": "Case not found"}

# Sort Cases By Complaint Name 
@app.post("/cases/complainant_name")
def get_by_complainant_name(req:CaseRequest):

    complainant_name= req.complainant_name
    state = req.state
    commission = req.commission
    search_val = req.search_val

    cases = fetch_cases_for_commission(commission,search_val,state)

    case_list= cases["cases"]
    case_obj = next((c for c in case_list if c.get("complainant_name") == complainant_name), None)

    print("case"+ complainant_name)

    if case_obj:
        return {"case": case_obj}
    else:
        return {"error": "Case not found"}

# Sort Cases By Respondent Name
@app.post("/cases/respondent_name")
def get_by_complainant_name(req:CaseRequest):

    respondent_name= req.respondent_name
    state = req.state
    commission = req.commission
    search_val = req.search_val

    cases = fetch_cases_for_commission(commission,search_val,state)

    case_list= cases["cases"]
    case_obj = next((c for c in case_list if c.get("respondent_name") == respondent_name), None)


    if case_obj:
        return {"case": case_obj}
    else:
        return {"error": "Case not found"}

# Sort Cases By Complaint Advocate
@app.post("/cases/complainant_advocate_name")
def get_by_complainant_name(req:CaseRequest):

    complainant_advocate_name= req.complainant_advocate_name
    state = req.state
    commission = req.commission
    search_val = req.search_val

    cases = fetch_cases_for_commission(commission,search_val,state)

    case_list= cases["cases"]
    case_obj = next((c for c in case_list if c.get("complainant_advocate_name") == complainant_advocate_name), None)


    if case_obj:
        return {"case": case_obj}
    else:
        return {"error": "Case not found"}

# Sort Cases By Case Type/ Industry 
@app.post("/cases/case_type_name")
def get_by_complainant_name(req:CaseRequest):

    case_type_name= req.case_type_name
    state = req.state
    commission = req.commission
    search_val = req.search_val

    cases = fetch_cases_for_commission(commission,search_val,state)

    case_list= cases["cases"]
    case_obj = next((c for c in case_list if c.get("case_type_name") == case_type_name), None)


    if case_obj:
        return {"case": case_obj}
    else:
        return {"error": "Case not found"}


# Sort Cases By Commission Type / Judge
@app.post("/cases/commission_type_en")
def get_by_complainant_name(req:CaseRequest):

    commission_type_en= req.commission_type_en
    state = req.state
    commission = req.commission
    search_val = req.search_val

    cases = fetch_cases_for_commission(commission,search_val,state)

    case_list= cases["cases"]
    case_obj = next((c for c in case_list if c.get("commission_type_en") == commission_type_en), None)


    if case_obj:
        return {"case": case_obj}
    else:
        return {"error": "Case not found"}


