from django.db import models


class Samples(models.Model):
    id = models.AutoField(primary_key=True)

    sample = models.CharField(max_length=100, unique=True)
    data_source = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=200, blank=True, null=True)
    enzyme_linker = models.CharField(max_length=100, blank=True, null=True)
    factor = models.CharField(max_length=100, blank=True, null=True)
    tissue = models.CharField(max_length=200, blank=True, null=True)
    health_status = models.CharField(max_length=200, blank=True, null=True)
    biomaterial_type = models.CharField(max_length=200, blank=True, null=True)
    cell_line_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'samples'

    def __str__(self):
        return self.sample


class Loop(models.Model):
    id = models.AutoField(primary_key=True)
    # 将 sample_name 定义为外键，指向 Samples 的 sample 字段
    sample_name = models.ForeignKey(Samples, to_field='sample', on_delete=models.CASCADE, db_column='sample_name')

    chrom1 = models.CharField(max_length=10, blank=True, null=True)
    start1 = models.BigIntegerField(blank=True, null=True)
    end1 = models.BigIntegerField(blank=True, null=True)
    chrom2 = models.CharField(max_length=10, blank=True, null=True)
    start2 = models.BigIntegerField(blank=True, null=True)
    end2 = models.BigIntegerField(blank=True, null=True)

    counts = models.IntegerField(blank=True, null=True)
    gene_anno_1 = models.CharField(max_length=500, blank=True, null=True)
    gene_anno_2 = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'loop'

    def __str__(self):
        return f"{self.sample_name.sample} {self.chrom1}:{self.start1}-{self.end1} <-> {self.chrom2}:{self.start2}-{self.end2}"


class Stripe(models.Model):
    id = models.AutoField(primary_key=True)
    # 将 sample_name 定义为外键，指向 Samples 的 sample 字段
    sample_name = models.ForeignKey(Samples, to_field='sample', on_delete=models.CASCADE, db_column='sample_name')

    chrom1 = models.CharField(max_length=10, blank=True, null=True)
    pos1 = models.BigIntegerField(blank=True, null=True)
    pos2 = models.BigIntegerField(blank=True, null=True)
    chrom2 = models.CharField(max_length=10, blank=True, null=True)
    pos3 = models.BigIntegerField(blank=True, null=True)
    pos4 = models.BigIntegerField(blank=True, null=True)

    pvalue = models.FloatField(blank=True, null=True)
    gene_anno_1 = models.CharField(max_length=500, blank=True, null=True)
    gene_anno_2 = models.CharField(max_length=500, blank=True, null=True)
    chipseq_anno_1 = models.CharField(max_length=500, blank=True, null=True)
    chipseq_anno_2 = models.CharField(max_length=500, blank=True, null=True)
    stripe_type = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'stripe'

    def __str__(self):
        return f"{self.sample_name.sample} {self.chrom1}:{self.pos1}-{self.pos2} <-> {self.chrom2}:{self.pos3}-{self.pos4}"


class Compartment(models.Model):
    id = models.AutoField(primary_key=True)
    # 将 sample_name 定义为外键，指向 Samples 的 sample 字段
    sample_name = models.ForeignKey(Samples, to_field='sample', on_delete=models.CASCADE, db_column='sample_name')

    chrom = models.CharField(max_length=10, blank=True, null=True)
    start = models.BigIntegerField(blank=True, null=True)
    end = models.BigIntegerField(blank=True, null=True)

    value = models.FloatField()

    class Meta:
        db_table = 'compartment'

    def str(self):
        return f"{self.sample_name.sample} {self.chrom}:{self.start}-{self.end} {self.value}"


class DomainBound(models.Model):
    id = models.AutoField(primary_key=True)
    # 将 sample_name 定义为外键，指向 Samples 的 sample 字段
    sample_name = models.ForeignKey(Samples, to_field='sample', on_delete=models.CASCADE, db_column='sample_name')

    chrom = models.CharField(max_length=10, blank=True, null=True)
    start = models.BigIntegerField(blank=True, null=True)
    end = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'domain_bound_samples'

    def str(self):
        return f"{self.sample_name.sample} {self.chrom}:{self.start}-{self.end}"


class Enhancer(models.Model):
    id = models.AutoField(primary_key=True)  # 自增主键

    chrom = models.CharField(max_length=10, blank=True, null=True)
    start = models.BigIntegerField(blank=True, null=True)
    end = models.BigIntegerField(blank=True, null=True)

    # 使用log_pvalue作为字段名，并通过db_column将其映射到数据库中的"-logPvalue"列
    log_pvalue = models.FloatField(blank=True, null=True, db_column='-logPvalue')

    file_id = models.CharField(max_length=100, blank=True, null=True)
    experiment = models.CharField(max_length=100, blank=True, null=True)
    subtissue = models.CharField(max_length=200, blank=True, null=True)
    tissue = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'enhancer'

    def __str__(self):
        return f"{self.chrom}:{self.start}-{self.end} {self.file_id}"
# 只有重新migrate，每张表中id才能从1开始
