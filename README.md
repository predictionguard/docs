# Fern Docs for Prediction Guard: Instruction Guide

## Updating Live Documentation

To update the live documentation:
1. Go to Fern -> Docs -> Pages and add your page there. 
2. If you are changing the title or adding a new doc update [docs.yml](https://github.com/predictionguard/ferndocs/blob/main/fern/docs.yml). 
3. Commit changes to the main branch.
4. Monitor the actions tab for any errors. Successful updates without errors will automatically push the docs to production at [docs.predictionguard.com](https://docs.predictionguard.com).


## Uploading and Using Images

To use images in the documentation, follow these steps (**do not use images from the asset folder**):

## Warning

> **Warning**: Any file uploaded to the "publicpgdocimages" bucket is publicly accessible to the Internet. Please be mindful of the data you upload.

1. Upload images to the Amazon S3 bucket: [publicpgdocimages](https://s3.console.aws.amazon.com/s3/buckets/publicpgdocimages?region=us-east-1&bucketType=general&tab=objects).
2. Incorporate the image into your documentation with the following line of code:

    ```markdown
    ![External Request Body](https://publicpgdocimages.s3.amazonaws.com/YOUR-IMAGE-NAME-HERE.png)
    ```

3. Commit your changes and verify that the image displays correctly in the documentation.

## Adding Code Blocks

For adding code blocks and multiple code blocks to your documentation, refer to the [Fern documentation on code blocks](https://docs.buildwithfern.com/generate-docs/component-library/code-block).

## Updating API Reference Part of the docs
Please edit the [OpenAPI file located here](https://github.com/predictionguard/docs/blob/main/fern/openapi/Prediction-Guard-Prediction-Guard-API-1.0-resolved.yaml). Must be a valid OPENAPI Spec. 

