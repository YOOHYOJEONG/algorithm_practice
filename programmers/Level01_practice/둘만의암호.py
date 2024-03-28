# -*- coding: utf-8 -*-

# 프로그래머스
# level01
# 연습문제
# 둘만의 암호


# 4개 / 19개 통과
def solution1(s, skip, index):
    
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphabet_num = {key: i for i, key in enumerate(alphabets)}
    
    answer = []
    for i in range(len(s)):
        s_index = alphabet_num[s[i]]
        print('orign : ', s_index)

        next_range = []
        for j in range(index):
            next_num = s_index + j + 1
            if next_num <= len(alphabets)-1:
                next_range.append(alphabets[next_num])
            
            elif next_num > len(alphabets)-1:
                next_range.append(alphabets[next_num - len(alphabets)])

        cnt = 0
        for k in next_range:
            if k in skip:
                cnt += 1

        last_num = alphabet_num[next_range[-1]]
        if last_num + cnt <= len(alphabets)-1:
            new_alphabet = alphabets[last_num + cnt]
        elif last_num + cnt > len(alphabets)-1:
            new_alphabet = alphabets[last_num + cnt - len(alphabets)]

        answer.append(new_alphabet)

    return ''.join(answer)


def solution(s, skip, index):
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for skip_ in skip:
        if skip_ in alphabets:
            alphabets.remove(skip_)

    answer = []
    for s_ in s:
        answer.append(alphabets[(alphabets.index(s_)+index) % len(alphabets)])
    
    return ''.join(answer)

answer = solution("aukks", "wbqd", 5)
print(answer)