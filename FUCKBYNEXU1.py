#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import datetime
import random
import uuid
import re
import instaloader
import requests
from colorama import Fore, Style, init
from pyfiglet import Figlet
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

# ================
# Initialization
# ================
init(autoreset=True)
console = Console()

# ===================================
# Helper Functions: Styling & Loading
# ===================================
def type_effect(text: str, delay: float = 0.03):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    fig = Figlet(font="slant")
    console.print(f"[bold magenta]{fig.renderText('Nᴇxᴜx Iɢ Tᴏᴏʟ')}[/bold magenta]")

def loading_task(description: str, steps: int = 20, delay: float = 0.05):
    with Progress(
        SpinnerColumn(),
        BarColumn(bar_width=None),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as prog:
        task = prog.add_task(description, total=steps)
        for _ in range(steps):
            time.sleep(delay)
            prog.advance(task)

# ====================
# Feature 1: IG Info
# ====================
def fetch_instagram_info(username: str):
    loader = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        loading_task(f"Fᴇᴛᴄʜɪɴɢ @{username} Iɴғᴏ", steps=25)
        print(f"\n{Fore.CYAN}--- Iɴsᴛᴀɢʀᴀᴍ Iɴғᴏ Fᴏʀ @{username} ---{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Fᴜʟʟ Nᴀᴍᴇ     :{Style.RESET_ALL} {profile.full_name}")
        print(f"{Fore.GREEN}Usᴇʀɴᴀᴍᴇ      :{Style.RESET_ALL} {profile.username}")
        print(f"{Fore.GREEN}Bɪᴏ           :{Style.RESET_ALL} {profile.biography}")
        print(f"{Fore.GREEN}Fᴏʟʟᴏᴡᴇʀs     :{Style.RESET_ALL} {profile.followers}")
        print(f"{Fore.GREEN}Fᴏʟʟᴏᴡɪɴɢ     :{Style.RESET_ALL} {profile.followees}")
        print(f"{Fore.GREEN}Pᴏsᴛs         :{Style.RESET_ALL} {profile.mediacount}")
        print(f"{Fore.GREEN}Is Pʀɪᴠᴀᴛᴇ?   :{Style.RESET_ALL} {profile.is_private}")
        print(f"{Fore.GREEN}Is Vᴇʀɪғɪᴇᴅ?  :{Style.RESET_ALL} {profile.is_verified}")
        print(f"{Fore.GREEN}Pʀᴏғɪʟᴇ Pɪᴄ   :{Style.RESET_ALL} {profile.profile_pic_url}\n")
    except Exception as e:
        print(f"{Fore.RED}Eʀʀᴏʀ Fᴇᴛᴄʜɪɴɢ Pʀᴏғɪʟᴇ: {e}{Style.RESET_ALL}")

# ============================================
# Feature 2: User Lookup & Password Reset v5
# ============================================
def user_lookup_and_reset():
    # ensure dependencies
    try:
        from OneClick import Hunter
    except ImportError:
        os.system("pip install OneClick")
        from OneClick import Hunter

    uid_val = str(uuid.uuid4())
    token = uuid.uuid4().hex * 2
    os.system("clear")
    print(f"{Fore.CYAN}====================================")
    print(f"{Fore.MAGENTA}|  Dᴇᴠʟᴏᴀᴘᴇʀ: @GODXNEXU           |")
    print(f"{Fore.MAGENTA}|  TG      : @NEXUXMANAGER       |")
    print(f"{Fore.CYAN}====================================\n")
    user = input(f"{Fore.YELLOW}Eɴᴛᴇʀ Iɴsᴛᴀɢʀᴀᴍ Usᴇʀɴᴀᴍᴇ Tᴏ Lᴏᴏᴋᴜᴘ: {Style.RESET_ALL}").strip()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "i.instagram.com",
        "Connection": "Keep-Alive",
        "User-Agent": Hunter.Services(),
        "Cookie": f"mid={uuid.uuid4()}; csrftoken={token}",
        "Accept-Language": "en-US",
        "X-IG-Capabilities": "AQ==",
        "Accept-Encoding": "gzip",
    }
    data = {
        "q": user,
        "device_id": f"android{uid_val}",
        "guid": uid_val,
        "_csrftoken": token
    }
    loading_task("Looking up user", steps=15)
    resp = requests.post("https://i.instagram.com/api/v1/users/lookup/", headers=headers, data=data).json()
    email = resp.get("obfuscated_email", "N/A")
    pk = resp.get("user", {}).get("pk", "N/A")
    prv = resp.get("user", {}).get("is_private", False)
    has_phone = resp.get("has_valid_phone", False)
    can_email = resp.get("can_email_reset", False)
    can_sms = resp.get("can_sms_reset", False)
    can_wa = resp.get("can_wa_reset", False)
    fb_opt = resp.get("fb_login_option", False)
    phone_no = resp.get("phone_number", "N/A")
    print(f"{Fore.GREEN}UserID           : {pk}")
    print(f"{Fore.GREEN}Is Private?      : {prv}")
    print(f"{Fore.GREEN}Email (obf)      : {email}")
    print(f"{Fore.GREEN}Has Phone?       : {has_phone}")
    print(f"{Fore.GREEN}Can Email Reset? : {can_email}")
    print(f"{Fore.GREEN}Can SMS Reset?   : {can_sms}")
    print(f"{Fore.GREEN}Can WA Reset?    : {can_wa}")
    print(f"{Fore.GREEN}FB Login Opt?    : {fb_opt}")
    print(f"{Fore.GREEN}Phone Number     : {phone_no}\n")

    if input(f"{Fore.YELLOW}Send reset email? (Y/N): {Style.RESET_ALL}").strip().lower() == 'y':
        data2 = {
            "user_email": user,
            "device_id": f"android{uid_val}",
            "guid": uid_val,
            "_csrftoken": token
        }
        loading_task("Sending reset", steps=10)
        r2 = requests.post("https://i.instagram.com/api/v1/accounts/send_password_reset/", headers=headers, data=data2)
        if "obfuscated_email" in r2.text:
            print(f"{Fore.GREEN}✅ Reset sent to {r2.json().get('obfuscated_email')}")
        else:
            print(f"{Fore.RED}❌ Reset failed.")
    input(f"\n{Fore.MAGENTA}Press Enter to continue...{Style.RESET_ALL}")

