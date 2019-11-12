# Azure Storage Blob Upload from a Node.js Web Application using the v10 SDK

This sample demonstrates how to use the Azure Storage v10 SDK in the context of an [Express](https://expressjs.com/) application to upload images into Azure Blob Storage.

## Prerequisites

Clone the repository to your machine:

```bash
git clone https://github.com/Azure-Samples/storage-blob-upload-from-webapp-node-v10.git
```

Change into the `storage-blob-upload-from-webapp-node-v10-v4` folder:

```bash
cd storage-blob-upload-from-webapp-node-v10-v4
```

Install dependencies via `npm`:

```bash
npm install
```

## In this sample you will do the following:

* Create a storage account.
* Create a container.
* Upload a stream to blockblob which consist of blocks of data assembled.

If you don't have a Microsoft Azure subscription, you can get a free trial account <a href="http://go.microsoft.com/fwlink/?LinkId=330212">here</a>.

## Adding your storage account name and key

Navigate to your storage account in the [Azure Portal](https://portal.azure.com) and copy the account name and key (under **Settings** > **Access keys**) into the `.env.example` file. Save the file and then rename it from `.env.example` to `.env`.

## Running the sample

Start the server:

```bash
npm start
```

Navigate to [http://localhost:3000](http://localhost:3000) and upload an image to blob storage.

You can use the [Azure Storage Explorer](https://azure.microsoft.com/features/storage-explorer/) to view blob containers and verify your upload is successful.

## Folders introduction

You will find the following folders: storage-blob-upload-from-webapp-node--v10-v3, which references the [@azure/storage-blob](https://www.npmjs.com/package/@azure/storage-blob/v/10.3.0) version 10.3.0 of the SDK and storage-blob-upload-from-webapp-node-v10-v4, which uses the [@azure/storage-blob](https://www.npmjs.com/package/@azure/storage-blob/v/12.0.0) version 12.0.0 of the SDK.