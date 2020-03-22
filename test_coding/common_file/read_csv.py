import pandas as pd


# 读取测试用例Excel文件
def read_csv_file(file_path):
    df = pd.read_excel(file_path)
    df.fillna("", inplace=True)  # 填充表格中失却的值
    test_data = []
    # 获取行号的索引，并对其进行遍历
    for i in df.index.values:
        # 根据i来获取每一行指定的数据 并利用to_dict转成字典
        row_data = df.loc[i, ['interface_name', 'domain_name', 'addre', 'headers', 'data_type', 'data', 'request_type', 'Actual_results', 'extract_word', 'reference_parameter', 'reference_header', 'cookies']].to_dict()
        test_data.append(row_data)
    # print("最终获取到的数据是：", test_data)
    return test_data
