import tkinter as tk
from tkinter import messagebox
import subprocess

class AWSCLIUtility(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("AWS CLI Utility")

        # AWS CLI Profile Configuration
        self.profile_label = tk.Label(self, text="Profile Name:")
        self.profile_label.grid(row=0, column=0, padx=5, pady=5)

        self.profile_entry = tk.Entry(self)
        self.profile_entry.grid(row=0, column=1, padx=5, pady=5)

        self.configure_button = tk.Button(self, text="Configure Profile", command=self.configure_profile)
        self.configure_button.grid(row=0, column=2, padx=5, pady=5)

        # AWS Access Key Configuration
        self.access_key_label = tk.Label(self, text="Access Key ID:")
        self.access_key_label.grid(row=1, column=0, padx=5, pady=5)

        self.access_key_entry = tk.Entry(self)
        self.access_key_entry.grid(row=1, column=1, padx=5, pady=5)

        self.secret_key_label = tk.Label(self, text="Secret Access Key:")
        self.secret_key_label.grid(row=2, column=0, padx=5, pady=5)

        self.secret_key_entry = tk.Entry(self)
        self.secret_key_entry.grid(row=2, column=1, padx=5, pady=5)

        self.update_keys_button = tk.Button(self, text="Update Access Keys", command=self.update_access_keys)
        self.update_keys_button.grid(row=2, column=2, padx=5, pady=5)

        # S3 Bucket Creation
        self.bucket_label = tk.Label(self, text="Bucket Name:")
        self.bucket_label.grid(row=3, column=0, padx=5, pady=5)

        self.bucket_entry = tk.Entry(self)
        self.bucket_entry.grid(row=3, column=1, padx=5, pady=5)

        self.region_label = tk.Label(self, text="Region:")
        self.region_label.grid(row=4, column=0, padx=5, pady=5)

        self.region_var = tk.StringVar(self)
        self.region_var.set("us-east-1")  # Set default region
        self.region_optionmenu = tk.OptionMenu(self, self.region_var, "us-east-1", "us-east-2")
        self.region_optionmenu.grid(row=4, column=1, padx=5, pady=5)

        self.create_bucket_button = tk.Button(self, text="Create S3 Bucket", command=self.create_s3_bucket)
        self.create_bucket_button.grid(row=4, column=2, padx=5, pady=5)

    def configure_profile(self):
        profile_name = self.profile_entry.get()
        if not profile_name:
            messagebox.showerror("Error", "Please enter a profile name.")
            return

        # Run the aws configure command with the provided profile name
        command = f"aws configure --profile {profile_name}"
        subprocess.run(command, shell=True)

    def update_access_keys(self):
        access_key_id = self.access_key_entry.get()
        secret_access_key = self.secret_key_entry.get()

        if not access_key_id or not secret_access_key:
            messagebox.showerror("Error", "Please enter both Access Key ID and Secret Access Key.")
            return

        # Run the aws configure command to update access keys
        command = f"aws configure set aws_access_key_id {access_key_id}"
        subprocess.run(command, shell=True)

        command = f"aws configure set aws_secret_access_key {secret_access_key}"
        subprocess.run(command, shell=True)

    def create_s3_bucket(self):
        bucket_name = self.bucket_entry.get()
        if not bucket_name:
            messagebox.showerror("Error", "Please enter a bucket name.")
            return

        region = self.region_var.get()

        # Run the aws s3api create-bucket command
        command = f"aws s3api create-bucket --bucket {bucket_name} --region {region}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            messagebox.showinfo("Success", f"Bucket {bucket_name} created successfully!")
            self.bucket_entry.delete(0, tk.END)  # Clear the entry after successful creation
        else:
            messagebox.showerror("Error", result.stderr)

if __name__ == "__main__":
    app = AWSCLIUtility()
    app.mainloop()
