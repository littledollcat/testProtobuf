import advantech_afs_pb2
from google.protobuf.json_format import MessageToJson
import pandas as pd
import json

def sample_func():
    print('Hello!')

def getS3Credential(originCredential):
    credential = advantech_afs_pb2.S3Credential()
    credential = Parse(originCredential, credential)
    return credential #dict

def setS3Credential(credential):
    protobufCredential = advantech_afs_pb2.S3Credential()
    protobufCredential.accessKey = credential['access_key']
    protobufCredential.secretAccessKey = credential['secret_key']
    protobufCredential.endPoint = credential['host_url']
    protobufCredential.bucket = credential['bucket']
    protobufCredential.blobPrefix = credential['blob_filter']
    protobufCredential.blobList.extend(credential['blob_list'])
    protobufCredential = MessageToJson(protobufCredential)
    return protobufCredential

def getAzureBlobCredential():
    azurblob = advantech_afs_pb2.AzureBlobStorage()

def setAzureBlobCredential(credential):
    azureblob_credential = advantech_afs_pb2.AzureBlobStorage()
    azureblob_credential.accountName = credential['account_name']
    azureblob_credential.accountKey = credential['account_key']
    azureblob_credential.container = credential['container']
    azureblob_credential.blobType = credential['blob_type']
    azureblob_credential.blobList.extend(credential['blob_list'])
    data = MessageToJson(azureblob_credential)
    return data

def getDataFrame(data):
    data_from_df = advantech_afs_pb2.DataFromDF()
    data_from_df = Parse(data, data_from_df)
    df = json.loads(data_from_df.data)
    df = pd.DataFrame.from_dict(df).astype(json.loads(data_from_df.dtype))
    df.columns = data_from_df.columnsName
    return df

def setDataFrame(df):
    data_from_df = advantech_afs_pb2.DataFromDF()
    data_from_df.data = json.dumps(df.astype(str).to_dict())
    data_from_df.columnsName.extend(list(df.columns))
    data_from_df.dtype = json.dumps(df.dtypes.astype(str).to_dict())
    data = MessageToJson(data_from_df)
    return data