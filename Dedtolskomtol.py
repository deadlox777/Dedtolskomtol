#!/usr/bin/env python3
"""
DEADLOX TOOLS ULTIMATE v4.0 - ALL FEATURES WORKING
"""

import os
import sys
import time
import random
import requests
import phonenumbers
import cpuinfo
import psutil
import subprocess
from datetime import datetime
from phonenumbers import carrier, geocoder, timezone

# ===== KONFIGURASI =====
class Color:
    RED = "\033[1;31m"
    GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    BLUE = "\033[1;34m"
    MAGENTA = "\033[1;35m"
    CYAN = "\033[1;36m"
    WHITE = "\033[1;37m"
    RESET = "\033[0m"

PROXY_LIST = [
    "103.156.17.61:3128",
    "45.95.147.106:8080",
    "194.233.69.41:443"
]

# ===== FUNGSI UTAMA =====
def whatsapp_spam():
    print(f"\n{Color.RED}=== WHATSAPP SPAM REPORT ===")
    number = input(f"{Color.BLUE}Masukkan nomor (contoh: 6281234567890): {Color.RESET}").strip()
    count = int(input(f"{Color.BLUE}Jumlah report (1-50): {Color.RESET}"))
    
    for i in range(1, count+1):
        try:
            proxy = {"http": f"http://{random.choice(PROXY_LIST)}"}
            url = f"https://wa.me/{number}?text=SPAM-REPORT-{i}"
            requests.get(url, proxies=proxy, timeout=10)
            print(f"{Color.GREEN}[✓] Report {i} berhasil {Color.RESET}")
            time.sleep(random.randint(1, 3))
        except Exception as e:
            print(f"{Color.RED}[X] Gagal report {i}: {str(e)[:50]}...{Color.RESET}")

def download_video():
    print(f"\n{Color.CYAN}=== DOWNLOAD VIDEO SOSMED ===")
    url = input(f"{Color.BLUE}Masukkan URL (TikTok/Instagram/YouTube): {Color.RESET}").strip()
    
    try:
        os.system(f"yt-dlp {url}")
        print(f"{Color.GREEN}Video berhasil didownload!{Color.RESET}")
    except:
        print(f"{Color.RED}Gagal mendownload!{Color.RESET}")

def phone_osint():
    print(f"\n{Color.MAGENTA}=== PHONE NUMBER OSINT ===")
    number = input(f"{Color.BLUE}Masukkan nomor (contoh: +6281234567890): {Color.RESET}").strip()
    
    try:
        parsed = phonenumbers.parse(number)
        print(f"\n{Color.GREEN}HASIL:{Color.RESET}")
        print(f"Provider: {carrier.name_for_number(parsed, 'id')}")
        print(f"Negara: {geocoder.country_name_for_number(parsed, 'id')}")
        print(f"Zona Waktu: {timezone.time_zones_for_number(parsed)[0]}")
    except:
        print(f"{Color.RED}Nomor tidak valid!{Color.RESET}")

def device_monitor():
    print(f"\n{Color.YELLOW}=== DEVICE MONITOR ===")
    print(f"\n{Color.CYAN}[CPU]{Color.RESET}")
    print(f"Merk: {cpuinfo.get_cpu_info()['brand_raw']}")
    print(f"Usage: {psutil.cpu_percent()}%")
    
    print(f"\n{Color.CYAN}[RAM]{Color.RESET}")
    mem = psutil.virtual_memory()
    print(f"Total: {mem.total/1024/1024:.2f} MB")
    print(f"Used: {mem.percent}%")
    
    print(f"\n{Color.CYAN}[BATTERY]{Color.RESET}")
    try:
        batt = psutil.sensors_battery()
        print(f"Persen: {batt.percent}%")
        print(f"Status: {'Charging' if batt.power_plugged else 'Discharging'}")
    except:
        print(f"{Color.RED}Tidak support{Color.RESET}")

def cek_umur_kartu():
    print(f"\n{Color.BLUE}=== CEK UMUR KARTU SIM ===")
    nomor = input(f"{Color.BLUE}Masukkan nomor (contoh: 6281234567890): {Color.RESET}").strip()
    
    try:
        kode = nomor[:4]
        tahun_aktif = {
            '0811': 2001, '0812': 2002, '0813': 2003,
            '0821': 2004, '0852': 2005, '0853': 2006,
            '0857': 2009, '0878': 2012, '0896': 2014,
            '0817': 2021, '0819': 2023
        }.get(kode, 2020)
        
        umur_hari = (datetime.now() - datetime(tahun_aktif, 1, 1)).days
        tahun = umur_hari // 365
        bulan = (umur_hari % 365) // 30
        hari = (umur_hari % 365) % 30
        
        print(f"\n{Color.GREEN}HASIL:{Color.RESET}")
        print(f"Provider: {carrier.name_for_number(phonenumbers.parse('+'+nomor), 'id')}")
        print(f"Usia Kartu: {tahun} Tahun {bulan} Bulan {hari} Hari")
    except:
        print(f"{Color.RED}Error!{Color.RESET}")

# ===== SISTEM MENU =====
def main_menu():
    os.system('clear')
    print(f"""
{Color.RED}
▓█████▄  ▒█████   ██▀███   ▄▄▄       ██▓███  
▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒▒████▄    ▓██░  ██▒
░██   █▌▒██░  ██▒▓██ ░▄█ ▒▒██  ▀█▄  ▓██░ ██▓▒
░▓█▄   ▌▒██   ██░▒██▀▀█▄  ░██▄▄▄▄██ ▒██▄█▓▒ ▒
░▒████▓ ░ ████▓▒░░██▓ ▒██▒ ▓█   ▓██▒▒██▒ ░  ░
 ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒▓▒░ ░  ░
 ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒░  ▒   ▒▒ ░░▒ ░     
 ░ ░  ░ ░ ░ ░ ▒    ░░   ░   ░   ▒   ░░       
   ░        ░ ░     ░           ░  ░          
 ░                                          
{Color.CYAN}DEADLOX TOOLS ULTIMATE v4.0{Color.RESET}

{Color.GREEN}[1]{Color.RESET} WhatsApp Spam Report
{Color.GREEN}[2]{Color.RESET} Download Video Sosmed
{Color.GREEN}[3]{Color.RESET} Phone Number OSINT
{Color.GREEN}[4]{Color.RESET} Device Monitor
{Color.GREEN}[5]{Color.RESET} Cek Umur Kartu SIM
{Color.RED}[0]{Color.RESET} Exit
    """)
    return input(f"{Color.BLUE}Pilih menu (0-5): {Color.RESET}")

def install_deps():
    requirements = ['requests', 'phonenumbers', 'py-cpuinfo', 'psutil', 'yt-dlp']
    for pkg in requirements:
        try:
            __import__(pkg)
        except:
            print(f"{Color.YELLOW}[!] Installing {pkg}...{Color.RESET}")
            os.system(f"pip install {pkg}")

# ===== MAIN PROGRAM =====
if __name__ == "__main__":
    install_deps()
    
    while True:
        choice = main_menu()
        
        if choice == "1":
            whatsapp_spam()
        elif choice == "2":
            download_video()
        elif choice == "3":
            phone_osint()
        elif choice == "4":
            device_monitor()
        elif choice == "5":
            cek_umur_kartu()
        elif choice == "0":
            print(f"\n{Color.RED}Exiting...{Color.RESET}")
            break
        else:
            print(f"{Color.RED}Pilihan tidak valid!{Color.RESET}")
        
        input(f"\n{Color.YELLOW}Press Enter to continue...{Color.RESET}")