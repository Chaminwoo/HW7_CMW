import pandas as pd
if __name__ == "__main__":
    # gender2.csv 파일 읽어오기
    df = pd.read_csv('gender2.csv', encoding= 'euc-kr', index_col=0)

    # 필요한 열 선택하여 새로운 DataFrame 생성
    new_df = df[['2022년_계_총인구수', '2022년_남_총인구수', '2022년_여_총인구수']].copy()

    # 열 이름 변경
    new_df.columns = ['Total', 'Male', 'Female']

    # 최종 DataFrame 출력
    print(new_df)

