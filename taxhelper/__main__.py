from taxhelper.tax_helper import TaxHelper
import argparse

def main():

  parser = argparse.ArgumentParser(description='TurboTax Helper')
  parser.add_argument('--trades', type=str, help='path to CSV file of trades', required=True)
  parser.add_arguments('--credentials', type=str, help='path to JSON credentials file', required=True)
  parser.add_argument('--start-index', type=int, help='Begin at the index of trade in trades CSV. Useful for when bot gets stuck and want to resume without starting over', default=0)

  args = parser.parse_args()

  t = TaxHelper(args.credentials, args.trades, start_index=args.start_index)
  t.start()

if __name__ == '__main__':
  main()
