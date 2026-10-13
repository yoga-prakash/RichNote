<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>RichNote</title>
<style>
  body {
    font-family: -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
    color: #1f2328;
    background: #ffffff;
    line-height: 1.6;
    max-width: 820px;
    margin: 40px auto;
    padding: 0 20px;
  }
  h1 { font-size: 2em; border-bottom: 1px solid #d0d7de; padding-bottom: 8px; }
  h2 { font-size: 1.4em; border-bottom: 1px solid #d0d7de; padding-bottom: 6px; margin-top: 36px; }
  h3 { font-size: 1.1em; margin-top: 24px; }
  code {
    background: #f3f4f6;
    padding: 2px 6px;
    border-radius: 4px;
    font-family: Consolas, "Courier New", monospace;
    font-size: 0.92em;
  }
  pre {
    background: #f6f8fa;
    padding: 14px 16px;
    border-radius: 6px;
    overflow-x: auto;
  }
  pre code { background: none; padding: 0; }
  table { border-collapse: collapse; width: 100%; margin-top: 12px; }
  th, td { border: 1px solid #d0d7de; padding: 8px 12px; text-align: left; }
  th { background: #f6f8fa; }
</style>
</head>
<body>

<h1>RichNote</h1>
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

</body>
</html>
