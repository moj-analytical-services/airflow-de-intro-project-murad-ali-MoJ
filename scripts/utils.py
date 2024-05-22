from urllib.parse import urlparse, urljoin, urlunparse

def s3_path_join(base: str, *url_parts: str) -> str:
    """
    Joins a base S3 path and URL parts.
    Args:
        base (str): Base S3 URL
        url_parts (str): one or more URL parts
    Example:
    s3_path_join("s3://bucket", "folder", "subfolder") # s3://bucket/folder/subfolder
    """
    
    def ensure_trailing_slash(path):
        return path if path.endswith("/") else path + "/"

    base = ensure_trailing_slash(base)

    for url_part in url_parts:
        base = urljoin(base, url_part)
        base = ensure_trailing_slash(base)

    return base
def s3_path_creator(bucket_name:str,*folders:str):
    base_path =f"s3://{bucket_name}/"
    for folder in folders:
        base_path += folder +'/'
    return base_path.strip('/')
        
    


def part_in_file(file_path):
    file_name = file_path.split('/')[-1]
    return "part" in file_name



