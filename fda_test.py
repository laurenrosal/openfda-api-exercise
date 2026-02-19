import requests

BASE_URL = "https://api.fda.gov/drug/label.json"

def search_drug_labels(brand_name: str, limit: int = 3, skip: int = 0):
    params = {
        "search": f'openfda.brand_name:"{brand_name}"',
        "limit": limit,
        "skip": skip
    }
    r = requests.get(BASE_URL, params=params, timeout=10)

    # openFDA sometimes returns 404 for no matches (or an error payload),
    # so handle non-200 cleanly:
    if r.status_code != 200:
        try:
            err = r.json()
        except Exception:
            err = {"message": r.text}
        return [], err

    data = r.json()
    results = data.get("results", [])
    return results, None

def summarize_label(item: dict) -> dict:
    openfda = item.get("openfda", {})
    # Many fields are lists of strings in openFDA
    def first_text(x):
        if isinstance(x, list) and x:
            return x[0]
        if isinstance(x, str):
            return x
        return None

    return {
        "brand_name": first_text(openfda.get("brand_name")),
        "generic_name": first_text(openfda.get("generic_name")),
        "purpose": first_text(item.get("purpose")),
        "warnings": first_text(item.get("warnings")),
    }

if __name__ == "__main__":
    brand = "Advil"

    # Page 1
    page1, err1 = search_drug_labels(brand, limit=3, skip=0)
    if err1:
        print("Error / Empty:", err1)
    else:
        print("Page 1:")
        for i, item in enumerate(page1, start=1):
            print(i, summarize_label(item))

    # Page 2
    page2, err2 = search_drug_labels(brand, limit=3, skip=3)
    if err2:
        print("Error / Empty:", err2)
    else:
        print("\nPage 2:")
        for i, item in enumerate(page2, start=1):
            print(i, summarize_label(item))

    # Empty test
    empty, err3 = search_drug_labels("THISSHOULDNOTEXIST12345", limit=1, skip=0)
    print("\nEmpty test:")
    print("results length:", len(empty))
    print("err:", err3)
