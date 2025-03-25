from zenml import pipeline


@pipeline
def digital_data_etl (user_full_name : str , links: list[str])-> str:
    pass

