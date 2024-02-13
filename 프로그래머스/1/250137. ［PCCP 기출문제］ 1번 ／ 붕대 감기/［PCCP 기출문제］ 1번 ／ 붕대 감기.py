def solution(bandage, health, attacks):
    answer = 0

    start = 0
    now = 0
    cur_heal = health

    a_idx = 0
    time, damage = attacks[a_idx]

    while True:
        now += 1
        if now == time:
            cur_heal -= damage
            if cur_heal <= 0: return -1
            a_idx += 1
            if a_idx == len(attacks):
                return cur_heal
            time, damage = attacks[a_idx]
            start = now

        else:
            cur_heal = min(health, cur_heal + bandage[1])
            if now - start == bandage[0]:
                cur_heal = min(health, cur_heal + bandage[2])
                start = now