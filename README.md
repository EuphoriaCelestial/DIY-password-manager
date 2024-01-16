- Actually this is more like a TODO or planning file than a README

- Maybe it is needed to install this, if not installed (not sure if the version is needed)  
<pre>
python3.9  
pip install cryptography==41.0.7
</pre>

- Some shit to run the test file, not actually needed  
<pre>
sudo apt-get install libx11-dev  
pip install keyboard
</pre>

- Planing
1. UI (consider using something else instead of tkinter, it looks dumb)
2. Change the way to store the hashed passphrase (currently fixed in code, configs.py)
3. Save and sync pass to a cloud storage (maybe build it your own or using Google Drive, One Drive, etc.)
4. Find a way to safety transfer data when syncing
5. Find a way to add it to clipboard safely? need it?
6. Maybe add the clipboard history function for Ubuntu (like in Windows)