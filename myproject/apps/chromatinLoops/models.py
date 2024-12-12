from django.db import models
from django.core.exceptions import ValidationError

class ChromLoops(models.Model):
    chrom1 = models.CharField(max_length=255)
    start1 = models.IntegerField()
    end1 = models.IntegerField()
    chrom2 = models.CharField(max_length=255)
    start2 = models.IntegerField()
    end2 = models.IntegerField()
    counts = models.IntegerField(default=2) 
    anchor1 = models.TextField()
    anchor2 = models.TextField()
    file_id = models.CharField(max_length=255, db_index=True)

    class Meta:
        db_table = 'ChromLoops'


class Assay(models.Model):
    ASSAY_CHOICES = [
        ('ChIA-PET', 'ChIA-PET'),
        ('HiChIP', 'HiChIP'),
        ('ATAC-seq', 'ATAC-seq'),
        ('RNA-seq', 'RNA-seq'),
        ('ChIP-seq', 'ChIP-seq'),
    ]

    name = models.CharField(max_length=20, choices=ASSAY_CHOICES, unique=True, primary_key=True)

    class Meta:
        db_table = 'Assay'
        
    def __str__(self):
        return self.name


class CellTypeSummary(models.Model):
    DISEASE_STATUSES = [
        ('Cancer', 'Cancer'),
        ('Non-Cancer', 'Non-Cancer'),
    ]

    BODY_SITES = [
        ('Aortic valves', 'Aortic valves'),
        ('Artery', 'Artery'),
        ('Ascites', 'Ascites'),
        ('B lymphocyte', 'B lymphocyte'),
        ('Blood', 'Blood'),
        ('Bone', 'Bone'),
        ('Bone marrow', 'Bone marrow'),
        ('Brain', 'Brain'),
        ('Breast', 'Breast'),
        ('Cervix', 'Cervix'),
        ('Colon', 'Colon'),
        ('Embryonic', 'Embryonic'),
        ('Esophagus', 'Esophagus'),
        ('Heart', 'Heart'),
        ('Kidney', 'Kidney'),
        ('Large intestine', 'Large intestine'),
        ('Liver', 'Liver'),
        ('Lung', 'Lung'),
        ('Lymph', 'Lymph'),
        ('Muscle', 'Muscle'),
        ('Myeloid', 'Myeloid'),
        ('Ovary', 'Ovary'),
        ('Pancreas', 'Pancreas'),
        ('Prostate', 'Prostate'),
        ('Skin', 'Skin'),
        ('Soft Tissue', 'Soft Tissue'),
        ('Stomach', 'Stomach'),
        ('Umbilical cord', 'Umbilical cord'),
        ('Uterus', 'Uterus'),
    ]

    FACTOR_TYPES = [
        ('RNAPII', 'RNAPII'),
        ('H3K27ac', 'H3K27ac'),
    ]

    CELL_TYPES = [
        ('Cell line', 'Cell line'),
        ('Primary cell', 'Primary cell')
    ]

    cell_id = models.CharField(max_length=255, primary_key=True)
    cell_type = models.CharField(max_length=20, choices=CELL_TYPES)
    disease_status = models.CharField(max_length=20, choices=DISEASE_STATUSES)
    body_site = models.CharField(max_length=20, choices=BODY_SITES)
    assays = models.ManyToManyField(Assay)
    factor = models.CharField(max_length=20, choices=FACTOR_TYPES)
    # activePromoters = models.IntegerField()
    # expressedTranscripts = models.IntegerField()
    # chromatinInteractions = models.IntegerField()

    class Meta:
        db_table = 'CellTypeSummary'

    def __str__(self):
        return self.cell_id


class File(models.Model):
    FILE_FORMATS = [
        ('bedpe', 'bedpe'),
        ('bed', 'bed'),
        ('hic', 'hic'),
        ('bigwig', 'bigwig'),
        ('txt', 'txt'),
    ]

    ASSAY_FORMATS = [
        ('ChIA-PET','ChIA-PET'),
        ('HiChIP', 'HiChIP'),
        ('ChIP-seq', 'ChIP-seq'),
        ('ATAC-seq', 'ATAC-seq'),
        ("RNA-seq",'RNA-seq')
    ]

    data_id = models.CharField(max_length=255)
    assay = models.CharField(max_length=20, choices=ASSAY_FORMATS)
    format = models.CharField(max_length=20, choices=FILE_FORMATS)
    cell_type_summary = models.ForeignKey(CellTypeSummary, related_name='files', on_delete=models.CASCADE)

    class Meta:
        db_table = 'File'

    def __str__(self):
        return f"{self.data_id} - {self.assay} - {self.format}"