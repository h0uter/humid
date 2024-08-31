<a name="readme-top"></a>
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Built with Material for MkDocs](https://img.shields.io/badge/Material_for_MkDocs-526CFE?style=for-the-badge&logo=MaterialForMkDocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)


<!-- PROJECT LOGO -->

<br />
<div align="center">
    <div align="center">
    <img src=".readme/the logo.png" alt="alt text" width="150" height="whatever">
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
  </ol>
</details>

# About the Project

<div align="center">
    <img src=".readme/demo.gif" alt="alt text" width="1000" height="whatever">
</div>

`humid` makes it easy to generate human friendly UUIDs that are readable and pronounceable.

<div align="right">(<a href="#readme-top">back to top</a>)</div>

# Quickstart

install
```sh
pip install humid
python -m humid
>> good-narrow-senior-zigzag-plum-Steelix
```

Use in Python code
```python
from humid import hrid

uuid = hrid()
print(uuid)
>> good-narrow-senior-zigzag-plum-Steelix
```


<div align="right">(<a href="#readme-top">back to top</a>)</div>
