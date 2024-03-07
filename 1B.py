f = list(map(int, input().split(':')))
s = list(map(int, input().split(':')))
host = int(input())


def sol(f, s, host):
    FRoundFcommand, FRoundScommand, SRoundFcommand, SRoundScommand = f[0], f[1], s[0], s[1]
    FGoals, SGoals = FRoundFcommand + SRoundFcommand, FRoundScommand + SRoundScommand
    delta = SGoals - FGoals
    ans = 0
    if host == 1:
        if FGoals <= SGoals:
            ans += delta
            SRoundFcommand += delta
            if SRoundFcommand <= FRoundScommand:
                return ans + 1
            else:
                return ans
        else:
            return 0
    else:
        if FGoals <= SGoals:
            ans += delta
            if FRoundFcommand <= SRoundScommand:
                return ans + 1
            else:
                return ans
        else:
            return 0


print(sol(f, s, host))