# PDF Q&A Web App

This is a Python Flask web application for querying PDF documents using the Llama 2 model from gradient.ai. Users can upload PDF files, extract text, and ask questions about the content of the documents.

## Features

- Upload PDF documents.
- Extract text from PDFs.
- Ask questions about the content using the Llama 2 model.
- Save and retrieve credentials for Gradient workspace.

## Prerequisites

- Python 3.x
- Flask
- Apache Cassandra
- Gradient Llama 2 model
- Llama 2 API credentials

## Installation

1. Clone the repository.

2. Install dependencies:pip install -r requirements.txt

3. Create a `.env` file in the root directory and add the following:

GRADIENT_WORKSPACE_ID=<your_gradient_workspace_id>
GRADIENT_ACCESS_TOKEN=<your_gradient_access_token>


4. Run the application:python app.py


## Usage

1. Open the web application in your browser.

2. Upload PDF documents using the provided form.

3. Ask questions about the content of the uploaded PDFs.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any improvements or new features.

## License

This project is licensed under the [MIT License](LICENSE).



