from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

def analyze_packet(packet):
    print("\n" + "=" * 60)

    # IP Layer Information
    if IP in packet:
        print("Source IP       :", packet[IP].src)
        print("Destination IP  :", packet[IP].dst)

        # Protocol Information
        if TCP in packet:
            print("Protocol        : TCP")
            print("Source Port     :", packet[TCP].sport)
            print("Destination Port:", packet[TCP].dport)

        elif UDP in packet:
            print("Protocol        : UDP")
            print("Source Port     :", packet[UDP].sport)
            print("Destination Port:", packet[UDP].dport)

        elif ICMP in packet:
            print("Protocol        : ICMP")

        else:
            print("Protocol        : Other")

    # Payload Information
    if Raw in packet:
        raw_data = packet[Raw].load

        try:
            # Convert bytes into readable text
            payload = raw_data.decode("utf-8")

            # Check if it contains readable characters
            if payload.isprintable():
                print("Payload         :", payload[:200])
            else:
                print("Payload         : Binary / Encrypted Data")

        except UnicodeDecodeError:
            print("Payload         : Binary / Encrypted Data")

    else:
        print("Payload         : No Payload")


print("=" * 60)
print("       NETWORK PACKET CAPTURE PROGRAM")
print("=" * 60)
print("Capturing 10 packets...")
print("Press Ctrl + C to stop early.\n")

try:
    # Capture 10 packets
    sniff(prn=analyze_packet, count=10, store=False)

    print("\n" + "=" * 60)
    print("Packet capture completed successfully!")
    print("=" * 60)

except KeyboardInterrupt:
    print("\nPacket capture stopped by user.")

except PermissionError:
    print("\nError: Please run CMD as Administrator.")

except Exception as e:
    print("\nAn error occurred:", e)
