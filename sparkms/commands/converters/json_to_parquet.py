import click
from pyspark.sql import SparkSession
import glob

from sparkms.commands.analysis.peptide_summary import Fields


@click.command('json-to-parquet', short_help='Command to convert to Json files to Parquet')
@click.option('-i', '--input-path', help="Input json files. ie., /path/to/abc.json or /path/to/*", required=True)
@click.option('-o', '--out-path', help="Output path to store parquets. ie., /out/path", required=True)
def json_to_parquet(input_path, out_path):
  """
  This method allows to convert a peptide json file into a parquet file for large scale data processing. The method
  allows to filter peptides by length.
  :param input_path: input path (folder) including all json files.
  :param out_path: folder where the parquet files will be generated
  :param peptide_length: peptide length to filter the peptides (default = 5)
  :return:
  """

  sql_context = SparkSession.builder.getOrCreate()
  files = [f for f in glob.glob(input_path) if f.endswith('.json')]
  if len(files) == 0:
    raise RuntimeError("The files provided should be json extension")

  for f in files:
    try:
      print("======= processing:" + f)
      df = sql_context.read.json(path=f, dropFieldIfAllNull=True)
      if df.rdd.isEmpty():
        continue

      df.write.parquet(out_path, mode='append', partitionBy=[Fields.EXTERNAL_PROJECT_ACCESSION, Fields.ASSAY_ACCESSION],
                       compression='snappy')

    except Exception as e:
      print("** Error while processing: " + f)
      print(e)


if __name__ == "__main__":
    json_to_parquet()
