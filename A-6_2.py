import json
import os
import tkinter as tk

# JSONファイルが格納されているフォルダのパス
folder_path = "kabeposter"

# ウィンドウを作成
window = tk.Tk()
window.title("人の図形")
canvas = tk.Canvas(window, width=1000, height=1000, bg="white")
canvas.pack()

def draw_person(x1,y1,x2,y2,color):
    canvas.create_line(x1-300, y1, x2-300, y1,fill=color)

# フォルダ内のJSONファイルを走査
for frame in range(1):
    # JSONファイルのパス
    file_name = f"kabeposter_000000000{frame:03d}_keypoints.json"
    json_file_path = os.path.join(folder_path, file_name)

    # JSONファイルを読み込む
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)

    # 2人の人の情報を取得
    persons = data["people"][:2]  # 最初の2人の情報を取得

    # 0フレーム目の鼻と首の座標を表示
    for i, person in enumerate(persons):
        keypoints = person["pose_keypoints_2d"]

        # 首の座標と信頼度
        neck_x = keypoints[3]
        neck_y = keypoints[4]
        neck_confidence = keypoints[5]

        # 右肩の座標と信頼度
        rkata_x = keypoints[6]
        rkata_y = keypoints[7]
        rkata_confidence = keypoints[8]

        # 右肩の座標と信頼度
        lkata_x = keypoints[15]
        lkata_y = keypoints[16]
        lkata_confidence = keypoints[17]

        # 結果を表示
        draw_person(rkata_x,rkata_y,neck_x,neck_y,"blue")
        draw_person(neck_x,neck_y,lkata_x,lkata_y,"red")

# ウィンドウのメインループ
window.mainloop()
        
        
