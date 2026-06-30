---
title: Configure the Matrix Loader
description: Use the Matrix Loader to efficiently add, edit, and migrate fields, field options, rules, and layouts in CPQ. Upload CSV files, validate configurations, and streamline bulk updates or environment migrations with error-handling and verification support.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/order-management/cpq-using-the-matrix-loader.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [CPQ app, Configure, price, quote apps, Configure, Sales Customer Relationship Management]
---

# Configure the Matrix Loader

Use the Matrix Loader to efficiently add, edit, and migrate [[fields|fields]], field options, [[rules_101|rules]], and [[layouts|layouts]] in CPQ. Upload CSV files, validate configurations, and streamline bulk updates or environment migrations with error-handling and verification support.

The Matrix Loader is the most efficient means of adding and editing fields, field options, rules, and layouts, particularly when the number of elements gets large. When using the Matrix Loader, administrators define their configuration elements in a spreadsheet file. This spreadsheet artifact provides a backup of data in CPQ; it also facilitates fast test-to-production migration processes.

Here is a quick tutorial on how to use the Matrix Loader.

1.  Click **Matrix Loader** in the navigation pane.

    \[Omitted image "cpq-matrix-loader.png"\] Alt text: Menu

2.  On the page that opens, export sample files in the upload formats that are accepted by the Matrix Loader: fields, field options, rules, and tables. Each sample file demonstrates a broad range of the features of the upload format.

    \[Omitted image "cpq-matrix-loader-tutorial-sample-files.png"\] Alt text: Sample files

3.  Drag, or use the file browser to select the CSV files you intend to upload.

    \[Omitted image "cpq-matrix-loader-tutorial-choose-files.png"\] Alt text: Drag and drop or use the file browser to select the CSV files

    We discuss the formats of these CSV files in the following articles:

    -   [[cpq-matrix-loader-csv-fields-and-field-options-upload-and-export|Matrix Loader CSV fields and field options upload and export]]
    -   [[matrix_loader_csv_rules_upload|Matrix Loader: CSV rules upload]]
    -   [[cpq-matrix-loader-csv-table-upload|Matrix Loader: CSV table upload]]
    Queued files are displayed. If necessary, add more files or delete files, and then click **Next**.\[Omitted image "cpq-matrix-loader-tutorial-choose-files-selected-files-shown.png"\] Alt text: Import

4.  The Matrix Loader guesses at the contents of each file according to keywords in the file titles. Confirm that the Matrix Loader guessed the upload file types correctly. If necessary, make corrections.

    The Matrix Loader performs the uploads in the sequence necessary to ensure all elements are uploaded correctly. Click **Import**.

    \[Omitted image "cpq-matrix-loader-tutorial-confirm-type.png"\] Alt text: Import user interface

5.  Confirm that all the uploads succeeded. Most errors originate in a mistake or mismatch in an upload file. When all uploads have succeeded, click **Continue**.\[Omitted image "cpq-matrix-loader-tutorial-import-files.png"\] Alt text: Import files
6.  In the appropriate administration areas \(fields and rules, if you uploaded these ﬁles\), check and confirm the elements that were created as a result of this Matrix Loader upload.

**Related topics**  


[[matrix_loader_table_of_contents|Matrix Loader]]

## Related

- [[cpq-matrix-loader-csv-fields-and-field-options-upload-and-export|Matrix Loader CSV fields and field options upload and export]]
- [[matrix_loader_csv_rules_upload|matrix_loader_csv_rules_upload]]
- [[cpq-matrix-loader-csv-table-upload|cpq matrix loader csv table upload]]
- [[matrix_loader_table_of_contents|Matrix Loader]]
- [[fields|Fields]]
- [[rules_101|Rules]]
- [[layouts|Layouts]]
