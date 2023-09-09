import tkinter as tk

# 創建主視窗
root = tk.Tk()
root.title("聊天軟體")

# 創建對話框
chat_box = tk.Text(root, height=20, width=50)
chat_box.pack()

# 創建輸入框
input_box = tk.Entry(root, width=50)
input_box.pack()

# 創建發送按鈕
def send_message():
    message = input_box.get()
    chat_box.insert(tk.END, "我： " + message + "\n")
    input_box.delete(0, tk.END)

send_button = tk.Button(root, text="發送", command=send_message)
send_button.pack()

# 創建接收訊息的函數
def receive_message(message):
    chat_box.insert(tk.END, "對方： " + message + "\n")

# 模擬收到訊息
receive_message("你好，這是一個聊天軟體")

# 開始執行主視窗
root.mainloop()
