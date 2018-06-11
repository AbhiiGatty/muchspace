# **makespace**
---
makespace is python tool to calculate the space required to download media links in a file. 

**makespace** uses [Google's Fire module] to make the command line interface. Refer their docs for mode info.

### Modules

makespace uses a number of open source python modules:

* [Requests] - HTML enhanced for web apps!

# Install
```
$ pip install muchspace
```

# Usage
```
$ muchspace getfilefrom <FILE PATH>
```

## Development
Want to contribute? Great!
To contribute to the project, Please take up the tasks specified in the issues. Add a comment in the issues if you are taking up one. 
### Instructions
- Fork the repository to your account.
- Copy the clone url of your repository.
- Clone the repository to your machine `git clone https://github.com/YOUR_USER_NAME/stackby.git`
- Make sure you create a branch with the name as the issue you are working on `git checkout -b YOUR_BRANCH_NAME`, and make sure you are working on the same branch and not the `master`, run `git status` to know which branch you are working on, run `git branch`, your branch will be highlighted with an `*`. If you are not in your branch or want to move to another branch use `git checkout BRANCH_NAME`. 
a good branch name should explain what this branch is about eg. `stackby_type`, `stackby_date`, `feature_undo` etc.
- Add the upstream url of original repository, follow the instructions [here](https://help.github.com/articles/configuring-a-remote-for-a-fork/)
- Make sure your repository is in sync with the original repository's master branch. Follow the instruction [here](https://help.github.com/articles/syncing-a-fork/) to know how to keep your local repository in sync.
- Finally when you have made the changes, submit a pull request through github from the original repository, choose your branch against the master of original or create a new branch.

### Todos

 - Better working with async mode
----
## License
MIT

**Free Software ❤️️, Hell Yeah!🍺**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [Requests]: <http://docs.python-requests.org/en/master/>
   [Google's Fire module]: <https://github.com/google/python-fire>