import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read raw data
datasource = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="csv",
    connection_options={"paths": ["s3://rahul-aws-data-raw-bucket/"], "recurse": True},
    transformation_ctx="datasource",
)

# Transform
applymapping = ApplyMapping.apply(
    frame=datasource,
    mappings=[("id", "string", "id", "string"), ("name", "string", "name", "string")],
    transformation_ctx="applymapping",
)

# Write curated data
glueContext.write_dynamic_frame.from_options(
    frame=applymapping,
    connection_type="s3",
    connection_options={"path": "s3://rahul-aws-data-curated-bucket/"},
    format="parquet",
    transformation_ctx="datasink",
)

job.commit()
