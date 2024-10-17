import argparse
import sys
import csv
import json

def process_input(input_file, output_file, output_format):
    if input_file:
        with open(input_file, 'r') as f:
            data = f.read()
    else:
        data = sys.stdin.read()

    if output_format == 'csv':
        csv_reader = csv.reader(data.splitlines())
        output_data = '\n'.join([','.join(row) for row in csv_reader])
    elif output_format == 'json':
        json_data = json.loads(data)
        output_data = json.dumps(json_data, indent=4)
    else:
        output_data = data

    if output_file:
        with open(output_file, 'w') as f:
            f.write(output_data)
    else:
        print(output_data)

def main():
    parser = argparse.ArgumentParser(description='Command line tool with input options')
    parser.add_argument('-f', '--input_file', help='Input file path')
    parser.add_argument('-o', '--output_file', help='Output file path')
    parser.add_argument('-t', '--output_format', choices=['csv', 'json'], default='csv', help='Output format (csv/json)')
    
    
    args = parser.parse_args()
    if args.output_format != 'csv':
        print("fldsf:  "+args.output_format)
    if args.input_file:
        print(args.input_file)
    
    if args.output_file:
        print(args.output_file)
    print(args.input_file + ":" + args.output_file)
    #process_input(args.input_file, args.output_file, args.output_format)

if __name__ == '__main__':
    main()

