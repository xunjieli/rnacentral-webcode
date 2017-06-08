# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0011_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='RfamAnalyzedSequences',
            fields=[
                ('upi', models.ForeignKey(primary_key=True, db_column=b'upi', serialize=False, to='portal.Rna')),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'rfam_analyzed_sequences',
            },
        ),
        migrations.CreateModel(
            name='RfamClan',
            fields=[
                ('rfam_clan_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=500)),
                ('family_count', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'rnc_rfam_clans',
            },
        ),
        migrations.CreateModel(
            name='RfamHit',
            fields=[
                ('rfam_hit_id', models.AutoField(serialize=False, primary_key=True)),
                ('sequence_start', models.PositiveIntegerField()),
                ('sequence_stop', models.PositiveIntegerField()),
                ('sequence_completness', models.FloatField()),
                ('model_start', models.PositiveIntegerField()),
                ('model_stop', models.PositiveIntegerField()),
                ('model_completeness', models.FloatField()),
                ('overlap', models.CharField(max_length=30)),
                ('e_value', models.FloatField()),
                ('score', models.FloatField()),
            ],
            options={
                'db_table': 'rnc_rfam_model_hits',
            },
        ),
        migrations.CreateModel(
            name='RfamInitialAnnotations',
            fields=[
                ('rfam_initial_annotation_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'rfam_initial_annotations',
            },
        ),
        migrations.CreateModel(
            name='RfamModel',
            fields=[
                ('rfam_model_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=500)),
                ('seed_count', models.PositiveIntegerField()),
                ('full_count', models.PositiveIntegerField()),
                ('length', models.PositiveIntegerField()),
                ('is_supressed', models.BooleanField(default=False)),
                ('rfam_clan_id', models.ForeignKey(db_column=b'rfam_clan_id', to='portal.RfamClan', null=True)),
            ],
            options={
                'db_table': 'rnc_rfam_models',
            },
        ),
        migrations.AddField(
            model_name='rfaminitialannotations',
            name='rfam_model',
            field=models.ForeignKey(to='portal.RfamModel', db_column=b'rfam_model_id'),
        ),
        migrations.AddField(
            model_name='rfaminitialannotations',
            name='upi',
            field=models.ForeignKey(to='portal.Rna', db_column=b'upi'),
        ),
        migrations.AddField(
            model_name='rfamhit',
            name='rfam_model',
            field=models.ForeignKey(to='portal.RfamModel', db_column=b'rfam_model_id'),
        ),
        migrations.AddField(
            model_name='rfamhit',
            name='upi',
            field=models.ForeignKey(to='portal.Rna', db_column=b'upi'),
        ),
    ]
