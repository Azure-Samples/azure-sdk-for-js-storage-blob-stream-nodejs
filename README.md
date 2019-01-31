# Azure Storage Blob Upload from a Node.js Web Application using the v10 SDK

This sample demonstrates how to use the Azure Storage v10 SDK in the context of an [Express](https://expressjs.com/) application to upload images into Azure Blob Storage.

## Getting started

Clone the repository to your machine:

```bash
git clone https://github.com/Azure-Samples/storage-blob-upload-from-webapp-node-v10.git
```

Change into the `storage-blob-upload-from-webapp-node-v10` folder:

```bash
cd storage-blob-upload-from-webapp-node-v10
```

Install dependencies via `npm`:

```bash
npm install
```

## Adding your storage account name and key

Navigate to your storage account in the [Azure Portal](https://portal.azure.com) and copy the account name and key (under **Settings** > **Access keys**) into the `.env.example` file. Save the file and then rename it from `.env.example` to `.env`.

## Running the sample

Start the server:

```bash
npm start
```

Navigate to [http://localhost:3000](http://localhost:3000) and upload an image to blob storage.

You can use the [Azure Storage Explorer](https://azure.microsoft.com/features/storage-explorer/) to view blob containers and verify your upload is successful.