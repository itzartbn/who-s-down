import tkinter as tk
from tkinter import messagebox, simpledialog, Scrollbar
from check_servers import load_servers, save_servers, add_server, remove_server_by_name, check_servers

class ServerCheckerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Who's Down - Server Checker")
        self.master.configure(bg="white")
        self.servers = load_servers()
        self.check_vars = []

        # Search Bar
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.filter_servers)
        tk.Entry(master, textvariable=self.search_var, width=30).place(x=20, y=10)

        # Server Frame
        self.server_frame = tk.Frame(master, bg="white", bd=2, relief="groove")
        self.server_frame.place(x=20, y=40, width=400, height=400)

        # Select All Checkbox
        self.select_all_var = tk.BooleanVar()
        self.select_all_checkbox = tk.Checkbutton(self.server_frame, text="Select All", variable=self.select_all_var, bg="white", command=self.toggle_all, bd=1, relief="ridge")
        self.select_all_checkbox.pack(anchor="w")

        # Scrollbar + List
        self.scroll_canvas = tk.Canvas(self.server_frame, bg="white", highlightthickness=0)
        self.scroll_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.checkbox_frame = tk.Frame(self.scroll_canvas, bg="white")
        self.scroll_window = self.scroll_canvas.create_window((0, 0), window=self.checkbox_frame, anchor="nw")
        self.scrollbar = Scrollbar(self.server_frame, orient="vertical", command=self.scroll_canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill="y")
        self.scroll_canvas.configure(yscrollcommand=self.scrollbar.set)
        self.checkbox_frame.bind("<Configure>", lambda e: self.scroll_canvas.configure(scrollregion=self.scroll_canvas.bbox("all")))

        # Reply Box
        self.reply_box = tk.Text(master, width=47, height=8, bg="white", bd=2, relief="solid")
        self.reply_box.place(x=450, y=140)

        # Buttons
        tk.Button(master, text="Add Server", command=self.add_server).place(x=450, y=40)
        tk.Button(master, text="Remove Server", command=self.remove_server_popup).place(x=540, y=40)
        self.check_btn = tk.Button(master, text="Check", command=self.check_selected_servers, height=2, width=10)
        self.check_btn.place(x=580, y=400)

        self.display_servers()

    def display_servers(self, filtered=None):
        for widget in self.checkbox_frame.winfo_children():
            widget.destroy()
        self.check_vars.clear()

        self.server_display_list = filtered if filtered is not None else self.servers

        for name, ip in self.server_display_list:
            var = tk.BooleanVar()
            cb = tk.Checkbutton(self.checkbox_frame, text=f"{name}\n{ip}", variable=var, bg="white", anchor="w", justify="left", bd=1, relief="ridge")
            cb.pack(fill="x", padx=2, pady=2, anchor="w")
            self.check_vars.append((var, name, ip))

    def toggle_all(self):
        for var, _, _ in self.check_vars:
            var.set(self.select_all_var.get())

    def update_select_all_state(self):
        all_selected = all(var.get() for var, _, _ in self.check_vars)
        self.select_all_var.set(all_selected)

    def add_server(self):
        input_val = simpledialog.askstring("Add Server", "Enter server as 'name ip':")
        if input_val:
            parts = input_val.strip().split()
            if len(parts) == 2:
                add_server(parts[0], parts[1])
                self.servers = load_servers()
                self.display_servers()
                self.update_select_all_state()
            else:
                messagebox.showerror("Invalid Format", "Enter in format: name ip")

    def remove_server_popup(self):
        popup = tk.Toplevel(self.master)
        popup.title("Remove Servers")
        popup.geometry("300x400")

        frame = tk.Frame(popup)
        frame.pack(fill="both", expand=True)

        canvas = tk.Canvas(frame)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)

        inner_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")

        remove_vars = []

        for name, ip in self.servers:
            var = tk.BooleanVar()
            cb = tk.Checkbutton(inner_frame, text=f"{name} ({ip})", variable=var, anchor="w")
            cb.pack(fill="x", padx=5, pady=2, anchor="w")
            remove_vars.append((var, name, ip))

        def confirm_remove():
            selected = [(name, ip) for var, name, ip in remove_vars if var.get()]
            remove_servers(selected)
            self.servers = load_servers()
            self.display_servers()
            self.update_select_all_state()
            popup.destroy()

        tk.Button(popup, text="Remove", command=confirm_remove).pack(pady=5)
        inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    def check_selected_servers(self):
        self.check_btn.config(relief="sunken")
        selected = [(name, ip) for var, name, ip in self.check_vars if var.get()]
        if not selected:
            messagebox.showwarning("No Selection", "Select at least one server.")
            self.check_btn.config(relief="raised")
            return

        down = check_servers(selected)
        self.reply_box.delete(1.0, tk.END)
        if down:
            self.reply_box.insert(tk.END, "The following servers are not responding:\n")
            for name, ip in down:
                self.reply_box.insert(tk.END, f"{name} ({ip})\n")
        else:
            self.reply_box.insert(tk.END, "All servers are up.")
        self.update_select_all_state()
        self.check_btn.config(relief="raised")

    def filter_servers(self, *args):
        keyword = self.search_var.get().lower()
        if not keyword:
            self.display_servers()
        else:
            filtered = [s for s in self.servers if keyword in s[0].lower()]
            self.display_servers(filtered)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("700x480")
    app = ServerCheckerApp(root)
    root.mainloop()
