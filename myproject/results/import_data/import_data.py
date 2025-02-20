import os
import django
from django.db import connection

# 设置环境变量，指向 Django 的 settings 模块
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")  # 替换为你的项目名称

# 初始化 Django
django.setup()
import pandas as pd
from results.models import Samples, Loop, Stripe, DomainBound, Compartment, Enhancer, Overview


def import_samples():
    # Step 1: 读取文件
    file_path = "./Metadata.txt"  # 替换为实际路径
    data = pd.read_csv(file_path, sep="\t")

    # Step 2: 遍历 DataFrame 并插入到数据库
    for _, row in data.iterrows():
        # print(111)
        sample = Samples(
            sample=row['id'],
            data_source=row['data_source'],
            data_type=row['data_type'],
            enzyme_linker=row['enzyme_linker'],
            factor=row['factor'],
            tissue=row['tissue'],
            health_status=row['health_status'],
            biomaterial_type=row['biomaterial_type'],
            cell_line_name=row['cell_line_name']
        )
        sample.save()
    print("Successfully import samples!")


def import_loop():
    # Step 1: 读取文件
    file_path = "./Loop_top100.txt"  # 替换为实际路径
    data = pd.read_csv(file_path, sep="\t")

    # Step 2: 遍历 DataFrame 并插入到数据库
    for _, row in data.iterrows():
        try:
            # 查找外键引用的 Sample 对象
            sample = Samples.objects.get(sample=row['sample_name'])
        except Samples.DoesNotExist:
            print(f"Sample '{row['sample_name']}' 不存在，跳过此条记录。")
            continue

        loop = Loop(
            chrom1=row['chrom1'],
            start1=row['start1'],
            end1=row['end1'],
            chrom2=row['chrom2'],
            start2=row['start2'],
            end2=row["end2"],
            sample_name=sample,  # 外键对象
            counts=row['counts'],
            gene_anno_1=row['gene_anno_1'],
            gene_anno_2=row['gene_anno_2']
        )
        loop.save()

    print("Successfully import loop!")


def import_stripe():
    # Step 1: 读取文件
    file_path = "./Stripe_top100.txt"  # 替换为实际路径
    data = pd.read_csv(file_path, sep="\t")

    # Step 2: 遍历 DataFrame 并插入到数据库
    for _, row in data.iterrows():
        try:
            # 查找外键引用的 Sample 对象
            sample = Samples.objects.get(sample=row['sample_name'])
        except Samples.DoesNotExist:
            print(f"Sample '{row['sample_name']}' 不存在，跳过此条记录。")
            continue

        stripe = Stripe(
            sample_name=sample,  # 外键对象
            chrom1=row['chrom1'],
            pos1=row['pos1'],
            pos2=row['pos2'],
            chrom2=row['chrom2'],
            pos3=row['pos3'],
            pos4=row['pos4'],
            pvalue=row['pvalue'],
            gene_anno_1=row.get('gene_anno_1', None),
            gene_anno_2=row.get('gene_anno_2', None),
            chipseq_anno_1=row.get('chipseq_anno_1', None),
            chipseq_anno_2=row.get('chipseq_anno_2', None),
            stripe_type=row.get('stripe_type', None),
        )
        stripe.save()

    print("Successfully import stripe!")


def import_domain_bound_samples():
    # Step 1: 读取文件
    file_path = "./Domain_reformat_4col.txt"  # 替换为实际路径
    data = pd.read_csv(file_path, sep="\t")

    # Step 2: 遍历 DataFrame 并插入到数据库
    i = 0
    for _, row in data.iterrows():
        if i >= 100:
            break
        i += 1
        samples = row['B_samples'].split(',')
        for sample_name in samples:
            sample_name = sample_name.strip()  # 去除首尾空格
            try:
                # 查找外键引用的 Sample 对象
                sample = Samples.objects.get(sample=sample_name)  # 假设 `name` 字段匹配
            except Samples.DoesNotExist:
                print(f"Sample '{sample_name}' 不存在，跳过此条记录。")
                continue

            domain = DomainBound(
                sample_name=sample,  # 外键对象
                chrom=row['chrom'],
                start=row['start'],
                end=row['end']
            )
            domain.save()

    print("Successfully import domain_bound_samples!")


def import_compartment():
    # Step 1: 读取文件
    file_path = "./Compartment_top100_cleaned.txt"  # 替换为实际路径
    data = pd.read_csv(file_path, sep="\t")

    # Step 2: 遍历 DataFrame 并插入到数据库
    i = 0
    for _, row in data.iterrows():
        if i >= 100:
            break
        i += 1
        try:
            # 查找外键引用的 Sample 对象
            sample = Samples.objects.get(sample=row['sample_name'])
        except Samples.DoesNotExist:
            print(f"Sample '{row['sample_name']}' 不存在，跳过此条记录。")
            continue

        compartment = Compartment(
            sample_name=sample,  # 外键对象
            chrom=row['chrom'],
            start=row['start'],
            end=row['end'],
            value=row['value']
        )
        compartment.save()

    print("Successfully import compartment!")


def import_enhancer():
    # Step 1: 读取文件
    file_path = "./Enhancer_top100.txt"
    data = pd.read_csv(file_path, sep="\t")

    # Step 2: 遍历 DataFrame 并插入到数据库
    for _, row in data.iterrows():
        try:
            # 创建 Enhancer 实例
            enhancer = Enhancer(
                chrom=row['chrom'],
                start=row['start'],
                end=row['end'],
                log_pvalue=row['log_pvalue'],
                file_id=row['file_id'],
                experiment=row['experiment'],
                subtissue=row['subtissue'],
                tissue=row['tissue']
            )
            enhancer.save()
        except Exception as e:
            print(f"导入记录失败，错误信息：{e}, 数据：{row.to_dict()}")
            continue

    print("Successfully imported enhancer data!")


def import_overview():
    # Step 1: 读取文件
    file_path = "./overview_datasets_top100.txt"
    data = pd.read_csv(file_path, sep="\t")

    # Step 2: 遍历 DataFrame 并插入到数据库
    for _, row in data.iterrows():
        try:
            # 创建 Enhancer 实例
            overview = Overview(
                chrom=row['chrom'],
                start=row['start'],
                end=row['end'],
                A_compartment=float(row["A_compartment"]),
                B_compartment=float(row["B_compartment"]),
                NA_compartment=float(row["NA_compartment"]),
                IS_lower_bound=float(row["IS_lower_bound"]),
                IS_average=float(row["IS_average"]),
                IS_higher_bound=float(row["IS_higher_bound"]),
            )
            overview.save()
        except Exception as e:
            print(f"导入记录失败，错误信息：{e}, 数据：{row.to_dict()}")
            continue

    print("Successfully imported overview data!")


def main():
    # Samples.objects.all().delete()
    # Loop.objects.all().delete()
    # Stripe.objects.all().delete()
    # DomainBound.objects.all().delete()
    # Compartment.objects.all().delete()
    # Enhancer.objects.all().delete()

    # import_samples()
    # import_loop()
    # import_stripe()
    # import_domain_bound_samples()
    # import_compartment()
    # import_enhancer()
    import_overview()
    # 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


if __name__ == "__main__":
    main()
