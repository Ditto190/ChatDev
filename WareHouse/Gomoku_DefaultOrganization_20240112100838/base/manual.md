# ProjectMASUI User Manual

## Introduction

Welcome to the user manual for ProjectMASUI! This manual will guide you on how to use the interface to activate and manage multiple MAS (Multi-Agent System) systems. ProjectMASUI is a Python-based application that allows you to interact with MAS agents, monitor their performance, and manage their activation and deactivation.

## Table of Contents

- [Installation](#installation)
- [Getting Started](#getting-started)
- [Interface Overview](#interface-overview)
- [Activating MAS Agents](#activating-mas-agents)
- [Deactivating MAS Agents](#deactivating-mas-agents)
- [Real-Time Interaction and Monitoring](#real-time-interaction-and-monitoring)
- [Agent Management Controls](#agent-management-controls)
- [Error Handling and Logging](#error-handling-and-logging)
- [Integration with ProjectMASUI](#integration-with-projectmasui)

## Installation

To install ProjectMASUI, follow these steps:

1. Make sure you have Python installed on your system. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Create a virtual environment for ProjectMASUI. Open a terminal or command prompt and navigate to the directory where you want to create the virtual environment. Run the following command to create the virtual environment:

   ```
   python -m venv projectmasui-env
   ```

3. Activate the virtual environment. Run the following command:

   - For Windows:

     ```
     projectmasui-env\Scripts\activate
     ```

   - For macOS/Linux:

     ```
     source projectmasui-env/bin/activate
     ```

4. Install the required dependencies. Run the following command:

   ```
   pip install -r requirements.txt
   ```

5. Clone the ProjectMASUI repository. Run the following command:

   ```
   git clone https://github.com/your-username/projectmasui.git
   ```

6. Navigate to the project directory. Run the following command:

   ```
   cd projectmasui
   ```

7. Start the application. Run the following command:

   ```
   python main.py
   ```

8. Access the application. Open a web browser and go to [http://localhost:5000](http://localhost:5000)

## Getting Started

Once you have installed ProjectMASUI and started the application, you will see the main interface. The interface consists of several sections that allow you to manage MAS agents and interact with them in real-time.

## Interface Overview

The ProjectMASUI interface is divided into the following sections:

1. MAS Agents List: This section displays a list of MAS agents detected in the predefined directory. You can see the main Python scripts of the agents and their status.

2. Agent Activation Interface: This section allows you to select and activate MAS agents. You can choose an agent from the list and start its respective Python script within its environment.

3. Real-Time Interaction and Monitoring: This section provides features for real-time interaction with activated MAS agents. You can view their outputs, status, and other relevant information in this section.

4. Agent Management Controls: This section allows you to start, stop, and restart MAS agents. You can also configure necessary settings for the agents in this section.

## Activating MAS Agents

To activate a MAS agent, follow these steps:

1. Go to the "MAS Agents List" section of the interface.

2. Select an agent from the list by clicking on it.

3. Click on the "Activate" button.

4. The selected MAS agent will be activated, and its Python script will start running within its environment.

## Deactivating MAS Agents

To deactivate a currently active MAS agent, follow these steps:

1. Go to the "MAS Agents List" section of the interface.

2. Select an active agent from the list by clicking on it.

3. Click on the "Deactivate" button.

4. The selected MAS agent will be deactivated, and its Python script will stop running.

## Real-Time Interaction and Monitoring

Once you have activated MAS agents, you can interact with them in real-time. The "Real-Time Interaction and Monitoring" section of the interface provides features for this purpose.

You can view the outputs, status, and other relevant information of the activated MAS agents in this section. The information will be updated in real-time as the agents generate outputs or change their status.

## Agent Management Controls

The "Agent Management Controls" section of the interface allows you to start, stop, and restart MAS agents. You can also configure necessary settings for the agents in this section.

To start a MAS agent, click on the "Start" button next to the agent in the "MAS Agents List" section.

To stop a MAS agent, click on the "Stop" button next to the agent in the "MAS Agents List" section.

To restart a MAS agent, click on the "Restart" button next to the agent in the "MAS Agents List" section.

## Error Handling and Logging

ProjectMASUI implements robust error handling for scenarios where MAS agents fail to activate or run. If an agent fails to activate or encounters an error during its execution, the application will display an error message and provide relevant information for troubleshooting.

Comprehensive logging is also implemented in ProjectMASUI. The application logs all relevant events and errors, allowing you to troubleshoot any issues that may arise during the activation and management of MAS agents.

## Integration with ProjectMASUI

ProjectMASUI is designed to seamlessly integrate with the rest of the components in the ProjectMASUI ecosystem. It provides a cohesive user experience by following the same design principles and user interface patterns.

The interface is built using React, a popular JavaScript library for building user interfaces. It communicates with the backend Python code to activate and manage MAS agents.

To integrate ProjectMASUI with other components in the ecosystem, follow the guidelines provided in the respective documentation of those components.

## Conclusion

Congratulations! You have completed the user manual for ProjectMASUI. You should now have a good understanding of how to install the application, navigate the interface, activate and manage MAS agents, and interact with them in real-time.

If you have any further questions or need assistance, please refer to the documentation or contact our support team.

Thank you for using ProjectMASUI!