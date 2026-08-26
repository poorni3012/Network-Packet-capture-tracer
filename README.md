Network Packet Capture and Analyzer
📌 Overview

This project is a simple Network Packet Capture and Analysis tool developed using Python and Scapy. The program captures live network packets and analyzes important information from each packet.

It helps in understanding how data flows through a network and provides basic knowledge about network protocols and packet structures.

🎯 Objective

The main objective of this project is to:

Capture live network traffic packets.
Analyze the structure and content of captured packets.
Identify Source and Destination IP addresses.
Detect network protocols such as TCP, UDP, and ICMP.
Display Source and Destination Port numbers.
Analyze packet payloads.
Understand the basics of data flow and network communication.
🛠️ Technologies Used
Python
Scapy Library
TCP/IP Protocols
⚙️ Features
Captures live network packets.
Displays Source IP Address.
Displays Destination IP Address.
Identifies TCP, UDP, and ICMP protocols.
Displays Source and Destination Ports.
Attempts to display readable payload data.
Identifies binary or encrypted payload data.
Handles basic errors during packet capture.
🔄 How It Works
Network Traffic
       ↓
Packet Capture using Scapy
       ↓
Analyze Packet Layers
       ↓
Extract IP Information
       ↓
Identify Protocol
       ↓
Extract Port Numbers
       ↓
Analyze Payload
       ↓
Display Packet Information
📦 Installation

Install the required Scapy library using:

pip install scapy
▶️ How to Run

Clone or download this repository and run:

python task1.py

On Windows, packet capturing may require running the terminal with Administrator privileges.

📊 Sample Output
============================================================
Source IP       : 14.102.231.207
Destination IP  : 10.167.88.159
Protocol        : TCP
Source Port     : 80
Destination Port: 61232
Payload         : Binary / Encrypted Data

============================================================
Packet capture completed successfully!
🧠 Learning Outcomes

Through this project, I learned:

Basics of network packet capturing.
Structure of network packets.
Source and Destination communication.
TCP, UDP, and ICMP protocols.
The role of port numbers in network communication.
How payload data can be readable, binary, compressed, or encrypted.
Practical usage of the Python Scapy library.
⚠️ Note

This project is created for educational and learning purposes only. Packet capturing should be performed only on networks and systems where you have permission to monitor traffic.

🚀 Author
poornimashri -cyber security student

Poornima

Cyber Security Student
