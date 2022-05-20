def solution(names):
    if len(names) == 0:
        return []

    seen = {}
    result = []
    for name in names:
        if name in seen.keys():
            # this was the missing piece! i needed a while-loop so i didn't have to keep nesting
            while f"{name}({seen[name]})" in seen.keys():
                seen[name] += 1
            seen[f"{name}({seen[name]})"] = 1
            result.append(f"{name}({seen[name]})")
            seen[name] += 1
        else:
            result.append(name)
            seen.update({name: 1})

    return result


if __name__ == "__main__":
    print(solution(["a", "a(1)", "a(6)", "a", "a", "a", "a", "a", "a", "a", "a", "a"]))
    print(solution(["a(1)", "a(1)", "a(1)", "a(1)", "a(1)"]))
    print(solution(["a", "a(1)", "a(2)", "a(3)", "a"]))
