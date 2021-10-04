def clear_int(n: str):
    ans = []
    for i in n:
        if i.isdigit():
            ans.append(i)
    return "".join(ans)
