import os
import shutil


def divide_list(list, j):
    for i in range(0, len(list), j):
        yield list[i:i + j]


def file_moves():
    oPath = '/Volumes/GoogleDrive/공유 드라이브/450.AI데이터/100.학습용데이터/100.실내이미지 학습용 이미지/레나'
    nPath = '/Volumes/GoogleDrive/공유 드라이브/450.AI데이터/100.학습용데이터/100.실내이미지 학습용 이미지/레나/원본이미지'
    file_list = os.listdir(oPath)

    mov_files = []

    # jpg파일들만 배열안에 담음(이동대상)
    for file in file_list:
        if file.endswith(".jpg"):
            print("jpg file : " + file)
            mov_files.append(file)

    slicing_mov_files = list(divide_list(mov_files, 1000))  # 1000개씩 나눔

    print('총 파일갯수' + str(len(mov_files)))
    print('작업을 ' + str(len(mov_files) / 1000) + '번 반복할 것입니다.')

    n = 0
    j = 0

    while n < len(mov_files) / 1000:
        # 폴더생성
        slicing_path = nPath + '/' + str(n+24)
        os.mkdir(slicing_path)
        # 파일이동
        for movfi in slicing_mov_files[j]:
            shutil.move(oPath + '/' + movfi, nPath + '/' + str(n) + '/' + movfi)
            print('move file : ' + oPath + ' 에 있는 ' + movfi + ' ----- > ' + nPath + '/' + str(n) + '로 이동됨.')
        j += 1
        n += 1


if __name__ == "__main__":
    file_moves()
