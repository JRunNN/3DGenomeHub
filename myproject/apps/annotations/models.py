from django.db import models

class AnnotationResult(models.Model):
    chrom1 = models.CharField(max_length=100)
    start1 = models.IntegerField()
    end1 = models.IntegerField()
    chrom2 = models.CharField(max_length=100)
    start2 = models.IntegerField()
    end2 = models.IntegerField()
    petCounts = models.IntegerField()
    GenomicAnno1 = models.TextField()
    GenomicAnno2 = models.TextField()
    ENCODE_ATAC1 = models.TextField()
    ENCODE_ATAC2 = models.TextField()
    TCGA_ATAC1 = models.TextField()
    TCGA_ATAC2 = models.TextField()

    class Meta:
        db_table = 'AnnotationResult'