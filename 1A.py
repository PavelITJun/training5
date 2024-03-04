PV = list(map(int, input().split()))
QM = list(map(int, input().split()))


def sol(PV, QM):
    pos_boy, dist_boy, pos_girl, dist_girl = PV[0], PV[1], QM[0], QM[1]
    unused = abs(pos_boy - pos_girl) - dist_boy - dist_girl
    if unused > 0:
        return (dist_boy + dist_girl) * 2 + 2
    else:
        min_boy, max_boy, min_girl, max_girl = pos_boy-dist_boy, pos_boy+dist_boy, pos_girl-dist_girl, pos_girl+dist_girl
        return max(max_boy, max_girl) - min(min_boy, min_girl) + 1


print(sol(PV, QM))