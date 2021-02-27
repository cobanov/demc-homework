def make_Principals(title_principals):

    print("\tMaking 'Principals' table")

    Principals = title_principals[[
        'tconst', 'ordering', 'nconst', 'category', 'job']]

    Principals = Principals.rename(columns={
        'tconst': 'title_id',
        'nconst': 'name_id',
        'category': 'job_category',
    })

    Principals.to_csv('Principals.tsv', index=False, na_rep=r'\N', sep='\t')

#-------------------------------------------------------------------------------


def make_Had_role(title_principals):
    print("\tMaking 'Had_role' table")
    Had_role = title_principals[['tconst', 'nconst', 'characters']]

    Had_role = Had_role.rename(columns={
        'tconst': 'title_id',
        'nconst': 'name_id',
        'characters': 'role_'
    })

    Had_role = Had_role.dropna()
    Had_role['role_'] = Had_role['role_'].str.replace(
        '[\"\[\]]', '', regex=True)
    Had_role['role_'] = Had_role['role_'].str.replace('\\', '|')

    Had_role = Had_role.assign(role_=Had_role.role_.str.split(
        ',')).explode('role_').reset_index(drop=True)
    Had_role['role_'] = Had_role['role_'].str.title()

    Had_role['role_'] = Had_role['role_'].str.replace('^ | $', '', regex=True)

    Had_role.drop_duplicates(keep=False, inplace=True)

    Had_role.to_csv('Had_role.tsv', index=False, na_rep=r'\N', sep='\t')
