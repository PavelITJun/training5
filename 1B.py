f = list(map(int, input().split(':')))
s = list(map(int, input().split(':')))
h = int(input())


def sol(f, s, h):
    FRoundFcommand, FRoundScommand, SRoundFcommand, SRoundScommand = f[0], f[1], s[0], s[1]
    FGoals, SGoals = FRoundFcommand + SRoundFcommand, FRoundScommand + SRoundScommand
    if SGoals < FGoals:
        return 0
    else:
        sup = SGoals - FGoals
        if h == 1:
            if sup + SRoundFcommand <= SRoundScommand:
                return sup + 1
            else:
                return sup
        else:
            return sup + 1


print(sol(f, s, h))