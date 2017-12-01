def captcha_solution_v1(captcha):
    total = 0
    for i in range(len(captcha)):
        if captcha[i] == captcha[(i + 1) % len(captcha)]:
            total += int(captcha[i])
    return total


def captcha_solution_v2(captcha):
    total = 0
    for i in range(len(captcha)):
        if captcha[i] == captcha[(i + (len(captcha) // 2)) % len(captcha)]:
            total += int(captcha[i])
    return total

if __name__ == '__main__':
    with open('day01_input.txt') as file:
        day01_input = file.read().strip()

    print(captcha_solution_v1(day01_input))
    print(captcha_solution_v2(day01_input))
