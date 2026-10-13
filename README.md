<h1>RichNote</h1>
<p>This project is no longer maintained so please if any pull requests do so with caution.</p>
<p>A simple desktop text editor built with Python and PySide6. Create and edit text files, and add tables, images and hyperlinks to your notes. Notes that contain these items are saved as Markdown (<code>.md</code>) files.</p>
<h2>Features</h2>
<h3>File Management</h3>
<ul>
<li><strong>New File</strong> (<code>Ctrl+N</code>): Opens a new, empty note in a separate window so you can work on several notes at once.</li>
<li><strong>Open</strong> (<code>Ctrl+O</code>): Opens an existing <code>.txt</code> or <code>.md</code> file. Markdown files are displayed with their tables, images and links.</li>
<li><strong>Save</strong> (<code>Ctrl+S</code>): Saves your note. On the first save you choose the file name and location; later saves update the same file.</li>
<li><strong>Exit</strong> (<code>Ctrl+E</code>): Closes the application and asks whether you want to save your work first.</li>
</ul>
<h3>Editing</h3>
<ul>
<li><strong>Table</strong> (<code>Ctrl+T</code>): Inserts a table at the cursor. You enter the number of rows and columns.</li>
<li><strong>Image</strong> (<code>Ctrl+I</code>): Inserts a <code>.png</code>, <code>.jpg</code> or <code>.jpeg</code> image at the cursor.</li>
<li><strong>Hyperlink</strong> (<code>Ctrl+H</code>): Adds a link to your note. Select text first to turn it into a link, or enter only a URL to insert it as a link.</li>
</ul>
<h3>Automatic Markdown Saving</h3>
<ul>
<li>A note with plain text only is saved as plain text (<code>.txt</code>, <code>.py</code> or any file type).</li>
<li>A note that contains a table, image or link is saved as a Markdown (<code>.md</code>) file.</li>
<li>If you open a <code>.txt</code> file and then add a table, image or link, saving asks for a new <code>.md</code> file name, so your original <code>.txt</code> file is not overwritten.</li>
<li>Images are saved by file path, so they appear when the note is reopened only if the image is still in the same location.</li>
</ul>
<h3>Status Bar</h3>
<ul>
<li>Shows today's date on the left.</li>
<li>Shows a live clock on the right, updated every second.</li>
</ul>
<h3>Interface</h3>
<ul>
<li>Plain writing area with a "Type here!" placeholder.</li>
<li>The window title shows the current file name, or "Untitled" for new notes.</li>
<li>Default window size of 1000 x 700.</li>
</ul>
<h2>Keyboard Shortcuts</h2>
<table>
<thead>
<tr><th>Shortcut</th><th>Action</th></tr>
</thead>
<tbody>
<tr><td><code>Ctrl+N</code></td><td>New File</td></tr>
<tr><td><code>Ctrl+O</code></td><td>Open</td></tr>
<tr><td><code>Ctrl+S</code></td><td>Save</td></tr>
<tr><td><code>Ctrl+E</code></td><td>Exit</td></tr>
<tr><td><code>Ctrl+T</code></td><td>Insert Table</td></tr>
<tr><td><code>Ctrl+I</code></td><td>Insert Image</td></tr>
<tr><td><code>Ctrl+H</code></td><td>Insert Hyperlink</td></tr>
</tbody>
</table>
<h2>Comparison with Notepad</h2>
<p>How RichNote compares with the classic Windows Notepad. Newer versions of Notepad have added some features, so results vary by Windows version.</p>
<table>
<thead>
<tr><th>Capability</th><th>RichNote</th><th>Notepad</th></tr>
</thead>
<tbody>
<tr><td>Edit and save plain text</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Insert tables</td><td>Yes</td><td>No</td></tr>
<tr><td>Insert images</td><td>Yes</td><td>No</td></tr>
<tr><td>Insert hyperlinks</td><td>Yes</td><td>No</td></tr>
<tr><td>Automatic Markdown saving</td><td>Yes</td><td>No</td></tr>
<tr><td>Open Markdown files with tables, images and links shown</td><td>Yes</td><td>No, opens as plain text</td></tr>
<tr><td>Multiple note windows</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Date and live clock in status bar</td><td>Yes</td><td>No</td></tr>
<tr><td>AI features</td><td>None</td><td>Optional in newer versions</td></tr>
<tr><td>Find and replace</td><td>Not yet</td><td>Yes</td></tr>
<tr><td>Tabs</td><td>Not yet</td><td>Newer versions</td></tr>
<tr><td>Word wrap, zoom and font settings</td><td>Not yet</td><td>Yes</td></tr>
<tr><td>Line and column numbers</td><td>Not yet</td><td>Yes</td></tr>
<tr><td>Save As</td><td>Not yet</td><td>Yes</td></tr>
</tbody>
</table>
<h2>Requirements</h2>
<ul>
<li>Python 3.9 or later</li>
<li>PySide6</li>
</ul>
<h2>Installation</h2>
<pre><code>pip install PySide6</code></pre>
<h2>Usage</h2>
<p>Run the application from your project folder:</p>
<pre><code>python main.py</code></pre>
