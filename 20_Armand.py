arr = [0 for element in range(100)]
arr[0] = 1
for i in range(1, 101):
    carry = 0
    for j in range(len(arr)):
        cur_dub = arr[j]
        cur_dub = cur_dub * i + carry
        carry = 0
        if len(str(cur_dub)) > 10:
            carry = int(cur_dub / 10000000000)
            cur_dub = cur_dub % 10000000000
        arr[j] = cur_dub
print(arr)
s = 0
for i in range(len(arr)):
    char_num = str(arr[i])
    for j in range(len(char_num)):
        s = s + int(char_num[j])
print(s)