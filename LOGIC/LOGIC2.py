# 原始字串
text = "Hello welcome to Cathay 60th year anniversary"

# 初始化計數字典
counter = {}

# 遍歷每個字元
for char in text:
    # 將字元轉為小寫，檢查是否為數字或字母
    if char.isalnum():
        char = char.lower()
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

# 按照鍵盤進行排序
sorted_counter = {k: counter[k] for k in sorted(counter)}

print(sorted_counter)

# 排版的版本
# 原始字串
text = "Hello welcome to Cathay 60th year anniversary"

# 初始化計數字典
counter = {}

# 遍歷所有字元
for char in text:
    # 將字元轉為小寫，檢查是否為數字或字母
    if char.isalnum():
        char = char.lower()
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

# 按照鍵盤進行排序
sorted_counter = {k: counter[k] for k in sorted(counter)}

# 排列輸出
for char, count in sorted_counter.items():
    print(f"{char}, {count}")