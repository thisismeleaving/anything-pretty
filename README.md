# anything-pretty
Make the output of any command pretty

# pre-requisites
relies on the fabulous `rich` module. (pip install rich)

# Installation
Symlink `pretty` to your /usr/bin path
`sudo cd /usr/bin && sudo ln -s ~/pretty-anything/pretty pretty`

or

add anything-pretty to your path
`export PATH=~/pretty-anything/:$PATH`

# Usage

```bash
pretty cat ~/some/file.yml
```

```bash
pretty aws iam list-users --output=text
```

```bash
pretty tail -f /var/log/mystuff.log
```
