import requests

BASE_URL = "https://api.fda.gov/drug/label.json"

def first(value):
    if isinstance(value, list) and value:
        return value[0]
    return value

def fetch_labels(brand, limit=3, skip=0):
    params = {
        "search": f"openfda.brand_name:({brand})",
        "limit": limit,
        "skip": skip
    }

    res = requests.get(BASE_URL, params=params, timeout=10)

    if res.status_code != 200:
        try:
            return [], res.json()
        except Exception:
            return [], {"message": res.text}

    return res.json().get("results", []), None

def print_results(title, results):
    print(title)
    for i, item in enumerate(results, start=1):
        openfda = item.get("openfda", {})
        print(i, {
            "brand_name": first(openfda.get("brand_name")),
            "generic_name": first(openfda.get("generic_name")),
            "purpose": first(item.get("purpose")),
            "warnings": first(item.get("warnings")),
        })

if __name__ == "__main__":
    brand = "Advil"

    results, err = fetch_labels(brand, limit=3, skip=0)
    if err:
        print("Error / Empty:", err)
    else:
        print_results("Page 1:", results)

    results, err = fetch_labels(brand, limit=3, skip=3)
    if err:
        print("Error / Empty:", err)
    else:
        print_results("\nPage 2:", results)

    results, err = fetch_labels("THISSHOULDNOTEXIST12345", limit=1, skip=0)
    print("\nEmpty test:")
    print("results length:", len(results))
    print("err:", err)