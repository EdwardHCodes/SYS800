from typing import Any, List, Tuple, DefaultDict, Optional, Sequence, Iterator
from comment_parser import comment_parser

with open(user_input, 'r') as source_file:
    extract_comments()

def extract_comments(test.txt, mime = None):



def file_reader(path: str) -> Iterator[str]:
    """
    Attempt to open 'path for reading. Read the file line by line and return the fields as a tuple on each call to next().
    - path specificies the file path
    -num_fields is the number of fields expected to be read from each line in the file
    -sep is the field separataor
    -header specifiies if the first row in the file is a header row.

    If the first row is a header then check the header for the proper number of fields,
    but dont yield the header row

    Exceptions:
        -Raise File Not Found Error if file cant be opened
        -Raise ValueError
    """
    try:
        fp: IO = open(path, "r", encoding="utf-8")
    except FileNotFoundError:
        raise FileNotFoundError(f"Can't open '{path}' for reading")
    else:
        with fp:
            for n, line in enumerate(fp, 1):
                fields: List[str] = line.rstrip('\n').split(sep)
                if len(fields) != num_fields:
                    raise ValueError(f"'{path}' line: {n}: read {len(fields)} fields but expected {num_fields}")
                elif n > 1 or header is False: #if past the first line or no header, then yield the fields
                    yield fields

def if __name__ == "__main__":
    file_reader()
