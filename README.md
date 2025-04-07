<<<<<<< HEAD
Who's Down Application

  This application allows you to check which servers/Gateways/switches/routers/computers are down in your network in seconds.

How to use
  add your server names and IP addresses into the servers.txt file in the following method
    cloudflare 1.1.1.1
    amazon 52.94.236.248

How this works
  This application/script have fully automated the ping process we does in day today life when we checking for servers and devices availability.
  This script pings every IP address you've supplied and return the device name thats not reply for the ping request.

Why Special
  When we say automating we can imagine pinging one after another like we usually do and that will probably take longer time if your network have hundreds of servers and devices.
  So the special thing about this script is multithread all the ping requests and return you the feedback in seconds.yes, thats it. Don't matter how many servers we have. it pings all at once.

GUI coming soon!!!!!

  
=======
# 👀 Who's Down Application

A simple and powerful tool to check which **servers**, **gateways**, **switches**, **routers**, or **computers** are down in your network — **in seconds**.

---

## 🚀 Features

- 🔍 Instantly detect unresponsive devices in your network.
- ⚡ Multithreaded pinging for lightning-fast results.
- 🧠 Automates the tedious process of manually checking server availability.
- 📄 Easy-to-configure `servers.txt` for managing your devices.
- 🧑‍💻 CLI-based tool — **GUI coming soon!**

---

## 📂 How to Use

1. Add your device names and IP addresses into a file called `servers.txt` using this format:

    ```
    cloudflare 1.1.1.1
    amazon 52.94.236.248
    ```

2. Run the script/application.

3. It will ping all the IPs **simultaneously** and show which ones are **not responding**.

---

## ⚙️ How It Works

- The script automates the basic `ping` process.
- It takes every IP address from your `servers.txt` and sends out ping requests **in parallel**.
- Any device that **fails to respond** will be listed as **down**.
- No need to wait — everything happens almost instantly thanks to **multithreading**.

---

## 🌟 Why It’s Special

Traditional automation often pings devices one by one — which can be **slow** in large networks.

This script:
- Pings **all devices at once**
- Returns results in **just seconds**, even with **hundreds of IPs**
- Saves your time, effort, and sanity 🔥

---

## 🖥️ GUI Coming Soon!

A clean graphical interface is on the way to make this even easier to use. Stay tuned!

---

## 📌 License

This project is open-source. Feel free to contribute or modify it for your own needs.
>>>>>>> 9ee76045cfa27b277258fdd3ae8b00f140513d32
