# -*- coding: utf-8 -*-

import contextlib
import inspect
import io
import os
import sys
from typing import List, Optional, Tuple
import types
import wx
import wx.dataview
import wx.grid
import wx.richtext
import ui


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
            # '__main__': sys.modules[__name__],
            'self': self,
            'unload': self.unload,
        }

        self.update_file_list()
        self.update_module_list()

        self.selected_file = None
        self.selected_module = None
        self.selected_parent_object = None
        self.selected_object = None
        self.object_breadcrumb: str = ''
        self.object_breadcrumb_queue: List = []
        self.active_page: Optional[wx.richtext.RichTextCtrl] = None
        self.current_dir: str = ''
        self.opened_file_path: str = ''
        self.text_to_find: str = ''

        self.clear_pop_up_menu()
        self.set_icon()

        self.set_status('Ready')

    def set_icon(self):
        icon_path = os.path.join(sys.path[0], 'pytalk.ico')
        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap(icon_path, wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)

    def clear_pop_up_menu(self) -> None:
        for index, (menu, label) in enumerate(self.m_menubar_main.GetMenus()):
            if label[:2] == '__':
                self.m_menubar_main.SetMenuLabel(index, '')
                menu.Detach()

    def update_file_list(self) -> None:
        #
        # def append_files(parent_node, file_list: List[str]):
        #     for file_node in file_list:
        #         self.pages.file_list.AppendItem(parent_node, file_node)

        self.current_dir = os.getcwd()
        # noinspection PyPep8Naming
        self.m_tree_list_ctrl_file.GetView().Parent.Columns[0].Title = self.current_dir

        self.pages.file_list.DeleteAllItems()
        root_node = self.pages.file_list.GetRootItem()

        for file in os.listdir(self.current_dir):
            self.pages.file_list.AppendItem(root_node, file)

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

    def update_object_list(self, breadcrumb: str, parent_object) -> None:
        self.object_breadcrumb = breadcrumb
        self.selected_parent_object = parent_object

        self.m_static_text_object_name.SetLabelText(breadcrumb)

        # Delete all rows.
        rows = self.pages.object_list.GetNumberRows()
        if rows > 0:
            self.pages.object_list.DeleteRows(0, rows)

        try:
            object_list = dir(parent_object)
        except AttributeError:
            return

        # Add rows.
        count = len(object_list)
        if count > 0:
            self.pages.object_list.AppendRows(count)

            # Update content.
            for index, key in enumerate(sorted(object_list)):
                self.pages.object_list.SetCellValue(index, 0, key)

                # noinspection PyBroadException
                try:
                    value = PyTalk.get_attribute(parent_object, key)
                    self.pages.object_list.SetCellValue(index, 1, str(type(value)))
                except:
                    self.pages.object_list.SetCellValue(index, 1, '?')

            self.pages.object_list.AutoSizeColumns()

    def update_code_page(self, title: str, code: str) -> None:
        self.m_static_text_code_name.SetLabelText(title)
        self.pages.code_page.ChangeValue(code)

    def clear_playground(self) -> None:
        self.pages.playground.Clear()

    def append_output(self, message: str) -> None:
        output = self.pages.output_page
        output.AppendText(message)
        output.ShowPosition(output.GetLastPosition())

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
            self.append_output(repr(exception) + '\n')

    def get_help(self, code: str) -> None:
        stdout, stderr, exception = self.execute_code('help(' + code + ')')

        if exception is not None:
            self.update_help(repr(exception))
        else:
            for output in [stdout.getvalue(), stderr.getvalue()]:
                if output is not None and output != '':
                    self.update_help(output)

    def unload(self, module):
        """Unload module from shared_globals."""
        self.unload_module_with_name(module.__name__)

    def unload_module_with_name(self, module_name: str) -> None:
        """Unload module from shared_globals."""
        print('Unloading', module_name)

        try:
            # Delete from current process.
            del sys.modules[module_name]
            # Delete from child process.
            del self.shared_globals[module_name]
            self.update_module_list()
        except Exception as ex:
            self.append_output(repr(ex) + '\n')

    def set_status(self, msg: str) -> None:
        self.m_status_bar_main.SetLabelText(msg)

    def get_selected_text(self):
        if self.active_page:
            return self.active_page.GetStringSelection()

        return ''

    def get_all_text(self):
        if self.active_page:
            return self.active_page.GetValue()

        return ''

    # Virtual event handlers, overide them in your derived class
    def on_menu_selection_file_new(self, event):
        self.new_playground()

    def set_opened_file_path(self, file_path: str):
        self.opened_file_path = file_path
        self.m_static_text_file_path.SetLabelText(file_path)

    def new_playground(self):
        if len(self.pages.playground.GetValue()) == 0:
            return
        response = wx.MessageBox('Clear playground?', 'Warning!', wx.OK + wx.CANCEL | wx.ICON_WARNING)
        if response == wx.OK:
            self.clear_playground()
            self.set_opened_file_path('')

    def on_menu_selection_file_open_directory(self, event):
        with wx.DirDialog(self,
                          "Open directory", "",
                          style=wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST) as dirDialog:
            if dirDialog.ShowModal() == wx.ID_CANCEL:
                return
            os.chdir(dirDialog.GetPath())
            self.update_file_list()

    def on_menu_selection_file_open(self, event):
        self.new_playground()
        wildcard = 'Python files (*.py)|*.py'
        with wx.FileDialog(self,
                           'Open python file',
                           wildcard=wildcard,
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            self.load_from_file(fileDialog.GetPath())

        with open(self.opened_file_path, 'rt') as file:
            code = file.read()
            self.pages.playground.SetValue(code)

    def load_from_file(self, file_path: str):
        self.new_playground()
        # If file opened or playground is not empty!
        if self.opened_file_path != '' or len(self.pages.playground.GetValue()) != 0:
            return

        self.set_opened_file_path(file_path)

        with open(file_path, 'rt') as file:
            code = file.read()
            self.pages.playground.SetValue(code)

    def on_menu_selection_file_save(self, event):
        self.save_playground_as(self.opened_file_path)

    def on_menu_selection_file_save_as(self, event):
        self.save_playground_as()

    def save_playground_as(self, file_path: str = ''):
        if file_path == '':
            wildcard = 'Python files (*.py)|*.py'
            with wx.FileDialog(self,
                               'Save python file',
                               wildcard=wildcard,
                               style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
                if fileDialog.ShowModal() == wx.ID_CANCEL:
                    return

                file_path = fileDialog.GetPath()
                self.set_opened_file_path(file_path)

        with open(file_path, 'wt') as file:
            code = self.pages.playground.GetValue()
            file.write(code)

    def on_menu_selection_file_close(self, event):
        self.Close()
        event.Skip()

    def on_menu_command_do_selection(self, event) -> None:
        code = self.get_selected_text()
        self.execute(code)

    def on_menu_command_do_all(self, event) -> None:
        code = self.get_all_text()
        self.execute(code)

    def on_menu_command_print_selection(self, event) -> None:
        code = self.get_selected_text()
        self.execute('print(repr(' + code + '))')

    def on_menu_command_clear_output(self, event) -> None:
        self.clear_output()

    def on_menu_command_help_on_selection(self, event) -> None:
        code = self.get_selected_text()
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
                self.update_object_list(module_name, self.selected_module)
                self.clear_object_breadcrumb_queue()

    @staticmethod
    def get_attribute(parent_object, attribute_name: str):
        # noinspection PyBroadException
        try:
            return parent_object.__getattribute__(attribute_name)
        except:
            # noinspection PyBroadException
            try:
                return parent_object.__getattribute__(parent_object, attribute_name)
            except:
                return parent_object.__dict__[attribute_name]

    def on_grid_select_cell_object(self, event):
        assert self.selected_module is not None, 'Invalid module!'
        assert self.selected_parent_object is not None, 'Invalid parent!'
        assert self.object_breadcrumb != '', 'Invalid breadcrumb!'

        index = event.GetRow()
        if index >= 0:
            object_name = self.m_grid_object.GetCellValue(index, 0)
            if object_name != '':
                self.m_static_text_object_name.SetLabelText(self.object_breadcrumb + '.' + object_name)

                # noinspection PyBroadException
                try:
                    self.selected_object = PyTalk.get_attribute(self.selected_parent_object, object_name)
                    title = self.object_breadcrumb + '.' + object_name
                    code = inspect.getsource(self.selected_object)
                    self.update_code_page(title, code)
                except:
                    self.update_code_page('<No name>', '<No source available>')

    @staticmethod
    def is_atom(selected_object) -> bool:
        """Return True if selected object is not browsable further."""

        if selected_object is None:
            return True
        if isinstance(selected_object, (bytes, int, float, str, bool)):
            return True
        if isinstance(selected_object, (types.BuiltinFunctionType, types.BuiltinMethodType)):
            return True

        return str(type(selected_object)) in [
            "<class 'method-wrapper'>",
            "<class 'method_descriptor'>",
            "<class 'member_descriptor'>",
            "<class 'wrapper_descriptor'>"]

    def on_grid_double_click_object(self, event):
        assert self.selected_module is not None, 'Invalid module!'
        assert self.selected_parent_object is not None, 'Invalid parent!'
        assert self.object_breadcrumb != '', 'Invalid breadcrumb!'

        index = event.GetRow()
        if index >= 0:
            object_name = self.m_grid_object.GetCellValue(index, 0)
            if object_name != '':
                # noinspection PyBroadException
                try:
                    selected_object = PyTalk.get_attribute(self.selected_parent_object, object_name)
                    if selected_object == self.selected_parent_object:
                        # Prevent recursive call.
                        return
                    if PyTalk.is_atom(selected_object):
                        return
                    child_list = dir(selected_object)
                    if len(child_list) == 0:
                        return
                    self.push_object_breadcrumb_queue(self.object_breadcrumb, self.selected_parent_object)
                    self.update_object_list(self.object_breadcrumb + '.' + object_name, selected_object)
                except:
                    pass

    def on_button_click_object_backward(self, event) -> None:
        if len(self.object_breadcrumb_queue) == 0:
            return

        path, parent_object = self.object_breadcrumb_queue[-1]
        self.object_breadcrumb_queue = self.object_breadcrumb_queue[:-1]
        self.update_object_list(path, parent_object)

        if len(self.object_breadcrumb_queue) == 0:
            self.m_button_object_backward.Enable(False)

    def on_menu_selection_find_file(self, event):
        wx.MessageBox('Not implemented yet!', 'Warning', wx.OK)

    def on_menu_selection_find_module(self, event):
        wx.MessageBox('Not implemented yet!', 'Warning', wx.OK)

    def on_menu_selection_find_object(self, event):
        wx.MessageBox('Not implemented yet!', 'Warning', wx.OK)

    def on_menu_selection_find_text(self, event):
        with wx.TextEntryDialog(self,
                                'Enter string to find',
                                'Find in text',
                                value=self.text_to_find, style=wx.TextEntryDialogStyle) as dialog:
            if dialog.ShowModal() == wx.ID_CANCEL:
                return
            self.find_text(dialog.GetValue())

    def on_menu_selection_find_next(self, event):
        self.find_text(self.text_to_find)

    def find_text(self, text: str):
        if len(text) == 0:
            return

        self.text_to_find = text
        page = self.active_page

        if page is None:
            return

        # Find from current position.
        position = page.GetCaretPosition()
        found = page.GetValue().find(text, position)
        if found > 0:
            page.SetSelection(found, found + len(text))
            page.ScrollIntoView(found, wx.WXK_DOWN)
            page.SetFocus()
        else:
            # Find from start position.
            found = page.GetValue().find(text, 0)
            if found > 0:
                page.SetSelection(found, found + len(text))
                page.ScrollIntoView(found, wx.WXK_UP)
                page.SetFocus()
            else:
                wx.MessageBox('Cannot find ' + text, 'Find in text')

    def on_menu_help_about(self, event) -> None:
        wx.MessageBox('PyTalk is a simple Python IDE inspired by Smalltalk.', 'PyTalk version 0.1')

    def clear_object_breadcrumb_queue(self):
        self.object_breadcrumb_queue = []
        self.m_button_object_backward.Enable(False)

    def push_object_breadcrumb_queue(self, path: str, parent_object):
        self.object_breadcrumb_queue.append((path, parent_object))
        self.m_button_object_backward.Enable(True)

    def on_menu_selection_select_font(self, event) -> None:

        font_data = wx.FontData()
        font_data.SetInitialFont(self.m_rich_text_code.GetFont())

        dialog = wx.FontDialog(None, font_data)
        if dialog.ShowModal() == wx.ID_OK:
            font = dialog.GetFontData().GetChosenFont()
            self.set_font(font)

    def set_font(self, font) -> None:
        self.m_rich_text_code.SetFont(font)
        self.m_rich_text_playground.SetFont(font)
        self.m_rich_text_output.SetFont(font)
        self.m_rich_text_help.SetFont(font)

    def on_menu_selection_show_file(self, event) -> None:
        self.m_notebook_file_module.SetSelection(0)
        self.m_tree_list_ctrl_file.SetFocus()

    def on_menu_selection_show_module(self, event) -> None:
        self.m_notebook_file_module.SetSelection(1)
        self.m_grid_module.SetFocus()

    def on_menu_selection_show_object(self, event) -> None:
        self.m_grid_object.SetFocus()

    def on_menu_selection_show_code(self, event) -> None:
        self.m_rich_text_code.SetFocus()

    def on_menu_selection_show_playground(self, event) -> None:
        self.m_rich_text_playground.SetFocus()

    def on_menu_selection_show_output(self, event) -> None:
        self.m_rich_text_output.SetFocus()

    def on_menu_selection_show_help(self, event) -> None:
        self.m_rich_text_help.SetFocus()

    def on_set_focus_code(self, event):
        self.active_page = self.m_rich_text_code
        event.Skip()

    def on_set_focus_playground(self, event):
        self.active_page = self.m_rich_text_playground
        event.Skip()

    def on_set_focus_output(self, event):
        self.active_page = self.m_rich_text_output
        event.Skip()

    def on_set_focus_help(self, event):
        self.active_page = self.m_rich_text_help
        event.Skip()

    def on_tree_list_item_context_menu(self, event):
        self.PopupMenu(self.m_menu_popup_file)

    def on_grid_cell_right_click_module(self, event):
        self.PopupMenu(self.m_menu_popup_module)

    def on_grid_cell_right_click_object(self, event):
        self.PopupMenu(self.m_menu_popup_object)

    def on_right_down_code(self, event):
        self.PopupMenu(self.m_menu_popup_code)

    def on_right_down_playground(self, event):
        self.PopupMenu(self.m_menu_popup_playground)

    def on_right_down_output(self, event):
        self.PopupMenu(self.m_menu_popup_output)

    def on_right_down_help(self, event):
        self.PopupMenu(self.m_menu_popup_help)

    def on_menu_selection_open_selected_file(self, event):
        file_path = self.get_selected_file_path()
        if file_path != '':
            self.load_from_file(file_path)

    def get_selected_file_path(self) -> str:
        tree_list_item = self.pages.file_list.GetSelection()
        file_path = self.pages.file_list.GetItemText(tree_list_item)

        return file_path

    def get_selected_module_name(self, event) -> str:
        cursor_row = self.m_grid_module.GetGridCursorRow()
        if cursor_row < 0:
            self.set_status('No module selected!')
            return ''
        return self.m_grid_module.GetCellValue(cursor_row, 0)

    def on_menu_selection_reload_module(self, event):
        module_name = self.get_selected_module_name(event)
        if module_name != '':
            self.unload_module_with_name(module_name)
            self.execute('import ' + module_name)

    def on_menu_selection_unload_module(self, event):
        module_name = self.get_selected_module_name(event)
        if module_name != '':
            self.unload_module_with_name(module_name)
        self.update_module_list()

    def on_menu_selection_copy_name(self, event):
        event.Skip()

    def on_menu_selection_copy_value(self, event):
        event.Skip()

    def on_menu_selection_copy_path(self, event):
        event.Skip()


def main() -> None:
    """Main function."""
    app = wx.App()
    pytalk = PyTalk(None)
    entries = [
        (wx.ACCEL_CTRL, ord('N'), pytalk.m_menu_item_file_new.GetId()),
        (wx.ACCEL_CTRL, ord('O'), pytalk.m_menu_item_file_open.GetId()),
        (wx.ACCEL_CTRL, ord('S'), pytalk.m_menu_item_file_save.GetId()),
        (wx.ACCEL_CTRL + wx.ACCEL_ALT, ord('S'), pytalk.m_menu_item_file_save_as.GetId()),
        (wx.ACCEL_CTRL, ord('U'), pytalk.m_menu_item_command_update_module_list.GetId()),
        (wx.ACCEL_CTRL, ord('D'), pytalk.m_menu_item_command_do_selection.GetId()),
        (wx.ACCEL_CTRL + wx.ACCEL_ALT, ord('D'), pytalk.m_menu_item_command_do_all.GetId()),
        (wx.ACCEL_CTRL, ord('P'), pytalk.m_menu_item_command_print_selection.GetId()),
        (wx.ACCEL_CTRL, ord('L'), pytalk.m_menu_item_command_clear_output.GetId()),
        (wx.ACCEL_CTRL, ord('H'), pytalk.m_menu_item_command_help_on_selection.GetId()),
        (0, wx.WXK_F1, pytalk.m_menu_item_command_help_on_selection.GetId()),
        (wx.ACCEL_CTRL, ord('F'), pytalk.m_menu_item_tool_find_text.GetId()),
        (wx.ACCEL_CTRL, ord('G'), pytalk.m_menu_item_tool_find_next.GetId()),
        (wx.ACCEL_CTRL, ord('1'), pytalk.m_menu_item_show_file.GetId()),
        (wx.ACCEL_CTRL, ord('2'), pytalk.m_menu_item_show_module.GetId()),
        (wx.ACCEL_CTRL, ord('3'), pytalk.m_menu_item_show_object.GetId()),
        (wx.ACCEL_CTRL, ord('4'), pytalk.m_menu_item_show_code.GetId()),
        (wx.ACCEL_CTRL, ord('5'), pytalk.m_menu_item_show_playground.GetId()),
        (wx.ACCEL_CTRL, ord('6'), pytalk.m_menu_item_show_output.GetId()),
        (wx.ACCEL_CTRL, ord('7'), pytalk.m_menu_item_show_help.GetId()),
    ]
    entries = [wx.AcceleratorEntry(flags=flags, keyCode=key_code, cmd=cmd_id) for flags, key_code, cmd_id in entries]
    pytalk.SetAcceleratorTable(wx.AcceleratorTable(entries))
    pytalk.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    main()
