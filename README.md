---
page_type: sample
languages:
- javascript
- nodejs
products:
- azure
- azure-storage
description: "This sample demonstrates how to stream blobs to Azure Blob Storage with Node.js."
urlFragment: stream-blobs-nodejs
---

# How to stream blobs to Azure Blob Storage with Node.js

This sample demonstrates how to stream blobs to Azure Blob Storage with Node.js.

If you don't have a Microsoft Azure subscription, you can get a free account <a href="http://go.microsoft.com/fwlink/?LinkId=330212">here</a>.

## SDK Versions

In this sample, you will find the following folders:

* **[azure-sdk-for-js-storage-blob-stream-nodejs-v10]** - references [Storage Blob SDK v10]
* **[azure-sdk-for-js-storage-blob-stream-nodejs-v12]** - references [Storage Blob SDK v12]

## Prerequisites

Clone the repository to your machine:

```bash
git clone https://github.com/Azure-Samples/storage-blob-upload-from-webapp-node-v12.git
```

Change into the `azure-sdk-for-js-storage-blob-stream-nodejs-v12` folder:

```bash
cd storage-blob-upload-from-webapp-node-v12
```

Install dependencies via `npm`:

```bash
npm install
```

## In this sample you will do the following:

* Create a storage account.
* Create a container.
* Upload a stream to [blockblob].

## Adding your storage account name and key

Navigate to your storage account in the [Azure Portal] and copy the account name and key (under **Settings** > **Access keys**) into the `.env.example` file. Save the file and then rename it from `.env.example` to `.env`.

## Running the sample

Start the server:

```bash
npm start
```

Navigate to [http://localhost:3000] and upload an image to blob storage.

You can use the [Azure Storage Explorer] to view blob containers and verify your upload is successful.

<!-- LINKS -->
[azure-sdk-for-js-storage-blob-stream-nodejs-v10]: https://github.com/Azure-Samples/azure-sdk-for-js-storage-blob-stream-nodejs/tree/master/azure-sdk-for-js-storage-blob-stream-nodejs-v10
[azure-sdk-for-js-storage-blob-stream-nodejs-v12]: https://github.com/Azure-Samples/azure-sdk-for-js-storage-blob-stream-nodejs/tree/master/azure-sdk-for-js-storage-blob-stream-nodejs-v12
[Storage Blob SDK v10]: https://www.npmjs.com/package/@azure/storage-blob/v/10.3.0
[Storage Blob SDK v12]: https://www.npmjs.com/package/@azure/storage-blob/v/12.0.0
[blockblob]: https://docs.microsoft.com/en-us/rest/api/storageservices/understanding-block-blobs--append-blobs--and-page-blobs
Azure Portal: https://portal.azure.com
http://localhost:3000: http://localhost:3000
Azure Storage Explorer: https://azure.microsoft.com/features/storage-explorer/
