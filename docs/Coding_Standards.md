\# Haryana Revenue Toolkit (HRTK)



\# Coding Standards



Version: 1.0



Status: Active



\---



\# Purpose



This document defines the coding standards used throughout the Haryana Revenue Toolkit (HRTK).



Every contributor should follow these standards to ensure consistency, readability and maintainability.



\---



\# Philosophy



Code should be written for people first and computers second.



Good code should be:



\- Readable

\- Predictable

\- Testable

\- Maintainable

\- Recoverable



Avoid unnecessary cleverness.



\---



\# General Principles



Always prefer:



Simple solutions



↓



Clear naming



↓



Small methods



↓



Small classes



↓



Reusable components



\---



\# File Organization



Every module should follow the same structure.



Example



```

ownership/



ownership\_widget.py



ownership\_dialog.py



ownership\_toolbar.py



ownership\_table.py



ownership\_model.py

```



Large files should be avoided.



\---



\# Naming Convention



\## Classes



Use PascalCase.



Examples



```

OwnershipWidget



VillageDialog



PartitionToolbar



OwnerService

```



\---



\## Methods



Use snake\_case.



Examples



```

load\_data()



refresh\_table()



validate\_share()



update\_summary()

```



\---



\## Variables



Use meaningful names.



Good



```

ownerships



selected\_owner



remaining\_area

```



Avoid



```

x



temp



data1



abc

```



\---



\# Constants



Use UPPER\_CASE.



Example



```

DEFAULT\_AREA



MAX\_ROWS



COLUMN\_COUNT

```



\---



\# Class Design



Every class should have one responsibility.



Correct



```

OwnershipWidget



↓



Displays Ownership

```



Incorrect



```

OwnershipWidget



↓



Display



↓



Validation



↓



Database



↓



Reports

```



\---



\# Method Length



Methods should normally remain below 50 lines.



If a method becomes difficult to understand, split it into helper methods.



\---



\# Comments



Use comments to explain \*\*why\*\*, not \*\*what\*\*.



Good



```

\# Prevent duplicate ownership

```



Avoid obvious comments



```

\# Add owner

```



\---



\# Imports



Standard Library



↓



Third Party



↓



Project Imports



Example



```python

from \_\_future\_\_ import annotations



from uuid import UUID



from PySide6.QtWidgets import QWidget



from hrtk.domain.owner import Owner

```



\---



\# Type Hints



Always use type hints where practical.



Example



```python

def update(

&#x20;   owner: Owner,

) -> None:

```



\---



\# Widgets



Widgets should only:



Display information



Handle signals



Call services



Widgets should never contain business rules.



\---



\# Services



Services contain business logic.



Examples



```

validate()



exists()



register()



calculate()



allocate()

```



\---



\# Repositories



Repositories handle persistence only.



No Qt code.



No dialogs.



No widgets.



\---



\# Domain



Domain objects represent business concepts.



Examples



```

Village



Owner



Khewat



Parcel



Ownership



Area

```



The domain must not depend on Qt.



\---



\# Error Handling



Never ignore exceptions.



Errors should:



Be logged



Show user-friendly messages



Preserve application stability



\---



\# Logging



Log important actions.



Examples



```

Application started



Owner created



Ownership deleted



Partition saved

```



Do not log unnecessary information.



\---



\# User Interface



Use Haryana Revenue terminology.



Examples



Parcel



↓



Khasra



Mutation



↓



Intkal



Partition



↓



Takseem



\---



\# Documentation



Every public class should include a docstring.



Every public method should include a short description.



\---



\# Stable Module Rule



Frozen modules must not receive feature work.



Only:



Critical bug fixes



Security fixes



Data integrity fixes



\---



\# Git Workflow



Every feature:



Implement



↓



Test



↓



Commit



↓



Tag



↓



Push



Never leave long-running uncommitted work.



\---



\# Testing



Before every commit verify:



Application starts



Navigation works



No traceback



Logs clean



Stable modules unaffected



\---



\# Formatting



Use consistent indentation.



Maximum line length approximately 88–100 characters where practical.



Leave blank lines between logical sections.



\---



\# Code Review Checklist



Before merging any feature:



□ Builds successfully



□ Runs successfully



□ Uses services correctly



□ No business logic in widgets



□ No duplicated code



□ Documentation updated



□ Commit completed



□ Tag created



\---



\# Guiding Principle



Write code that another developer can understand one year later without needing an explanation.



Readable code is professional code.

