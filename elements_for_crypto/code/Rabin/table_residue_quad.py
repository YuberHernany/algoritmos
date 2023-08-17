import pandas as pd
import numpy as np

def table_residue_quad(p):
    """INPUTS: p (int) prime.
    OUTPUTS: table (DataFrame) with index b = 1, 2,..., p-1, and column
            of residues of b**2"""
    col1 = np.arange(1, p).astype(int)
    col2 = np.array([pow(b, 2, p) for b in range(1, p)])
    cols = np.hstack([col1.reshape(-1,1), col2.reshape(-1,1)])
    table = pd.DataFrame(col2, index=col1, columns=['b**2'])
    table.index.name = 'b'
    return table

if __name__ == "__main__":
    # print(table_residue_quad(11))
    pass