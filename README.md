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
usage: girepo [-h] [--headless]
              [-a {fullname,star,star/day,created_at,updated_at,license,language,description,url} | -d {fullname,star,star/day,created_at,updated_at,license,language,description,url}]
              repo_full_names [repo_full_names ...]

Print Git Repositories information with the markdown format for your
documents. This uses github api without authentication. So you could reach the
rate-limitation if you use this 60 requests per hour.
https://developer.github.com/v3/#rate-limiting Could you take a cup of coffee
☕ until recovering if you exceed.

positional arguments:
  repo_full_names       the target repositories written like owner/repository

optional arguments:
  -h, --help            show this help message and exit
  --headless            not to describe table headers
  -a {fullname,star,star/day,created_at,updated_at,license,language,description,url}, --asc {fullname,star,star/day,created_at,updated_at,license,language,description,url}
                        sort by asc with the field
  -d {fullname,star,star/day,created_at,updated_at,license,language,description,url}, --desc {fullname,star,star/day,created_at,updated_at,license,language,description,url}
                        sort by desc with the field

God bless you.


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
| fullname | star | star/day | created_at | updated_at | license | language | description | url |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| angular/angular | 50,988 | 28.14 | 2014-09-18 | 2019-09-03 | MIT License | TypeScript | One framework. Mobile & desktop. | [link](https://github.com/angular/angular) |
| facebook/react | 135,443 | 59.04 | 2013-05-24 | 2019-09-03 | MIT License | JavaScript | A declarative, efficient, and flexible JavaScript library for building user interfaces. | [link](https://github.com/facebook/react) |
| vuejs/vue | 147,354 | 66.14 | 2013-07-29 | 2019-09-03 | MIT License | JavaScript | 🖖 Vue.js is a progressive, incrementally-adoptable JavaScript framework for building UI on the web. | [link](https://github.com/vuejs/vue) |
```

Then you can get the table format of markdown.

| fullname | star | star/day | created_at | updated_at | license | language | description | url |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| angular/angular | 50,988 | 28.14 | 2014-09-18 | 2019-09-03 | MIT License | TypeScript | One framework. Mobile & desktop. | [link](https://github.com/angular/angular) |
| facebook/react | 135,443 | 59.04 | 2013-05-24 | 2019-09-03 | MIT License | JavaScript | A declarative, efficient, and flexible JavaScript library for building user interfaces. | [link](https://github.com/facebook/react) |
| vuejs/vue | 147,354 | 66.14 | 2013-07-29 | 2019-09-03 | MIT License | JavaScript | 🖖 Vue.js is a progressive, incrementally-adoptable JavaScript framework for building UI on the web. | [link](https://github.com/vuejs/vue) |


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
girepo @misc/input.txt
```

Output:
```markdown
| fullname | star | star/day | created_at | updated_at | license | language | description | url |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| angular/angular | 50,988 | 28.14 | 2014-09-18 | 2019-09-03 | MIT License | TypeScript | One framework. Mobile & desktop. | [link](https://github.com/angular/angular) |
| facebook/react | 135,443 | 59.04 | 2013-05-24 | 2019-09-03 | MIT License | JavaScript | A declarative, efficient, and flexible JavaScript library for building user interfaces. | [link](https://github.com/facebook/react) |
| vuetifyjs/vuetify | 21,359 | 19.65 | 2016-09-12 | 2019-09-03 | MIT License | TypeScript | 🐉 Material Component Framework for Vue.js 2 | [link](https://github.com/vuetifyjs/vuetify) |
| vuejs/vue | 147,354 | 66.14 | 2013-07-29 | 2019-09-03 | MIT License | JavaScript | 🖖 Vue.js is a progressive, incrementally-adoptable JavaScript framework for building UI on the web. | [link](https://github.com/vuejs/vue) |
```


### Whitespace
<a id="markdown-whitespace-case" name="whitespace-case"></a>
when you copy a name of an owner and a repository on a topic page the below, you might get whitespaces between the owner and repository like ` vuetifyjs / vuetify `. So this script enables to parse them. 

![topic_page](misc/screenshot.png)

Please surround the owner/repository name with " if it contains whitespaces. 

```sh
girepo " vuetifyjs / vuetify " "kriasoft / react-starter-kit " 
```

Output:

```markdown
| fullname | star | star/day | created_at | updated_at | license | language | description | url |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| vuetifyjs/vuetify | 21,359 | 19.65 | 2016-09-12 | 2019-09-03 | MIT License | TypeScript | 🐉 Material Component Framework for Vue.js 2 | [link](https://github.com/vuetifyjs/vuetify) |
| kriasoft/react-starter-kit | 19,478 | 9.9 | 2014-04-16 | 2019-09-03 | MIT License | JavaScript | React Starter Kit — isomorphic web app boilerplate (Node.js, Express, GraphQL, React.js, Babel, PostCSS, Webpack, Browsersync) | [link](https://github.com/kriasoft/react-starter-kit) |
```

### etc
<a id="markdown-etc" name="etc"></a>
```sh
girepo angular/angular facebook/react vuejs/vue  --asc star
``` 
    
