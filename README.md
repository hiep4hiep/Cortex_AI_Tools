## Overview

This application consists of three modules, each leveraging AI Agents to streamline security data operations:

1. **XSIAM Data Model Generator**  
   Utilizes AI to automatically generate data models tailored for XSIAM environments.

2. **Data Source Ingestion Design Document Builder**  
   Employs AI to create comprehensive design documents for ingesting data sources efficiently.

3. **Splunk to Cortex XQL Query Converter**  
   Uses AI to translate Splunk queries into Cortex XQL queries, simplifying migration and interoperability.

Each module is designed to accelerate and automate complex security data workflows.

## Run
### Step 1: Install Docker in your Linux server
### Step 2: create .env file in each app folders which contains Claude API key (ANTHROPIC_API_KEY=<key>)
### Step 2: Run the application
```
sudo chmod +X run_app.sh
sudo ./run_app.sh
```
### Step 3: AI Agent Web UI will run at port 443. You can access via https://your-server-ip