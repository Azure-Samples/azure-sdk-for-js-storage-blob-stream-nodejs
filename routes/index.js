if (process.env.NODE_ENV !== 'production') {
  require('dotenv').load();
}

const {
  Aborter,
  ContainerURL,
  ServiceURL,
  StorageURL,
  SharedKeyCredential
} = require('@azure/storage-blob');

const express = require('express');
const router = express.Router();
const containerName = 'thumbnails';

const sharedKeyCredential = new SharedKeyCredential(
  process.env.AZURE_STORAGE_ACCOUNT_NAME,
  process.env.AZURE_STORAGE_ACCOUNT_ACCESS_KEY);
const pipeline = StorageURL.newPipeline(sharedKeyCredential);

const serviceURL = new ServiceURL(
  `https://${process.env.AZURE_STORAGE_ACCOUNT_NAME}.blob.core.windows.net`,
  pipeline
);

const containerURL = ContainerURL.fromServiceURL(serviceURL, containerName);

router.get('/', async (req, res, next) => {

  let viewData;

  try {

    const listBlobsResponse = await containerURL.listBlobFlatSegment(Aborter.none);

    for (const blob of listBlobsResponse.segment.blobItems) {
      console.log(`Blob: ${blob.name}`);
    }

    viewData = {
      title: 'Home',
      viewName: 'index',
      accountName: process.env.AZURE_STORAGE_ACCOUNT_NAME,
      containerName: containerName
    };

    if (listBlobsResponse.segment.blobItems.length) {
      viewData.thumbnails = listBlobsResponse.segment.blobItems;
    }

  } catch (err) {

    viewData = {
      title: 'Error',
      viewName: 'error',
      message: 'There was an error contacting the blob storage container.',
      error: err
    };
    
    res.status(500);

  } finally {

    res.render(viewData.viewName, viewData);

  }
});

module.exports = router;