# ========================
# Feature 3: Report System
# ========================
def report_instagram():
    console.print(f"\n{Fore.CYAN}--- Instagram Report System ---{Style.RESET_ALL}")
    uid_val = str(uuid.uuid4())
    user = input(f"{Fore.YELLOW}Login Username: {Style.RESET_ALL}").strip()
    passwd = input(f"{Fore.YELLOW}Login Password: {Style.RESET_ALL}").strip()
    time.sleep(random.uniform(1.2, 3.5))
    session = requests.Session()
    login = session.post(
        "https://i.instagram.com/api/v1/accounts/login/",
        headers={"User-Agent": "Instagram 114.0.0.38.120 Android"},
        data={"_uuid": uid_val, "device_id": uid_val, "username": user, "password": passwd, "login_attempt_count": "0", "_csrftoken": "missing"},
    )
    if "logged_in_user" not in login.text:
        print(f"{Fore.RED}Login failed.{Style.RESET_ALL}")
        input("\nPress Enter to continue...")
        return
    csrf = login.cookies.get("csrftoken", "")
    console.print("1. Battle Arc Mode\n2. Noti Claiming Mode")
    mode = input(f"{Fore.YELLOW}Mode (1/2): {Style.RESET_ALL}").strip()
    count = int(input(f"{Fore.YELLOW}How many targets? {Style.RESET_ALL}"))
    targets = [input(f"{Fore.YELLOW}Target #{i+1}: {Style.RESET_ALL}").strip() for i in range(count)]
    reasons = ["Spam","Self-Harm","Drugs","Nudity","Violence","Hate","Bullying","Impersonation"]
    for i,r in enumerate(reasons,1):
        console.print(f"{i}. {r}")
    rtype = int(input(f"{Fore.YELLOW}Reason (1-8): {Style.RESET_ALL}"))

    def fetch_id(name):
        time.sleep(random.uniform(1.0, 2.0))
        r = session.get(f"https://www.instagram.com/{name}/?__a=1")
        m = re.search(r'"profile_id":"(\d+)"', r.text)
        return m.group(1) if m else None

    for t in targets:
        tid = fetch_id(t)
        if not tid:
            print(f"{Fore.RED}ID fetch failed for {t}{Style.RESET_ALL}")
            continue
        loading_task(f"Reporting {t}", steps=8)
        rpt = session.post(
            f"https://i.instagram.com/users/{tid}/flag/",
            headers={"X-CSRFToken": csrf, "User-Agent": "Mozilla/5.0"},
            data=f"source_name=&reason_id={rtype}&frx_context="
        )
        if rpt.status_code == 200:
            print(f"{Fore.GREEN}✔ Report sent for {t}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}✖ Report failed for {t}{Style.RESET_ALL}")
    input("\nPress Enter to continue...")

# ========================
# Main Menu & Dispatcher
# ========================
def main_menu():
    while True:
        banner()
        type_effect("Sᴇʟᴇᴄᴛ Aɴ Oᴘᴛɪᴏɴ:", 0.03)
        print(f"{Fore.CYAN}1.{Style.RESET_ALL} Iɴsᴛᴀɢʀᴀᴍ Iɴғᴏ")
        print(f"{Fore.CYAN}2.{Style.RESET_ALL} Lᴏᴏᴋᴜᴘ & Rᴇsᴇᴛ")
        print(f"{Fore.CYAN}3.{Style.RESET_ALL} Rᴇᴘᴏʀᴛ Iɴsᴛᴀɢʀᴀᴍ")
        print(f"{Fore.CYAN}0.{Style.RESET_ALL} Exɪᴛ")
        choice = input(f"{Fore.YELLOW}Eɴᴛᴇʀ Cʜᴏɪᴄᴇ: {Style.RESET_ALL}").strip()
        if choice == "1":
            uname = input(f"{Fore.GREEN}Username: {Style.RESET_ALL}").strip()
            fetch_instagram_info(uname)
            input("\nPress Enter to continue...")
        elif choice == "2":
            user_lookup_and_reset()
        elif choice == "3":
            report_instagram()
        elif choice == "0":
            type_effect("Exiting... Goodbye!", 0.03)
            break
        else:
            print(f"{Fore.RED}Invalid choice.{Style.RESET_ALL}")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
