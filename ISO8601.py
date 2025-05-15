import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timezone
import pyperclip  # 用於複製文字

def calculate_date_formats():
    try:
        # 讀取使用者輸入的日期
        date_str = entry_date.get()
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")

        # 計算 UTC 日期時間
        utc_time = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")

        # 週數計算
        year, week_num, week_day = date_obj.isocalendar()
        week_str = f"{year}-W{week_num}"

        # 日期與週數的格式
        week_day_number = date_obj.weekday() + 1  # ISO 週的天數 (星期一為 1，星期日為 7)
        week_with_day = f"{year}-W{week_num}-{week_day_number}"

        # 無年份的日期格式
        no_year_date = f"--{date_obj.strftime('%m-%d')}"

        # 當年累積日數
        start_of_year = datetime(date_obj.year, 1, 1)
        day_of_year = (date_obj - start_of_year).days + 1
        accumulated_day = f"{date_obj.year}-{day_of_year:03d}"

        # 設定結果到 Text 區域
        result_text = f"""日期: {date_str}
UTC 日期與時間: {utc_time}
週數: {week_str}
日期與週數: {week_with_day}
無年份標示之日期: {no_year_date}
當年度累積日數: {accumulated_day}
"""
        text_result.config(state=tk.NORMAL)  # 允許寫入
        text_result.delete("1.0", tk.END)  # 清除舊內容
        text_result.insert(tk.END, result_text)  # 插入新內容
        text_result.config(state=tk.DISABLED)  # 設為唯讀

    except ValueError:
        messagebox.showerror("錯誤", "請輸入正確的日期格式 (YYYY-MM-DD)")

def copy_to_clipboard():
    text = text_result.get("1.0", tk.END).strip()  # 取得所有內容
    pyperclip.copy(text)
    messagebox.showinfo("複製成功", "結果已複製到剪貼簿")

# 創建 GUI 介面
root = tk.Tk()
root.title("日期格式轉換器")

# 輸入框
tk.Label(root, text="請輸入日期 (YYYY-MM-DD):").pack()
entry_date = tk.Entry(root)
entry_date.pack()

# 按鈕
tk.Button(root, text="計算", command=calculate_date_formats).pack()

# 顯示結果的 Text 區域（可複製）
text_result = tk.Text(root, height=8, width=50, wrap=tk.WORD)
text_result.pack()
text_result.config(state=tk.DISABLED)  # 預設為唯讀

# 複製按鈕
tk.Button(root, text="複製結果", command=copy_to_clipboard).pack()

# 運行主迴圈
root.mainloop()
