import os
import django

# 设置环境变量，指向 Django 的 settings 模块
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")  # 替换为你的项目名称

# 初始化 Django
django.setup()
import pandas as pd
from results.models import Samples, Loop, Stripe, DomainBound


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
            id=row['id'],
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
    # TODO: cut domain_re into top 100
    data = pd.read_csv(file_path, sep="\t")

    # Step 2: 遍历 DataFrame 并插入到数据库
    for _, row in data.iterrows():
        try:
            # 查找外键引用的 Sample 对象
            sample = Samples.objects.get(sample=row['sample_name'])
        except Samples.DoesNotExist:
            print(f"Sample '{row['sample_name']}' 不存在，跳过此条记录。")
            continue

        domain = DomainBound(
            sample_name=sample,  # 外键对象
            # TODO: implement this part
        )
        domain.save()

    print("Successfully import domain_bound_samples!")


def main():
    # Samples.objects.all().delete()
    # Loop.objects.all().delete()
    Stripe.objects.all().delete()
    # import_samples()
    # import_loop()
    import_stripe()


if __name__ == "__main__":
    main()
