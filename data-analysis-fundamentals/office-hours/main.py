"""A small example of uploading data to redshift."""

from redshift_connector import connect
import pandas as pd

if __name__ == "__main__":

    conn = connect(user="coach_dan",
                   host="c17-redshift-cluster.cdq12ms5gjyk.eu-west-2.redshift.amazonaws.com",
                   password="Melephant_Royal2",
                   database="dw_air_travel")
    

    data = pd.DataFrame(columns=["state_id", "state", "state_code"],
                        data=[(101, 'New Zealand', 'NZ'), (102, 'Birmingham', 'BM')])

    row_lists = data.values.tolist()

    with conn.cursor() as cur:

        q = """
            INSERT INTO
                state (state_id, state, state_code)
            VALUES
                (%s, %s, %s);
        """

        # cur.executemany(q, row_lists)
        cur.write_dataframe(data, "s_coach_dan.state")

    conn.commit()

    conn.close()