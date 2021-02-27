import shutil
import gzip
import os
import pandas as pd
import numpy as np


def make_Aliases(title_akas):
    # title.akas.tsv
    # FORMAT: ['titleId', 'ordering', 'title', 'region', 'language', 'types',
    # 'attributes', 'isOriginalTitle']

    print("\tMaking 'Aliases' table")

    # Extract columns
    Aliases = title_akas[['titleId', 'ordering', 'title', 'region', 'language',
                          'isOriginalTitle']]

    # Rename columns
    Aliases = Aliases.rename(columns={
        'titleId': 'title_id',
        'isOriginalTitle': 'is_original_title'
    })

    # Output to file
    Aliases.to_csv('Aliases.tsv', index=False, na_rep=r'\N', sep='\t')


def make_Alias_types(title_akas):
    # title.akas.tsv
    # FORMAT: ['titleId', 'ordering', 'title', 'region', 'language', 'types',
    # 'attributes', 'isOriginalTitle']

    print("\tMaking 'Alias_types' table")

    # Extract columns
    Alias_types = title_akas[['titleId', 'ordering', 'types']]

    # Rename columns
    Alias_types = Alias_types.rename(columns={
        'titleId': 'title_id',
        'types': 'type'
    })

    # types is said to be an array. In the data we have this appears to not be
    # true. There appears to be only one string for each pair of titleId and
    # ordering values. There are many NULL (\N) values (~95%) in this field. We
    # don't keep these NULL values. Only entries with non-NULL values in the
    # field are kept and if if there is no entry in this table for a given
    # title_id and ordering pair it is considered to be NULL.
    Alias_types = Alias_types.dropna()

    # Output to file
    Alias_types.to_csv('Alias_types.tsv', index=False, na_rep=r'\N', sep='\t')

# Create Alias_attributes table


def make_Alias_attributes(title_akas):
    # title.akas.tsv
    # FORMAT: ['titleId', 'ordering', 'title', 'region', 'language', 'types',
    # 'attributes', 'isOriginalTitle']

    print("\tMaking 'Alias_attributes' table")

    # Extract columns
    Alias_attributes = title_akas[['titleId', 'ordering', 'attributes']]

    # Rename columns
    Alias_attributes = Alias_attributes.rename(columns={
        'titleId': 'title_id',
        'attributes': 'attribute'
    })

    # attributes is said to be an array. In the data we have this appears to not
    # be true. There appears to be only one string for each pair of titleId and
    # ordering values. There are many NULL (\N) values (~99%) in this field. We
    # don't keep these NULL values. Only entries with non-NULL values in the
    # field are kept and if if there is no entry in this table for a given
    # title_id and ordering pair it is considered to be NULL.
    Alias_attributes = Alias_attributes.dropna()

    # Output to file
    Alias_attributes.to_csv('Alias_attributes.tsv',
                            index=False, na_rep=r'\N', sep='\t')



title_akas = pd.read_csv('./datasets/title.akas.tsv',
                         dtype={'titleId': 'str', 'ordering': 'int', 'title': 'str', 'region': 'str',
                                'language': 'str', 'types': 'str', 'attributes': 'str',
                                'isOriginalTitle': 'Int64'},
                         sep='\t', na_values='\\N', quoting=3)
# Make tables
make_Aliases(title_akas)
make_Alias_types(title_akas)
make_Alias_attributes(title_akas)
# Delete title_akas
del title_akas
