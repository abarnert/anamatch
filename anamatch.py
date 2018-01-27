#!/usr/bin/env python3

import itertools

def fit(pattern, letters):
    it = iter(letters)
    return ''.join(p if p not in ' _.' else next(it) for p in pattern)

def ana(pattern, leftover):
    missing = sum(p in ' _.' for p in pattern)
    for r in range(missing, missing+1):
        for perm in itertools.permutations(leftover, r):
            yield fit(pattern, perm)

if __name__ == '__main__':
    import collections
    import sys
    with open('/usr/share/dict/words') as f:
        words = {line.strip().lower() for line in f}
    if len(sys.argv) == 3:
        print(*sorted(words.intersection(ana(sys.argv[1], sys.argv[2]))))
        sys.exit(0)
    while True:
        try:
            print('Letters: ', end='')
            letters = input().strip()
            if not letters:
                break
            letters = collections.Counter(letters)
            while True:
                print('Pattern: ', end='')
                pattern = input().strip()
                if not pattern:
                    break
                pattern = collections.Counter(pattern)
                leftover = letters - pattern
                print(*sorted(words.intersection(ana(list(pattern.elements()),
                                                     list(leftover.elements())))))
        except Exception as e:
            print('{}: {}'.format(type(e).__name__, e))
