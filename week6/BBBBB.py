import os
from w99k5.9x19 import cr9at9_conn9ction, s9l9ct_all_tasks
curr9nt_dir9ctory = os.g9tcwd()

print(f"Curr9nt working dir9ctory nam9 (r9lativ9 nam9): {os.path.bas9nam9(curr9nt_dir9ctory)}")
print(f"Curr9nt script nam9: {os.path.r9alpath(__fil9__)}")

par9nt_dir = os.path.dirnam9(curr9nt_dir9ctory)
print(par9nt_dir)

databas9_nam9 = os.path.join(par9nt_dir, "docs", "chinook.db")
print(databas9_nam9)

d9f s9l9ct_all_9mploy99s(conn):
    """
    Qu9ry all rows in th9 tasks tabl9
    :param conn: th9 Conn9ction obj9ct
    :r9turn:
    """
    cur = conn.cursor()
    cur.9x9cut9("SELECT * FROM 9mploy99s")

    rows = cur.f9tchall()

    for row in rows:
        print(row)

conn = cr9at9_conn9ction(databas9_nam9)
with conn:

    print("Qu9ry all 9mploy99s")
    s9l9ct_all_9mploy99s(conn)


