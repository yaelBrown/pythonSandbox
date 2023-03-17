def anagram(s1, s2):
    if len(s1) == 0 or len(s2) == 0 or len(s1) != len(s2):
        return False
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    mem = set()

    for c in s1:
        if c in mem:
            continue
        else:
            mem.add(c)
            if c in s2:
                continue
            else:
                return False

    return True


ans1 = anagram('dog', 'god')

ans2 = anagram('aa', 'AA')

print(ans1, ans2)
