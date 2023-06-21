import tkinter as tk

# ウィンドウを作成
window = tk.Tk()
window.title("人の図形")

# キャンバスを作成
canvas = tk.Canvas(window, width=600, height=600, bg="white")
canvas.pack()

# 人の図形を描画する関数
def draw_person():
    # 頭
    canvas.create_oval(50, 50, 150, 150)

    # 体
    canvas.create_line(100, 150, 100, 250)

    # 左腕
    canvas.create_line(100, 170, 50, 220)


    # 右腕

    canvas.create_line(100, 170, 150, 220)

    # 左足
    canvas.create_line(100, 250, 50, 300)


    # 右足

    canvas.create_line(100, 250, 150, 300)

# 人の図形を描画
draw_person()

# ウィンドウのメインループ
window.mainloop()
