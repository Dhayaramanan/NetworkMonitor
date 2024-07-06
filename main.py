import pandas as pd

from datetime import datetime
from scapy.all import sniff


def main():
    while True:
        packets = sniff(timeout=5)
        number_of_packets = len(packets)
        total_size = 0
        for packet in packets:
            total_size += len(packet)
        current_time = datetime.now()
        data = pd.DataFrame([[current_time.strftime("%d/%m/%Y"), current_time.strftime("%H:%M:%S"), number_of_packets,
                              total_size]])
        with open('network_data.csv', 'a', newline='') as f:
            data.to_csv(f, index=False, header=False)


if __name__ == '__main__':
    main()
