#**********************************************
#	This file was automatically generated 2018:05:29T14:58:00
#	
#	DO NOT EDIT THIS FILE -- Use Dialog Builder Tools to edit this file.
#***********************************************

import vs

# control IDs
kOK                   = 1
kCancel               = 2
kFixtureNameLabel     = 4
kFixtureNumberLabel   = 5
kDmaUniverseLabel     = 6
kDmxAddressLabel      = 8
kFixtureNamePopup     = 15
kFixtureNumberPopup   = 16
kDmxUniversePopup     = 17
kDmxAddressPopup      = 18
kLightingTypesLB      = 32

def CreateDialog():
    # Alignment constants
    kRight                = 1
    kBottom               = 2
    kLeft                 = 3
    kColumn               = 4
    kResize               = 0
    kShift                = 1

    def GetPluginString(ndx):
        # Static Text
        if ndx == 1001:			return 'OK'
        elif ndx == 1002:		return 'Cancel'
        elif ndx == 1003:		return 'Jands Vista Export Patch'
        elif ndx == 1004:		return 'Fixture Name:'
        elif ndx == 1005:		return 'Fixture Number:'
        elif ndx == 1006:		return 'DMX Universe:'
        elif ndx == 1008:		return 'DMX Address:'
        elif ndx == 1015:		return ''
        elif ndx == 1016:		return ''
        elif ndx == 1017:		return ''
        elif ndx == 1018:		return ''
        elif ndx == 1032:		return ''
        # Help Text
        elif ndx == 2001:		return 'Accepts the dialog data.'
        elif ndx == 2002:		return 'Cancels the dialog data.'
        elif ndx == 2004:		return 'Help text.'
        elif ndx == 2005:		return 'Help text.'
        elif ndx == 2006:		return 'Help text.'
        elif ndx == 2008:		return 'Help text.'
        elif ndx == 2015:		return 'Help text.'
        elif ndx == 2016:		return 'Help text.'
        elif ndx == 2017:		return 'Help text.'
        elif ndx == 2018:		return 'Help text.'
        elif ndx == 2032:		return 'Help text.'
        return ''

    def GetStr(ndx):
        result = GetPluginString( ndx + 1000 )
        return result

    def GetHelpStr(ndx):
        result = GetPluginString( ndx + 2000 )
        return result

    dialog = vs.CreateLayout( GetStr(3), False, GetStr(kOK), GetStr(kCancel) )

    # create controls
    vs.CreateStaticText( dialog, kFixtureNameLabel, GetStr(kFixtureNameLabel), -1 )
    vs.CreatePullDownMenu( dialog, kFixtureNamePopup, 16 )
    vs.CreateStaticText( dialog, kFixtureNumberLabel, GetStr(kFixtureNumberLabel), -1 )
    vs.CreatePullDownMenu( dialog, kFixtureNumberPopup, 16 )
    vs.CreateStaticText( dialog, kDmaUniverseLabel, GetStr(kDmaUniverseLabel), -1 )
    vs.CreatePullDownMenu( dialog, kDmxUniversePopup, 16 )
    vs.CreateStaticText( dialog, kDmxAddressLabel, GetStr(kDmxAddressLabel), -1 )
    vs.CreatePullDownMenu( dialog, kDmxAddressPopup, 16 )
    vs.CreateLB( dialog, kLightingTypesLB, 34, 15 )

    # set relations
    vs.SetFirstLayoutItem( dialog, kFixtureNameLabel )
    vs.SetRightItem( dialog, kFixtureNameLabel, kFixtureNamePopup, 5, 0 )
    vs.SetBelowItem( dialog, kFixtureNameLabel, kFixtureNumberLabel, 0, 0 )
    vs.SetRightItem( dialog, kFixtureNumberLabel, kFixtureNumberPopup, 5, 0 )
    vs.SetBelowItem( dialog, kFixtureNumberLabel, kDmaUniverseLabel, 0, 0 )
    vs.SetRightItem( dialog, kDmaUniverseLabel, kDmxUniversePopup, 5, 0 )
    vs.SetBelowItem( dialog, kDmaUniverseLabel, kDmxAddressLabel, 0, 0 )
    vs.SetRightItem( dialog, kDmxAddressLabel, kDmxAddressPopup, 5, 0 )
    vs.SetBelowItem( dialog, kDmxAddressLabel, kLightingTypesLB, 0, 0 )

    # set alignments
    vs.AlignItemEdge( dialog, kFixtureNamePopup, kRight, 1, kShift );
    vs.AlignItemEdge( dialog, kFixtureNumberPopup, kRight, 1, kShift );
    vs.AlignItemEdge( dialog, kDmxUniversePopup, kRight, 1, kShift );
    vs.AlignItemEdge( dialog, kDmxAddressPopup, kRight, 1, kShift );

    # set help strings
    cnt = 1
    while ( cnt <= 32 ):
        vs.SetHelpText( dialog, cnt, GetHelpStr(cnt) )
        cnt += 1

    return dialog

