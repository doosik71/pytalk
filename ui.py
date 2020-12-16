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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PyTalk", pos = wx.DefaultPosition, size = wx.Size( 1024,768 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar_main = wx.MenuBar( 0 )
		self.m_menu_file = wx.Menu()
		self.m_menu_item_close = wx.MenuItem( self.m_menu_file, wx.ID_CLOSE, u"&Close"+ u"\t" + u"Alt+C", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.Append( self.m_menu_item_close )

		self.m_menubar_main.Append( self.m_menu_file, u"File" )

		self.m_menu_command = wx.Menu()
		self.m_menu_item_do_selection = wx.MenuItem( self.m_menu_command, wx.ID_ANY, u"Do selection"+ u"\t" + u"Alt+D", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_command.Append( self.m_menu_item_do_selection )

		self.m_menu_item_do_all = wx.MenuItem( self.m_menu_command, wx.ID_ANY, u"Do all"+ u"\t" + u"Ctrl+Alt+D", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_command.Append( self.m_menu_item_do_all )

		self.m_menu_item_print_selection = wx.MenuItem( self.m_menu_command, wx.ID_ANY, u"Print selection"+ u"\t" + u"Alt+P", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_command.Append( self.m_menu_item_print_selection )

		self.m_menu_item_clear_output = wx.MenuItem( self.m_menu_command, wx.ID_ANY, u"Clear output", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_command.Append( self.m_menu_item_clear_output )

		self.m_menu_item_update_module_list = wx.MenuItem( self.m_menu_command, wx.ID_ANY, u"Update module list", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_command.Append( self.m_menu_item_update_module_list )

		self.m_menu_item_help_on_selection = wx.MenuItem( self.m_menu_command, wx.ID_ANY, u"Help on selection"+ u"\t" + u"Ctrl+H", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_command.Append( self.m_menu_item_help_on_selection )

		self.m_menubar_main.Append( self.m_menu_command, u"Command" )

		self.m_menu_tool = wx.Menu()
		self.m_menubar_main.Append( self.m_menu_tool, u"Tool" )

		self.m_menu_show = wx.Menu()
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

		self.m_splitter_main_horizontal = wx.SplitterWindow( self.m_panel_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_3DBORDER|wx.SP_3DSASH|wx.SP_BORDER|wx.SP_LIVE_UPDATE )
		self.m_splitter_main_horizontal.SetSashGravity( 0.5 )
		self.m_splitter_main_horizontal.Bind( wx.EVT_IDLE, self.m_splitter_main_horizontalOnIdle )
		self.m_splitter_main_horizontal.SetMinimumPaneSize( 100 )

		self.m_panel_file_object_code = wx.Panel( self.m_splitter_main_horizontal, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_north = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter_file_code = wx.SplitterWindow( self.m_panel_file_object_code, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter_file_code.SetSashGravity( 0.5 )
		self.m_splitter_file_code.Bind( wx.EVT_IDLE, self.m_splitter_file_codeOnIdle )
		self.m_splitter_file_code.SetMinimumPaneSize( 100 )

		self.m_panel_file_object = wx.Panel( self.m_splitter_file_code, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
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
		self.m_notebook_file_module.AddPage( self.m_panel_file, u"File", False )
		self.m_panel_module = wx.Panel( self.m_notebook_file_module, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_module = wx.BoxSizer( wx.VERTICAL )

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

		self.m_static_text_module_name = wx.StaticText( self.m_panel_module, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_static_text_module_name.Wrap( -1 )

		b_sizer_module.Add( self.m_static_text_module_name, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel_module.SetSizer( b_sizer_module )
		self.m_panel_module.Layout()
		b_sizer_module.Fit( self.m_panel_module )
		self.m_notebook_file_module.AddPage( self.m_panel_module, u"Module", True )

		b_sizer_file_module.Add( self.m_notebook_file_module, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel_file_module.SetSizer( b_sizer_file_module )
		self.m_panel_file_module.Layout()
		b_sizer_file_module.Fit( self.m_panel_file_module )
		self.m_panel_object_outer = wx.Panel( self.m_splitter_file_object, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_object_outer = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook_object = wx.Notebook( self.m_panel_object_outer, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_object = wx.Panel( self.m_notebook_object, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_object = wx.BoxSizer( wx.VERTICAL )

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

		self.m_static_text_object_name = wx.StaticText( self.m_panel_object, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_static_text_object_name.Wrap( -1 )

		b_sizer_object.Add( self.m_static_text_object_name, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel_object.SetSizer( b_sizer_object )
		self.m_panel_object.Layout()
		b_sizer_object.Fit( self.m_panel_object )
		self.m_notebook_object.AddPage( self.m_panel_object, u"Object", True )

		b_sizer_object_outer.Add( self.m_notebook_object, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel_object_outer.SetSizer( b_sizer_object_outer )
		self.m_panel_object_outer.Layout()
		b_sizer_object_outer.Fit( self.m_panel_object_outer )
		self.m_splitter_file_object.SplitVertically( self.m_panel_file_module, self.m_panel_object_outer, 0 )
		b_sizer_file_object.Add( self.m_splitter_file_object, 1, wx.EXPAND, 5 )


		self.m_panel_file_object.SetSizer( b_sizer_file_object )
		self.m_panel_file_object.Layout()
		b_sizer_file_object.Fit( self.m_panel_file_object )
		self.m_panel_code_outer = wx.Panel( self.m_splitter_file_code, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_code_outer = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook_code = wx.Notebook( self.m_panel_code_outer, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_code = wx.Panel( self.m_notebook_code, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_code = wx.BoxSizer( wx.VERTICAL )

		self.m_rich_text_code = wx.richtext.RichTextCtrl( self.m_panel_code, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.ALWAYS_SHOW_SB|wx.BORDER_STATIC|wx.HSCROLL|wx.VSCROLL|wx.WANTS_CHARS )
		b_sizer_code.Add( self.m_rich_text_code, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel_code.SetSizer( b_sizer_code )
		self.m_panel_code.Layout()
		b_sizer_code.Fit( self.m_panel_code )
		self.m_notebook_code.AddPage( self.m_panel_code, u"Code", True )

		b_sizer_code_outer.Add( self.m_notebook_code, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel_code_outer.SetSizer( b_sizer_code_outer )
		self.m_panel_code_outer.Layout()
		b_sizer_code_outer.Fit( self.m_panel_code_outer )
		self.m_splitter_file_code.SplitVertically( self.m_panel_file_object, self.m_panel_code_outer, 0 )
		b_sizer_north.Add( self.m_splitter_file_code, 1, wx.EXPAND, 5 )


		self.m_panel_file_object_code.SetSizer( b_sizer_north )
		self.m_panel_file_object_code.Layout()
		b_sizer_north.Fit( self.m_panel_file_object_code )
		self.m_panel_playground_output = wx.Panel( self.m_splitter_main_horizontal, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_playground_output = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter_playground_output = wx.SplitterWindow( self.m_panel_playground_output, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter_playground_output.SetSashGravity( 0.5 )
		self.m_splitter_playground_output.Bind( wx.EVT_IDLE, self.m_splitter_playground_outputOnIdle )

		self.m_panel_playground_outer = wx.Panel( self.m_splitter_playground_output, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_playground_outer = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook_playground = wx.Notebook( self.m_panel_playground_outer, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_playground = wx.Panel( self.m_notebook_playground, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_playground = wx.BoxSizer( wx.VERTICAL )

		self.m_rich_text_playground = wx.richtext.RichTextCtrl( self.m_panel_playground, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.ALWAYS_SHOW_SB|wx.BORDER_STATIC|wx.HSCROLL|wx.VSCROLL|wx.WANTS_CHARS )
		b_sizer_playground.Add( self.m_rich_text_playground, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel_playground.SetSizer( b_sizer_playground )
		self.m_panel_playground.Layout()
		b_sizer_playground.Fit( self.m_panel_playground )
		self.m_notebook_playground.AddPage( self.m_panel_playground, u"Playground", False )

		b_sizer_playground_outer.Add( self.m_notebook_playground, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel_playground_outer.SetSizer( b_sizer_playground_outer )
		self.m_panel_playground_outer.Layout()
		b_sizer_playground_outer.Fit( self.m_panel_playground_outer )
		self.m_panel_output_outer = wx.Panel( self.m_splitter_playground_output, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_output_outer = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook_output = wx.Notebook( self.m_panel_output_outer, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_output = wx.Panel( self.m_notebook_output, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_output = wx.BoxSizer( wx.VERTICAL )

		self.m_rich_text_output = wx.richtext.RichTextCtrl( self.m_panel_output, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.ALWAYS_SHOW_SB|wx.BORDER_STATIC|wx.HSCROLL|wx.VSCROLL|wx.WANTS_CHARS )
		b_sizer_output.Add( self.m_rich_text_output, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel_output.SetSizer( b_sizer_output )
		self.m_panel_output.Layout()
		b_sizer_output.Fit( self.m_panel_output )
		self.m_notebook_output.AddPage( self.m_panel_output, u"Output", False )

		b_sizer_output_outer.Add( self.m_notebook_output, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel_output_outer.SetSizer( b_sizer_output_outer )
		self.m_panel_output_outer.Layout()
		b_sizer_output_outer.Fit( self.m_panel_output_outer )
		self.m_splitter_playground_output.SplitVertically( self.m_panel_playground_outer, self.m_panel_output_outer, 0 )
		b_sizer_playground_output.Add( self.m_splitter_playground_output, 1, wx.EXPAND, 5 )


		self.m_panel_playground_output.SetSizer( b_sizer_playground_output )
		self.m_panel_playground_output.Layout()
		b_sizer_playground_output.Fit( self.m_panel_playground_output )
		self.m_splitter_main_horizontal.SplitHorizontally( self.m_panel_file_object_code, self.m_panel_playground_output, 0 )
		b_sizer_main.Add( self.m_splitter_main_horizontal, 1, wx.EXPAND, 5 )


		self.m_panel_main.SetSizer( b_sizer_main )
		self.m_panel_main.Layout()
		b_sizer_main.Fit( self.m_panel_main )
		self.m_panel_help_outer = wx.Panel( self.m_splitter_main_help, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_help_outer = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook_help = wx.Notebook( self.m_panel_help_outer, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_help = wx.Panel( self.m_notebook_help, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		b_sizer_help = wx.BoxSizer( wx.VERTICAL )

		self.m_rich_text_help = wx.richtext.RichTextCtrl( self.m_panel_help, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.ALWAYS_SHOW_SB|wx.BORDER_STATIC|wx.HSCROLL|wx.VSCROLL|wx.WANTS_CHARS )
		b_sizer_help.Add( self.m_rich_text_help, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel_help.SetSizer( b_sizer_help )
		self.m_panel_help.Layout()
		b_sizer_help.Fit( self.m_panel_help )
		self.m_notebook_help.AddPage( self.m_panel_help, u"Help", True )

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
		self.Bind( wx.EVT_MENU, self.on_menu_command_do_selection, id = self.m_menu_item_do_selection.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_command_do_all, id = self.m_menu_item_do_all.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_command_print_selection, id = self.m_menu_item_print_selection.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_command_clear_output, id = self.m_menu_item_clear_output.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_command_update_module_list, id = self.m_menu_item_update_module_list.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_command_help_on_selection, id = self.m_menu_item_help_on_selection.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_help_about, id = self.m_menu_item_about.GetId() )
		self.m_grid_module.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.on_grid_select_cell_module )
		self.m_grid_object.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.on_grid_select_cell_object )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_menu_command_do_selection( self, event ):
		event.Skip()

	def on_menu_command_do_all( self, event ):
		event.Skip()

	def on_menu_command_print_selection( self, event ):
		event.Skip()

	def on_menu_command_clear_output( self, event ):
		event.Skip()

	def on_menu_command_update_module_list( self, event ):
		event.Skip()

	def on_menu_command_help_on_selection( self, event ):
		event.Skip()

	def on_menu_help_about( self, event ):
		event.Skip()

	def on_grid_select_cell_module( self, event ):
		event.Skip()

	def on_grid_select_cell_object( self, event ):
		event.Skip()

	def m_splitter_main_helpOnIdle( self, event ):
		self.m_splitter_main_help.SetSashPosition( -200 )
		self.m_splitter_main_help.Unbind( wx.EVT_IDLE )

	def m_splitter_main_horizontalOnIdle( self, event ):
		self.m_splitter_main_horizontal.SetSashPosition( 0 )
		self.m_splitter_main_horizontal.Unbind( wx.EVT_IDLE )

	def m_splitter_file_codeOnIdle( self, event ):
		self.m_splitter_file_code.SetSashPosition( 0 )
		self.m_splitter_file_code.Unbind( wx.EVT_IDLE )

	def m_splitter_file_objectOnIdle( self, event ):
		self.m_splitter_file_object.SetSashPosition( 0 )
		self.m_splitter_file_object.Unbind( wx.EVT_IDLE )

	def m_splitter_playground_outputOnIdle( self, event ):
		self.m_splitter_playground_output.SetSashPosition( 0 )
		self.m_splitter_playground_output.Unbind( wx.EVT_IDLE )


###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1045,739 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


