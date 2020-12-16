# -*- coding: utf-8 -*-

import contextlib
import inspect
import io
from typing import Dict, Optional, Tuple
import wx
import wx.dataview
import wx.grid
import wx.richtext
import ui


TextPage = wx.richtext.RichTextCtrl


class Pages:
    def __init__(self,
                 file_list: wx.dataview.TreeListCtrl,
                 module_list: wx.grid.Grid,
                 object_list: wx.grid.Grid,
                 code_page: wx.richtext.RichTextCtrl,
                 playground: wx.richtext.RichTextCtrl,
                 output_page: wx.richtext.RichTextCtrl,
                 help_page: wx.richtext.RichTextCtrl):

        self.file_list: wx.dataview.TreeListCtrl = file_list
        self.module_list: wx.grid.Grid = module_list
        self.object_list: wx.grid.Grid = object_list
        self.code_page: wx.richtext.RichTextCtrl = code_page
        self.playground: wx.richtext.RichTextCtrl = playground
        self.output_page: wx.richtext.RichTextCtrl = output_page
        self.help_page: wx.richtext.RichTextCtrl = help_page


class PyTalk(ui.MainWindow):

    def __init__(self, parent):
        super().__init__(parent)

        self.pages = Pages(self.m_tree_list_ctrl_file,
                           self.m_grid_module,
                           self.m_grid_object,
                           self.m_rich_text_code,
                           self.m_rich_text_playground,
                           self.m_rich_text_output,
                           self.m_rich_text_help)

        self.shared_globals = {
            '__builtins__': __builtins__,
            'pytalk': self
        }
        self.update_file_list('.')
        self.update_module_list()

        self.selected_file = None
        self.selected_module = None
        self.selected_object = None

    def update_file_list(self, path: str) -> None:
        #
        # def append_files(parent_node, file_list: List[str]):
        #     for file_node in file_list:
        #         self.pages.file_list.AppendItem(parent_node, file_node)

        root_node = self.pages.file_list.GetRootItem()
        current_node = self.pages.file_list.AppendItem(root_node, '.')
        _ = current_node
        _ = path

    def update_module_list(self) -> None:
        # Delete all rows.
        rows = self.pages.module_list.GetNumberRows()
        if rows > 0:
            self.pages.module_list.DeleteRows(0, rows)

        # Add rows.
        count = len(self.shared_globals)
        if count > 0:
            self.pages.module_list.AppendRows(count)

            # Update content.
            for index, key in enumerate(sorted(self.shared_globals)):
                self.pages.module_list.SetCellValue(index, 0, key)
                self.pages.module_list.SetCellValue(index, 1, str(type(self.shared_globals[key])))

            self.pages.module_list.AutoSizeColumns()

    def update_object_list(self, object_list: Dict) -> None:
        # Delete all rows.
        rows = self.pages.object_list.GetNumberRows()
        if rows > 0:
            self.pages.object_list.DeleteRows(0, rows)

        # Add rows.
        count = len(object_list)
        if count > 0:
            self.pages.object_list.AppendRows(count)

            # Update content.
            for index, key in enumerate(sorted(object_list)):
                self.pages.object_list.SetCellValue(index, 0, key)
                self.pages.object_list.SetCellValue(index, 1, str(type(object_list[key])))

            self.pages.object_list.AutoSizeColumns()

    def update_code_page(self, message: str) -> None:
        self.pages.code_page.ChangeValue(message)

    def clear_playground(self) -> None:
        self.pages.playground.Clear()

    def append_output(self, message: str) -> None:
        self.pages.output_page.AppendText(message)

    def clear_output(self) -> None:
        self.pages.output_page.Clear()

    def update_help(self, message: str) -> None:
        self.pages.help_page.ChangeValue(message)

    def execute_code(self, code: str) -> Tuple[io.StringIO, io.StringIO, Optional[Exception]]:
        stdout = io.StringIO()
        stderr = io.StringIO()
        exception: Optional[Exception] = None

        try:
            with contextlib.redirect_stdout(stdout):
                with contextlib.redirect_stderr(stderr):
                    exec(code, self.shared_globals)
        except Exception as ex:
            exception = ex

        return stdout, stderr, exception

    def execute(self, code: str) -> None:
        stdout, stderr, exception = self.execute_code(code)

        for output in [stdout.getvalue(), stderr.getvalue()]:
            if output is not None and output != '':
                self.append_output(output)

        if exception is not None:
            self.append_output(repr(exception))

    def get_help(self, code: str) -> None:
        stdout, stderr, exception = self.execute_code('help(' + code + ')')

        if exception is not None:
            self.update_help(repr(exception))
        else:
            for output in [stdout.getvalue(), stderr.getvalue()]:
                if output is not None and output != '':
                    self.update_help(output)

    def on_menu_command_do_selection(self, event) -> None:
        code = self.pages.playground.GetStringSelection()
        self.execute(code)

    def on_menu_command_do_all(self, event) -> None:
        code = self.pages.playground.GetValue()
        self.execute(code)

    def on_menu_command_print_selection(self, event) -> None:
        code = self.pages.playground.GetStringSelection()
        print('print(repr(' + code + '))')
        self.execute('print(repr(' + code + '))')

    def on_menu_command_clear_output(self, event) -> None:
        self.clear_output()

    def on_menu_command_help_on_selection(self, event) -> None:
        code = self.pages.playground.GetStringSelection()
        self.get_help(code)

    def on_menu_command_update_module_list(self, event) -> None:
        self.update_module_list()

    def on_grid_select_cell_module(self, event) -> None:
        index = event.GetRow()
        if index >= 0:
            module_name = self.m_grid_module.GetCellValue(index, 0)
            if module_name != '':
                self.m_static_text_module_name.SetLabelText(module_name)
                self.selected_module = self.shared_globals[module_name]
                self.update_object_list(self.selected_module.__dict__)

    def on_grid_select_cell_object(self, event):
        assert self.selected_module is not None, "No module selected yet!"

        index = event.GetRow()
        if index >= 0:
            object_name = self.m_grid_object.GetCellValue(index, 0)
            if object_name != '':
                self.m_static_text_object_name.SetLabelText(object_name)
                self.selected_object = self.selected_module.__dict__[object_name]
                try:
                    source = inspect.getsource(self.selected_object)
                    self.update_code_page(source)
                except TypeError:
                    self.update_code_page('<No source available>')

    def on_menu_help_about(self, event) -> None:
        wx.MessageBox('PyTalk is a simple Python IDE impressed by Smalltalk.', 'PyTalk version 0.1')


def main() -> None:
    """Main function."""

    print('Start')

    app = wx.App()
    frame = PyTalk(None)

    entries = [
        wx.AcceleratorEntry(flags=wx.ACCEL_ALT, keyCode=ord('D'), cmd=frame.m_menu_item_do_selection.GetId()),
        wx.AcceleratorEntry(flags=wx.ACCEL_ALT, keyCode=ord('P'), cmd=frame.m_menu_item_print_selection.GetId()),
        wx.AcceleratorEntry(flags=wx.ACCEL_CTRL, keyCode=ord('H'), cmd=frame.m_menu_item_help_on_selection.GetId()),
    ]

    accel = wx.AcceleratorTable(entries)
    frame.SetAcceleratorTable(accel)

    frame.Show(True)
    app.MainLoop()


if __name__ == "__main__":
    main()
