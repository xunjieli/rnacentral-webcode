"""
Copyright [2009-2017] EMBL-European Bioinformatics Institute
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
     http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

"""
Expert databases.
"""

# new database template
    # {
    #     'name': '',
    #     'label': '',
    #     'url': '',
    #     'description': '',
    #     'hint': '',
    #     'tags': ['', '', ''],
    #     'abbreviation': '',
    #     'examples': [
    #         {'upi': '', 'taxid': 0},
    #         {'upi': '', 'taxid': 0},
    #         {'upi': '', 'taxid': 0},
    #     ],
    #     'references': [
    #         {
    #             'title': '',
    #             'authors': '',
    #             'journal': '',
    #             'pubmed_id': '',
    #         },
    #     ],
    #     'imported': True,
    #     'status': 'new',
    #     'version': '',
    # },

expert_dbs = [
    {
        'name': 'ENA',
        'label': 'ena',
        'url': 'https://www.ebi.ac.uk/ena/browser/',
        'description': "provides a comprehensive record of the world's nucleotide sequencing information",
        'hint': "ENA is a comprehensive record of the world's nucleotide sequencing information",
        'tags': ['all ncRNA types', 'sequence archive'],
        'abbreviation': 'European Nucleotide Archive',
        'examples': [
            {'upi': 'URS00002D0E0C', 'taxid': 10090},
            {'upi': 'URS000035EE7E', 'taxid': 9606},
            {'upi': 'URS0000000001', 'taxid': 77133},
        ],
        'references': [
            {
                'title': 'The European Nucleotide Archive in 2017',
                'authors': 'Silvester et al.',
                'journal': 'Nucleic Acids Res. 2017',
                'pubmed_id': '29140475',
            },
        ],
        'imported': True,
        'status': 'updated',
        'version': 'as of 3 Sept 2021',
    },

    {
        'name': 'PDBe',
        'label': 'pdbe',
        'url': 'http://www.ebi.ac.uk/pdbe/',
        'description': 'is the European repository of information about the 3D structures of large biological molecules. PDBe is a member of the Worldwide Protein Data Bank',
        'hint': 'PDBe is the European repository of information about the 3D structures of large biological molecules. PDBe is a member of the Worldwide Protein Data Bank',
        'tags': ['curated', '3D structure'],
        'abbreviation': 'Protein Data Bank in Europe',
        'examples': [
            {'upi': 'URS00000ABFE9', 'taxid': 562},  # E.coli SSU, 4V4Q chain AA
            {'upi': 'URS00005A14E2', 'taxid': 9606},  # Human SSU, 4V6X chain B2
            {'upi': 'URS000032B6B6', 'taxid': 9606},  # Human U1 snRNA, PDB 3PGW chain N
        ],
        'references': [
            {
                'title': 'PDBe: Protein Data Bank in Europe',
                'authors': 'Gutmanas A, Alhroub Y, Battle GM, Berrisford JM, Bochet E, Conroy MJ, Dana JM, Fernandez Montecelo MA, van Ginkel G, Gore SP et al.',
                'journal': 'Nucleic Acids Res. 2014 Jan;42(Database issue):D285-91',
                'pubmed_id': '24288376',
            },
        ],
        'imported': True,
        'status': 'updated',
        'version': 'as of 3 Sept 2021',
    },

    {
        'name': 'FlyBase',
        'label': 'flybase',
        'url': 'http://flybase.org/',
        'description': 'is a database of Drosophila genes and genomes',
        'hint': 'FlyBase is a database of Drosophila genes and genomes',
        'tags': ['curated', 'model organism', 'Drosophila'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS00007F7879', 'taxid': 7227},
            {'upi': 'URS00007EBD0C', 'taxid': 7227},
            {'upi': 'URS00002B64E6', 'taxid': 7227},
        ],
        'references': [
            {
                'title': 'FlyBase 2.0: the next generation',
                'authors': 'The FlyBase Consortium',
                'journal': 'Nucleic Acids Res. 2019;47(D1):D759-D765',
                'pubmed_id': '30364959',
            },
        ],
        'imported': True,
        'status': 'updated',
        'version': 'FB2021_04',
    },

    {
        'name': 'Ensembl',
        'label': 'ensembl',
        'url': 'http://ensembl.org/',
        'description': 'is a genome browser for vertebrate genomes and model organisms that supports research in comparative genomics, evolution, sequence variation and transcriptional regulation',
        'hint': 'Ensembl is a genome browser for vertebrate genomes and model organisms that supports research in comparative genomics, evolution, sequence variation and transcriptional regulation',
        'tags': ['reference genomes'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS000025784F', 'taxid': 9606},
            {'upi': 'URS000075A546', 'taxid': 9606},
            {'upi': 'URS00005CF03F', 'taxid': 9606},
        ],
        'references': [
            {
                'title': 'Ensembl 2017',
                'authors': 'Aken BL, Achuthan P, Akanni W, Amode MR, Bernsdorff F, Bhai J, Billis K, Carvalho-Silva D, Cummins C, Clapham P et al.',
                'journal': 'Nucleic Acids Res. 2017 Jan 4;45(D1):D635-D642',
                'pubmed_id': '27899575',
            },
            {
                'title': 'The Ensembl gene annotation system.',
                'authors': 'Aken BL, Ayling S, Barrell D, Clarke L, Curwen V, Fairley S, Fernandez Banet J, Billis K, Garcia Giron C, Hourlier T, Howe K, Kahari A, Kokocinski F, Martin FJ, Murphy DN, Nag R, Ruffier M, Schuster M, Tang YA, Vogel JH, White S, Zadissa A, Flicek P, Searle SM.',
                'journal': 'Database (Oxford). 2016 Jun 23;2016.',
                'pubmed_id': '27337980',
            }
        ],
        'imported': True,
        'status': '',
        'version': '104',
    },

    {
        'name': 'Ensembl Plants',
        'label': 'ensembl_plants',
        'url': 'https://plants.ensembl.org/',
        'description': 'is a genome browser for plant genomes that complements the Ensembl database',
        'hint': 'Ensembl Plants is a genome browser for plant genomes that complements the Ensembl database',
        'tags': ['reference genomes'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS0000A77357', 'taxid': 3702},
            {'upi': 'URS0000A7685E', 'taxid': 3702},
            {'upi': 'URS00005391BB', 'taxid': 3702},
        ],
        'references': [
            {
                'title': 'Ensembl Genomes 2018: an integrated omics infrastructure for non-vertebrate species',
                'authors': 'Kersey PJ, Allen JE, Allot A, Barba M, Boddu S, Bolt BJ, Carvalho-Silva D, et al.',
                'journal': 'Nucleic Acids Res. 2018 Jan 4;46(D1):D802-D808',
                'pubmed_id': '29092050',
            },
        ],
        'imported': True,
        'status': '',
        'version': '51',
    },

    {
        'name': 'Ensembl Fungi',
        'label': 'ensembl_fungi',
        'url': 'https://fungi.ensembl.org/',
        'description': 'is a genome browser for fungi genomes that complements the Ensembl database',
        'hint': 'Ensembl Fungi is a genome browser for fungi genomes that complements the Ensembl database',
        'tags': ['reference genomes'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS00006E4BC8', 'taxid': 644358},
            {'upi': 'URS00006DF6F8', 'taxid': 334819},
            {'upi': 'URS00004CEEE1', 'taxid': 402676},
        ],
        'references': [
            {
                'title': 'Ensembl Genomes 2018: an integrated omics infrastructure for non-vertebrate species',
                'authors': 'Kersey PJ, Allen JE, Allot A, Barba M, Boddu S, Bolt BJ, Carvalho-Silva D, et al.',
                'journal': 'Nucleic Acids Res. 2018 Jan 4;46(D1):D802-D808',
                'pubmed_id': '29092050',
            },
        ],
        'imported': True,
        'status': '',
        'version': '51',
    },

    {
        'name': 'Ensembl Metazoa',
        'label': 'ensembl_metazoa',
        'url': 'https://metazoa.ensembl.org/',
        'description': 'is a genome browser for metazoan genomes that complements the Ensembl database',
        'hint': 'Ensembl Metazoa is a genome browser for metazoan genomes that complements the Ensembl database',
        'tags': ['reference genomes'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS00006F2B82', 'taxid': 121224},
            {'upi': 'URS0000C28C34', 'taxid': 136037},
            {'upi': 'URS00006AD331', 'taxid': 7668},
        ],
        'references': [
            {
                'title': 'Ensembl Genomes 2018: an integrated omics infrastructure for non-vertebrate species',
                'authors': 'Kersey PJ, Allen JE, Allot A, Barba M, Boddu S, Bolt BJ, Carvalho-Silva D, et al.',
                'journal': 'Nucleic Acids Res. 2018 Jan 4;46(D1):D802-D808',
                'pubmed_id': '29092050',
            },
        ],
        'imported': True,
        'status': '',
        'version': '51',
    },

    {
        'name': 'Ensembl Protists',
        'label': 'ensembl_protists',
        'url': 'https://protists.ensembl.org/',
        'description': 'is a genome browser for protist genomes that complements the Ensembl database',
        'hint': 'Ensembl Protists is a genome browser for protist genomes that complements the Ensembl database',
        'tags': ['reference genomes'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS00000900A9', 'taxid': 347515},
            {'upi': 'URS0000716773', 'taxid': 312017},
            {'upi': 'URS0000C74655', 'taxid': 559515},
        ],
        'references': [
            {
                'title': 'Ensembl Genomes 2018: an integrated omics infrastructure for non-vertebrate species',
                'authors': 'Kersey PJ, Allen JE, Allot A, Barba M, Boddu S, Bolt BJ, Carvalho-Silva D, et al.',
                'journal': 'Nucleic Acids Res. 2018 Jan 4;46(D1):D802-D808',
                'pubmed_id': '29092050',
            },
        ],
        'imported': True,
        'status': '',
        'version': '51',
    },

    {
        'name': 'Ensembl/GENCODE',
        'label': 'ensembl_gencode',
        'url': 'http://gencodegenes.org/',
        'description': 'produces high quality reference gene annotation and experimental validation for human and mouse genomes',
        'hint': 'GENCODE produces high quality reference gene annotation and experimental validation for human and mouse genomes',
        'tags': ['curated', 'human', 'mouse', 'gene annotation'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS00000B15DA', 'taxid': 9606},
            {'upi': 'URS00000A54A6', 'taxid': 9606},
            {'upi': 'URS000078452D', 'taxid': 10090},
        ],
        'references': [
            {
                'title': 'GENCODE: the reference human genome annotation for The ENCODE Project',
                'authors': 'Harrow J, Frankish A, Gonzalez JM, Tapanari E, Diekhans M, Kokocinski F, Aken BL, Barrell D, Zadissa A et al.',
                'journal': 'Genome research 2012;22;9;1760-74',
                'pubmed_id': '22955987',
            },
        ],
        'imported': True,
        'status': '',
        'version': 'human 38/mouse M27',
    },

    {
        'name': 'Rfam',
        'label': 'rfam',
        'url': 'http://rfam.org',
        'description': 'is a collection of non-coding RNA families represented by manually curated sequence alignments, consensus secondary structures and predicted homologues',
        'hint': 'Rfam is a collection of non-coding RNA families, represented by manually curated sequence alignments, consensus secondary structures and predicted homologues',
        'tags': ['curated', 'automatic', 'alignments'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS00000478B7', 'taxid': 9606},
            {'upi': 'URS000023DE4C', 'taxid': 9606},
            {'upi': 'URS000068EEC5', 'taxid': 8752},
        ],
        'references': [
            {
                'title': 'Rfam 13.0: Shifting to a genome-centric resource for non- coding RNA families',
                'authors': 'Kalvari I, Argasinska J, Quinones-Olvera N, Nawrocki EP, Rivas E, Eddy SR, Bateman A, Finn RD, Petrov AI',
                'journal': 'Nucleic Acids Res. 2017 (Accepted)',
                'pubmed_id': '29112718',
            },
        ],
        'imported': True,
        'status': '',
        'version': '14.2',
    },

    {
        'name': 'miRBase',
        'label': 'mirbase',
        'url': 'http://www.mirbase.org/',
        'description': 'is a database of published miRNA sequences and annotations that provides a centralised system for assigning names to miRNA genes',
        'hint': 'miRBase contains high-quality miRNA annotations; miRBase is responsible for assigning official miRNA gene names',
        'tags': ['curated', 'miRNA'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS000075A685', 'taxid': 9606},
            {'upi': 'URS00003B7674', 'taxid': 10090},
            {'upi': 'URS000016FD1A', 'taxid': 9598},
        ],
        'references': [
            {
                'title': 'miRBase: integrating microRNA annotation and deep-sequencing data',
                'authors': 'Kozomara A., Griffiths-Jones S.',
                'journal': 'Nucleic Acids Res. 39(Database issue): D152-7 (2011 Jan)',
                'pubmed_id': '21037258',
            },
            {
                'title': 'miRBase: microRNA sequences, targets and gene nomenclature',
                'authors': 'Griffiths-Jones S, Grocock RJ, van Dongen S, Bateman A, Enright AJ',
                'journal': 'Nucleic Acids Res. 34(Database issue):D140-4 (2006 Jan1)',
                'pubmed_id': '16381832'
            }
        ],
        'imported': True,
        'status': '',
        'version': '22.1',
    },

    {
        'name': 'Vega',
        'label': 'vega',
        'url': 'http://vega.sanger.ac.uk/',
        'description': 'is a repository for high-quality gene models produced by the manual annotation of vertebrate genomes. Human and mouse data from Vega are merged into <a href="http://www.gencodegenes.org/" target="_blank">GENCODE</a>',
        'hint': 'Vega will be replaced by GENCODE in the next release of RNAcentral',
        'tags': ['curated', 'lncRNA'],
        'abbreviation': 'Vertebrate Genome Annotation',
        'examples': [
            {'upi': 'URS00000B15DA', 'taxid': 9606},
            {'upi': 'URS00000A54A6', 'taxid': 9606},
            {'upi': 'URS0000301B08', 'taxid': 9606},
        ],
        'references': [
            {
                'title': 'The GENCODE v7 catalog of human long noncoding RNAs: analysis of their gene structure, evolution, and expression.',
                'authors': 'Derrien T., Johnson R., Bussotti G., Tanzer A., Djebali S., Tilgner H., Guernec G., Martin D., Merkel A., Knowles DG. et al.',
                'journal': 'Genome Res. 22(9): 1775-1789 (2012 Sep)',
                'pubmed_id': '22955988',
            },
            {
                'title': 'GENCODE: the reference human genome annotation for The ENCODE Project',
                'authors': 'Harrow J., Frankish A., Gonzalez JM., Tapanari E., Diekhans M., Kokocinski F., Aken BL., Barrell D., Zadissa A., Searle S. et al.',
                'journal': 'Genome Res. 22(9): 1760-1774 (2012 Sep)',
                'pubmed_id': '22955987',
            },
        ],
        'imported': False,
        'status': 'archived',
        'version': 'release 65',
    },

    {
        'name': 'tmRNA Website',
        'label': 'tmrna-website',
        'url': 'http://bioinformatics.sandia.gov/tmrna/',
        'description': 'contains predicted tmRNA sequences from RefSeq bacterial genomes, plasmids, phages and some organelles; these include two-piece tmRNAs from permuted genes',
        'hint': 'tmRNA Website contains predicted tmRNA sequences from RefSeq bacterial genomes, plasmids, phages and some organelles',
        'tags': ['automatic', 'tmRNA'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS000060F5B3', 'taxid': 398580},
            {'upi': 'URS000058C344', 'taxid': 1291358},
            {'upi': 'URS000048A91D', 'taxid': 224911},
        ],
        'references': [
            {
                'title': 'The tmRNA website',
                'authors': 'Hudson CM, Williams KP',
                'journal': 'Nucleic Acids Res. 43(Database issue):D138-40. (2015 Jan)',
                'pubmed_id': '25378311',
            },
            {
                'title': 'The tmRNA website: reductive evolution of tmRNA in plastids and other endosymbionts',
                'authors': 'Gueneau de Novoa P., Williams KP.',
                'journal': 'Nucleic Acids Res. 32(Database issue): D104-8 (2004 Jan)',
                'pubmed_id': '14681369',
            }
        ],
        'imported': True,
        'status': '',
        'version': '',
    },

    {
        'name': 'SRPDB',
        'label': 'srpdb',
        'url': 'https://rth.dk/resources/rnp/SRPDB',
        'description': 'provides aligned, annotated and phylogenetically ordered sequences related to structure and function of SRP',
        'hint': 'SRPDB provides aligned, annotated and phylogenetically ordered sequences related to structure and function of SRP',
        'tags': ['curated', 'signal recognition particle'],
        'abbreviation': 'Signal Recognition Particle Database',
        'examples': [
            {'upi': 'URS00000478B7', 'taxid': 9606},
            {'upi': 'URS00001C03DC', 'taxid': 1423},
            {'upi': 'URS00005C64FE', 'taxid': 216594},
        ],
        'references': [
            {
                'title': 'Kinship in the SRP RNA family',
                'authors': 'Rosenblad MA., Larsen N., Samuelsson T., Zwieb C.',
                'journal': 'RNA Biol 6(5): 508-516 (2009 Nov-Dec)',
                'pubmed_id': '19838050',
            },
            {
                'title': 'The tmRDB and SRPDB resources',
                'authors': 'Andersen ES., Rosenblad MA., Larsen N., Westergaard JC., Burks J., Wower IK., Wower J., Gorodkin J., Samuelsson T., Zwieb C.',
                'journal': 'Nucleic Acids Res. 34(Database issue): D163-8 (2006 Jan)',
                'pubmed_id': '16381838',
            },
        ],
        'imported': True,
        'status': '',
        'version': '',
    },

    {
        'name': 'lncRNAdb',
        'label': 'lncrnadb',
        'url': 'http://lncrnadb.org/',
        'description': 'is a database providing comprehensive annotations of eukaryotic long non-coding RNAs (lncRNAs)',
        'hint': 'lncRNAdb is a database providing comprehensive annotations of eukaryotic long non-coding RNAs (lncRNAs)',
        'tags': ['curated', 'lncRNA'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS00000478B7', 'taxid': 9606},
            {'upi': 'URS00005E1511', 'taxid': 9606},
            {'upi': 'URS0000147018', 'taxid': 10090},
        ],
        'references': [
            {
                'title': 'lncRNAdb: a reference database for long noncoding RNAs',
                'authors': 'Amaral P.P., Clark M.B., Gascoigne D.K., Dinger M.E., Mattick J.S.',
                'journal': 'Nucleic Acids Res. 39(Database issue):D146-D151(2011)',
                'pubmed_id': '21112873',
            },
        ],
        'imported': True,
        'status': '',
        'version': '',
    },

    {
        'name': 'GtRNAdb',
        'label': 'gtrnadb',
        'url': 'http://gtrnadb.ucsc.edu/',
        'description': 'contains tRNA gene predictions on complete or nearly complete genomes',
        'hint': 'GtRNAdb contains tRNA gene predictions on complete or nearly complete genomes',
        'tags': ['automatic', 'tRNA', 'secondary structure'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS000047C79B', 'taxid': 9606},
            {'upi': 'URS000074448D', 'taxid': 10090},
            {'upi': 'URS00001F9D54', 'taxid': 10116},
        ],
        'references': [
            {
                'title': 'GtRNAdb 2.0: an expanded database of transfer RNA genes identified in complete and draft genomes',
                'authors': 'Chan P.P., Lowe T.M.',
                'journal': 'Nucleic Acids Res. 2016 Jan 4;44(D1):D184-9',
                'pubmed_id': '26673694',
            },
            {
                'title': 'GtRNAdb: a database of transfer RNA genes detected in genomic sequence',
                'authors': 'Chan P.P., Lowe T.M.',
                'journal': 'Nucleic Acids Res. 37(Database issue):D93-D97(2009)',
                'pubmed_id': '18984615',
            },
        ],
        'imported': True,
        'status': 'updated',
        'version': 'release 19',
    },

    {
        'name': 'RefSeq',
        'label': 'refseq',
        'url': 'http://www.ncbi.nlm.nih.gov/refseq/',
        'description': 'is a comprehensive, integrated, non-redundant, well-annotated set of reference sequences',
        'hint': 'RefSeq is a comprehensive, integrated, non-redundant, well-annotated set of reference sequences',
        'tags': ['curated', 'all ncRNA types'],
        'abbreviation': 'NCBI Reference Sequence Database',
        'examples': [
            {'upi': 'URS000075A3E5', 'taxid': 10090},
            {'upi': 'URS000075ADFF', 'taxid': 9606},
            {'upi': 'URS00003A96B7', 'taxid': 192222},
        ],
        'references': [
            {
                'title': 'RefSeq: an update on mammalian reference sequences.',
                'authors': 'Pruitt K.D., Brown G.R., Hiatt S.M., Thibaud-Nissen F., Astashyn A., Ermolaeva O., Farrell C.M., Hart J., Landrum M.J., McGarvey K.M. et al.',
                'journal': 'Nucleic Acids Res. 2014 Jan;42(Database issue):D756-63',
                'pubmed_id': '24259432',
            },
        ],
        'imported': True,
        'status': 'updated',
        'version': '208',  # ftp://ftp.ncbi.nlm.nih.gov/refseq/release/RELEASE_NUMBER
    },

    {
        'name': 'RDP',
        'label': 'rdp',
        'url': 'http://rdp.cme.msu.edu/',
        'description': 'provides quality-controlled, aligned and annotated rRNA sequences and a suite of analysis tools',
        'hint': 'RDP provides quality-controlled, aligned and annotated rRNA sequences and a suite of analysis tools',
        'tags': ['automatic', 'SSU rRNA'],
        'abbreviation': 'Ribosomal Database Project',
        'examples': [
            {'upi': 'URS0000434740', 'taxid': 338963},
            {'upi': 'URS000071C755', 'taxid': 224308},
            {'upi': 'URS0000090853', 'taxid': 637905},
        ],
        'references': [
            {
                'title': 'Ribosomal Database Project: data and tools for high throughput rRNA analysis',
                'authors': 'Cole J.R., Wang Q., Fish J.A., Chai B., McGarrell D.M., Sun Y., Brown C.T., Porras-Alfaro A., Kuske C.R., Tiedje J.M.',
                'journal': 'Nucleic Acids Res. 2014 Jan;42(Database issue):D633-42',
                'pubmed_id': '24288368',
            },
        ],
        'imported': True,
        'status': '',
        'version': '',
    },

    {
        'name': 'CRW',
        'label': 'crw',
        'url': 'http://crw-site.chemistry.gatech.edu/',
        'description': 'provides comparative sequence and structure information for ribosomal, intron, and other RNAs',
        'hint': 'CRW provides comparative sequence and structure information for ribosomal, intron, and other RNAs',
        'tags': ['curated', 'SSU rRNA', '5S rRNA'],
        'abbreviation': 'Comparative RNA Website',
        'examples': [
            {'upi': 'URS0001BCA6C0', 'taxid': 562}, # E.coli SSU
            {'upi': 'URS0001BCA4A9', 'taxid': 9606}, # Human SSU
            {'upi': 'URS0001BCA572', 'taxid': 9606}, # Human 5S
        ],
        'references': [
            {
                'title': 'The comparative RNA web (CRW) site: an online database of comparative sequence and structure information for ribosomal, intron, and other RNAs',
                'authors': 'Jamie J Cannone, Sankar Subramanian, Murray N Schnare, James R Collett, Lisa M DSouza, Yushi Du, Brian Feng, Nan Lin, Lakshmi V Madabusi, Kirsten M Muller, Nupur Pande, Zhidi Shang, Nan Yu, Robin R Gutell',
                'journal': 'BMC Bioinformatics. 2002;3:2',
                'pubmed_id': '11869452',
            },
        ],
        'imported': True,
        'status': '',
        'version': '',
    },

    {
        'name': 'HGNC',
        'label': 'hgnc',
        'url': 'http://www.genenames.org/',
        'description': 'is the worldwide authority that assigns standardised nomenclature to human genes',
        'hint': 'HGNC is the worldwide authority that assigns standardised nomenclature to human genes',
        'tags': ['curated', 'human', 'gene nomenclature'],
        'abbreviation': 'HUGO Gene Nomenclature Committee',
        'examples': [
            {'upi': 'URS000075C808', 'taxid': 9606},  # HOTAIR
            {'upi': 'URS00004ACFCF', 'taxid': 9606},  # SNORA1
            {'upi': 'URS000075CF56', 'taxid': 9606},  # MIRNA-1
        ],
        'references': [
            {
                'title': 'Genenames.org: the HGNC and VGNC resources in 2017.',
                'authors': 'Yates B, Braschi B, Gray KA, Seal RL, Tweedie S, Bruford EA',
                'journal': 'Nucleic Acids Res. 2017 Jan 4;45(D1):D619-D625',
                'pubmed_id': '27799471',
            },
            {
                'title': 'Genenames.org: the HGNC resources in 2015',
                'authors': 'Gray KA, Yates B, Seal RL, Wright MW, Bruford EA',
                'journal': 'Nucleic Acids Res. 2015 Jan;43(Database issue):D1079-85',
                'pubmed_id': '25361968',
            }
        ],
        'imported': True,
        'status': 'updated',
        'version': 'as of 3 Sept 2021',
    },

    {
        'name': 'Greengenes',
        'label': 'greengenes',
        'url': 'http://greengenes.secondgenome.com/?prefix=downloads/greengenes_database/gg_13_5/',
        'description': 'is a full-length 16S rRNA gene database that provides a curated taxonomy based on de novo tree inference',
        'hint': 'Greengenes is a database of full-length 16S rRNA gene that provides a curated taxonomy based on de novo tree inference',
        'tags': ['automatic', 'SSU rRNA'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS000080E226', 'taxid': 274},
            {'upi': 'URS00006DE01B', 'taxid': 575788},
            {'upi': 'URS00004DD3DC', 'taxid': 511145},
        ],
        'references': [
            {
                'title': 'An improved Greengenes taxonomy with explicit ranks for ecological and evolutionary analyses of bacteria and archaea',
                'authors': 'McDonald D, Price MN, Goodrich J, Nawrocki EP, DeSantis TZ, Probst A, Andersen GL, Knight R, Hugenholtz P',
                'journal': 'ISME J. 2012 Mar;6(3):610-8',
                'pubmed_id': '22134646',
            },
        ],
        'imported': True,
        'status': '',
        'version': '13.5',
    },

    {
        'name': 'LncBase',
        'label': 'lncbase',
        'url': 'http://www.microrna.gr/LncBase',
        'description': 'experimentally verified and computationally predicted microRNA targets on long non-coding RNAs',
        'hint': 'LncBase provides experimentally verified and computationally predicted microRNA targets on long non-coding RNAs',
        'tags': ['automatic', 'curated', 'experimentally determined', 'miRNA', 'lncRNA'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS000075EAB0', 'taxid': 9606},
            {'upi': 'URS00005A4DCF', 'taxid': 10090},
            {'upi': 'URS00003B7674', 'taxid': 9606},
        ],
        'references': [
            {
                'title': 'DIANA-LncBase v2: indexing microRNA targets on non-coding transcripts',
                'authors': 'Paraskevopoulou MD, Vlachos IS, Karagkouni D, Georgakilas G, Kanellos I, Vergoulis T, Zagganas K, Tsanakas P, Floros E, Dalamagas T, Hatzigeorgiou AG',
                'journal': 'Nucleic Acids Res 44(d1):D231-8 (2016)',
                'pubmed_id': '26612864',
            }
        ],
        'imported': True,
        'status': '',
        'version': 'v2',
    },

    {
        'name': 'LNCipedia',
        'label': 'lncipedia',
        'url': 'http://www.lncipedia.org/',
        'description': 'is a comprehensive compendium of human long non-coding RNAs',
        'hint': 'LNCipedia is a comprehensive compendium of human long non-coding RNAs',
        'tags': ['automatic', 'human', 'lncRNA'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS000081175C', 'taxid': 9606},
            {'upi': 'URS0000812103', 'taxid': 9606},
            {'upi': 'URS00001F1863', 'taxid': 9606},
        ],
        'references': [
            {
                'title': 'An update on LNCipedia: a database for annotated human lncRNA sequences',
                'authors': 'Volders PJ, Verheggen K, Menschaert G, Vandepoele K, Martens L, Vandesompele J, Mestdagh P',
                'journal': 'Nucleic Acids Res. 2015 Jan;43(Database issue):D174-80',
                'pubmed_id': '25378313',
            },
        ],
        'imported': True,
        'status': '',
        'version': '5.2',
    },

    {
        'name': 'Modomics',
        'label': 'modomics',
        'url': 'http://modomics.genesilico.pl/',
        'description': 'is a comprehensive database of RNA modifications',
        'hint': 'Modomics is a comprehensive database of RNA modifications',
        'tags': ['curated', 'RNA modifications', 'tRNA', 'rRNA'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS00001BBAFC', 'taxid': 562},
            {'upi': 'URS000019192F', 'taxid': 2102},
            {'upi': 'URS000026426D', 'taxid': 9031},
        ],
        'references': [
            {
                'title': 'MODOMICS: a database of RNA modification pathways. 2017 update',
                'authors': 'Boccaletto P, Machnicka MA, Purta E, Piatkowski P, Baginski B, Wirecki TK, de Crecy-Lagard V, Ross R, Limbach PA, Kotter A, Helm M, Bujnicki JM',
                'journal': 'Nucleic Acids Res. 2018 Jan 4;46(D1):D303-D307',
                'pubmed_id': '29106616',
            },
        ],
        'imported': True,
        'status': '',
        'version': '',
    },

    {
        'name': 'NONCODE',
        'label': 'noncode',
        'url': 'http://www.noncode.org/',
        'description': 'is an integrated knowledge database dedicated to non-coding RNAs',
        'hint': 'NONCODE is an integrated knowledge database dedicated to non-coding RNAs',
        'tags': ['automatic', 'curated', 'lncRNA'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS000019B796', 'taxid': 9606},
            {'upi': 'URS00008189E4', 'taxid': 9606},
            {'upi': 'URS000058E3EB', 'taxid': 9606},
        ],
        'references': [
            {
                'title': 'NONCODE 2016: an informative and valuable data source of long non-coding RNAs',
                'authors': 'Zhao Y, Li H, Fang S, Kang Y, Wu W, Hao Y, Li Z, Bu D, Sun N, Zhang MQ, Chen R',
                'journal': 'Nucleic Acids Res. 2016 Jan 4;44(D1):D203-8',
                'pubmed_id': '26586799',
            },
        ],
        'imported': True,
        'status': '',
        'version': 'NONCODE2016',
    },

    {
        'name': 'NPInter',
        'label': '',
        'url': 'http://bioinfo.ibp.ac.cn/NPInter/',
        'description': 'experimentally determined functional interactions between ncRNAs and proteins, mRNAs or genomic DNA',
        'hint': 'NPInter contains data on experimentally determined functional interactions between ncRNAs and proteins, mRNAs or genomic DNA',
        'tags': ['automatic', 'curated'],
        'abbreviation': '',
        'examples': '',
        'references': [],
        'imported': False,
        'status': '',
        'version': '',
    },

    {
        'name': 'piRBase',
        'label': 'pirbase',
        'url': 'http://www.regulatoryrna.org/database/piRNA/',
        'description': 'a database of various piRNA associated data to support piRNA functional study ',
        'hint': 'piRBase is a database of various piRNA associated data to support piRNA functional study',
        'tags': ['automatic', 'curated', 'piRNA'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS0000061ED0', 'taxid': 9606},
            {'upi': 'URS0000298B36', 'taxid': 10090},
            {'upi': 'URS00000FDFAF', 'taxid': 7227},
        ],
        'references': [
            {
                'title': 'piRBase: a comprehensive database of piRNA sequences',
                'authors': 'Wang J, Zhang P, Lu Y, Li Y, Zheng Y, Kan Y, Chen R, He S',
                'journal': 'Nucleic Acids Res. 2019 Jan 8;47(D1):D175-D180',
                'pubmed_id': '30371818',
            },
        ],
        'imported': True,
        'status': '',
        'version': '2.0 (only sequences matching existing RNAcentral accessions have been imported)'
    },

    {
        'name': 'PLncDB',
        'label': 'plncdb',
        'url': 'http://chualab.rockefeller.edu/gbrowse2/homepage.html',
        'description': 'provides comprehensive genomic view of Arabidopsis lncRNAs',
        'hint': 'PLncDB provides comprehensive genomic view of Arabidopsis lncRNAs',
        'tags': ['curated', 'Arabidopsis thaliana'],
        'abbreviation': 'Plant Long Non-Coding DataBase',
        'examples': [''],
        'references': [
            {
                'title': 'PLncDB: plant long non-coding RNA database',
                'authors': 'Jin J., Liu J., Wang H., Wong L., Chua N.H.',
                'journal': 'Bioinformatics. 2013 Apr 15;29(8):1068-71',
                'pubmed_id': '23476021',
            },
        ],
        'imported': False,
        'status': '',
        'version': '',
    },

    {
        'name': 'PomBase',
        'label': 'pombase',
        'url': 'http://www.pombase.org/',
        'description': 'is a comprehensive database for the fission yeast Schizosaccharomyces pombe',
        'hint': 'PomBase is a comprehensive database for the fission yeast Schizosaccharomyces pombe',
        'tags': ['curated', 'model organism', 'yeast', 'Schizosaccharomyces pombe'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS000044FEB9', 'taxid': 4896},
            {'upi': 'URS00003F73E3', 'taxid': 4896},
            {'upi': 'URS00002743E8', 'taxid': 4896},
        ],
        'references': [
            {
                'title': 'PomBase: a comprehensive online resource for fission yeast',
                'authors': 'Wood V., Harris M.A., McDowall M.D., Rutherford K., Vaughan B.W., Staines D.M., Aslett M., Lock A., Bahler J., Kersey P.J., Oliver S.G.',
                'journal': 'Nucleic Acids Res. 2012 Jan;40(Database issue):D695-9',
                'pubmed_id': '22039153',
            },
        ],
        'imported': True,
        'status': 'updated',
        'version': 'as of 02 Sept 2021',
    },

    {
        'name': 'RNApathwaysDB',
        'label': '',
        'url': 'http://genesilico.pl/rnapathwaysdb',
        'description': 'RNA maturation and decay pathways',
        'hint': 'RNApathwaysDB contains RNA maturation and decay pathways',
        'tags': ['curated', 'pathways'],
        'abbreviation': '',
        'examples': '',
        'references': [],
        'imported': False,
        'status': '',
        'version': '',
    },

    {
        'name': 'SILVA',
        'label': 'silva',
        'url': 'https://www.arb-silva.de/',
        'description': 'is a comprehensive resource for quality checked and aligned ribosomal RNA sequence data',
        'hint': 'SILVA is a comprehensive resource for quality checked and aligned ribosomal RNA sequence data',
        'tags': ['semi-automatic', 'SSU rRNA', 'LSU rRNA'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS00005A14E2', 'taxid': 9606},
            {'upi': 'URS00004DD3DC', 'taxid': 511145},
            {'upi': 'URS0000224E47', 'taxid': 10090},
        ],
        'references': [
            {
                'title': 'The SILVA ribosomal RNA gene database project: improved data processing and web-based tools',
                'authors': 'Quast C., Pruesse E., Yilmaz P., Gerken J., Schweer T., Yarza P., Peplies J., Glockner F.O.',
                'journal': 'Nucleic Acids Res. 2013 Jan;41(Database issue):D590-6',
                'pubmed_id': '23193283',
            },
        ],
        'imported': True,
        'status': '',
        'version': 'r138.1',
    },

    {
        'name': 'SGD',
        'label': 'sgd',
        'url': 'http://yeastgenome.org/',
        'description': 'provides comprehensive integrated biological information for the budding yeast',
        'hint': 'SGD provides comprehensive integrated biological information for the budding yeast',
        'tags': ['curated', 'model organism', 'yeast', 'Saccharomyces'],
        'abbreviation': 'Saccharomyces Genome Database',
        'examples': [
            {'upi': 'URS0000224E47', 'taxid': 559292},  # HRA1 gene
            {'upi': 'URS00001CAAE9', 'taxid': 559292},  # SRP
            {'upi': 'URS0000077671', 'taxid': 559292},  # snoRNA
        ],
        'references': [
            {
                'title': 'Saccharomyces Genome Database: the genomics resource of budding yeast',
                'authors': 'Cherry J.M., Hong E.L., Amundsen C., Balakrishnan R., Binkley G., Chan E.T., Christie K.R., Costanzo M.C., Dwight S.S., Engel S.R. et al.',
                'journal': 'Nucleic Acids Res. 2012 Jan;40(Database issue):D700-5',
                'pubmed_id': '22110037',
            },
        ],
        'imported': True,
        'status': 'updated',
        'version': 'as of 03 Sept 2021',
    },

    {
        'name': 'snOPY',
        'label': 'snopy',
        'url': 'http://snoopy.med.miyazaki-u.ac.jp',
        'description': "provides comprehensive information about snoRNAs, snoRNA gene loci, and target RNAs as well as information about snoRNA orthologues",
        'hint': 'snOPY provides comprehensive information about snoRNAs, their gene loci, orthologues and their target RNAs',
        'tags': ['curated', 'snoRNA'],
        'abbreviation': 'snoRNA Orthological Gene Database',
        'examples': [
            {'upi': 'URS00004B0879', 'taxid': 3702},
            {'upi': 'URS0000600DF1', 'taxid': 7227},
            {'upi': 'URS000015A509', 'taxid': 7227},
        ],
        'references': [
            {
                'title': 'snOPY: a small nucleolar RNA orthological gene database',
                'authors': 'Yoshihama M., Nakao A., Kenmochi N.',
                'journal': 'BMC Res Notes 6:426-426(2013)',
                'pubmed_id': '24148649',
            },
        ],
        'imported': True,
        'status': '',
        'version': '',
    },

    {
        'name': 'snoRNA Database',
        'label': 'snornadb',
        'url': 'http://lowelab.ucsc.edu/snoRNAdb/',
        'description': 'is a curated collection of archaeal snoRNAs maintained by the Lowe Lab at UC Santa Cruz',
        'hint': 'The snoRNA Database is a curated collection of archaeal snoRNAs maintained by the Lowe Lab at UC Santa Cruz',
        'tags': ['automatic', 'curated', 'snoRNA'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS0000600702', 'taxid': 340102},
            {'upi': 'URS000020B9CF', 'taxid': 698757},
            {'upi': 'URS00000A48A9', 'taxid': 698757},
        ],
        'references': [
            {
                'title': 'Homologs of small nucleolar RNAs in Archaea',
                'authors': 'A D Omer, T M Lowe, A G Russell, H Ebhardt, S R Eddy, P P Dennis',
                'journal': 'Science. 2000 Apr 21;288(5465):517-22',
                'pubmed_id': '10775111',
            },
            {
                'title': 'Archaeal homologs of eukaryotic methylation guide small nucleolar RNAs: lessons from the Pyrococcus genomes',
                'authors': 'C Gaspin, J Cavaille, G Erauso, J P Bachellerie',
                'journal': 'J Mol Biol. 2000 Apr 7;297(4):895-906',
                'pubmed_id': '10736225',
            },
            {
                'title': 'Methylation guide RNA evolution in archaea: structure, function and genomic organization of 110 C/D box sRNA families across six Pyrobaculum species',
                'authors': 'Lauren M Lui, Andrew V Uzilov, David L Bernick, Andrea Corredor, Todd M Lowe, Patrick P Dennis',
                'journal': 'Nucleic Acids Res. 2018 Jun 20;46(11):5678-5691',
                'pubmed_id': '29771354',
            },
            {
                'title': 'Diversity of Antisense and Other Non-Coding RNAs in Archaea Revealed by Comparative Small RNA Sequencing in Four Pyrobaculum Species',
                'authors': 'David L Bernick, Patrick P Dennis, Lauren M Lui, Todd M Lowe',
                'journal': 'Front Microbiol. 2012 Jul 2;3:231',
                'pubmed_id': '22783241',
            },
            {
                'title': 'Complete genome sequence of Pyrobaculum oguniense',
                'authors': 'David L Bernick, Kevin Karplus, Lauren M Lui, Joanna K C Coker, Julie N Murphy, Patricia P Chan, Aaron E Cozen, Todd M Lowe',
                'journal': 'Stand Genomic Sci. 2012 Jul 30;6(3):336-45',
                'pubmed_id': '23407329',
            },
        ],
        'imported': True,
        'status': '',
        'version': '',
    },

    {
        'name': 'sRNAmap',
        'label': '',
        'url': 'http://srnamap.mbc.nctu.edu.tw/',
        'description': 'a collection of sRNA sequences and interactions',
        'hint': 'sRNAmap is a collection of sRNA sequences and interactions',
        'tags': ['curated', 'sRNA'],
        'abbreviation': '',
        'examples': '',
        'references': [],
        'imported': False,
        'status': '',
        'version': '',
    },

    {
        'name': 'TarBase',
        'label': 'tarbase',
        'url': 'http://www.microrna.gr/tarbase',
        'description': 'a collection of manually curated experimentally validated miRNA-gene interactions',
        'hint': 'TarBase is a collection of manually curated experimentally validated miRNA-gene interactions',
        'tags': ['curated', 'miRNA', 'gene', 'interactions'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS0000021B51', 'taxid': 10090},
            {'upi': 'URS00001DC04F', 'taxid': 10090},
            {'upi': 'URS00004BCD9C', 'taxid': 9606},
        ],
        'references': [
            {
                'title': 'DIANA-TarBase v8: a decade-long collection of experimentally supported miRNA-gene interactions',
                'authors': 'Karagkouni D., Paraskevopoulou MD., Chatzopoulos S., Vlachos IS., Tastsoglou S., Kanellos I., Papadimitriou D., Kavakiotis I., Maniou S., Skoufos G., Vergoulis T., Dalamagas T., Hatzigeorgiou AG',
                'journal': 'Nucleic Acids Res. 2018 Jan 4;46(D1):D239-D245',
                'pubmed_id': '29156006',
            },
        ],
        'imported': True,
        'status': '',
        'version': 'v8',
    },

    {
        'name': 'tmRDB',
        'label': '',
        'url': 'http://rth.dk/resources/rnp/tmRDB/',
        'description': 'aligned, annotated and phylogenetically ordered sequences related to structure and function of tmRNA',
        'hint': 'tmRDB is a collection of aligned, annotated and phylogenetically ordered sequences related to structure and function of tmRNA',
        'tags': ['curated', 'tmRNA'],
        'abbreviation': '',
        'examples': '',
        'references': [],
        'imported': False,
        'status': '',
        'version': '',
    },

    {
        'name': 'tRNAdb',
        'label': '',
        'url': 'http://trna.bioinf.uni-leipzig.de/DataOutput/',
        'description': 'compilation of tRNA sequences and tRNA genes',
        'hint': 'tRNAdb is a compilation of tRNA sequences and tRNA genes.',
        'tags': ['curated', 'tRNA'],
        'description': 'compilation of tRNA sequences and tRNA genes',
        'abbreviation': '',
        'examples': '',
        'references': [],
        'imported': False,
        'status': '',
        'version': '',
    },

    {
        'name': 'WormBase',
        'label': 'wormbase',
        'url': 'http://www.wormbase.org/',
        'description': "curates, stores and displays genomic and genetic data about nematodes with primary emphasis on <em>C. elegans</em> and related nematodes",
        'hint': 'WormBase curates, stores and displays genomic and genetic data about nematodes with primary emphasis on C. elegans and related nematodes',
        'tags': ['curated', 'model organism', 'nematode', 'Caenorhabditis elegans'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS000022A09E', 'taxid': 6239},  # miRNA
            {'upi': 'URS00001218EE', 'taxid': 6239},  # rRNA
            {'upi': 'URS00003E1CE3', 'taxid': 6239},  # snoRNA
        ],
        'references': [
            {
                'title': 'WormBase 2012: more genomes, more data, new website',
                'authors': 'Yook K., Harris TW., Bieri T., Cabunoc A., Chan J., Chen WJ., Davis P., de la Cruz N., Duong A., Fang R. et al.',
                'journal': 'Nucleic Acids Res. 2012 Jan;40(Database issue):D735-41',
                'pubmed_id': '22067452',
            },
        ],
        'imported': True,
        'status': 'updated',
        'version': 'WS270',
    },

    {
        'name': 'MGI',
        'label': 'mgi',
        'url': 'http://www.informatics.jax.org/',
        'description': 'is the international database resource for the laboratory mouse',
        'hint': 'MGI is the international database resource for the laboratory mouse',
        'tags': ['curated', 'model organism', 'mouse', 'Mus musculus'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS00009AEDBB', 'taxid': 10090},
            {'upi': 'URS00009B2FC2', 'taxid': 10090},
            {'upi': 'URS00007742B3', 'taxid': 10090},
        ],
        'references': [
            {
                'title': 'Mouse Genome Database (MGD)-2017: community knowledge resource for the laboratory mouse',
                'authors': 'Blake JA, Eppig JT, Kadin JA, Richardson JE, Smith CL, Bult CJ; the Mouse Genome Database Group',
                'journal': 'Nucleic Acids Res. 2017 Jan 4;45(D1):D723-D729',
                'pubmed_id': '27899570',
            }
        ],
        'imported': True,
        'status': '',
        'version': 'MGI 6.10',
    },

    {
        'name': 'RGD',
        'label': 'rgd',
        'url': 'http://rgd.mcw.edu/',
        'description': 'a collaborative effort between leading research institutions involved in rat genetic and genomic research',
        'hint': 'RGD is a rat genetic and genomic research resource',
        'tags': ['curated', 'model organism', 'rat', 'Rattus norvegicus'],
        'abbreviation': 'Rat Genome Database',
        'examples': [
            {'upi': 'URS000075AA07', 'taxid': 10116},  # Miat
            {'upi': 'URS00004B2C76', 'taxid': 10116},  # 5.8S rRNA
            {'upi': 'URS000075C796', 'taxid': 10116},  # SRP
        ],
        'references': [
            {
                'title': 'The Rat Genome Database 2015: genomic, phenotypic and environmental variations and disease',
                'authors': 'Shimoyama M, De Pons J, Hayman GT, Laulederkind SJ, Liu W, Nigam R, Petri V, Smith JR, Tutaj M, Wang SJ, Worthey E, Dwinell M, Jacob H.',
                'journal': 'Nucleic Acids Res. 2015 Jan 28;43(Database issue):D743-50',
                'pubmed_id': '25355511',
            }
        ],
        'imported': True,
        'status': '',
        'version': 'as of March 2018',
    },

    {
        'name': 'TAIR',
        'label': 'tair',
        'url': 'http://www.arabidopsis.org/',
        'description': 'is a database of genetic and molecular biology data for the model higher plant Arabidopsis thaliana',
        'hint': 'TAIR is a database of genetic and molecular biology data for the model higher plant Arabidopsis thaliana',
        'tags': ['curated', 'model organism', 'Arabidopsis thaliana'],
        'abbreviation': 'The Arabidopsis Information Resource',
        'examples': [
            {'upi': 'URS0000591E4F', 'taxid': 3702},  # tRNA
            {'upi': 'URS000008172F', 'taxid': 3702},  # rRNA
            {'upi': 'URS000035F1B7', 'taxid': 3702},  # snoRNA
        ],
        'references': [
            {
                'title': 'The Arabidopsis Information Resource (TAIR): improved gene annotation and new tools',
                'authors': 'Lamesch P., Berardini T.Z., Li D., Swarbreck D., Wilks C., Sasidharan R., Muller R., Dreher K., Alexander D.L., Garcia-Hernandez M., Karthikeyan A.S. et al.',
                'journal': 'Nucleic Acids Res. 2012 Jan;40(Database issue):D1202-10',
                'pubmed_id': '22140109',
            },
        ],
        'imported': True,
        'status': '',
        'version': 'TAIR10',
    },

    {
        'name': 'dictyBase',
        'label': 'dictybase',
        'url': 'http://dictybase.org/',
        'description': 'is the model organism database for the social amoeba Dictyostelium discoideum',
        'hint': 'dictyBase is the model organism database for the social amoeba Dictyostelium discoideum',
        'tags': ['curated', 'model organism', 'Dicytostelium discoideum'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS00003BBB9E', 'taxid': 352472},
            {'upi': 'URS0000235EB0', 'taxid': 352472},
            {'upi': 'URS00004A9A20', 'taxid': 352472},
        ],
        'references': [
            {
                'title': 'DictyBase 2013: integrating multiple Dictyostelid species',
                'authors': 'Basu S, Fey P, Pandit Y, Dodson R, Kibbe WA, Chisholm RL',
                'journal': 'Nucleic Acids Res. 2013 Jan;41(Database issue):D676-83',
                'pubmed_id': '23172289',
            },
        ],
        'imported': True,
        'status': '',
        'version': '',
    },

    {
        'name': '5SrRNAdb',
        'label': '5srrnadb',
        'url': 'http://combio.pl/rrna/',
        'description': 'is an information resource for 5S ribosomal RNAs',
        'hint': '5SrRNAdb is an information resource for 5S ribosomal RNAs',
        'tags': ['curated', '5S', 'rRNA'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS000002B0D5', 'taxid': 9606},
            {'upi': 'URS000002B0D5', 'taxid': 10090},
        ],
        'references': [
            {
                'title': '5SRNAdb: an information resource for 5S ribosomal RNAs',
                'authors': 'Szymanski M, Zielezinski A, Barciszewski J, Erdmann VA, Karlowski WM',
                'journal': 'Nucleic Acids Res. 2015 Oct 20. pii: gkv1081',
                'pubmed_id': '26490961',
            },
        ],
        'imported': True,
        'status': '',
        'version': '17',
    },

    {
        'name': 'miRTarBase',
        'label': 'mirtarbase',
        'url': 'http://mirtarbase.mbc.nctu.edu.tw',
        'description': 'is an experimentally validated microRNA-target interactions database',
        'hint': 'miRTarBawse is an experimentally validated microRNA-target interactions database',
        'tags': ['curated', 'experimentally determined', 'miRNA', 'interactions'],
        'abbreviation': '',
        'examples': [],
        'references': [
            {
                'title': 'miRTarBase 2016: updates to the eimentally validated miRNA-target interactions database',
                'authors': 'Chou et al',
                'journal': 'Nucleic Acids Res. 2016 Jan 4;44(D1):D239-47',
                'pubmed_id': '26590260',
            },
        ],
        'imported': False,
        'status': '',
        'version': '',
    },

    {
        'name': 'LncBook',
        'label': 'lncbook',
        'url': 'http://bigd.big.ac.cn/lncbook',
        'description': 'is a curated knowledgebase of human long non-coding RNAs',
        'hint': 'LncBook is a curated knowledgebase of human long non-coding RNAs',
        'tags': ['community curated', 'human', 'lncRNA'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS00003E9E7E', 'taxid': 9606},
            {'upi': 'URS000075E1E7', 'taxid': 9606},
            {'upi': 'URS0000050347', 'taxid': 9606},
        ],
        'references': [
            {
                'title': 'LncBook: a curated knowledgebase of human long non-coding RNAs',
                'authors': 'Ma L,  Cao J, Liu L, Du Q, Li Z, Zou D, Bajic VB, Zhang Z',
                'journal': 'Nucleic Acids Res. 2019 Jan 8;47(D1):D128-D134',
                'pubmed_id': '30329098',
            },
        ],
        'imported': True,
        'status': '',
        'version': '1.0',
    },

    {
        'name': 'ZWD',
        'label': 'zwd',
        'url': 'https://bitbucket.org/zashaw/zashaweinbergdata',
        'description': 'is a git-based collection of non-coding RNA alignments maintained by Dr Zasha Weinberg',
        'hint': 'ZWD is a git-based collection of non-coding RNA alignments maintained by Dr Zasha Weinberg',
        'tags': ['metagenome', 'predicted', 'riboswitch'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS000065A032', 'taxid': 224308},
            {'upi': 'URS000067336D', 'taxid': 264730},
            {'upi': 'URS0000D66279', 'taxid': 997891},
        ],
        'references': [
            {
                'title': 'Detection of 224 candidate structured RNAs by comparative analysis of specific subsets of intergenic regions',
                'authors': 'Weinberg Z, Lunse CE, Corbino KA, Ames TD, Nelson JW, Roth A, Perkins KR, Sherlock ME, Breaker RR',
                'journal': 'Nucleic Acids Res. 2017 Oct 13;45(18):10811-10823',
                'pubmed_id': '28977401',
            },
        ],
        'imported': True,
        'status': 'updated',
        'version': '1.2',
    },

    {
        'name': 'snoDB',
        'label': 'snodb',
        'url': 'http://scottgroup.med.usherbrooke.ca/snoDB/',
        'description': 'is an interactive database of human snoRNA sequences, abundance and interactions',
        'hint': 'snoDB is an interactive database of human snoRNA sequences, abundance and interactions',
        'tags': ['snoRNA', 'curated', 'human'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS000071F072', 'taxid': 9606},
            {'upi': 'URS0000726F61', 'taxid': 9606},
            {'upi': 'URS00005D7632', 'taxid': 9606},
        ],
        'references': [
            {
                'title': 'snoDB: an interactive database of human snoRNA sequences, abundance and interactions',
                'authors': 'Bouchard-Bourelle P, Desjardins-Henri C, Mathurin-St-Pierre D, Deschamps-Francoeur G, Fafard-Couture E, Garant JM, Elela SA, Scott MS',
                'journal': 'Nucleic Acids Res. 2019 Oct 10. pii: gkz884',
                'pubmed_id': '31598696',
            },
        ],
        'imported': True,
        'status': '',
        'version': '1.1.0',
    },

    {
        'name': 'MirGeneDB',
        'label': 'mirgenedb',
        'url': 'https://mirgenedb.org',
        'description': 'is a curated microRNA gene database covering 45 metazoan organisms',
        'hint': 'MirGeneDB is a curated microRNA gene database covering 45 metazoan organisms',
        'tags': ['miRNA', 'curated'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS00000157F5', 'taxid': 9606},
            {'upi': 'URS000075DE8D', 'taxid': 10090},
            {'upi': 'URS0000416056', 'taxid': 7955},
        ],
        'references': [
            {
                'title': 'MirGeneDB 2.0: the metazoan microRNA complement',
                'authors': 'Fromm B, Domanska D, Hoye E, Ovchinnikov V, Kang W, Aparicio-Puerta E, Johansen M, Flatmark K, Mathelier A, Hovig E, Hackenberg M, Friedlander MR, Peterson KJ',
                'journal': 'Nucleic Acids Res. 2019 Oct 23',
                'pubmed_id': '31642479',
            },
        ],
        'imported': True,
        'status': '',
        'version': '2.0',
    },

    {
        'name': 'MalaCards',
        'label': 'malacards',
        'url': 'https://www.malacards.org/',
        'description': 'integrates manually-curated and text-mining sources to associate genes, including ncRNAs, with diseases, and lists the supporting evidence',
        'hint': 'MalaCards integrates manually-curated and text-mining sources to associate genes, including ncRNAs, with diseases, and lists the supporting evidence',
        'tags': ['disease', 'human'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS0000EBFCE3', 'taxid': 9606},
            {'upi': 'URS0000EBF55E', 'taxid': 9606},
            {'upi': 'URS0000EBF67F', 'taxid': 9606},
        ],
        'references': [
            {
                'title': 'MalaCards: an amalgamated human disease compendium with diverse clinical and genetic annotation and structured search',
                'authors': 'Rappaport N, Twik M, Plaschkes I, Nudel R, Iny Stein T, Levitt J, Gershoni M, Morrey CP, Safran M, Lancet D',
                'journal': 'Nucleic Acids Res. 2017 Jan 4;45(D1):D877-D887',
                'pubmed_id': '27899610',
            },
        ],
        'imported': True,
        'status': 'updated',
        'version': '5.5',
    },

    {
        'name': 'GeneCards',
        'label': 'genecards',
        'url': 'https://www.genecards.org/',
        'description': 'is a searchable, integrative database that provides comprehensive, user-friendly information on all annotated and predicted human genes',
        'hint': 'GeneCards is a searchable, integrative database that provides comprehensive, user-friendly information on all annotated and predicted human genes',
        'tags': ['human', 'RNA gene'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS0000EBFCE3', 'taxid': 9606},
            {'upi': 'URS0000EBF55E', 'taxid': 9606},
            {'upi': 'URS0000EBF67F', 'taxid': 9606},
        ],
        'references': [
            {
                'title': 'The GeneCards Suite: From Gene Data Mining to Disease Genome Sequence Analyses',
                'authors': 'Stelzer G, Rosen N, Plaschkes I, Zimmerman S, Twik M, Fishilevich S, Stein T, Nudel R, Lieder I, Mazor Y, Kaplan S, Dahary D, Warshawsky D, Guan-Golan Y, Kohn A, Rappaport N, Safran M, Lancet D',
                'journal': 'Curr Protoc Bioinformatics. 2016 Jun 20;54:1.30.1-1.30.33',
                'pubmed_id': '27322403',
            },
        ],
        'imported': True,
        'status': 'updated',
        'version': '5.5',
    },

    {
        'name': 'CRS',
        'label': 'crs',
        'url': 'https://rth.dk/resources/rnannotator/crs/vert/',
        'description': 'is a database of conserved RNA motifs identified computationally in multi-species vertebrate alignments using 2D structure',
        'hint': 'CRS is a database of conserved RNA motifs identified computationally in multi-species vertebrate alignments using 2D structure',
        'tags': ['predicted'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS0000759F81', 'taxid': 9606},
            {'upi': 'URS0000A7D0F3', 'taxid': 10090},
        ],
        'references': [
            {
                'title': 'The identification and functional annotation of RNA structures conserved in vertebrates',
                'authors': 'Seemann SE, Mirza AH, Hansen C, Bang-Berthelsen CH, Garde C, Christensen-Dalsgaard M, Torarinsson E, Yao Z, Workman CT, Pociot F, Nielsen H, Tommerup N, Ruzzo WL, Gorodkin J',
                'journal': 'Genome Res. 2017 Aug;27(8):1371-1383',
                'pubmed_id': '28487280',
            },
        ],
        'imported': True,
        'status': '',
        'version': '2.1',
    },

    {
        'name': 'IntAct',
        'label': 'intact',
        'url': 'https://www.ebi.ac.uk/intact',
        'description': 'provides a freely available, open source database system and analysis tools for molecular interaction data. All interactions are derived from literature curation or direct user submissions',
        'hint': 'IntAct provides a freely available, open source database system and analysis tools for molecular interaction data. All interactions are derived from literature curation or direct user submissions',
        'tags': ['curated', 'interaction', 'RNA-protein'],
        'abbreviation': '',
        'examples': [
            {'upi': 'URS000075DAEC', 'taxid': 9606}, # human NEAT1
            {'upi': 'URS0000723DBB', 'taxid': 10090}, # mouse miRNA
            {'upi': 'URS00002BC0C6', 'taxid': 559292}, # yeast snoRNA
        ],
        'references': [
            {
                'title': 'The MIntAct project--IntAct as a common curation platform for 11 molecular interaction databases',
                'authors': 'Orchard S, Ammari M, Aranda B, Breuza L, Briganti L, Broackes-Carter F, Campbell NH, Chavali G, Chen C, del-Toro N et al.',
                'journal': 'Nucleic Acids Res. 2014 Jan;42(Database issue):D358-63',
                'pubmed_id': '24234451',
            },
        ],
        'imported': True,
        'status': 'updated',
        'version': 'as of 03 Sept 2021',
    },

    {
        'name': 'ZFIN',
        'label': 'zfin',
        'url': 'https://zfin.org',
        'description': 'is the database of genetic and genomic data for the zebrafish (Danio rerio) as a model organism',
        'hint': 'The Zebrafish Information Network (ZFIN) is the database of genetic and genomic data for the zebrafish (Danio rerio) as a model organism',
        'tags': ['curated', 'model organism', 'zebrafish'],
        'abbreviation': 'The Zebrafish Information Network',
        'examples': [
            {'upi': 'URS00003B6A21', 'taxid': 7955}, # mir196c
            {'upi': 'URS00008E3972', 'taxid': 7955}, # linc.alien
            {'upi': 'URS0000A8261D', 'taxid': 7955}, # dre-let-7a-1
        ],
        'references': [
            {
                'title': 'The Zebrafish Information Network: new support for non-coding genes, richer Gene Ontology annotations and the Alliance of Genome Resources',
                'authors': 'Leyla Ruzicka, Douglas G Howe, Sridhar Ramachandran, Sabrina Toro, Ceri E Van Slyke, Yvonne M Bradford, Anne Eagle, David Fashena, Ken Frazer, Patrick Kalita, Prita Mani, Ryan Martin, Sierra Taylor Moxon, Holly Paddock, Christian Pich, Kevin Schaper, Xiang Shao, Amy Singer, Monte Westerfield',
                'journal': 'Nucleic Acids Res. 2019 Jan 8;47(D1):D867-D873',
                'pubmed_id': '30407545',
            },
        ],
        'imported': True,
        'status': '',
        'version': 'as of 22 April 2021',
    },

    {
        'name': 'snoRNA Atlas',
        'label': 'snoatlas',
        'url': 'http://snoatlas.bioinf.uni-leipzig.de/',
        'description': '',
        'hint': 'snoRNA Atlas is a database of human snoRNAs',
        'tags': ['', '', ''],
        'abbreviation': '',
        'examples': [],
        'references': [],
        'imported': False,
        'status': '',
        'version': '',
    },

    {
            'name': 'PSICQUIC',
            'label': 'psicquic',
            'url': 'http://www.ebi.ac.uk/Tools/webservices/psicquic/view/home.xhtml',
            'description': 'provides computational access to molecular-interaction data. miRNA annotations are a collaboration between the UCL functional gene annotation team and the UniProt-GOA group at the EBI and is funded by the British Heart Foundation',
            'hint': 'A database of manually annotated human miRNA interactions',
            'tags': ['curated', '', ''],
            'abbreviation': 'PSICQUIC',
            'examples': [
                {'upi': 'URS00005A4DCF', 'taxid': 9606},  # hsa-miR-125a-5p
                {'upi': 'URS00005BBC98', 'taxid': 9606},  # hsa-mir-183 precursor
                {'upi': 'URS0000D54CAD', 'taxid': 9606},  # hsa-miR-155-5p
            ],
            'references': [
                {
                    'title': 'A new reference implementation of the PSICQUIC web service',
                    'authors': 'Noemi del-Toro, Marine Dumousseau, Sandra Orchard, Rafael C Jimenez, Eugenia Galeota, Guillaume Launay, Johannes Goll, Karin Breuer, Keiichiro Ono, Lukasz Salwinski, Henning Hermjakob',
                    'journal': 'Nucleic Acids Res. 2013 Jul;41(Web Server issue):W601-6',
                    'pubmed_id': '23671334',
                }
            ],
            'imported': True,
            'status': 'New',
            'version': 'as of 03 Sept 2021',
    }
]
