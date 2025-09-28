import requests
from typing import Dict, Any
from routes.state import STATE_CODES

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}

def fetch_cases_for_commission(commission_id: str, search_val: str, state:str) -> Dict[str, Any]:

    code =  STATE_CODES.get(state)
    if code is None or code == "":
        print("Code not found!")
        return {"error": "Code not found! Check the State"} 
    
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
            }
    
    response = requests.get(f"https://e-jagriti.gov.in/services/report/report/getDistrictCommissionByCommissionId?commissionId={code}",headers=headers)

    if response.status_code != 200:
        return {"error": f"API returned status  {response.status_code}"}
        
    try:
        data = response.json()
    except ValueError:
        return {"error": "API did not return valid JSON", "raw_response": response.text}
    
    commission_list = data.get("data", [])
    commission_name = commission_id

    commission_obj = next(
        (c for c in commission_list if c["commissionNameEn"] == commission_name),None
        )

    if commission_obj:
        commissionId = commission_obj["commissionId"]
        search = search_val
        case_response = requests.get(
            f"https://e-jagriti.gov.in/services/report/report/getCauseTitleListByCompany?commissionTypeId=3&commissionId={commissionId}&filingDate1=2025-01-01&filingDate2=2025-09-27&complainant_respondent_name_en={search}",
        headers=headers
    )

    if case_response.status_code != 200:
        return {"error": f"API returned status {case_response.status_code}"}

    try:
        case_data = case_response.json()
    except ValueError:
        return {"error": "Second API did not return valid JSON", "raw_response": case_response.text}

    return {"cases": case_data}
    
