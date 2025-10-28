Reflection 

**1. Which issues were the easiest to fix, and which were the hardest? Why?**
The easiest to fix was replacing except: clauses with "except Exception as e:" clauses. Where exception is the name of specific exceptions like FileNotFound, json.JSONDecodeError, KeyError, etc. The hardest errors to solve were adding logging functionality as it required attention to detail.

**2. Did the static analysis tools report any false positives? If so, describe one example.**
When I added "global stock_item" to the load_data() function, I got an error stating "W0603: Using the global statement". Which is a bad practice. This was avoided by returning the value and making all changes in the main function.

**3. How would you integrate static analysis tools into your actual software development workflow? Consider continuous integration (CI) or local development practices.**

**4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?**
