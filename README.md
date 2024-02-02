# How to use
Login into your livechart.me account and go to your [list](https://www.livechart.me/users/yourusername/library).


Select all or some of your lists. Press F12 and find `script id="library_entries"`. Open it and copy everything
into a .txt file. If your currently selected list has multiple pages, you should do it for every page. 
Place .txt file and this script into same directory. Enter the .txt name into loadtxt. 

Like this:
`f = np.loadtxt('YOUR TXT HERE.txt', dtype="str", delimiter="\0").tolist()`

Run the script.

After completion you'll find file animelist.txt with all your entries in the same path.
