# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview
import wx.grid
import wx.richtext

###########################################################################
## Class MainWindow
###########################################################################

class MainWindow ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PyTalk verson 0.1", pos = wx.DefaultPosition, size = wx.Size( 1024,768 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		self.m_menubar_main = wx.MenuBar( 0 )
		self.m_menu_file = wx.Menu()
		self.m_menu_item_file_open_directory = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"Open directory", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.Append( self.m_menu_item_file_open_directory )

		self.m_menu_file.AppendSeparator()

		self.m_menu_item_file_new = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"New"+ u"\t" + u"Ctrl+N", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.Append( self.m_menu_item_file_new )

		self.m_menu_item_file_open = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"Open"+ u"\t" + u"Ctrl+O", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.Append( self.m_menu_item_file_open )

		self.m_menu_item_file_save = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"Save"+ u"\t" + u"Ctrl+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.Append( self.m_menu_item_file_save )

		self.m_menu_item_file_save_as = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"Save as"+ u"\t" + u"Ctrl+Alt+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.Append( self.m_menu_item_file_save_as )

		self.m_menu_file.AppendSeparator()

		self.m_menu_item_file_close = wx.MenuItem( self.m_menu_file, wx.ID_CLOSE, u"Close"+ u"\t" + u"Alt+C", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.Append( self.m_menu_item_file_close )

		self.m_menubar_main.Append( self.m_menu_file, u"File" )

		self.m_menu_command = wx.Menu()
		self.m_menu_item_command_update_module_list = wx.MenuItem( self.m_menu_command, wx.ID_ANY, u"Update module list"+ u"\t" + u"Ctrl+U", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_command.Append( self.m_menu_item_command_update_module_list )

		self.m_menu_command.AppendSeparator()

		self.m_menu_item_command_do_selection = wx.MenuItem( self.m_menu_command, wx.ID_ANY, u"Do selection"+ u"\t" + u"Ctrl+D", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_command.Append( self.m_menu_item_command_do_selection )

		self.m_menu_item_command_do_all = wx.MenuItem( self.m_menu_command, wx.ID_ANY, u"Do all"+ u"\t" + u"Ctrl+Alt+D", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_command.Append( self.m_menu_item_command_do_all )

		self.m_menu_item_command_print_selection = wx.MenuItem( self.m_menu_command, wx.ID_ANY, u"Print selection"+ u"\t" + u"Ctrl+P", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_command.Append( self.m_menu_item_command_print_selection )

		self.m_menu_command.AppendSeparator()

		self.m_menu_item_command_clear_output = wx.MenuItem( self.m_menu_command, wx.ID_ANY, u"Clear output"+ u"\t" + u"Ctrl+L", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_command.Append( self.m_menu_item_command_clear_output )

		self.m_menu_item_command_help_on_selection = wx.MenuItem( self.m_menu_command, wx.ID_ANY, u"Help on selection"+ u"\t" + u"Ctrl+H", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_command.Append( self.m_menu_item_command_help_on_selection )

		self.m_menubar_main.Append( self.m_menu_command, u"Command" )

		self.m_menu_tool = wx.Menu()
		self.m_menu_item_tool_font = wx.MenuItem( self.m_menu_tool, wx.ID_ANY, u"Select font", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_tool.Append( self.m_menu_item_tool_font )

		self.m_menu_tool.AppendSeparator()

		self.m_menu_item_tool_find_file = wx.MenuItem( self.m_menu_tool, wx.ID_ANY, u"Find file", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_tool.Append( self.m_menu_item_tool_find_file )
		self.m_menu_item_tool_find_file.Enable( False )

		self.m_menu_item_tool_find_module = wx.MenuItem( self.m_menu_tool, wx.ID_ANY, u"Find module", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_tool.Append( self.m_menu_item_tool_find_module )
		self.m_menu_item_tool_find_module.Enable( False )

		self.m_menu_item_tool_find_object = wx.MenuItem( self.m_menu_tool, wx.ID_ANY, u"Find object", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_tool.Append( self.m_menu_item_tool_find_object )
		self.m_menu_item_tool_find_object.Enable( False )

		self.m_menu_item_tool_find_text = wx.MenuItem( self.m_menu_tool, wx.ID_ANY, u"Find text"+ u"\t" + u"Ctrl+F", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_tool.Append( self.m_menu_item_tool_find_text )

		self.m_menu_item_tool_find_next = wx.MenuItem( self.m_menu_tool, wx.ID_ANY, u"Find next"+ u"\t" + u"Ctrl+G", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_tool.Append( self.m_menu_item_tool_find_next )

		self.m_menubar_main.Append( self.m_menu_tool, u"Tool" )

		self.m_menu_show = wx.Menu()
		self.m_menu_item_show_file = wx.MenuItem( self.m_menu_show, wx.ID_ANY, u"File"+ u"\t" + u"Ctrl+1", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_show.Append( self.m_menu_item_show_file )

		self.m_menu_item_show_module = wx.MenuItem( self.m_menu_show, wx.ID_ANY, u"Module"+ u"\t" + u"Ctrl+2", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_show.Append( self.m_menu_item_show_module )

		self.m_menu_item_show_object = wx.MenuItem( self.m_menu_show, wx.ID_ANY, u"Object"+ u"\t" + u"Ctrl+3", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_show.Append( self.m_menu_item_show_object )

		self.m_menu_item_show_code = wx.MenuItem( self.m_menu_show, wx.ID_ANY, u"Code"+ u"\t" + u"Ctrl+4", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_show.Append( self.m_menu_item_show_code )

		self.m_menu_item_show_playground = wx.MenuItem( self.m_menu_show, wx.ID_ANY, u"Playground"+ u"\t" + u"Ctrl+5", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_show.Append( self.m_menu_item_show_playground )

		self.m_menu_item_show_output = wx.MenuItem( self.m_menu_show, wx.ID_ANY, u"Output"+ u"\t" + u"Ctrl+6", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_show.Append( self.m_menu_item_show_output )

		self.m_menu_item_show_help = wx.MenuItem( self.m_menu_show, wx.ID_ANY, u"Help"+ u"\t" + u"Ctrl+7", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_show.Append( self.m_menu_item_show_help )

		self.m_menubar_main.Append( self.m_menu_show, u"Show" )

		self.m_menu_help = wx.Menu()
		self.m_menu_item_about = wx.MenuItem( self.m_menu_help, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_help.Append( self.m_menu_item_about )

		self.m_menubar_main.Append( self.m_menu_help, u"Help" )

		self.SetMenuBar( self.m_menubar_main )

		b_sizer_main_outer = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter_main_help = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter_main_help.SetSashGravity( 1 )
		self.m_splitter_main_help.Bind( wx.EVT_IDLE, self.m_splitter_main_helpOnIdle )

		self.m_panel_main = wx.Panel( self.m_splitter_main_help, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_main = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter_file_playground = wx.SplitterWindow( self.m_panel_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_3DBORDER|wx.SP_3DSASH|wx.SP_BORDER|wx.SP_LIVE_UPDATE )
		self.m_splitter_file_playground.SetSashGravity( 0 )
		self.m_splitter_file_playground.Bind( wx.EVT_IDLE, self.m_splitter_file_playgroundOnIdle )
		self.m_splitter_file_playground.SetMinimumPaneSize( 100 )

		self.m_panel_file_object_code = wx.Panel( self.m_splitter_file_playground, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_north = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter_file_object_code = wx.SplitterWindow( self.m_panel_file_object_code, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter_file_object_code.SetSashGravity( 0.5 )
		self.m_splitter_file_object_code.Bind( wx.EVT_IDLE, self.m_splitter_file_object_codeOnIdle )
		self.m_splitter_file_object_code.SetMinimumPaneSize( 100 )

		self.m_panel_file_object = wx.Panel( self.m_splitter_file_object_code, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_file_object = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter_file_object = wx.SplitterWindow( self.m_panel_file_object, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter_file_object.SetSashGravity( 0.5 )
		self.m_splitter_file_object.Bind( wx.EVT_IDLE, self.m_splitter_file_objectOnIdle )

		self.m_panel_file_module = wx.Panel( self.m_splitter_file_object, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_file_module = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook_file_module = wx.Notebook( self.m_panel_file_module, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_file = wx.Panel( self.m_notebook_file_module, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_file = wx.BoxSizer( wx.VERTICAL )

		self.m_tree_list_ctrl_file = wx.dataview.TreeListCtrl( self.m_panel_file, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.TL_DEFAULT_STYLE )
		self.m_tree_list_ctrl_file.AppendColumn( wx.EmptyString, wx.COL_WIDTH_DEFAULT, wx.ALIGN_LEFT, 0 )

		b_sizer_file.Add( self.m_tree_list_ctrl_file, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel_file.SetSizer( b_sizer_file )
		self.m_panel_file.Layout()
		b_sizer_file.Fit( self.m_panel_file )
		self.m_notebook_file_module.AddPage( self.m_panel_file, u"File (1)", False )
		self.m_panel_module = wx.Panel( self.m_notebook_file_module, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_module = wx.BoxSizer( wx.VERTICAL )

		self.m_static_text_module_name = wx.StaticText( self.m_panel_module, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_static_text_module_name.Wrap( -1 )

		b_sizer_module.Add( self.m_static_text_module_name, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_grid_module = wx.grid.Grid( self.m_panel_module, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid_module.CreateGrid( 0, 2 )
		self.m_grid_module.EnableEditing( False )
		self.m_grid_module.EnableGridLines( False )
		self.m_grid_module.EnableDragGridSize( False )
		self.m_grid_module.SetMargins( 0, 0 )

		# Columns
		self.m_grid_module.EnableDragColMove( False )
		self.m_grid_module.EnableDragColSize( True )
		self.m_grid_module.SetColLabelSize( 20 )
		self.m_grid_module.SetColLabelValue( 0, u"Name" )
		self.m_grid_module.SetColLabelValue( 1, u"Type" )
		self.m_grid_module.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid_module.EnableDragRowSize( False )
		self.m_grid_module.SetRowLabelSize( 0 )
		self.m_grid_module.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid_module.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_CENTER )
		b_sizer_module.Add( self.m_grid_module, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel_module.SetSizer( b_sizer_module )
		self.m_panel_module.Layout()
		b_sizer_module.Fit( self.m_panel_module )
		self.m_notebook_file_module.AddPage( self.m_panel_module, u"Module (2)", True )

		b_sizer_file_module.Add( self.m_notebook_file_module, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel_file_module.SetSizer( b_sizer_file_module )
		self.m_panel_file_module.Layout()
		b_sizer_file_module.Fit( self.m_panel_file_module )
		self.m_panel_object_outer = wx.Panel( self.m_splitter_file_object, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_object_outer = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook_object = wx.Notebook( self.m_panel_object_outer, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_object = wx.Panel( self.m_notebook_object, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_object = wx.BoxSizer( wx.VERTICAL )

		b_sizer_object_name = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_object_backward = wx.Button( self.m_panel_object, wx.ID_ANY, u"<", wx.DefaultPosition, wx.Size( 20,-1 ), 0 )
		b_sizer_object_name.Add( self.m_button_object_backward, 0, 0, 5 )

		self.m_static_text_object_name = wx.StaticText( self.m_panel_object, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_static_text_object_name.Wrap( -1 )

		b_sizer_object_name.Add( self.m_static_text_object_name, 0, wx.ALL|wx.EXPAND, 5 )


		b_sizer_object.Add( b_sizer_object_name, 0, wx.EXPAND, 5 )

		self.m_grid_object = wx.grid.Grid( self.m_panel_object, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid_object.CreateGrid( 0, 2 )
		self.m_grid_object.EnableEditing( False )
		self.m_grid_object.EnableGridLines( False )
		self.m_grid_object.EnableDragGridSize( False )
		self.m_grid_object.SetMargins( 0, 0 )

		# Columns
		self.m_grid_object.EnableDragColMove( False )
		self.m_grid_object.EnableDragColSize( True )
		self.m_grid_object.SetColLabelSize( 20 )
		self.m_grid_object.SetColLabelValue( 0, u"Name" )
		self.m_grid_object.SetColLabelValue( 1, u"Type" )
		self.m_grid_object.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid_object.EnableDragRowSize( False )
		self.m_grid_object.SetRowLabelSize( 0 )
		self.m_grid_object.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid_object.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_CENTER )
		b_sizer_object.Add( self.m_grid_object, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel_object.SetSizer( b_sizer_object )
		self.m_panel_object.Layout()
		b_sizer_object.Fit( self.m_panel_object )
		self.m_notebook_object.AddPage( self.m_panel_object, u"Object (3)", True )

		b_sizer_object_outer.Add( self.m_notebook_object, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel_object_outer.SetSizer( b_sizer_object_outer )
		self.m_panel_object_outer.Layout()
		b_sizer_object_outer.Fit( self.m_panel_object_outer )
		self.m_splitter_file_object.SplitVertically( self.m_panel_file_module, self.m_panel_object_outer, 0 )
		b_sizer_file_object.Add( self.m_splitter_file_object, 1, wx.EXPAND, 5 )


		self.m_panel_file_object.SetSizer( b_sizer_file_object )
		self.m_panel_file_object.Layout()
		b_sizer_file_object.Fit( self.m_panel_file_object )
		self.m_panel_code_outer = wx.Panel( self.m_splitter_file_object_code, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_code_outer = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook_code = wx.Notebook( self.m_panel_code_outer, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_code = wx.Panel( self.m_notebook_code, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_code = wx.BoxSizer( wx.VERTICAL )

		self.m_static_text_code_name = wx.StaticText( self.m_panel_code, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_static_text_code_name.Wrap( -1 )

		b_sizer_code.Add( self.m_static_text_code_name, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_rich_text_code = wx.richtext.RichTextCtrl( self.m_panel_code, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.ALWAYS_SHOW_SB|wx.BORDER_STATIC|wx.HSCROLL|wx.VSCROLL|wx.WANTS_CHARS )
		self.m_rich_text_code.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "D2Coding" ) )

		b_sizer_code.Add( self.m_rich_text_code, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel_code.SetSizer( b_sizer_code )
		self.m_panel_code.Layout()
		b_sizer_code.Fit( self.m_panel_code )
		self.m_notebook_code.AddPage( self.m_panel_code, u"Code (4)", True )

		b_sizer_code_outer.Add( self.m_notebook_code, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel_code_outer.SetSizer( b_sizer_code_outer )
		self.m_panel_code_outer.Layout()
		b_sizer_code_outer.Fit( self.m_panel_code_outer )
		self.m_splitter_file_object_code.SplitHorizontally( self.m_panel_file_object, self.m_panel_code_outer, 0 )
		b_sizer_north.Add( self.m_splitter_file_object_code, 1, wx.EXPAND, 5 )


		self.m_panel_file_object_code.SetSizer( b_sizer_north )
		self.m_panel_file_object_code.Layout()
		b_sizer_north.Fit( self.m_panel_file_object_code )
		self.m_panel_playground_output = wx.Panel( self.m_splitter_file_playground, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_code_playground = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter_code_playground = wx.SplitterWindow( self.m_panel_playground_output, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter_code_playground.SetSashGravity( 1 )
		self.m_splitter_code_playground.Bind( wx.EVT_IDLE, self.m_splitter_code_playgroundOnIdle )

		self.m_panel_playground_outer = wx.Panel( self.m_splitter_code_playground, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_playground_outer = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook_playground = wx.Notebook( self.m_panel_playground_outer, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_playground = wx.Panel( self.m_notebook_playground, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_playground = wx.BoxSizer( wx.VERTICAL )

		self.m_static_text_file_path = wx.StaticText( self.m_panel_playground, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_static_text_file_path.Wrap( -1 )

		b_sizer_playground.Add( self.m_static_text_file_path, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_rich_text_playground = wx.richtext.RichTextCtrl( self.m_panel_playground, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.ALWAYS_SHOW_SB|wx.BORDER_STATIC|wx.HSCROLL|wx.VSCROLL|wx.WANTS_CHARS )
		self.m_rich_text_playground.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "D2Coding" ) )

		b_sizer_playground.Add( self.m_rich_text_playground, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel_playground.SetSizer( b_sizer_playground )
		self.m_panel_playground.Layout()
		b_sizer_playground.Fit( self.m_panel_playground )
		self.m_notebook_playground.AddPage( self.m_panel_playground, u"Playground (5)", False )

		b_sizer_playground_outer.Add( self.m_notebook_playground, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel_playground_outer.SetSizer( b_sizer_playground_outer )
		self.m_panel_playground_outer.Layout()
		b_sizer_playground_outer.Fit( self.m_panel_playground_outer )
		self.m_panel_output_outer = wx.Panel( self.m_splitter_code_playground, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_output_outer = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook_output = wx.Notebook( self.m_panel_output_outer, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_output = wx.Panel( self.m_notebook_output, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_output = wx.BoxSizer( wx.VERTICAL )

		self.m_rich_text_output = wx.richtext.RichTextCtrl( self.m_panel_output, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.ALWAYS_SHOW_SB|wx.BORDER_STATIC|wx.HSCROLL|wx.VSCROLL|wx.WANTS_CHARS )
		self.m_rich_text_output.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "D2Coding" ) )

		b_sizer_output.Add( self.m_rich_text_output, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel_output.SetSizer( b_sizer_output )
		self.m_panel_output.Layout()
		b_sizer_output.Fit( self.m_panel_output )
		self.m_notebook_output.AddPage( self.m_panel_output, u"Output (6)", False )

		b_sizer_output_outer.Add( self.m_notebook_output, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel_output_outer.SetSizer( b_sizer_output_outer )
		self.m_panel_output_outer.Layout()
		b_sizer_output_outer.Fit( self.m_panel_output_outer )
		self.m_splitter_code_playground.SplitHorizontally( self.m_panel_playground_outer, self.m_panel_output_outer, -200 )
		b_sizer_code_playground.Add( self.m_splitter_code_playground, 1, wx.EXPAND, 5 )


		self.m_panel_playground_output.SetSizer( b_sizer_code_playground )
		self.m_panel_playground_output.Layout()
		b_sizer_code_playground.Fit( self.m_panel_playground_output )
		self.m_splitter_file_playground.SplitVertically( self.m_panel_file_object_code, self.m_panel_playground_output, 300 )
		b_sizer_main.Add( self.m_splitter_file_playground, 1, wx.EXPAND, 5 )


		self.m_panel_main.SetSizer( b_sizer_main )
		self.m_panel_main.Layout()
		b_sizer_main.Fit( self.m_panel_main )
		self.m_panel_help_outer = wx.Panel( self.m_splitter_main_help, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_help_outer = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook_help = wx.Notebook( self.m_panel_help_outer, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_help = wx.Panel( self.m_notebook_help, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_help = wx.BoxSizer( wx.VERTICAL )

		self.m_rich_text_help = wx.richtext.RichTextCtrl( self.m_panel_help, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.ALWAYS_SHOW_SB|wx.BORDER_STATIC|wx.HSCROLL|wx.VSCROLL|wx.WANTS_CHARS )
		self.m_rich_text_help.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "D2Coding" ) )

		b_sizer_help.Add( self.m_rich_text_help, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel_help.SetSizer( b_sizer_help )
		self.m_panel_help.Layout()
		b_sizer_help.Fit( self.m_panel_help )
		self.m_notebook_help.AddPage( self.m_panel_help, u"Help (7)", True )

		b_sizer_help_outer.Add( self.m_notebook_help, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel_help_outer.SetSizer( b_sizer_help_outer )
		self.m_panel_help_outer.Layout()
		b_sizer_help_outer.Fit( self.m_panel_help_outer )
		self.m_splitter_main_help.SplitVertically( self.m_panel_main, self.m_panel_help_outer, -200 )
		b_sizer_main_outer.Add( self.m_splitter_main_help, 1, wx.EXPAND, 5 )


		self.SetSizer( b_sizer_main_outer )
		self.Layout()
		self.m_status_bar_main = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.on_menu_selection_file_open_directory, id = self.m_menu_item_file_open_directory.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_selection_file_new, id = self.m_menu_item_file_new.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_selection_file_open, id = self.m_menu_item_file_open.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_selection_file_save, id = self.m_menu_item_file_save.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_selection_file_save_as, id = self.m_menu_item_file_save_as.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_selection_file_close, id = self.m_menu_item_file_close.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_command_update_module_list, id = self.m_menu_item_command_update_module_list.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_command_do_selection, id = self.m_menu_item_command_do_selection.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_command_do_all, id = self.m_menu_item_command_do_all.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_command_print_selection, id = self.m_menu_item_command_print_selection.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_command_clear_output, id = self.m_menu_item_command_clear_output.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_command_help_on_selection, id = self.m_menu_item_command_help_on_selection.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_selection_select_font, id = self.m_menu_item_tool_font.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_selection_find_file, id = self.m_menu_item_tool_find_file.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_selection_find_module, id = self.m_menu_item_tool_find_module.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_selection_find_object, id = self.m_menu_item_tool_find_object.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_selection_find_text, id = self.m_menu_item_tool_find_text.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_selection_find_next, id = self.m_menu_item_tool_find_next.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_selection_show_file, id = self.m_menu_item_show_file.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_selection_show_module, id = self.m_menu_item_show_module.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_selection_show_object, id = self.m_menu_item_show_object.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_selection_show_code, id = self.m_menu_item_show_code.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_selection_show_playground, id = self.m_menu_item_show_playground.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_selection_show_output, id = self.m_menu_item_show_output.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_selection_show_help, id = self.m_menu_item_show_help.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_help_about, id = self.m_menu_item_about.GetId() )
		self.m_grid_module.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.on_grid_select_cell_module )
		self.m_button_object_backward.Bind( wx.EVT_BUTTON, self.on_button_click_object_backward )
		self.m_grid_object.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.on_grid_double_click_object )
		self.m_grid_object.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.on_grid_select_cell_object )
		self.m_rich_text_code.Bind( wx.EVT_SET_FOCUS, self.on_set_focus_code )
		self.m_rich_text_playground.Bind( wx.EVT_SET_FOCUS, self.on_set_focus_playground )
		self.m_rich_text_output.Bind( wx.EVT_SET_FOCUS, self.on_set_focus_output )
		self.m_rich_text_help.Bind( wx.EVT_SET_FOCUS, self.on_set_focus_help )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_menu_selection_file_open_directory( self, event ):
		event.Skip()

	def on_menu_selection_file_new( self, event ):
		event.Skip()

	def on_menu_selection_file_open( self, event ):
		event.Skip()

	def on_menu_selection_file_save( self, event ):
		event.Skip()

	def on_menu_selection_file_save_as( self, event ):
		event.Skip()

	def on_menu_selection_file_close( self, event ):
		event.Skip()

	def on_menu_command_update_module_list( self, event ):
		event.Skip()

	def on_menu_command_do_selection( self, event ):
		event.Skip()

	def on_menu_command_do_all( self, event ):
		event.Skip()

	def on_menu_command_print_selection( self, event ):
		event.Skip()

	def on_menu_command_clear_output( self, event ):
		event.Skip()

	def on_menu_command_help_on_selection( self, event ):
		event.Skip()

	def on_menu_selection_select_font( self, event ):
		event.Skip()

	def on_menu_selection_find_file( self, event ):
		event.Skip()

	def on_menu_selection_find_module( self, event ):
		event.Skip()

	def on_menu_selection_find_object( self, event ):
		event.Skip()

	def on_menu_selection_find_text( self, event ):
		event.Skip()

	def on_menu_selection_find_next( self, event ):
		event.Skip()

	def on_menu_selection_show_file( self, event ):
		event.Skip()

	def on_menu_selection_show_module( self, event ):
		event.Skip()

	def on_menu_selection_show_object( self, event ):
		event.Skip()

	def on_menu_selection_show_code( self, event ):
		event.Skip()

	def on_menu_selection_show_playground( self, event ):
		event.Skip()

	def on_menu_selection_show_output( self, event ):
		event.Skip()

	def on_menu_selection_show_help( self, event ):
		event.Skip()

	def on_menu_help_about( self, event ):
		event.Skip()

	def on_grid_select_cell_module( self, event ):
		event.Skip()

	def on_button_click_object_backward( self, event ):
		event.Skip()

	def on_grid_double_click_object( self, event ):
		event.Skip()

	def on_grid_select_cell_object( self, event ):
		event.Skip()

	def on_set_focus_code( self, event ):
		event.Skip()

	def on_set_focus_playground( self, event ):
		event.Skip()

	def on_set_focus_output( self, event ):
		event.Skip()

	def on_set_focus_help( self, event ):
		event.Skip()

	def m_splitter_main_helpOnIdle( self, event ):
		self.m_splitter_main_help.SetSashPosition( -200 )
		self.m_splitter_main_help.Unbind( wx.EVT_IDLE )

	def m_splitter_file_playgroundOnIdle( self, event ):
		self.m_splitter_file_playground.SetSashPosition( 300 )
		self.m_splitter_file_playground.Unbind( wx.EVT_IDLE )

	def m_splitter_file_object_codeOnIdle( self, event ):
		self.m_splitter_file_object_code.SetSashPosition( 0 )
		self.m_splitter_file_object_code.Unbind( wx.EVT_IDLE )

	def m_splitter_file_objectOnIdle( self, event ):
		self.m_splitter_file_object.SetSashPosition( 0 )
		self.m_splitter_file_object.Unbind( wx.EVT_IDLE )

	def m_splitter_code_playgroundOnIdle( self, event ):
		self.m_splitter_code_playground.SetSashPosition( -200 )
		self.m_splitter_code_playground.Unbind( wx.EVT_IDLE )


###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


