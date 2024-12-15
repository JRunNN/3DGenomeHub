import pandas as pd
import numpy as np

# 文件名
input_file = "Compartment_top100.txt"
output_file = "Compartment_top100_cleaned.txt"

# 读取数据
df = pd.read_csv(input_file, sep="\t", dtype=str)

# 数据清洗
# 替换 "NA" 为 np.nan
df.replace("NA", np.nan, inplace=True)

# 将数值列转换为浮点型（假设非前三列为数值列）
value_columns = df.columns[3:]
df[value_columns] = df[value_columns].apply(pd.to_numeric, errors='coerce')

# 转换为长格式
df_cleaned = df.melt(id_vars=["chrom", "start", "end"],
                     var_name="sample_name",
                     value_name="value")
# 删除包含 NaN 的行
df_cleaned.dropna(inplace=True)
# 保存为新文件
df_cleaned.to_csv(output_file, sep="\t", index=False)
print(f"清洗后的数据已保存到文件: {output_file}")
