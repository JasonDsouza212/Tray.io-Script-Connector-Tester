# Tray.io Script Connector Tester

This is a tool to test a script intended for the Tray.io Script/Python Script connector. You can use it to quickly debug and modify a script based on standard input.

1. [Script Connector](#js-scripts)
2. [Python Script Connector](#python-scripts)

# Usage

## JS Scripts

### Prerequisites:
[NodeJs](https://nodejs.org/en/) should be installed.

1. Copy the `input JSON` from the tray connector logs into `input.json`. This should be in the exact format that the connector receives.
2. Add your actual JS script code to `script.js`.

### Steps To Run the Script:
1. Go to your terminal.
2. Make sure to run `npm install` on the repo to install dependencies.

    ```markdown
    npm install
    ```
3. Finally, run the below script to test your `script.js` with the `input.json`.

    ```markdown
    node run.js
    ```

## Python Scripts
[Python3](https://www.python.org/) should be installed.

1. Copy `input JSON` from the tray connector logs into `input.json`. This should be in the exact format that the connector receives.
2. Then add your actual Python code to `script.py`.

### Steps To Run the Script:
1. Go to your terminal.
2. Run the below script to test your `script.py` with the `input.json`.

    ```markdown
    python3 run.py
    ```
