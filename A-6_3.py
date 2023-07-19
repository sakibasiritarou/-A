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
    if x1!=0:
        if x2!=0:
            if y1!=0:
                if y2!=0:
                    canvas.create_line((x1-250)*0.6, (y1-60)*0.6, (x2-250)*0.6, (y2-60)*0.6,fill=color)
        
        
def update_animation():
    global frame
    frame+=1
    # キャンバスをクリア
    canvas.delete("all")
    # JSONファイルのパス
    if(frame>=100):
        return
    file_name = f"kabeposter_0000000000{frame:02d}_keypoints.json"
    json_file_path = os.path.join(folder_path, file_name)

    # JSONファイルを読み込む
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)

    # 2人の人の情報を取得
    persons = data["people"][:2]  # 最初の2人の情報を取得

    for i, person in enumerate(persons):
        keypoints = person["pose_keypoints_2d"]

        # 鼻の座標と信頼度
        nose_x = keypoints[0]
        nose_y = keypoints[1]
        nose_confidence = keypoints[2]

        # 首の座標と信頼度
        neck_x = keypoints[3]
        neck_y = keypoints[4]
        neck_confidence = keypoints[5]

        # 右肩の座標と信頼度
        rkata_x = keypoints[6]
        rkata_y = keypoints[7]
        rkata_confidence = keypoints[8]

        # 右ひじの座標と信頼度
        rh_x = keypoints[9]
        rh_y = keypoints[10]
        rh_confidence = keypoints[11]

        # 右手首の座標と信頼度
        rt_x = keypoints[12]
        rt_y = keypoints[13]
        rt_confidence = keypoints[14]


        # 左肩の座標と信頼度
        lkata_x = keypoints[15]
        lkata_y = keypoints[16]
        lkata_confidence = keypoints[17]

        # 左ひじの座標と信頼度
        lh_x = keypoints[18]
        lh_y = keypoints[19]
        lh_confidence = keypoints[20]

        # 左手首の座標と信頼度
        lt_x = keypoints[21]
        lt_y = keypoints[22]
        lt_confidence = keypoints[23]

        # 腰中央の座標と信頼度
        kt_x = keypoints[24]
        kt_y = keypoints[25]
        kt_confidence = keypoints[26]

        # 右腰の座標と信頼度
        rk_x = keypoints[27]
        rk_y = keypoints[28]
        rk_confidence = keypoints[29]

        # 右ひざの座標と信頼度
        rhi_x = keypoints[30]
        rhi_y = keypoints[31]
        rhi_confidence = keypoints[32]

        # 右足首の座標と信頼度
        ra_x = keypoints[33]
        ra_y = keypoints[34]
        ra_confidence = keypoints[35]

        # 左腰の座標と信頼度
        lk_x = keypoints[36]
        lk_y = keypoints[37]
        lk_confidence = keypoints[38]

        # 左ひざの座標と信頼度
        lhi_x = keypoints[39]
        lhi_y = keypoints[40]
        lhi_confidence = keypoints[41]

        # 左あしくびの座標と信頼度
        la_x = keypoints[42]
        la_y = keypoints[43]
        la_confidence = keypoints[44]

        # 右目の座標と信頼度
        reye_x = keypoints[45]
        reye_y = keypoints[46]
        rye_confidence = keypoints[47]

        # 左目の座標と信頼度
        leye_x = keypoints[48]
        leye_y = keypoints[49]
        lye_confidence = keypoints[50]



        # 右耳の座標と信頼度
        rmimi_x = keypoints[51]
        rmimi_y = keypoints[52]
        rmimi_confidence = keypoints[53]

        # 左耳の座標と信頼度
        lmimi_x = keypoints[54]
        lmimi_y = keypoints[55]
        lmimi_confidence = keypoints[56]

        # 左足親指の座標と信頼度
        lao_x = keypoints[57]
        lao_y = keypoints[58]
        lao_confidence = keypoints[59]

        # 左小指の座標と信頼度
        lak_x = keypoints[60]
        lak_y = keypoints[61]
        lak_confidence = keypoints[62]

        
        # 左かかとの座標と信頼度
        lkaka_x = keypoints[63]
        lkaka_y = keypoints[64]
        lkaka_confidence = keypoints[65]

        # 右親指の座標と信頼度
        rao_x = keypoints[66]
        rao_y = keypoints[67]
        rao_confidence = keypoints[68]

        # 右足小指の座標と信頼度
        rak_x = keypoints[69]
        rak_y = keypoints[70]
        rak_confidence = keypoints[71]

        # 右かかとの座標と信頼度
        rkaka_x = keypoints[72]
        rkaka_y = keypoints[73]
        rkaka_confidence = keypoints[74]


        #肩の描写2-1
        draw_person(rkata_x,rkata_y,neck_x,neck_y,"blue")
        #肩の描写2-3
        draw_person(rkata_x,rkata_y,rh_x,rh_y,"blue")
        #肩の描写4-3
        draw_person(rt_x,rt_y,rh_x,rh_y,"red")
        #肩の描写1-5
        draw_person(neck_x,neck_y,lkata_x,lkata_y,"blue")
        #肩の描写5-6
        draw_person(lkata_x,lkata_y,lh_x,lh_y,"blue")
        #肩の描写6-7
        draw_person(lh_x,lh_y,lt_x,lt_y,"red")
        #肩の描写0-1
        draw_person(nose_x,nose_y,neck_x,neck_y,"red")
        #肩の描写17-15
        draw_person(rmimi_x,rmimi_y,reye_x,reye_y,"red")
        #肩の描写15-0
        draw_person(reye_x,reye_y,nose_x,nose_y,"red")
        #肩の描写0-16
        draw_person(nose_x,nose_y,leye_x,leye_y,"red")
        #肩の描写16-18
        draw_person(leye_x,leye_y,lmimi_x,lmimi_y,"red")
        #肩の描写1-8
        draw_person(neck_x,neck_y,kt_x,kt_y,"red")
        #肩の描写9-8
        draw_person(rk_x,rk_y,kt_x,kt_y,"red")
        #肩の描写8-12
        draw_person(kt_x,kt_y,lk_x,lk_y,"blue")
        #肩の描写9-10
        draw_person(rk_x,rk_y,rhi_x,rhi_y,"red")
        #肩の描写10-11
        draw_person(rhi_x,rhi_y,ra_x,ra_y,"red")
        #肩の描写11-24
        draw_person(ra_x,ra_y,rkaka_x,rkaka_y,"red")
        #肩の描写11-22
        draw_person(ra_x,ra_y,rao_x,rao_y,"red")
        #肩の描写23-22
        draw_person(rak_x,rak_y,rao_x,rao_y,"blue")
        #肩の描写12-13
        draw_person(lk_x,lk_y,lhi_x,lhi_y,"blue")
        print(lhi_x,lhi_y)
        #肩の描写13-14
        draw_person(lhi_x,lhi_y,la_x,la_y,"blue")
        #肩の描写14-21
        draw_person(la_x,la_y,lkaka_x,lkaka_y,"red")
        #肩の描写14-19
        draw_person(la_x,la_y,lao_x,lao_y,"red")
        #肩の描写19-20
        draw_person(lao_x,lao_y,lak_x,lak_y,"red")
    # アニメーションの再更新
    window.after(50, update_animation)

    

# アニメーションの開始
frame = -1
update_animation()
    



# ウィンドウのメインループ
window.mainloop()