# Sample dialog handler
# Uncomment this code if you want to display the dialog
'''
def DialogHandler(item, data):
	pass

dlg = CreateDialog()
vs.RunLayoutDialog( dlg, DialogHandler )
'''

# XML defintion of the layout
#
# <BEGIN_XML>
#<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
# <DialogBuilder>
# 
#   <LayoutData>
#     <Name>dlg</Name>
#     <Title>Jands Vista Export Patch</Title>
#     <OKText>OK</OKText>
#     <OKHelpText>Accepts the dialog data.</OKHelpText>
#     <CancelText>Cancel</CancelText>
#     <CancelHelpText>Cancels the dialog data.</CancelHelpText>
#     <HasHelp>FALSE</HasHelp>
#     <ResizableWidth>FALSE</ResizableWidth>
#     <ResizableHeight>FALSE</ResizableHeight>
#     <StringsStartID>0</StringsStartID>
#     <HelpStrStartID>1</HelpStrStartID>
#     <TablesAddToDlgRes>TRUE</TablesAddToDlgRes>
#     <AltStringStartID>0</AltStringStartID>
#     <ResourceRoot>PluginModule_resource_file_vwr</ResourceRoot>
#   </LayoutData>
# 
#   <Controls>
#     <Control name="DialogBuilderControl" x="0" y="0">
#       <Parameter Name="__UUID">{2E6492D2-5EB8-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="id">4</Parameter>
#       <Parameter Name="constName">FixtureNameLabel</Parameter>
#       <Parameter Name="label">Fixture Name:</Parameter>
#       <Parameter Name="helpText">Help text.</Parameter>
#       <Parameter Name="alignEdge">kLeft</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">42mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-14mm</Parameter>
#       <Parameter Name="ControlPoint01X">14mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-12mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__RightUUID">{05915EE9-5EB9-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="__BottomUUID">{69F4DB2E-5EB8-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="__savedHandleRightX">42mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-14mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">14mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-12mm</Parameter>
#       <Parameter Name="__fVisControlWidth">24</Parameter>
#       <Parameter Name="__fVisControlHeight">5</Parameter>
#     </Control>
#     <Control name="DialogBuilderControl" x="0" y="-12">
#       <Parameter Name="__UUID">{69F4DB2E-5EB8-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="id">5</Parameter>
#       <Parameter Name="constName">FixtureNumberLabel</Parameter>
#       <Parameter Name="label">Fixture Number:</Parameter>
#       <Parameter Name="helpText">Help text.</Parameter>
#       <Parameter Name="alignEdge">kLeft</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">42mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-3mm</Parameter>
#       <Parameter Name="ControlPoint01X">13mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-13mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__RightUUID">{05915EEA-5EB9-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="__BottomUUID">{69F4DBF5-5EB8-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="__savedHandleRightX">42mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-3mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">13mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-13mm</Parameter>
#       <Parameter Name="__fVisControlWidth">28</Parameter>
#       <Parameter Name="__fVisControlHeight">5</Parameter>
#     </Control>
#     <Control name="DialogBuilderControl" x="0" y="-25">
#       <Parameter Name="__UUID">{69F4DBF5-5EB8-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="id">6</Parameter>
#       <Parameter Name="constName">DmaUniverseLabel</Parameter>
#       <Parameter Name="label">DMX Universe:</Parameter>
#       <Parameter Name="helpText">Help text.</Parameter>
#       <Parameter Name="alignEdge">kLeft</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">42mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-3mm</Parameter>
#       <Parameter Name="ControlPoint01X">12mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-13mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__RightUUID">{05915EEB-5EB9-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="__BottomUUID">{B33D7957-5EB8-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="__savedHandleRightX">42mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-3mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">12mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-13mm</Parameter>
#       <Parameter Name="__fVisControlWidth">25</Parameter>
#       <Parameter Name="__fVisControlHeight">5</Parameter>
#     </Control>
#     <Control name="DialogBuilderControl" x="0" y="-38">
#       <Parameter Name="__UUID">{B33D7957-5EB8-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="id">8</Parameter>
#       <Parameter Name="constName">DmxAddressLabel</Parameter>
#       <Parameter Name="label">DMX Address:</Parameter>
#       <Parameter Name="helpText">Help text.</Parameter>
#       <Parameter Name="alignEdge">kLeft</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">42mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-3mm</Parameter>
#       <Parameter Name="ControlPoint01X">28mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-26mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__RightUUID">{05915EEC-5EB9-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="__BottomUUID">{6A2830BF-60E9-11E8-A5FA-80FA5B3AEA67}</Parameter>
#       <Parameter Name="__savedHandleRightX">42mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-3mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">28mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-26mm</Parameter>
#       <Parameter Name="__fVisControlWidth">24</Parameter>
#       <Parameter Name="__fVisControlHeight">5</Parameter>
#     </Control>
#     <Control name="Dialog Builder Link" x="0" y="0">
#       <Parameter Name="ParentObj">{69F4DB2E-5EB8-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="RelatedObj">{69F4DBF5-5EB8-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="ParentMode">1</Parameter>
#     </Control>
#     <Control name="Dialog Builder Link" x="0" y="0">
#       <Parameter Name="ParentObj">{2E6492D2-5EB8-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="RelatedObj">{69F4DB2E-5EB8-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="ParentMode">1</Parameter>
#     </Control>
#     <Control name="Dialog Builder Link" x="0" y="0">
#       <Parameter Name="ParentObj">{69F4DBF5-5EB8-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="RelatedObj">{B33D7957-5EB8-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="ParentMode">1</Parameter>
#     </Control>
#     <Control name="DialogBuilderControl" x="42" y="0">
#       <Parameter Name="__UUID">{05915EE9-5EB9-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="type">kTextPopup</Parameter>
#       <Parameter Name="id">15</Parameter>
#       <Parameter Name="constName">FixtureNamePopup</Parameter>
#       <Parameter Name="value">a;b;c;</Parameter>
#       <Parameter Name="helpText">Help text.</Parameter>
#       <Parameter Name="horzOffset">5</Parameter>
#       <Parameter Name="alignGroup">1</Parameter>
#       <Parameter Name="alignMode">kShift</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">20mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-2mm</Parameter>
#       <Parameter Name="ControlPoint01X">10mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-5mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__savedHandleRightX">20mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-2mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">10mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-5mm</Parameter>
#       <Parameter Name="__fVisControlWidth">20</Parameter>
#       <Parameter Name="__fVisControlHeight">5</Parameter>
#     </Control>
#     <Control name="DialogBuilderControl" x="42" y="-12">
#       <Parameter Name="__UUID">{05915EEA-5EB9-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="type">kTextPopup</Parameter>
#       <Parameter Name="id">16</Parameter>
#       <Parameter Name="constName">FixtureNumberPopup</Parameter>
#       <Parameter Name="value">d;e;f;</Parameter>
#       <Parameter Name="helpText">Help text.</Parameter>
#       <Parameter Name="horzOffset">5</Parameter>
#       <Parameter Name="alignGroup">1</Parameter>
#       <Parameter Name="alignMode">kShift</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">20mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-2mm</Parameter>
#       <Parameter Name="ControlPoint01X">10mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-5mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__savedHandleRightX">20mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-2mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">10mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-5mm</Parameter>
#       <Parameter Name="__fVisControlWidth">20</Parameter>
#       <Parameter Name="__fVisControlHeight">5</Parameter>
#     </Control>
#     <Control name="DialogBuilderControl" x="42" y="-25">
#       <Parameter Name="__UUID">{05915EEB-5EB9-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="type">kTextPopup</Parameter>
#       <Parameter Name="id">17</Parameter>
#       <Parameter Name="constName">DmxUniversePopup</Parameter>
#       <Parameter Name="value">g;h;i;</Parameter>
#       <Parameter Name="helpText">Help text.</Parameter>
#       <Parameter Name="horzOffset">5</Parameter>
#       <Parameter Name="alignGroup">1</Parameter>
#       <Parameter Name="alignMode">kShift</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">20mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-2mm</Parameter>
#       <Parameter Name="ControlPoint01X">10mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-5mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__savedHandleRightX">20mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-2mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">10mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-5mm</Parameter>
#       <Parameter Name="__fVisControlWidth">20</Parameter>
#       <Parameter Name="__fVisControlHeight">5</Parameter>
#     </Control>
#     <Control name="DialogBuilderControl" x="42" y="-38">
#       <Parameter Name="__UUID">{05915EEC-5EB9-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="type">kTextPopup</Parameter>
#       <Parameter Name="id">18</Parameter>
#       <Parameter Name="constName">DmxAddressPopup</Parameter>
#       <Parameter Name="value">j;k;l;</Parameter>
#       <Parameter Name="helpText">Help text.</Parameter>
#       <Parameter Name="horzOffset">5</Parameter>
#       <Parameter Name="alignGroup">1</Parameter>
#       <Parameter Name="alignMode">kShift</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">20mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-2mm</Parameter>
#       <Parameter Name="ControlPoint01X">10mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-5mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__savedHandleRightX">20mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-2mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">10mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-5mm</Parameter>
#       <Parameter Name="__fVisControlWidth">20</Parameter>
#       <Parameter Name="__fVisControlHeight">5</Parameter>
#     </Control>
#     <Control name="Dialog Builder Link" x="0" y="0">
#       <Parameter Name="ParentObj">{2E6492D2-5EB8-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="RelatedObj">{05915EE9-5EB9-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="ParentMode">0</Parameter>
#     </Control>
#     <Control name="Dialog Builder Link" x="0" y="0">
#       <Parameter Name="ParentObj">{69F4DB2E-5EB8-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="RelatedObj">{05915EEA-5EB9-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="ParentMode">0</Parameter>
#     </Control>
#     <Control name="Dialog Builder Link" x="0" y="0">
#       <Parameter Name="ParentObj">{69F4DBF5-5EB8-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="RelatedObj">{05915EEB-5EB9-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="ParentMode">0</Parameter>
#     </Control>
#     <Control name="Dialog Builder Link" x="0" y="0">
#       <Parameter Name="ParentObj">{B33D7957-5EB8-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="RelatedObj">{05915EEC-5EB9-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="ParentMode">0</Parameter>
#     </Control>
#     <Control name="DialogBuilderControl" x="5" y="-64">
#       <Parameter Name="__UUID">{6A2830BF-60E9-11E8-A5FA-80FA5B3AEA67}</Parameter>
#       <Parameter Name="type">kListBrowser</Parameter>
#       <Parameter Name="id">32</Parameter>
#       <Parameter Name="constName">LightingTypesLB</Parameter>
#       <Parameter Name="value">TRUE;TRUE;FALSE;Export.10.2.[a,TRUE,0,1];Light Type.30.32762.[b,TRUE,0,1];</Parameter>
#       <Parameter Name="helpText">Help text.</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="ctrlWidth">40</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">46mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-14mm</Parameter>
#       <Parameter Name="ControlPoint01X">23mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-28mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__savedHandleRightX">46mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-14mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">23mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-28mm</Parameter>
#       <Parameter Name="__fVisControlWidth">46</Parameter>
#       <Parameter Name="__fVisControlHeight">28</Parameter>
#     </Control>
#     <Control name="Dialog Builder Link" x="0" y="0">
#       <Parameter Name="ParentObj">{B33D7957-5EB8-11E8-A5F3-80FA5B3AEA67}</Parameter>
#       <Parameter Name="RelatedObj">{6A2830BF-60E9-11E8-A5FA-80FA5B3AEA67}</Parameter>
#       <Parameter Name="ParentMode">1</Parameter>
#     </Control>
#   </Controls>
# 
# </DialogBuilder>
# 
# <END_XML>
