import json
import os

# JSONファイルが格納されているフォルダのパス
folder_path = "kabeposter"

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

        # 鼻の座標と信頼度
        nose_x = keypoints[0]
        nose_y = keypoints[1]
        nose_confidence = keypoints[2]

        # 首の座標と信頼度
        neck_x = keypoints[3]
        neck_y = keypoints[4]
        neck_confidence = keypoints[5]

        # 結果を表示
        print(f"Frame {frame} - Person {i+1}:")
        print(f"Nose: X={nose_x}, Y={nose_y}, Confidence={nose_confidence}")
        print(f"Neck: X={neck_x}, Y={neck_y}, Confidence={neck_confidence}")
        print()
