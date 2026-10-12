
from settings import get_conaction

query = '''
SELECT a.id, a.collar_code, a.species, a.nickname, r.name, r.region, r.description
FROM animals a
JOIN reserves r ON a.last_seen_reserve_id = r.id
WHERE a.id = %s
'''


def find_last_reserve(search_type: str, search_value):
    id = search_value if search_type == 'id' else (search_value)
    con = get_conaction()
    cur = con.cursor()
    cur.execute(query,(id,))
    datils = cur.fetchone()
    cur.close()
    con.close()
    return datils







def find_id_by_collar(collar_code:str) -> int:
    print(collar_code)
    con = get_conaction()
    cur = con.cursor()
    cur. execute('''SELECT id FROM animals WHERE collar_code = %s ''', (collar_code,))
    id = cur.fetchone()[0]
    cur.close()
    return id


# print(find_last_reserve('id',5))