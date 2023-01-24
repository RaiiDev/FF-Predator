from scapy.all import *

nick_dict = {}


print('''
Este script esta em desenvolvimento,, Apenas para testes, pode ser que não funcione ainda.
BY:Rai
=========================================================================================
    ''')

def free_fire_sniff():
    def packet_callback(packet):
        if packet[TCP].dport == 5222 or packet[TCP].sport == 5222:
            if packet[IP].src != "your_device_ip":
                if packet[IP].src in nick_dict:
                    print(f"[+] Free Fire Packet Captured: {nick_dict[packet[IP].src]} ({packet[IP].src})")
                else:
                    nick_name = input(f"[+] Please enter nick name for IP {packet[IP].src}: ")
                    nick_dict[packet[IP].src] = nick_name
                    print(f"[+] Free Fire Packet Captured: {nick_name} ({packet[IP].src})")
            
    sniff(filter="tcp port 5222", prn=packet_callback, store=0)

free_fire_sniff()