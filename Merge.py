import os,sys,pandas as pd

if __name__ == "__main__":
    if os.path.exists('./new.xlsx'):
        sys.exit()
    filenames = os.listdir('./')
    data = pd.DataFrame({})
    for i in range(len(filenames)):
        filename=filenames[i]
        if filename.endswith('.xlsx')|filename.endswith('xls'):
                df=pd.read_excel('./'+filename)
                col_name=df.columns.tolist()
                col_name.insert(0,'产品代码')
                col_name.insert(1,'型号')
                df=df.reindex(columns=col_name)
                df['产品代码']=filename[0:1]
                df['型号']=filename[1:2]
                print("正在复制 "+filename+"的数据...")
                data=pd.concat([df,data])
    print('正在生成新文件...')
    data.to_excel("./new.xlsx",index=False)
    print('成功！！！！！！！！！！！！！！！')
    sys.exit()