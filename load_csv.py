import pandas as pd


def load(path: str) -> pd.DataFrame:
    # (You have to adapt the type of return according to your library)

    '''
    This function takes a path as argument, writes the dimensions
    of the data set and returns it
    '''

    if not path.endswith('.csv'):
        return print("CSV only")
    try:
        df = pd.read_csv(path, index_col=0)
        print("Loading dataset of dimensions")
    except Exception:
        return print("Unvalid path/file")
    return df
