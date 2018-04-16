# Generated by Django 2.0.1 on 2018-04-16 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('variants', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variant',
            old_name='hgmd_entries',
            new_name='hgmd_class',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='snpeff_biotype',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='snpeff_exon_rank',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='snpeff_gene_coding',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='snpeff_gene_name',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='snpeff_transcript_id',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='vep_allele',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='vep_amino_acids',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='vep_cdna_position',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='vep_cds_position',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='vep_codons',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='vep_condel',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='vep_consequence',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='vep_distance',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='vep_existing_variation',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='vep_feature',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='vep_feature_type',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='vep_gene',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='vep_polyphen',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='vep_protein_position',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='vep_sift',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='vep_strand',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='vep_symbol',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='vep_symbol_source',
        ),
    ]
