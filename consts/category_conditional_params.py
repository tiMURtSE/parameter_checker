CATEGORY_CONDITIONAL_PARAMS = {
    "люстры": [
        "размер",
        "внешний вид"
        "цоколь"
    ]
}

CONDITIONS = {
    
}

def condition(required_params):
    DIAM = "ol:422"
    VIS = "ol:32"
    DL = "ol:22"

    diametr = [param for param in required_params if param["name"] == DIAM][0]
    visota = [param for param in required_params if param["name"] == VIS][0]
    dlina = [param for param in required_params if param["name"]] == DL[0]
    print(diametr)
    print(visota)
    print(dlina)

    # Всем проставить is_conditional: True

    if diametr["value"]:
        visota["is_required"] = False
        dlina["is_required"] = False
    elif visota["value"] and dlina["value"]:
        diametr["is_required"] = False

    return required_params
