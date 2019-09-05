import subprocess
import shlex


def exec_command(command_text):
    cmd = shlex.split(command_text)
    return subprocess.run(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE).stdout.decode('utf-8')


if __name__ == '__main__':
    girepo_help = "girepo --help"
    girepo_simple = "girepo strict angular/angular facebook/react vuejs/vue"
    girepo_rough_simple = "girepo rough angular react vue"
    girepo_file = "girepo strict @misc/input.txt"
    gireop_space = r"""girepo strict " vuetifyjs / vuetify " "kriasoft / react-starter-kit " """

    commands = [
        girepo_help,
        girepo_simple,
        girepo_rough_simple,
        girepo_file,
        gireop_space
    ]

    girepo_dic = {}

    for command in commands:
        girepo_dic[command] = exec_command(command)

    text = f"""
# girepo
<a id="markdown-girepo" name="girepo"></a>

This makes it easy to investigate repositories at Github and to describe the results as a markdown table format. 

<!-- TOC -->

- [Installation](#installation)
- [Usage](#usage)
- [Realworld Example](#realworld-example)
    - [Simple (ver. strict)](#simple-ver-strict)
    - [Simple (ver. rough)](#simple-ver-rough)
    - [Input From File](#input-from-file)
    - [Whitespace](#whitespace)
    - [etc](#etc)

<!-- /TOC -->

## Installation
<a id="markdown-installation" name="installation"></a>

```
pip install girepo
```

## Usage
<a id="markdown-usage" name="usage"></a>

```
{girepo_help}
```


```markdown
{girepo_dic[girepo_help]}

```
## Realworld Example
<a id="markdown-realworld-example" name="realworld-example"></a>

### Simple (ver. strict)
<a id="markdown-simple-ver-strict" name="simple-ver-strict"></a>

If you want to investigate repositories of frontend framework, you can run this script like below.

```sh
{girepo_simple} 
```

Output:
```markdown
{girepo_dic[girepo_simple]}```

Then you can get the table format of markdown.

{girepo_dic[girepo_simple]}

### Simple (ver. rough)
<a id="markdown-simple-ver-rough" name="simple-ver-rough"></a>

If you want to investigate repositories of frontend framework, you can run this script like below.

```sh
{girepo_rough_simple}
```

Output:
```markdown
{girepo_dic[girepo_rough_simple]}```

Then you can get the table format of markdown.

{girepo_dic[girepo_rough_simple]}


### Input From File
<a id="markdown-input-from-file" name="input-from-file"></a>

If you want to use a bulk input, please prepare a file whose content is like below. Do not contain a blank line.

```markdown
angular/angular
facebook/react
vuetifyjs / vuetify
vuejs/vue
```

For example, if the file name is ./misc/input.txt, then

```sh
{girepo_file}
```

Output:
```markdown
{girepo_dic[girepo_file]}```


### Whitespace
<a id="markdown-whitespace" name="simple-whitespace"></a>

when you copy a name of an owner and a repository on a topic page the below, you might get whitespaces between the owner and repository like ` vuetifyjs / vuetify `. So this script enables to parse them. 

![topic_page](misc/screenshot.png)

Please surround the owner/repository name with " if it contains whitespaces. 

```sh
{gireop_space}
```

Output:

```markdown
{girepo_dic[gireop_space]}```

### etc
<a id="markdown-etc" name="etc"></a>

```sh
girepo strict angular/angular facebook/react vuejs/vue  --asc star
```

```sh
girepo rough angular react vue  --headless
```

"""

    print(text)
