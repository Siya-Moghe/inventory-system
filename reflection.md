Reflection 

**1. Which issues were the easiest to fix, and which were the hardest? Why?**
The easiest to fix was replacing except: clauses with "except Exception as e:" clauses. Where exception is the name of specific exceptions like FileNotFound, json.JSONDecodeError, KeyError, etc. The hardest errors to solve were adding logging functionality as it required attention to detail.

**2. Did the static analysis tools report any false positives? If so, describe one example.**
When I added "global stock_item" to the load_data() function, I got an error stating "W0603: Using the global statement". There was no coding error here as the code still works correctly. However, this can be considered a bad coding practice which was why Pylint flagged it. The warning in this case was a false postive since the code still ran correctly.

**3. How would you integrate static analysis tools into your actual software development workflow? Consider continuous integration (CI) or local development practices.**
Statis analysis tools can be integrated both in continuous integration (CI) and local development. 
In local development, Pylint, Flake8, Bandit can be run before committing code. This will catch style violations and potential bugs.
In CI, we can include static analysis in the CI pipeline. If critical warnings or errors are detected, the pipeline can fail, preventing problematic code from being merged ensuring consistent code quality, improves maintainability, and reduces runtime error

**4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?**
After applying fixes the code was more clear. It made the process of debugging easier as log messages provided necessary information. Code is now more readable as accurate docstrings were added. All exceptions are explicitly handled and type checking while opening files was included. These checks ensure safe execution and prevent runtime crashes adding to its robustness.
