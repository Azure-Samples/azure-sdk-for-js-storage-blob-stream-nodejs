# Nutrition Assistant Project

## Prerequisites
Clone the repository to your machine:
```bash
git clone https://github.com/baerdal/NutritionAssistant.git
```

Then, switch to the nutrition_assistant folder:

```bash
cd nutrition_assistant
```

Install dependencies via `npm`:

```bash
npm install
```

## Adding Azure Storage Account name and key
Navigate to your storage account in the Azure and copy the account name and key (under **Settings** > **Access keys**) into the a new `.env` file. This project assumes you have one storage account with two containers `label-images` and `food-images`.
```
AZURE_STORAGE_ACCOUNT_NAME=
AZURE_STORAGE_ACCOUNT_ACCESS_KEY=
```

## Running Locally
Start the server:

```bash
npm start
```

Navigate to http://localhost:3000 and upload an image to blob storage.

