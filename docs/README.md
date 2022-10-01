# CHAOS: heuristic analyzer of syntax

An attempt at creating a norminette from scratch

- [ ] Stage 1: Build a wrapper around the current norm checker, 
optionally without the docker image to avoid the requirement to use sudo everytime we want to run it.

- [ ] Stage 2: Create a new vera profile to rewrite the rules of the style checker
and give a major quality improvement to the inner code.

- [ ] Stage 3: Rebuilt CHAOS using a custom-made parser that will provide the ast, 
parser and general information structures about the code in order to remove the vera dependency
making the tool easier to install.


## What is currently planned

- [ ] Provide a helpful output for the lint command to help people understand the change to do 
and the context of the error messages. This will be done by providing short description for each problem
as well as providing a small chunk of the area where the problem was encountered, with syntax highlighting.

- [ ] Provide detailed information about the error messages with a `more [rule]` sub command 
that will give explanations, tips, warning and code examples. This will be done by using the .rule_spect files
in the docs/rules directory.

- [ ] Provide a `fix` command that will reformat the codebase to eliminate some easier syntax problem 
in order to save a lot of time. This wil be done by tokenizing the code and generating a new formatting version
out of the tokens.


## Pros and cons of using this tool instead of the standard tool


| Pros                                                        | Cons                                             |
|-------------------------------------------------------------|--------------------------------------------------|
| Built-in help sub command to get information upon the rules | Necessity to check the pdf code style            |  
| A result command that give more context upon the code       | Only the line is given.                          |
| A formatting command to fix small problems right away       | No formatting                                    |
| You will no learn the syntax by using autofix               | Force you to use the mandatory syntax right away |
| Provide a strict mode                                       | Ignore other files and directories               |
| Require python3.9 and vera binary                           | Easier to install                                |
| No sudo command to run it                                   | Has to be run in using sudo                      |
| Has to be updated with                                      | Automatically update                             |
| Open sources                                                | Semi open-sourced                                |
