
# ClearVision Scripts

<p>Scripts designed to assist with managing and modifying SCSS files within the ClearVision theme. These scripts help with tasks like replacing shorthand variables, removing invalid selectors, and converting raw CSS to placeholders. They are intended for use with the ClearVision project but can be modified for individual use cases.</p>

<p><strong>Support:</strong> <a href="https://discord.gg/7pNUC9C">ClearVision Support Server</a></p>

<hr>

<h2>Table of Contents</h2>
<ul>
  <li><a href="#scripts-overview">Scripts Overview</a></li>
  <li><a href="#detect-and-replace">Detect and Replace</a> | <a href="#detect-and-replace-usage">Usage</a></li>
  <li><a href="#remove-invalids">Remove Invalids</a> | <a href="#remove-invalids-usage">Usage</a></li>
  <li><a href="#replace-raw-css">Replace Raw CSS</a> | <a href="#replace-raw-css-usage">Usage</a></li>
</ul>

<hr>

<h2 id="scripts-overview">Scripts Overview</h2>

<p>The ClearVision Scripts help automate certain tasks within the theme, such as replacing shorthand variables, cleaning up obsolete selectors, and converting raw CSS into placeholder names. Below is an overview of each script and its purpose:</p>

<ul>
  <li><strong>Detect and Replace:</strong> Scans SCSS files for shorthand references that can be replaced with variables defined in the <code>variables.scss</code> file.</li>
  <li><strong>Remove Invalids:</strong> Scans SCSS files for placeholder selectors that no longer exist, helping to clean up outdated or orphaned code.</li>
  <li><strong>Replace Raw CSS:</strong> Replaces raw CSS selectors with placeholders, making it easier to manage styles across projects and reduce duplication.</li>
</ul>

<hr>

<h2 id="detect-and-replace">Detect and Replace</h2>
<p>This script aids in finding references that can be shorthand and replacing them with the appropriate variable from the <code>variables.scss</code> file.</p>
<p><strong>Maintained by <a href="https://github.com/babyboysnow">Snow</a></strong></p>

<details>
  <summary>Usage</summary>
  <a id="detect-and-replace-usage"></a>
  <pre><code>
python detect_and_replace.py
</code></pre>

  <p>Modify the <code>variables.scss</code> file to ensure all your shorthands are defined. Run the script to automatically replace any shorthand references in your SCSS files.</p>

  <p><strong>Note:</strong> This script was designed for use with the ClearVision variables and may need modification for other use cases.</p>
</details>

<hr>

<h2 id="remove-invalids">Remove Invalids</h2>
<p>This script scans SCSS files for selectors that no longer exist, helping to clean up invalid placeholders.</p>
<p><strong>Maintained by <a href="https://github.com/babyboysnow">Snow</a></strong></p>

<details>
  <summary>Usage</summary>
  <a id="remove-invalids-usage"></a>
  <pre><code>
python remove_invalids.py
</code></pre>

  <p>Make sure to adjust the <code>selector_file_path</code> and <code>scss_directory</code> in the script to fit your project structure. Running the script will remove any invalid or obsolete selectors from your SCSS files.</p>

  <p><strong>Note:</strong> This script was designed specifically for ClearVision-v6, so some adjustments will be necessary for other projects.</p>
</details>

<hr>

<h2 id="replace-raw-css">Replace Raw CSS</h2>
<p>This script replaces raw CSS selectors with placeholders, making the code more modular and easier to manage.</p>
<p><strong>Maintained by <a href="https://github.com/babyboysnow">Snow</a></strong></p>

<details>
  <summary>Usage</summary>
  <a id="replace-raw-css-usage"></a>
  <pre><code>
python replace_raw_css.py
</code></pre>

  <p>Ensure that the <code>selector_file_path</code> and <code>ignore_files</code> are set correctly for your project. This script will generate placeholders for CSS selectors, using the class name without any suffixes.</p>

  <p><strong>Example:</strong> The class <code>.archivedDivider_a6d69a</code> will be replaced with the placeholder <code>%archivedDivider</code>.</p>
</details>

<hr>
