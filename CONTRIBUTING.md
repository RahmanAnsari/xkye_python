# Notes for Xkye Contributors

Hi! If you are new to the Xkye community: welcome, and thanks for trying Xkye. Please be sure to respect our [community standards](https://github.com/RahmanAnsari/xkye_python/blob/main/CODE_OF_CONDUCT.md) in all interactions.


## Before filing an issue

- Reporting a potential bug? Please read the "[How to file a bug report](https://github.com/RahmanAnsari/xkye_python/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)" section to make sure that all necessary information is included.

- Contributing code? Be sure to review the [contributor checklist](https://github.com/RahmanAnsari/xkye_python/blob/master/CONTRIBUTING.md#contributor-checklist) for helpful tips on the tools we use to build Xkye.

- Library feature requests are generally not accepted on this issue tracker. New libraries should be developed as packages.


## Contributor Checklist

* Create a [GitHub account](https://github.com/signup/free).

* [Fork Xkye](https://github.com/RahmanAnsari/xkye_python/fork).

* Build the software and libraries (the first time takes a while, but it's fast after that). Detailed build instructions are in the [README](https://github.com/RahmanAnsari/xkye_python/tree/master/README.md). Xkye depends on few external packages; most are automatically downloaded and installed, but are less frequently updated than Xkye itself.

* Keep Xkye current. Xkye is a fast-moving target, and many details of the language are still settling out. Keep the repository up-to-date and rebase work-in-progress frequently to make merges simpler.

* Learn to use [git](https://git-scm.com), the version control system used by GitHub and the Xkye project. Try a tutorial such as the one [provided by GitHub](https://try.GitHub.io/levels/1/challenges/1).

* For more detailed tips, read the [submission guide](https://github.com/RahmanAnsari/xkye_python/blob/master/CONTRIBUTING.md#submitting-contributions) below.

* Relax and have fun!

## How to file a bug report

A useful bug report filed as a GitHub issue provides information about how to reproduce the error.

1. Before opening a new [GitHub issue](https://github.com/RahmanAnsari/xkye_python/issues):
  - Check if the problem is caused by a Xkye package rather than core Xkye specification, file a bug report with the relevant package author rather than here.

2. When filing a bug report, provide where possible:
  - The full error message, including the backtrace.
  - A minimal working example, i.e. the smallest chunk of code that triggers the error. Ideally, this should be code that can be pasted into a REPL or run from a source file. If the code is larger than (say) 50 lines, consider putting it in a [gist](https://gist.github.com).
  - The version of Xkye, especially if the issue is related to a specific package.

3. When pasting code blocks or output, put triple backquotes (\`\`\`) around the text so GitHub will format it nicely. Code statements should be surrounded by single backquotes (\`). Be aware that the `@` sign tags users on GitHub, so references to macros should always be in single backquotes. See [GitHub's guide on Markdown](https://guides.github.com/features/mastering-markdown) for more formatting tricks.

## Submitting contributions

### Improving documentation

*By contributing documentation to Xkye, you are agreeing to release it under the [MIT License](https://github.com/RahmanAnsari/xkye-lang/tree/master/LICENSE.md).*

Xkye's documentation source files are stored in the `doc/` directory and [README.md](https://github.com/RahmanAnsari/xkye_python/tree/master/README.md) . Like everything else these can be modified using `git`. Documentation is built with Markdown syntax.


### Contributing to core functionality or base libraries

*By contributing code to Xkye, you are agreeing to release it under the [MIT License](https://github.com/RahmanAnsari/xkye-lang/tree/master/LICENSE.md).*

The Xkye community uses [GitHub issues](https://github.com/RahmanAnsari/xkye-lang/issues) to track and discuss problems, feature requests, and pull requests (PR). You can make pull requests for incomplete features to get code review. The convention is to prefix the pull request title with "WIP:" for Work In Progress, or "RFC:" for Request for Comments when work is completed and ready for merging. This will prevent accidental merging of work that is in progress.

Note: These instructions are for adding to or improving functionality and syntax in the base grammar. Before getting started, it can be helpful to discuss the proposed changes or additions in a GitHub issue---it's possible your proposed change belongs in a package rather than the core language. Also, keep in mind that changing stuff in the base can potentially break a lot of things.


### Code Formatting Guidelines

#### General Formatting Guidelines for Xkye code contributions

 - 4 spaces per indentation level, no tabs
 - use whitespace to make the code more readable
 - no whitespace at the end of a line (trailing whitespace)
 - comments are good, especially when they explain the algorithm
 - try to adhere to a 92 character line length limit
 - use upper camel case convention for modules, type names
 - use lower case with underscores for method names
 - it is generally preferred to use ASCII operators and identifiers over
   Unicode equivalents whenever possible

#### General Formatting Guidelines For C code contributions

 - 4 spaces per indentation level, no tabs
 - space between `if` and `(` (`if (x) ...`)
 - newline before opening `{` in function definitions
 - `f(void)` for 0-argument function declarations
 - newline between `}` and `else` instead of `} else {`
 - if one part of an `if..else` chain uses `{ }` then all should
 - no whitespace at the end of a line

### Git Recommendations For Pull Requests

 - Avoid working from the `master` branch of your fork, creating a new branch will make it easier if Xkye's `master` changes and you need to update your pull request.
 - Try to [squash](http://gitready.com/advanced/2009/02/10/squashing-commits-with-rebase.html) together small commits that make repeated changes to the same section of code so your pull request is easier to review, and Xkye's history won't have any broken intermediate commits. A reasonable number of separate well-factored commits is fine, especially for larger changes.
 - If any conflicts arise due to changes in Xkye's `master`, prefer updating your pull request branch with `git rebase` versus `git merge` or `git pull`, since the latter will introduce merge commits that clutter the git history with noise that makes your changes more difficult to review.
 - Descriptive commit messages are good.
 - Using `git add -p` or `git add -i` can be useful to avoid accidentally committing unrelated changes.
 - GitHub does not send notifications when you push a new commit to a pull request, so please add a comment to the pull request thread to let reviewers know when you've made changes.
 - When linking to specific lines of code in discussion of an issue or pull request, hit the `y` key while viewing code on GitHub to reload the page with a URL that includes the specific version that you're viewing. That way any lines of code that you refer to will still make sense in the future, even if the content of the file changes.
 - Whitespace can be automatically removed from existing commits with `git rebase`.
   - To remove whitespace for the previous commit, run
     `git rebase --whitespace=fix HEAD~1`.
   - To remove whitespace relative to the `master` branch, run
     `git rebase --whitespace=fix master`.

## Resources

* Using GitHub
  - [General GitHub documentation](https://help.github.com)
  - [GitHub pull request documentation](https://help.github.com/articles/creating-a-pull-request/)
