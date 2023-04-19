import pandas as pd
import numpy as np
import csv
import argparse

def main(input_gtf_file, input_alias_file, output_file_path):
    gtf_file = pd.read_csv(input_gtf_file, sep="\t", header=None)
    chr_alias = pd.read_csv(input_alias_file, sep="\t")

    chr_alias_dict = dict(zip(chr_alias['# refseq'], chr_alias['assembly']))

    gtf_file[0] = gtf_file[0].map(chr_alias_dict)

    gtf_file.to_csv(output_file_path, sep="\t", index=False, header=False, quoting=3)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process GTF file and replace chromosome IDs.')
    parser.add_argument('input_gtf_file', help='Input GTF file path')
    parser.add_argument('input_alias_file', help='Input chromosome alias file path')
    parser.add_argument('output_file_path', help='Output file path')

    args = parser.parse_args()

    main(args.input_gtf_file, args.input_alias_file, args.output_file_path)
