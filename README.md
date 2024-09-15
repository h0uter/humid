<a name="readme-top"></a>
[![text](https://img.shields.io/pypi/v/humid?logo=python&logoColor=%23cccccc)](https://pypi.org/project/humid/)
[![Downloads](https://static.pepy.tech/badge/humid)](https://pepy.tech/project/humid)
![tests](https://github.com/h0uter/humid/workflows/Test/badge.svg)
[![PDM](https://camo.githubusercontent.com/2f56a2dc4c9b19beec5347774a078871a81e00d624a51fe9cc20a8ae8ac4e957/68747470733a2f2f696d672e736869656c64732e696f2f656e64706f696e743f75726c3d687474707325334125324625324663646e2e6a7364656c6976722e6e6574253246676825324670646d2d70726f6a6563742532462e67697468756225324662616467652e6a736f6e)](https://pdm-project.org/en/latest/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://pre-commit.com/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Built with Material for MkDocs](https://img.shields.io/badge/Material_for_MkDocs-526CFE?style=for-the-badge&logo=MaterialForMkDocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)

<!-- PROJECT LOGO -->

<br />
<div align="center">
    <div align="center">
    <!-- <img src=".readme/the logo.png" alt="alt text" width="250" height="whatever"> -->
    <img src="https://raw.githubusercontent.com/h0uter/humid/main/.readme/the%20logo.png" alt="alt text" width="250" height="whatever">
    </div>
  <!-- <h3 align="center">humid</h3> -->

  <p align="center">
    Human Friendly UUIDs
    <br />
    <a href="https://h0uter.github.io/humid"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/h0uter/humid/issues/new?labels=bug&title=New+bug+report">Report Bug</a>
    ·
    <a href="https://github.com/h0uter/humid/issues/new?labels=enhancement&title=New+feature+request">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About the Project</a></li>
    <li><a href="#quickstart">Quickstart</a></li>
    <li><a href="#why-humid">Why humid?</a></li>
  </ol>
</details>

# About the Project

<div align="center">
    <img src="https://raw.githubusercontent.com/h0uter/humid/main/.readme/demo.gif" alt="alt text" width="1000" height="whatever">
</div>

`humid` makes it easy to generate **h**uman **F**riendly uu**id**'s (`hfid`'s) that are readable and pronounceable. Creation follows the pattern: `{ADJECTIVE}-{ANIMAL|POKEMON}-{UUID*22}`.

<div align="right">(<a href="#readme-top">back to top</a>)</div>

# Quickstart

Install and run from shell

```sh
> pip install humid
> python -m humid
archaic-goose-y8yMIYjt91V8cejIxMa6G4
# or
> humid
archaic-goose-y8yMIYjt91V8cejIxMa6G4
```

Use in Python code

```python
>> from humid import hfid

>> uuid = hfid()
>> print(uuid)
archaic-goose-y8yMIYjt91V8cejIxMa6G4
```

<div align="right">(<a href="#readme-top">back to top</a>)</div>

# Why HUMan friendly IDs?
- **Improved Usability and Readability::** Human friendly IDs are easier to remember, recognize, and read compared to traditional IDs (like UUIDs or hashes). For example, instead of dealing with an ID like `4f52a6c7-e938-4d5e-9ad6-d89d62c7a90b`, a human friendly ID such as `archaic-goose-y8yMIYjt91V8cejIxMa6G4` is far more user-friendly.

- **Enhanced Communication::** When IDs are readable, they can be easily communicated over different channels, such as spoken language, emails, or text messages. This is especially useful in contexts like customer support or during collaborative work sessions, where team members need to quickly and accurately communicate specific IDs.

<div align="right">(<a href="#readme-top">back to top</a>)</div>
