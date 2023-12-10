import pandas as pd


df = pd.read_csv('dataset-3.csv')
def calculate_distance_matrix(df)->pd.DataFrame():
    """
    Calculate a distance matrix based on the dataframe, df.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Distance matrix
    """
    # Create a set of unique IDs from both 'id_star' and 'id_end' columns
    unique_ids = set(df['id_start'].unique()).union(df['id_end'].unique())
    
    # Initialize an empty DataFrame for the distance matrix
    distance_matrix = pd.DataFrame(index=unique_ids, columns=unique_ids)
    
    # Fill the diagonal with zeros
    distance_matrix.values[[range(len(unique_ids))]*2] = 0
    
    # Iterate over rows and fill in the distance matrix
    for _, row in df.iterrows():
        id_start = row['id_start']
        id_end = row['id_end']
        distance = row['distance']
        
        # Assign distance to both directions (bidirectional distances)
        distance_matrix.at[id_start, id_end] = distance
        distance_matrix.at[id_end, id_start] = distance
    
    df = distance_matrix
    
    return df



def unroll_distance_matrix(df)->pd.DataFrame():
    """
    Unroll a distance matrix to a DataFrame in the style of the initial dataset.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Unrolled DataFrame containing columns 'id_start', 'id_end', and 'distance'.
    """
    # Create an empty list to store unrolled data
    unrolled_data = []

    # Iterate over rows and columns of the distance matrix
    for id_start, row in distance_matrix.iterrows():
        for id_end, distance in row.iteritems():
            # Skip entries where id_start is equal to id_end
            if id_start != id_end:
                unrolled_data.append({'id_start': id_start, 'id_end': id_end, 'distance': distance})

    # Create a DataFrame from the unrolled data
    df = pd.DataFrame(unrolled_data)

    return df


def find_ids_within_ten_percentage_threshold(df, reference_id)->pd.DataFrame():
    """
    Find all IDs whose average distance lies within 10% of the average distance of the reference ID.

    Args:
        df (pandas.DataFrame)
        reference_id (int)

    Returns:
        pandas.DataFrame: DataFrame with IDs whose average distance is within the specified percentage threshold
                          of the reference ID's average distance.
    """
    # Write your logic here

    return df


def calculate_toll_rate(df)->pd.DataFrame():
    """
    Calculate toll rates for each vehicle type based on the unrolled DataFrame.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Wrie your logic here

    return df


def calculate_time_based_toll_rates(df)->pd.DataFrame():
    """
    Calculate time-based toll rates for different time intervals within a day.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Write your logic here

    return df
