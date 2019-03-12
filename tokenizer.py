from plyj import parser
import sys

if __name__ == "__main__":

    p = parser.Parser()
    tokens = p.tokenize_file_clean(sys.argv[1])
    for t in tokens:
        print (t)