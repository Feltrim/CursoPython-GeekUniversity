def dentroRet(v1, v2, p):
    if v1.x <= p.x <= v2.x and v1.y <= p.y <= v2.y:
        return 1
    else:
        return 0
