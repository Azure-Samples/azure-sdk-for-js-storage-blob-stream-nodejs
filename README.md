---
page_type: sample
languages:
- javascript
- nodejs
products:
- azure
- azure-storage
description: "This sample demonstrates how to use the Azure Storage v12 SDK in the context of an Express application to upload images into Azure Blob Storage."
---

# Azure Storage Blob Upload from a Node.js Web Application using the v12 SDK

This sample demonstrates how to use the Azure Storage v12 SDK in the context of an [Express](https://expressjs.com/) application to upload images into Azure Blob Storage.

If you don't have a Microsoft Azure subscription, you can get a free account <a href="http://go.microsoft.com/fwlink/?LinkId=330212">here</a>.

## SDK Versions

In this sample, you will find the following folders:

* **[storage-blob-upload-from-webapp-node-v10](./storage-blob-upload-from-webapp-node-v10)** - references [Storage Blob SDK v10.3.0](https://www.npmjs.com/package/@azure/storage-blob/v/10.3.0)
* **[storage-blob-upload-from-webapp-node-v12](./storage-blob-upload-from-webapp-node-v12)** - references [Storage Blob SDK v12.0.0](https://www.npmjs.com/package/@azure/storage-blob/v/12.0.0)

## Prerequisites

Clone the repository to your machine:

```bash
git clone https://github.com/Azure-Samples/storage-blob-upload-from-webapp-node-v12.git
```

Change into the `storage-blob-upload-from-webapp-node-v12` folder:

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
* Upload a stream to [blockblob](https://docs.microsoft.com/en-us/rest/api/storageservices/understanding-block-blobs--append-blobs--and-page-blobs).

## Adding your storage account name and key

Navigate to your storage account in the [Azure Portal](https://portal.azure.com) and copy the account name and key (under **Settings** > **Access keys**) into the `.env.example` file. Save the file and then rename it from `.env.example` to `.env`.

## Running the sample

Start the server:

```bash
npm start
```

Navigate to [http://localhost:3000](http://localhost:3000) and upload an image to blob storage.

You can use the [Azure Storage Explorer](https://azure.microsoft.com/features/storage-explorer/) to view blob containers and verify your upload is successful.

