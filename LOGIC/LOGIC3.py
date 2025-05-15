def QAteam(n, k):
    """
    :param n: 人數
    :param k: 報數的間隔（題目為 3）
    :return: 最後留下的人的位置（從 1 開始計數）
    """
    people = list(range(1, n + 1))  # 初始人員列表
    index = 0  # 從第一個人開始

    while len(people) > 1:
        index = (index + k - 1) % len(people)  # 計算需要移除的人索引
        people.pop(index)  # 移除該人

    return people[0]  # 剩下的最後一個人

# 測試程式
if __name__ == "__main__":
    n = int(input("請輸入總人數："))
    k = 3  
    result = QAteam(n, k)
    print(f"最後留下的人是原本第 {result} 順位的人。")