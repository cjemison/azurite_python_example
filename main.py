#!/usr/bin/env python
import sys
import uuid
import logging

from azure.storage.blob import BlobServiceClient

root = logging.getLogger()
root.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
root.addHandler(handler)

if __name__ == "__main__":
    local_file_name = str(uuid.uuid4()) + ".txt"
    root.info("file name: {}".format(local_file_name))

    blob_service_client = BlobServiceClient.from_connection_string(
        'AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1O'
        'UzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;'
        'DefaultEndpointsProtocol=http;'
        'BlobEndpoint={}/devstoreaccount1'.format("http://0.0.0.0:10000"),
        logging_enable=True)

    container_client = blob_service_client.get_container_client("test")
    try:
        container_client.create_container()
    except Exception:
        # ignore errors if container exists.
        pass
    blob_client = blob_service_client.get_blob_client(container="test", blob=local_file_name)
    data = b'a'*4*1024*1024
    blob_client.upload_blob(data, blob_type="BlockBlob")
    list_response = container_client.list_blobs()
    for l in list_response:
        root.info("file name: {}".format(l.name))
        download_stream = blob_client.download_blob()
        root.debug(download_stream.readall())