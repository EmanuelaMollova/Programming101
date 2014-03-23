def slope_style_score(scores):
    score = (sum(scores) - min(scores) - max(scores)) / (len(scores) - 2)
    return int(score * 100) / 100
