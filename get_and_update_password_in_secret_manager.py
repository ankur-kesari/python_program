
import boto3
import json

iam = boto3.client('iam')

# Retrieve the list of access keys for a user
response = iam.list_access_keys(UserName='test')

# Retrieve the most recently created access key
access_key_id = response['AccessKeyMetadata'][0]['AccessKeyId']
print("older_access_key_id:"+ access_key_id)

# Delete the access key
response = iam.delete_access_key(UserName='test', AccessKeyId=access_key_id)

# Print the response to confirm that the access key was deleted
# print(response)


# Create an access key
response = iam.create_access_key(
    UserName='test'
)

# print(response['AccessKey'])

access_key_id = response['AccessKey']['AccessKeyId']
secret_access_key = response['AccessKey']['SecretAccessKey']

print("new_access_key_id: "+ access_key_id)
print("new_secret_access_key: "+ secret_access_key)


##################################################
#updating in secret manager

client = boto3.client('secretsmanager')

# Define the secret ID and the keys to update
secret_id = 'test'
key1 = 'aws_access_key_value'
key2 = 'aws_secret_key_value'

# Retrieve the current value of the secret
response = client.get_secret_value(SecretId=secret_id)
current_value = json.loads(response['SecretString'])

# Update the values for the specified keys
current_value[key1] = access_key_id
current_value[key2] = secret_access_key
updated_value_json = json.dumps(current_value)

# Put the updated value for the entire secret
response = client.put_secret_value(
    SecretId=secret_id,
    SecretString=updated_value_json,
    VersionStages=['AWSCURRENT']
)

# Print the response to confirm that the secret value was updated
print(response)
