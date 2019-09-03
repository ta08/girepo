import subprocess
import shlex


def exec_command(command_text):
    cmd = shlex.split(command_text)
    return subprocess.run(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE).stdout.decode('utf-8')


if __name__ == '__main__':
    girepo_help = "girepo --help"
    girepo_simple = "girepo angular/angular facebook/react vuejs/vue"
    girepo_file = "girepo @misc/input.txt"
    gireop_space = r"""girepo " vuetifyjs / vuetify " "kriasoft / react-starter-kit " """

    commands = [
        girepo_help,
        girepo_simple,
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
    - [Simple](#simple)
    - [Input From File](#input-from-file)
    - [Whitespace](#whitespace)
    - [Sort](#sort)

<!-- /TOC -->

## Installation

```
pip install girepo
```

## Usage
<a id="markdown-usage" name="usage"></a>

```markdown
{girepo_dic[girepo_help]}

```
## Realworld Example
<a id="markdown-realworld-example" name="realworld-example"></a>

### Simple
<a id="markdown-simple-case" name="simple-case"></a>

If you want to investigate repositories of frontend framework, you can run this script like below.

```sh
girepo angular/angular facebook/react vuejs/vue 
```

Output:
```markdown
{girepo_dic[girepo_simple]}```

Then you can get the table format of markdown.

{girepo_dic[girepo_simple]}

### Input From File
<a id="markdown-input-from-file-case" name="input-from-file-case"></a>

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
<a id="markdown-whitespace-case" name="whitespace-case"></a>
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
girepo angular/angular facebook/react vuejs/vue  --asc star
``` 
    """

    print(text)
