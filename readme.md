# Data Engineering Projects

This repository contains various data engineering projects that connect to different data warehouses, including Redshift, Snowflake, and BigQuery. Each project demonstrates how to establish connections, execute queries, and handle data using Python.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Challenges and Bug Fixes](#challenges-and-bug-fixes)
- [Contributing](#contributing)

## Project Overview

### Redshift Connection

This project connects to an Amazon Redshift database, retrieves data from the `journeys` table, and displays the results in a Pandas DataFrame.

### Snowflake Connection

This project connects to a Snowflake database, executes various queries to analyze transport data, and outputs the results.

### BigQuery Connection

This project connects to Google BigQuery, retrieves datasets, and executes queries to analyze transport data.

## Technologies Used

- Python
- Pandas
- psycopg2 (for Redshift)
- snowflake-connector-python (for Snowflake)
- google-cloud-bigquery (for BigQuery)
- Jupyter Notebooks
- ConfigParser for configuration management
- dotenv for environment variable management

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/data-engineering-projects.git
   cd data-engineering-projects
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a configuration file (`config.ini` or `.env`) with your database credentials.

4. Run the Jupyter notebooks to execute the projects:
   ```bash
   jupyter notebook
   ```

## Challenges and Bug Fixes

- **Connection Issues**: Initially faced challenges with establishing connections to the databases. Resolved by ensuring correct credentials and network configurations.
  
- **Data Retrieval Warnings**: Encountered warnings related to using Pandas with SQLAlchemy. Updated the code to ensure compatibility and avoid warnings.

- **Cursor Closure Error**: Fixed an issue where the cursor was closed before executing a query. Implemented proper error handling to ensure the cursor remains open during operations.

- **Environment Configuration**: Ensured sensitive data is not exposed by using `.gitignore` to exclude configuration files from version control.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.
