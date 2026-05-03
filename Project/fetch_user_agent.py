"""
Program untuk mengambil user-agent secara real-time dan selalu update setiap 
1 jam dari repository github HyperBeats/User-Agent-List, 
dan menyimpannya ke dalam file
"""

from ast import While
from urllib import response
import requests
import json 
import sys 
import os 
import rich 
from rich import print 
import pyfiglet

user_agent_desktop = "https://raw.githubusercontent.com/HyperBeats/User-Agent-List/refs/heads/main/useragents-desktop.txt"
user_agent_mobile = "https://raw.githubusercontent.com/HyperBeats/User-Agent-List/refs/heads/main/useragents-android.txt"
    
response_desktop = requests.get(user_agent_desktop)
response_mobile = requests.get(user_agent_mobile)


def fetch_user_agents_desktop():
    if response_desktop.status_code == 200:
        print("[green] Desktop User Agents : [/green]")
        print(response_desktop.text)
        # save to file
        with open("user_agents_desktop.txt", "w") as f:
            f.write(response_desktop.text)
    else:
        print("[red]Failed to fetch desktop user agents![/red]")
def fetch_user_agents_mobile():
    if response_mobile.status_code == 200:
        print("[green] Mobile User Agents : [/green]")
        print(response_mobile.text)
        # save to file
        with open("user_agents_mobile.txt", "w") as f:
            f.write(response_mobile.text)
    else:
        print("[red]Failed to fetch mobile user agents![/red]")
    
def fetch_user_agents_all():
    if response_desktop.status_code == 200 and response_mobile.status_code == 200:
        print("[green] Desktop User Agents : [/green]")
        print(response_desktop.text)
        print("[green] Mobile User Agents : [/green]")
        print(response_mobile.text)
        # save to file
        with open("user_agents_all.txt", "w") as f:
            f.write(response_desktop.text)
            f.write("\n")
            f.write(response_mobile.text)
    else:
        print("[red]Failed to fetch user agents![/red]")

if __name__ == "__main__":
    while True:
        deskripsi = pyfiglet.figlet_format("Fetch User Agent", font="slant")
        print(deskripsi)
        print("[cyan]Program untuk mengambil user-agent[/cyan]")
        print("[yellow]Created by : [red]Ibnu Rusdianto[/red][/yellow]")
        print("1. Fetch Desktop User Agents")
        print("2. Fetch Mobile User Agents")
        print("3. Fetch All User Agents")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            fetch_user_agents_desktop()
            print("[green]User agents saved to user_agents_desktop.txt[/green]")
        elif choice == "2":
            fetch_user_agents_mobile()
            print("[green]User agents saved to user_agents_mobile.txt[/green]")
        elif choice == "3":
            fetch_user_agents_all()
            print("[green]User agents saved to user_agents_all.txt[/green]")
        elif choice == "4":
            print("Exiting...")
            sys.exit(0)
        else:
            print("[red]Invalid choice![/red]")
            
