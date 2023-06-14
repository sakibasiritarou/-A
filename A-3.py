import zipfile

# sample.zipを解凍
with zipfile.ZipFile('sample.zip', 'r') as zip_ref:
    zip_ref.extractall('sample')

file_sum = 0

# ファイルごとに処理
for i in range(10000):
    file_name = f'kitamura_{str(i).zfill(5)}_kug.txt'
    
    # ファイル名の数字が奇数の場合のみ処理
    if i % 2 != 0:
        file_path = f'sample\{file_name}'
        
        # ファイルを開いて数字を読み取り、合計に加算
        with open(file_path, 'r') as file:
            number = int(file.read())
            file_sum += number

print("奇数ファイルの数字の合計:", file_sum)
