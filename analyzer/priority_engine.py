def assign_priority(score):
    
    if score >= 80:
        return "★★★★★ Must Download"

    elif score >= 60:
        return "★★★★ Highly Recommended"

    elif score >= 40:
        return "★★★ Good"

    elif score >= 20:
        return "★★ Maybe"

    else:
        return "Skip"