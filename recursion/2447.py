n = int(input())
star = ["***", "* *", "***"]
cnt = 0


def getStars(star):
    mat = []
    for i in range(3 * len(star)):
        if i // len(star) == 1: # 각 행을 3^n 으로 나누었을 때 몫이 1이라면 비어있다.
            mat.append(star[i % len(star)] + " " * len(star) + star[i % len(star)])
        else:
            mat.append(star[i % len(star)] * 3)
    return mat


while n > 3:
    n /= 3
    cnt += 1

for i in range(cnt):
    star = getStars(star)

for i in star:
    print(i)