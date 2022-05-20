def solution(names):
    if len(names) == 0:
        return []

    seen = {}
    result = []
    for name in names:
        if name in seen.keys():
            while f"{name}({seen[name]})" in seen.keys:
                seen[name] += 1
            new_name = f"{name}({seen[name]})"
            if new_name in seen.keys():
                seen[name] += 1
                new_name = f"{name}({seen[name]})"
            result.append(new_name)
            seen[name] += 1
            seen.update({new_name: 1})
        else:
            result.append(name)
            seen.update({name: 1})

    return result


if __name__ == "__main__":
    print(solution(["a", "a(1)", "a(6)", "a", "a", "a", "a", "a", "a", "a", "a", "a"]))
    print(solution(["a(1)", "a(1)", "a(1)", "a(1)", "a(1)"]))
