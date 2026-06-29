"""
Haryana Revenue Toolkit (HRTK)

Application launcher.
"""

from __future__ import annotations

import sys

from hrtk.application.application import Application
from hrtk.presentation import MainWindow


def main() -> int:
    """
    Launch the Haryana Revenue Toolkit.
    """

    application = Application()

    window = MainWindow(application.context)

    application.set_main_window(window)

    return application.run()


if __name__ == "__main__":
    sys.exit(main())