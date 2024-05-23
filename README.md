# AWS CLI Utility

This project is a Python-based graphical user interface (GUI) application built with Tkinter to interact with AWS CLI commands. It simplifies the process of configuring AWS profiles, updating access keys, and creating S3 buckets.

## Features

1. **Configure AWS CLI Profile**: Input a profile name and configure it using AWS CLI.
2. **Update Access Keys**: Update AWS access keys (Access Key ID and Secret Access Key) directly from the GUI.
3. **Create S3 Bucket**: Input a bucket name and region to create an S3 bucket.

## Requirements

- Python 3.x
- Tkinter library (included with Python standard library)
- AWS CLI installed and configured on your system

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/aws-cli-utility.git
   cd aws-cli-utility
   ```

2. **Install Dependencies**: Ensure you have AWS CLI installed.
   ```bash
   pip install awscli
   ```

## Usage

1. **Run the Application**:
   ```bash
   python aws_cli_utility.py
   ```

2. **Configure AWS Profile**:
   - Enter a profile name.
   - Click "Configure Profile" to set up the profile.

3. **Update Access Keys**:
   - Enter the Access Key ID and Secret Access Key.
   - Click "Update Access Keys" to update the keys.

4. **Create S3 Bucket**:
   - Enter the bucket name and select the region.
   - Click "Create S3 Bucket" to create the bucket.

## Code Overview

### Class Initialization

- `AWSCLIUtility`: Inherits from `tk.Tk` and initializes the GUI components.

### Methods

- `configure_profile()`: Configures an AWS CLI profile.
- `update_access_keys()`: Updates the AWS access keys.
- `create_s3_bucket()`: Creates an S3 bucket.

### GUI Components

- Labels, entries, and buttons for user inputs and actions.
- Message boxes for error and success notifications.

## Example

```bash
python aws_cli_utility.py
```

1. Enter "myprofile" as the profile name and click "Configure Profile".
2. Enter your AWS access keys and click "Update Access Keys".
3. Enter "mybucket" as the bucket name, select "us-east-1" as the region, and click "Create S3 Bucket".

## License

This project is licensed under the MIT License.

## Acknowledgements

- Tkinter: For providing the GUI components.
- AWS CLI: For enabling command-line interaction with AWS services.

---

