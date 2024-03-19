# Python Downloader From Spreadsheet

The Python-Downloader-From-Spreadsheet is a program designed to download batch files listed in a spreadsheet stored in CSV format. It simplifies the process of downloading multiple files by fetching them directly from the URLs provided in the spreadsheet.

## Features

- **Batch File Download**: The program enables users to download multiple files listed in a spreadsheet with just one execution.
- **CSV Format Support**: It supports spreadsheets saved in CSV format, making it compatible with various spreadsheet applications.
- **Ease of Use**: Users only need to run the program, and it handles the downloading process automatically.
- **Google Drive Compatibility**: Supports Google Drive links by automatically converting them to direct download links using the specified format.

## Requirements

- Python 3.x
- gdown

## Installation

1. Clone the repository:

```
git clone https://github.com/hernanda16/python_downloader_from_spreadsheet.git
```

2. Install dependencies:

```
pip3 install gdown
```

## Usage

1. Prepare your spreadsheet file in CSV format, listing the files to be downloaded along with their URLs.
2. Ensure that the file is accessible to anyone who has the link.
3. If the file contains Google Drive links, ensure that they are in the correct format according to [this specification](https://sites.google.com/site/gdocs2direct/).
4. Run the program:

```
python exec.py
```

5. Follow the prompts to input the path to your CSV file.
6. Sit back and relax as the program automatically downloads the batch files listed in the spreadsheet.

## Notes

- Ensure that your CSV file is formatted correctly and contains valid URLs for the files to be downloaded.
- Make sure to provide the correct path to your CSV file when prompted by the program.

## Disclaimer

This program is provided as-is, without any warranties or guarantees. Use it at your own risk. The developers shall not be held responsible for any misuse or damage caused by this program.

## License

This program is licensed under the [MIT License](LICENSE). Feel free to modify and distribute it as per the terms of the license.

For any questions or issues, please [open an issue](https://github.com/your/repository/issues) on GitHub.
