"""
Haryana Revenue Toolkit (HRTK)

Base dialog.
"""

from __future__ import annotations

from PySide6.QtWidgets import QDialog

from hrtk.presentation.common.form_mode import FormMode


class BaseDialog(QDialog):
    """
    Base class for all HRTK dialogs.
    """

    def __init__(
        self,
        mode: FormMode,
    ) -> None:
        super().__init__()

        self._mode = mode

    @property
    def mode(self) -> FormMode:
        """
        Return the dialog mode.
        """
        return self._mode

    @property
    def is_create_mode(self) -> bool:
        """
        Return True when dialog is in create mode.
        """
        return self.mode is FormMode.CREATE

    @property
    def is_edit_mode(self) -> bool:
        """
        Return True when dialog is in edit mode.
        """
        return self.mode is FormMode.EDIT