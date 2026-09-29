# the room tackled using this is on AfricanHackon X Dojo platform. sequence Break

import scapy.all as scapy

    pkts = scapy.rdpcap("capture.pcap")

    # Extract initial sequence numbers (ISNs) from SYN packets targeting 45.33.22.11:4444
    seqs = [
        p[scapy.TCP].seq for p in pkts 
        if p.haslayer(scapy.IP) and p[scapy.IP].dst == "45.33.22.11" and p[scapy.TCP].flags == "S"
    ]

    # Extract lowest byte of each sequence number
    flag = bytes([s % 256 for s in seqs]).decode("utf-8")
    print(f"Flag: {flag}")
