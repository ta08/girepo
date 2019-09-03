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
usage: girepo [-h]
              [-a {owner,name,star,star/day,created_at,updated_at,license,language,description,url} | -d {owner,name,star,star/day,created_at,updated_at,license,language,description,url}]
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
  -a {owner,name,star,star/day,created_at,updated_at,license,language,description,url}, --asc {owner,name,star,star/day,created_at,updated_at,license,language,description,url}
                        sort by asc with the field
  -d {owner,name,star,star/day,created_at,updated_at,license,language,description,url}, --desc {owner,name,star,star/day,created_at,updated_at,license,language,description,url}
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
| owner | name | star | star/day | created_at | updated_at | license | language | description | url |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| angular | angular | 50978 | 28.15 | 2014-09-18 | 2019-09-03 | MIT License | TypeScript | One framework. Mobile & desktop. | https://github.com/angular/angular |
| facebook | react | 135433 | 59.06 | 2013-05-24 | 2019-09-03 | MIT License | JavaScript | A declarative, efficient, and flexible JavaScript library for building user interfaces. | https://github.com/facebook/react |
| vuejs | vue | 147347 | 66.13 | 2013-07-29 | 2019-09-03 | MIT License | JavaScript | 🖖 Vue.js is a progressive, incrementally-adoptable JavaScript framework for building UI on the web. | https://github.com/vuejs/vue |
```

Then you can get the table format of markdown.

| owner | name | star | star/day | created_at | updated_at | license | language | description | url |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| angular | angular | 50978 | 28.15 | 2014-09-18 | 2019-09-03 | MIT License | TypeScript | One framework. Mobile & desktop. | https://github.com/angular/angular |
| facebook | react | 135433 | 59.06 | 2013-05-24 | 2019-09-03 | MIT License | JavaScript | A declarative, efficient, and flexible JavaScript library for building user interfaces. | https://github.com/facebook/react |
| vuejs | vue | 147347 | 66.13 | 2013-07-29 | 2019-09-03 | MIT License | JavaScript | 🖖 Vue.js is a progressive, incrementally-adoptable JavaScript framework for building UI on the web. | https://github.com/vuejs/vue |


### Input From File
<a id="markdown-input-from-file-case" name="input-from-file-case"></a>

If you want to use a bulk input, please prepare a file whose content is like below. Do not contain a blank line.

```markdown
angular/angular
facebook/react
vuetifyjs / vuetify
vuejs/vue
```

For example, if the file name is ./doc/input.txt, then

```sh
girepo @misc/input.txt
```

Output:
```markdown
| owner | name | star | star/day | created_at | updated_at | license | language | description | url |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| angular | angular | 50978 | 28.15 | 2014-09-18 | 2019-09-03 | MIT License | TypeScript | One framework. Mobile & desktop. | https://github.com/angular/angular |
| facebook | react | 135433 | 59.06 | 2013-05-24 | 2019-09-03 | MIT License | JavaScript | A declarative, efficient, and flexible JavaScript library for building user interfaces. | https://github.com/facebook/react |
| vuetifyjs | vuetify | 21358 | 19.65 | 2016-09-12 | 2019-09-03 | MIT License | TypeScript | 🐉 Material Component Framework for Vue.js 2 | https://github.com/vuetifyjs/vuetify |
| vuejs | vue | 147347 | 66.13 | 2013-07-29 | 2019-09-03 | MIT License | JavaScript | 🖖 Vue.js is a progressive, incrementally-adoptable JavaScript framework for building UI on the web. | https://github.com/vuejs/vue |
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
| owner | name | star | star/day | created_at | updated_at | license | language | description | url |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| vuetifyjs | vuetify | 21358 | 19.65 | 2016-09-12 | 2019-09-03 | MIT License | TypeScript | 🐉 Material Component Framework for Vue.js 2 | https://github.com/vuetifyjs/vuetify |
| kriasoft | react-starter-kit | 19479 | 9.91 | 2014-04-16 | 2019-09-03 | MIT License | JavaScript | React Starter Kit — isomorphic web app boilerplate (Node.js, Express, GraphQL, React.js, Babel, PostCSS, Webpack, Browsersync) | https://github.com/kriasoft/react-starter-kit |
```

### Sort
<a id="markdown-sort-case" name="sort-case"></a>
```sh
girepo angular/angular facebook/react vuejs/vue  --asc star
``` 
    
