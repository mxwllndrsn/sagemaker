import sagemaker
import boto3

sess = sagemaker.Session()

# session bucket -> upload data/model/log
# automatically create bucket if !exist

sagemaker_session_bucket = None

if sagemaker_session_bucket is None and sess is not None:
    sagemaker_session_bucket = sess.default_bucket() # set to default bucket

try: 
    role = sagemaker.get_execution_role()
except ValueError:
    iam = boto3.client('iam')
    role = iam.get_role(RoleName='sagemaker_execution_role')['Role']['Arn']

sess = sagemaker.Session(default_bucket = sagemaker_session_bucket)

print(f"sagemaker role arn: {role}")
print(f"sagemaker session region: {sess.boto_region_name}")

