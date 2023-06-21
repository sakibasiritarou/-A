import tkinter as tk

# ウィンドウを作成
window = tk.Tk()
window.title("人の図形")

# キャンバスを作成
canvas = tk.Canvas(window, width=600, height=600, bg="white")
canvas.pack()

# 人の図形を描画する関数
def draw_person(x):
    # 頭
    canvas.create_oval(50 + x, 50, 150 + x, 150)

    # 体
    canvas.create_line(100 + x, 150, 100 + x, 250)

    # 左腕
    canvas.create_line(100 + x, 170, 50 + x, 220)


    # 右腕

    canvas.create_line(100 + x, 170, 150 + x, 220)

    # 左足
    canvas.create_line(100 + x, 250, 50 + x, 300)
  

    # 右足
    
    canvas.create_line(100 + x, 250, 150 + x, 300)

# アニメーションの更新処理
def update_animation():
    global x_pos
    x_pos += 5  # 移動速度を調整する場合は値を変更してください

    # キャンバスをクリア
    canvas.delete("all")

    # 人の図形を描画
    draw_person(x_pos)

    # アニメーションの再更新
    window.after(50, update_animation)

# アニメーションの開始
x_pos = 0
update_animation()

# ウィンドウのメインループ
window.mainloop()
