# How to use
Login to your livechart.me account and go to ```https://www.livechart.me/users/%yourusername%/library```. Replace ```%yourusername%``` with your actual username.


Select all or some of your lists. Press F12 and search for `script id="library_entries"`. Open it and copy everything
to a .txt file. If your currently selected list has multiple pages, you should do this for each page. 
Place .txt file and this script into same directory. Enter the .txt name into loadtxt. 

Like this:
`f = np.loadtxt('YOUR TXT HERE.txt', dtype="str", delimiter="\0").tolist()`

Run the script.

When it finishes, you'll find a file called animelist.txt with all your entries in the same path.
