# **[components-navigation-and-search] path-controls**

## A path control shows the file system path of a selected file or folder.
> 경로 제어는 선택한 파일 또는 폴더의 파일 시스템 경로를 표시합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/path-control-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/path-control-intro-dark_2x.png)

For example, choosing View > Show Path Bar in the Finder displays a path bar at the bottom of the window. It shows the path of the selected item, or the path of the window’s folder if nothing is selected.
> 예를 들어, Finder에서 View > Show Path Bar를 선택하면 창 하단에 경로 표시줄이 표시됩니다. 선택한 항목의 경로 또는 아무것도 선택되지 않은 경우 창의 폴더 경로를 표시합니다.
>




There are two styles of path control.
> 경로 제어에는 두 가지 유형이 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/path-controls/images/path-controls-standard_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/path-controls/images/path-controls-standard_2x.png)

**Standard.** A linear list that includes the root disk, parent folders, and selected item. Each item appears with an icon and a name. If the list is too long to fit within the control, it hides names between the first and last items. If you make the control editable, people can drag an item onto the control to select the item and display its path in the control.
> 표준. 루트 디스크, 상위 폴더 및 선택한 항목을 포함하는 선형 목록입니다. 각 항목에는 아이콘과 이름이 표시됩니다. 목록이 너무 길어서 컨트롤에 맞지 않으면 첫 번째 항목과 마지막 항목 사이의 이름을 숨깁니다. 컨트롤을 편집 가능으로 설정하면 사용자가 항목을 컨트롤로 끌어 항목을 선택하고 컨트롤에 해당 경로를 표시할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/path-controls/images/path-controls-popup_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/path-controls/images/path-controls-popup_2x.png)

**Pop up.** A control similar to a [pop-up button](../components/menus-and-actions/pop-up-buttons) that shows the icon and name of the selected item. People can click the item to open a menu containing the root disk, parent folders, and selected item. If you make the control editable, the menu contains an additional Choose command that people can use to select an item and display it in the control. They can also drag an item onto the control to select it and display its path.
> 팝업. 선택한 항목의 아이콘과 이름을 표시하는 팝업 단추와 유사한 컨트롤입니다. 항목을 눌러 루트 디스크, 상위 폴더 및 선택한 항목이 포함된 메뉴를 열 수 있습니다. 컨트롤을 편집 가능으로 설정한 경우 메뉴에는 사용자가 항목을 선택하고 컨트롤에 표시하는 데 사용할 수 있는 추가 선택 명령이 포함되어 있습니다. 또한 항목을 컨트롤로 끌어 선택하고 경로를 표시할 수 있습니다.
>




# **Best practices**

**Use a path control in the window body, not the window frame.** Path controls aren’t intended for use in toolbars or status bars. Note that the path control in the Finder appears at the bottom of the window body, not in the status bar.
> 창 프레임이 아닌 창 본문에서 경로 컨트롤을 사용하십시오. 경로 컨트롤은 도구 모음이나 상태 표시줄에서 사용할 수 없습니다. Finder의 경로 제어는 상태 표시줄이 아닌 창 본문의 하단에 나타납니다.
>




# **Platform considerations**

*Not supported in iOS, iPadOS, tvOS, or watchOS.*
> iOS, iPadOS, tvOS 또는 watch에서 지원되지 않음운영 체제
>



