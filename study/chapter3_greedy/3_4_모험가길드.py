"""
모험가 길드
"""

n = int(input())
fears = list(map(int, input().split()))
fears.sort()

party_count = 0
party = 0

# 30분내에 못 풀다가 해답 봐버림
for fear in fears:
    party_count += 1

    if party_count >= fear:
        party += 1
        party_count = 0

print(party)
