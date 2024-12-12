from django.db import models

# Create your models here.
class ChromLoopsCancer(models.Model):
    chrom1 = models.CharField(max_length=5)
    start1 = models.IntegerField()
    end1 = models.IntegerField()
    chrom2 = models.CharField(max_length=5)
    start2 = models.IntegerField()
    end2 = models.IntegerField()
    counts = models.IntegerField()
    anchor1_in_cancer = models.TextField()
    anchor2_in_cancer = models.TextField()
    anchor1_genes = models.TextField() # Assuming multiple genes can be stored
    anchor2_genes = models.TextField() # Assuming multiple genes can be stored
    file_id = models.CharField(max_length=50)
    body_site = models.CharField(max_length=50)

    class Meta:
        db_table = 'ChromLoopsCancer'

    def __str__(self):
        return f"{self.chrom1}:{self.start1}-{self.end1} | {self.chrom2}:{self.start2}-{self.end2}"


from django.db import models

class NonCodingElementSV(models.Model):
    chrom_sv = models.CharField(max_length=5)
    start_sv = models.IntegerField()
    end_sv = models.IntegerField()
    info = models.TextField()
    cancer_type_sv = models.CharField(max_length=30)
    chrom_cre = models.CharField(max_length=5)
    start_cre = models.IntegerField()
    end_cre = models.IntegerField()
    cre_id = models.CharField(max_length=20) # 'id' is a reserved word in Python, so use 'identifier' or similar
    cancer_type_cre = models.CharField(max_length=30)

    class Meta:
        db_table = 'NonCodingElementSV'

    def __str__(self):
        return f"{self.chrom_sv}:{self.start_sv}-{self.end_sv} | {self.chrom_cre}:{self.start_cre}-{self.end_cre}"


class NonCodingElementSNV(models.Model):
    chrom_snv = models.CharField(max_length=5)
    start_snv = models.IntegerField()
    end_snv = models.IntegerField()
    info = models.TextField()
    cancer_type_snv = models.CharField(max_length=30)
    chrom_cre = models.CharField(max_length=5)
    start_cre = models.IntegerField()
    end_cre = models.IntegerField()
    # As 'id' is a reserved keyword in Django for the primary key of the model, we use 'sv_id' instead
    cre_id = models.CharField(max_length=20)  
    cancer_type_cre = models.CharField(max_length=30)

    def __str__(self):
        return f"SNV: {self.chrom_snv}:{self.start_snv}-{self.end_snv} | CRE: {self.chrom_cre}:{self.start_cre}-{self.end_cre}"

    class Meta:
        # Optional: To ensure there is no duplicate combination of chrom_snv, start_snv, and end_snv
        db_table = 'NonCodingElementSNV'