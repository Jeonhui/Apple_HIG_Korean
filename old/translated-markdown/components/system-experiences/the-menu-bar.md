# **[components-status] the-menu-bar**

## On a Mac, the menu bar at the top of the screen displays the top-level menus in your app or game, which typically include both system-provided menus and custom ones.
> Mac에서는 화면 상단의 메뉴 표시줄에 앱 또는 게임의 최상위 메뉴가 표시되며, 일반적으로 시스템에서 제공하는 메뉴와 사용자 지정 메뉴가 모두 포함됩니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/the-menu-bar-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/the-menu-bar-intro-dark_2x.png)

Mac users are very familiar with the macOS menu bar, and they rely on it to help them learn what an app does and find the commands they need. To help your app or game feel at home in macOS, it’s essential to provide a consistent menu bar experience.
> Mac 사용자들은 MacOS 메뉴 모음에 매우 익숙하며, 앱이 무엇을 하는지 배우고 필요한 명령을 찾는 데 도움을 주기 위해 Mac OS 메뉴 모음에 의존합니다. MacOS에서 앱이나 게임이 집에 있는 것처럼 느끼도록 하려면 일관된 메뉴 모음 경험을 제공하는 것이 필수적이다.
>




**NOTE**In iPadOS, an app’s keyboard shortcuts can appear in the shortcut interface that displays when people hold the Command key on an attached hardware keyboard. The shortcut interface is similar in appearance and organization to the menu bar in macOS — and it can contain familiar menu items like New Window and Copy — but unlike the menu bar, it doesn’t contain every command an app supports. For guidance, see [Keyboard shortcuts](https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards/#keyboard-shortcuts).
> 참고 iPadOS에서 앱의 바로 가기 키는 연결된 하드웨어 키보드에서 명령 키를 누를 때 표시되는 바로 가기 인터페이스에 나타날 수 있습니다. 바로 가기 인터페이스는 MacOS의 메뉴 모음과 모양과 구성이 비슷하며 새 창 및 복사와 같은 친숙한 메뉴 항목을 포함할 수 있지만 메뉴 모음과 달리 앱이 지원하는 모든 명령을 포함하지는 않습니다. 자세한 내용은 바로 가기 키를 참조하십시오.
>




Menus in the menu bar share most of the appearance and behavior characteristics that all menu types have. To learn about menus in general — and how organize and label menu items — see [Menus](../components/menus-and-actions/menus).
> 메뉴 모음의 메뉴는 모든 메뉴 유형이 가지는 모양 및 동작 특성의 대부분을 공유합니다. 메뉴에 대한 일반적인 내용과 메뉴 항목 구성 및 레이블 지정 방법에 대한 자세한 내용은 메뉴를 참조하십시오.
>




# **Anatomy**

The Apple menu, which is always the first item on the leading side of the menu bar, includes system-defined menu items that are always available. You can’t modify or remove the Apple menu.
> 항상 메뉴 모음의 맨 앞에 있는 첫 번째 항목인 Apple 메뉴에는 항상 사용할 수 있는 시스템 정의 메뉴 항목이 포함되어 있습니다. Apple 메뉴는 수정하거나 제거할 수 없습니다.
>




When present in the menu bar, the following menus appear after the Apple menu in the order listed below.
> 메뉴 표시줄에 표시되면 아래 나열된 순서대로 Apple 메뉴 뒤에 다음 메뉴가 나타납니다.
>




- *AppName* (you supply a short version of your app’s name for this menu’s title)
- >  AppName(이 메뉴의 제목에 대한 앱 이름의 짧은 버전을 제공합니다.)

- File
- Edit
- Format
- View
- App-specific menus, if any
- Window
- Help

Space permitting, the system can display menu bar extras in the trailing end of the menu bar. A *menu bar extra* provides a menu of app- or system-defined items that people can access in most contexts. With the exception of essential menu bar extras, like Clock, people choose the menu bar extras they want to keep in the menu bar. For example, people might want to include the system-provided Bluetooth menu bar extra to help them manage Bluetooth connections at any time. For guidance, see [Menu bar extras](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/the-menu-bar#menu-bar-extras).
> 공간이 허용되면 시스템은 메뉴 모음의 뒤쪽 끝에 추가 메뉴 모음을 표시할 수 있습니다. 메뉴 모음 추가 기능은 대부분의 컨텍스트에서 사용자가 액세스할 수 있는 앱 또는 시스템 정의 항목의 메뉴를 제공합니다. 시계와 같은 필수 메뉴 모음 추가 기능을 제외하고, 사람들은 메뉴 모음에서 보관할 메뉴 모음 추가 기능을 선택합니다. 예를 들어 언제든지 Bluetooth 연결을 관리할 수 있도록 시스템에서 제공하는 Bluetooth 메뉴 모음을 추가로 포함할 수 있습니다. 자세한 내용은 추가 메뉴 모음을 참조하십시오.
>




When menu bar space is constrained, the system prioritizes the display of menus and essential menu bar extras. To ensure that menus remain readable, the system may decrease the space between the titles, truncating them if necessary.
> 메뉴 모음 공간이 제한되면 시스템은 메뉴 및 필수 메뉴 모음 추가 정보의 표시를 우선시합니다. 메뉴를 읽기 쉽게 유지하기 위해 시스템은 제목 사이의 공간을 줄이고 필요한 경우 제목을 잘라낼 수 있습니다.
>




When people enter full-screen mode, the menu bar typically hides until they reveal it by moving the pointer to the top of the screen. For guidance, see [Going full screen](../patterns/going-full-screen).
> 사람들이 전체 화면 모드로 들어갈 때, 일반적으로 메뉴 모음은 포인터를 화면 상단으로 이동하여 표시될 때까지 숨깁니다. 자세한 내용은 전체 화면으로 이동을 참조하십시오.
>




# **Best practices**

**Enable the system-defined menus and menu items that are relevant in your app.** People generally expect to find familiar menus and menu items in the apps and games they use. In many cases, the system implements the functionality of standard menu items so you don’t have to. For example, when people select text in a standard text field, the system enables the Edit > Copy menu item.
> 앱과 관련된 시스템 정의 메뉴 및 메뉴 항목을 활성화합니다. 사람들은 일반적으로 자신이 사용하는 앱과 게임에서 친숙한 메뉴 및 메뉴 항목을 찾기를 기대합니다. 대부분의 경우 시스템은 표준 메뉴 항목의 기능을 구현하므로 사용자가 그럴 필요가 없습니다. 예를 들어, 사람들이 표준 텍스트 필드에서 텍스트를 선택할 때 시스템은 편집 > 복사 메뉴 항목을 활성화합니다.
>




**Prefer using the default ordering of menu bar menus and the default ordering of menu items within each menu.** It’s easier for people to find what they're looking for when your menus and menu items use the ordering they expect.
> 각 메뉴에서 메뉴 모음 메뉴의 기본 순서와 메뉴 항목의 기본 순서를 사용하는 것을 선호합니다. 메뉴 및 메뉴 항목이 원하는 순서를 사용할 때 사람들이 원하는 항목을 더 쉽게 찾을 수 있습니다.
>




**Enable the keyboard shortcuts defined for the standard menu items you include.** People expect to use the keyboard shortcuts they already know for standard menu items, like Copy, Cut, Paste, Save, and Print. Define custom keyboard shortcuts only when necessary.
> 포함한 표준 메뉴 항목에 대해 정의된 바로 가기 키를 사용합니다. 사람들은 복사, 잘라내기, 붙여넣기, 저장 및 인쇄와 같은 표준 메뉴 항목에 대해 이미 알고 있는 바로 가기 키를 사용할 것으로 예상합니다. 필요한 경우에만 사용자 지정 키보드 단축키를 정의합니다.
>




**Prefer short, one-word menu titles.** Various factors — like different display sizes and the presence of menu bar extras — can affect the spacing and appearance of your menus. One-word menu titles work especially well in the menu bar because they take little space and are easy for people to scan. Consider the following guidance as you write a menu title.
> 다양한 디스플레이 크기 및 메뉴 모음 추가 기능과 같은 다양한 요소가 메뉴의 간격과 모양에 영향을 줄 수 있습니다. 한 단어 메뉴 제목은 공간을 거의 차지하지 않고 사람들이 스캔하기 쉽기 때문에 메뉴 모음에서 특히 잘 작동합니다. 메뉴 제목을 작성할 때 다음 지침을 고려하십시오.
>




- Aim for a title that helps people predict the items within the menu. For example, a menu labeled “Font” implies that it lists items for adjusting text attributes, not for performing edit actions like copy and paste.
- >  메뉴 내의 항목을 예측하는 데 도움이 되는 제목을 목표로 합니다. 예를 들어, "글꼴" 메뉴는 복사 및 붙여넣기와 같은 편집 작업을 수행하기 위한 것이 아니라 텍스트 특성을 조정하기 위한 항목을 나열한다는 것을 의미합니다.

- Avoid mixing text with symbols or interface icons in a menu title. Only a menu bar extra uses a symbol or icon as a title.
- >  메뉴 제목에 텍스트를 기호 또는 인터페이스 아이콘과 함께 사용하지 마십시오. 추가 메뉴 모음만 기호 또는 아이콘을 제목으로 사용합니다.

- Use title-style capitalization if you need to use more than one word in the menu title.
- >  메뉴 제목에 둘 이상의 단어를 사용해야 하는 경우 제목 스타일 대문자를 사용합니다.


# **App menu**

The app menu lists items that apply to your app or game as a whole, rather than to a specific task, document, or window. To help people quickly identify the active app, the menu bar displays your app name in bold.
> 앱 메뉴에는 특정 작업, 문서 또는 창이 아닌 앱 또는 게임 전체에 적용되는 항목이 나열됩니다. 사용자가 활성 앱을 빠르게 식별할 수 있도록 메뉴 표시줄에 앱 이름이 굵게 표시됩니다.
>




The app menu typically contains the following menu items — along with their standard keyboard shortcuts — listed in the following order.
> 앱 메뉴에는 일반적으로 다음과 같은 메뉴 항목과 표준 바로 가기 키가 다음 순서로 나열되어 있습니다.
>




| Menu item | Keyboard shortcut | Action | Guidance |
| --- | --- | --- | --- |
| About YourAppName |  | Displays the About window for your app, which includes copyright and version information | Prefer a short name of 16 characters or fewer. Don't include a version number. |
| Settings… | Command-Comma (,) | Opens your Settings window. | Use only for app-level settings. If you also offer document-specific settings, put them in the File menu. |
| Optional app-specific items |  | Performs custom app-level setting or configuration actions | List custom app-configuration items after the Settings item and within the same group. |
| Services |  | Displays a submenu of services from the system and other apps that apply to the current context |  |
| Hide YourAppName | Command-H | Hides your app and all of its windows, and then activates the most recently used app | Use the same short app name you supply for the About item. |
| Hide Others | Option-Command-H | Hides all other open apps and their windows |  |
| Show All |  | Shows all other open apps and their windows behind your app’s windows |  |
| Quit YourAppName | Command-Q | Quits your app. Pressing Option changes Quit YourAppName to Quit and Keep Windows. | Use the same short app name you supply for the About item. |

**Display the About menu item first.** Include a separator after the About menu item so that it appears by itself in a group.
> 정보 메뉴 항목을 먼저 표시합니다. 정보 메뉴 항목 뒤에 구분 기호를 포함하여 그룹에 표시됩니다.
>




# **File menu**

The File menu contains commands that help people manage the files or documents an app supports. If your app doesn’t handle any types of files, you can rename or eliminate this menu. For example, System Settings doesn’t include a File menu.
> 파일 메뉴에는 앱이 지원하는 파일 또는 문서를 사용자가 관리하는 데 도움이 되는 명령이 포함되어 있습니다. 앱에서 파일 형식을 처리하지 않는 경우 이 메뉴의 이름을 바꾸거나 제거할 수 있습니다. 예를 들어 시스템 설정에는 파일 메뉴가 없습니다.
>




The File menu typically contains the following menu items — along with their standard keyboard shortcuts — listed in the following order.
> 파일 메뉴에는 일반적으로 다음과 같은 메뉴 항목과 표준 바로 가기 키가 다음 순서로 나열되어 있습니다.
>




| Menu item | Keyboard shortcut | Action | Guidance |
| --- | --- | --- | --- |
| New Item | Command-N | Creates a new document, file, or window | For Item, use a term that names the type of item your app creates. For example, Calendar uses "Event" and "Calendar." |
| Open | Command-O | Can open the selected item or present an interface in which people select an item to open | If people need to select an item in a separate interface, an ellipsis follows the command to indicate that more input is required. |
| Open Recent |  | Displays a submenu that lists recently opened documents and files that people can select, and typically includes a Clear Menuitem | List document and filenames that people recognize in the submenu; don't display file paths. List the documents in the order people last opened them, with the most recently opened document first. |
| Close | Command-W | Closes the current window or document. Pressing Option changes Close to Close All. For a tab-based window, Close Tab replaces Close. | In a tab-based window, consider adding a Close Window item to let people close the entire window with one click or tap. |
| Close Tab | Command-W | Closes the current tab in a tab-based window. Pressing Option changes Close Tab to Close Other Tabs. |  |
| Close File | Shift-Command-W | Closes the current file and all its associated windows | Consider enabling this menu item if your app can open multiple views of the same file. |
| Save | Command-S | Saves the current document or file | Automatically save changes periodically as people work so they don’t need to keep choosing File > Save. For a new document, prompt people for a name and location. If you need to let people save a file in multiple formats, prefer a pop-up menu that lets people choose a format in the Save sheet. |
| Save All |  | Saves all open documents |  |
| Duplicate | Shift-Command-S | Duplicates the current document, leaving both documents open. Pressing Option changes Duplicate to Save As. | Prefer Duplicate to menu items like Save As, Export, Copy To, and Save To because these items don't clarify the relationship between the original file and the new one. |
| Rename… |  | Lets people change the name of the current document |  |
| Move To… |  | Prompts people to choose a new location for the document |  |
| Export As... |  | Prompts people for a name, output location, and export file format. After exporting the file, the current document remains open; the exported file doesn’t open. | Reserve the Export As item for when you need to let people export content in a format your app doesn’t typically handle. |
| Revert to |  | When people enable autosaving, displays a submenu that lists recent document versions and an option to display the version browser. After people choose a version to restore, it replaces the current document. |  |
| Page Setup... | Shift-Command-P | Opens a panel for specifying printing parameters like paper size and printing orientation. A document can save the printing parameters that people specify. | Include the Page Setup item if you need to support printing parameters that apply to a specific document. Parameters that are global in nature, like a printer's name, or that people change frequently, like the number of copies to print, belong in the Print panel. |
| Print... | Command-P | Opens the standard Print panel, which lets people print to a printer, send a fax, or save as a PDF |  |

# **Edit menu**

The Edit menu lets people make changes to content in the current document or text container, and provides commands for interacting with the Clipboard. Because many editing commands apply to any editable content, the Edit menu is useful even in apps that aren’t document-based.
> 편집 메뉴를 사용하여 사용자는 현재 문서 또는 텍스트 컨테이너의 내용을 변경하고 클립보드와 상호 작용하는 명령을 제공할 수 있습니다. 편집 가능한 콘텐츠에는 많은 편집 명령이 적용되므로 편집 메뉴는 문서 기반이 아닌 앱에서도 유용합니다.
>




**Determine whether Find menu items belong in the Edit menu.** For example, if your app lets people search for files or other types of objects, Find menu items might be more appropriate in the File menu.
> 메뉴 항목 찾기가 편집 메뉴에 속하는지 여부를 확인합니다. 예를 들어 앱에서 사용자가 파일 또는 다른 유형의 개체를 검색할 수 있는 경우 파일 메뉴에서 메뉴 항목 찾기가 더 적합할 수 있습니다.
>




The Edit menu typically contains the following top-level menu items, listed in the following order.
> 편집 메뉴에는 일반적으로 다음과 같은 최상위 메뉴 항목이 다음 순서로 나열되어 있습니다.
>




| Menu item             | Keyboard shortcut | Action                                                                                                                                                                          | Guidance                                                                                                                                                                                                                                             |
|-----------------------|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Undo                  | Command-Z         | Reverses the effect of the previous user operation                                                                                                                              | Clarify the target of the undo. For example, if people just selected a menu item, you can append the item's title, such as Undo Paste and Match Style. For a text entry operation, you might append the word *Typing* to give Undo Typing.           |
| Redo                  | Shift–Command-Z   | Reverses the effect of the previous Undo operation                                                                                                                              | Clarify the target of the redo. For example, if people just reversed a menu item selection, you can append the item's title, such as Redo Paste and Match Style. For a text entry operation, you might append the word _Typing_ to give Redo Typing. |
| Cut                   | Command-X         | Removes the selected data and stores it on the Clipboard, replacing the previous contents of the Clipboard                                                                      |                                                                                                                                                                                                                                                      |
| Copy                  | Command-C         | Duplicates the selected data and stores it on the Clipboard                                                                                                                     |                                                                                                                                                                                                                                                      |
| Paste                 | Command-P         | Inserts the contents of the Clipboard at the current insertion point. The Clipboard contents remain unchanged, permitting people to choose Paste multiple times.                |                                                                                                                                                                                                                                                      |
| Paste and Match Style | Command-P         | Inserts the contents of the Clipboard at the current insertion point, matching the style of the inserted text to the surrounding text                                           |                                                                                                                                                                                                                                                      |
| Delete                | Delete            | Removes the selected data, but doesn’t place it on the Clipboard                                                                                                                | Provide a Delete menu item instead of an Erase or Clear menu item. Choosing Delete is the equivalent of pressing the Delete key, so it’s important for the naming to be consistent.                                                                  |
| Select All            | Command-A         | Highlights all selectable content in the current document or text container                                                                                                     |                                                                                                                                                                                                                                                      |
| Find                  | Command-F         | Displays a submenu containing menu items for performing search operations in the current document or text container. Standard submenus (and their keyboard shortcuts) include:  |                                                                                                                                                                                                                                                      |

• Find
• Find and Replace… (Option-Command-F)
• Find Next (Command-G)
• Find Previous (Shift-Command-G)
• Use Selection for Find (Command-E)
> • 찾기에 선택 사용(명령-E)
>



• Jump to Selection (Command-J) |  |
> • 선택 영역으로 이동(Command-J) | |
>



| Spelling and Grammar |  | Displays a submenu containing menu items for checking for and correcting spelling and grammar in the current document or text container. Standard submenus (and their keyboard shortcuts) include:
• Show Spelling and Grammar (Command-Colon (:))
> • 맞춤법 및 문법 표시(명령-콜론(:))
>



• Check Document Now (Command-Semicolon (;))
> • 지금 문서 확인(명령-세미콜론(;)
>



• Check Spelling While Typing
• Check Grammar With Spelling
• Correct Spelling Automatically |  |
> • 자동으로 맞춤법 수정 | | |
>



| Substitutions |  | Displays a submenu containing items that let people toggle automatic substitutions while they type in a document or text container. Standard submenus include:
• Show Substitutions
• Smart Copy/Paste
• Smart Quotes
• Smart Dashes
• Smart Links
• Data Detectors
• Text Replacement |  |
> • 텍스트 바꾸기 | |
>



| Transformations |  | Displays a submenu containing items that transform selected text. Standard submenus include:
• Make Uppercase
• Make Lowercase
• Capitalize |  |
| Speech |  | Displays a submenu containing Start Speaking and Stop Speaking items, which control when the system audibly reads selected text. |  |
| Start Dictation… | Function Function | Opens the dictation window and converts spoken words into text that’s added at the current insertion point. The system automatically adds the Start Dictation menu item at the bottom of the Edit menu. |  |
| Emoji & Symbols | Control-Command-Space | Displays a Character Viewer, which includes emoji, symbols, and other characters people can insert at the current insertion point. The system automatically adds the Emoji & Symbols menu item at the bottom of the Edit menu. |  |

# **Format menu**

The Format menu lets people adjust text formatting attributes in the current document or text container. You can exclude this menu if your app doesn’t support formatted text editing.
> 형식 메뉴를 사용하여 현재 문서 또는 텍스트 컨테이너의 텍스트 형식 속성을 조정할 수 있습니다. 앱에서 서식 있는 텍스트 편집을 지원하지 않는 경우 이 메뉴를 제외할 수 있습니다.
>




The Format menu typically contains the following top-level menu items, listed in the following order.
> 형식 메뉴에는 일반적으로 다음과 같은 최상위 메뉴 항목이 다음 순서로 나열되어 있습니다.
>




| Menu item | Keyboard shortcut | Action                                                                                                                                             | Guidance |
|-----------|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| Font      |                   | Displays a submenu containing items for adjusting font attributes of the selected text. Standard submenus (and their keyboard shortcuts) include:  |          |

• Show Fonts (Command-T)
• Bold (Command-B)
• Italic (Command-I)
• Underline (Command-U)
• Bigger (Command-Plus sign (+))
• Smaller (Command-Hyphen (-))
• Show Colors (Shift–Command-C)
• Copy Style (Option–Command-C)
• Paste Style (Option–Command-V) |  |
> • 스타일 붙여넣기(옵션-명령-V) | |
>



| Text |  | Displays a submenu containing items for adjusting text attributes of the selected text. Standard submenus (and their keyboard shortcuts) include:
• Align Left (Command-Left Brace ({))
> • 왼쪽 정렬(명령-왼쪽 가새({))
>



• Align Center (Command-Pipe (|))
• Justify
• Align Right (Command-Right Brace (}))
> • 오른쪽 맞춤(명령-오른쪽 가새(})
>



• Writing Direction
• Show Ruler
• Copy Ruler (Control–Command-C)
• Paste Ruler (Control–Command-V) |  |
> • 눈금자 붙여넣기(Control-Command-V) | |
>




# **View menu**

The View menu lets people customize the appearance of all an app’s windows, regardless of type.
> 보기 메뉴를 사용하면 유형에 관계없이 모든 앱 창의 모양을 사용자 지정할 수 있습니다.
>




**IMPORTANT**The View menu doesn’t include items for navigating between or managing specific windows; the [Window menu](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/the-menu-bar#window-menu) provides these commands.
> 중요 보기 메뉴에는 특정 창을 탐색하거나 관리하기 위한 항목이 포함되어 있지 않습니다. 창 메뉴에는 이러한 명령이 제공됩니다.
>




**Provide a View menu even if your app supports only a subset of the standard view functions.** For example, if your app doesn’t include a tab bar, toolbar, or sidebar, but does support full-screen mode, provide a View menu that includes only the Enter/Exit Full Screen menu item.
> 예를 들어 앱에 탭 모음, 도구 모음 또는 사이드바가 없지만 전체 화면 모드를 지원하는 경우 전체 화면 메뉴 항목만 포함된 보기 메뉴를 제공합니다.
>




**Ensure that each show/hide item title reflects the current state of the corresponding view.** For example, when the toolbar is hidden, provide a Show Toolbar menu item; when the toolbar is visible, provide a Hide Toolbar menu item.
> 각 항목 제목 표시/숨기기는 해당 보기의 현재 상태를 반영해야 합니다. 예를 들어, 도구 모음이 숨겨져 있으면 도구 모음 메뉴 항목 표시를 제공하고, 도구 모음이 표시되면 도구 모음 메뉴 항목 숨기기를 제공합니다.
>




The View menu typically contains the following top-level menu items, listed in the following order.
> 보기 메뉴에는 일반적으로 다음과 같은 최상위 메뉴 항목이 다음 순서로 나열되어 있습니다.
>




| Menu item | Keyboard shortcut | Action | Guidance |
| --- | --- | --- | --- |
| Show/Hide Tab Bar |  | Toggles the visibility of the tab bar above the body area in a tab-based window |  |
| Show All Tabs/Exit Tab Overview |  | Enters and exits a view (similar to Mission Control) that provides an overview of all open tabs in a tab-based window |  |
| Show/Hide Toolbar | Option-Command-T | In a window that includes a toolbar, toggles the toolbar’s visibility. |  |
| Customize Toolbar… |  | In a window that includes a toolbar, opens a view that lets people customize toolbar items |  |
| Show/Hide Sidebar | Control-Command-S | In a window that includes a sidebar, toggles the sidebar’s visibility. |  |
| Enter/Exit Full Screen | Function-F | In an app that supports a full-screen experience, opens the window at full-screen size in a new space |  |

# **App-specific menus**

Your app’s custom menus appear in the menu bar between the View menu and the Window menu. For example, Safari’s menu bar includes app-specific History and Bookmarks menus.
> 보기 메뉴와 창 메뉴 사이의 메뉴 모음에 앱의 사용자 지정 메뉴가 나타납니다. 예를 들어, Safari의 메뉴 모음에는 앱별 기록 및 책갈피 메뉴가 포함되어 있습니다.
>




**Provide app-specific menus for custom commands.** People look in the menu bar when searching for app-specific commands, especially when using an app for the first time. Even when commands are available elsewhere in your app, it’s important to list them in the menu bar. Putting commands in the menu bar makes them easier for people to find, lets you assign keyboard shortcuts to them, and makes them more accessible to people using Full Keyboard Access. Excluding commands from the menu bar — even infrequently used or advanced commands — risks making them difficult for everyone to find.
> 사용자 지정 명령에 대한 앱별 메뉴를 제공합니다. 사람들은 특히 앱을 처음 사용할 때 앱별 명령을 검색할 때 메뉴 모음을 찾습니다. 앱의 다른 곳에서 명령을 사용할 수 있는 경우에도 메뉴 모음에 명령을 나열하는 것이 중요합니다. 메뉴 모음에 명령을 입력하면 사용자가 명령을 쉽게 찾을 수 있고 사용자가 바로 가기 키를 할당할 수 있으며 전체 키보드 액세스를 사용하는 사용자가 명령을 쉽게 찾을 수 있습니다. 자주 사용하지 않거나 고급 명령을 메뉴 모음에서 제외하면 모든 사용자가 해당 명령을 찾기 어려울 수 있습니다.
>




**As much as possible, reflect your app’s hierarchy in app-specific menus.** For example, Mail lists the Mailbox, Message, and Format menus in an order that mirrors the relationships of these items: mailboxes contain messages, and messages contain formatting.
> 가능한 한 앱의 계층을 앱별 메뉴에 반영하십시오. 예를 들어, 메일에는 우편함, 메시지 및 형식 메뉴가 이러한 항목의 관계를 반영하는 순서로 나열됩니다. 사서함에는 메시지가 포함되고 메시지에는 형식이 포함됩니다.
>




**In general, list universally applicable menus first and more focused menus last.** Place universal menus closer to the Apple menu; place focused menus closer to the Help menu.
> 일반적으로 보편적으로 적용 가능한 메뉴를 먼저 나열하고 초점을 맞춘 메뉴를 마지막으로 정렬합니다. 범용 메뉴를 Apple 메뉴에 더 가깝게 배치하고 초점을 맞춘 메뉴를 도움말 메뉴에 더 가까이 배치합니다.
>




# **Window menu**

The Window menu lets people navigate, organize, and manage an app’s windows.
> 창 메뉴를 사용하면 사용자가 앱의 창을 탐색, 구성 및 관리할 수 있습니다.
>




**IMPORTANT**The Window menu doesn’t help people customize the appearance of windows or close them. To customize a window, people use commands in the [View menu](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/the-menu-bar#view-menu); to close a window, people choose Close in the [File menu](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/the-menu-bar#file-menu).
> 중요 창 메뉴는 창 모양을 사용자 지정하거나 창을 닫는 데 도움이 되지 않습니다. 창을 사용자 지정하려면 보기 메뉴에서 명령을 사용하고, 창을 닫으려면 파일 메뉴에서 닫기를 선택합니다.
>




**Provide a Window menu even if your app has only one window.** Include the Minimize and Zoom menu items so people using Full Keyboard Access can use the keyboard to invoke these functions.
> 앱에 창이 하나뿐인 경우에도 창 메뉴를 제공하십시오. 전체 키보드 액세스를 사용하는 사용자가 키보드를 사용하여 이러한 기능을 호출할 수 있도록 최소화 및 확대/축소 메뉴 항목을 포함하십시오.
>




**Consider including menu items for showing and hiding panels.** A [panel](../macos/windows-and-views/panels/)provides information, configuration options, or tools for interacting with content in a primary window, and typically appears only when people need it. There’s no need to provide access to the font panel or text color panel because the Format menu lists these panels.
> 패널은 기본 창에서 콘텐츠와 상호 작용하기 위한 정보, 구성 옵션 또는 도구를 제공하며 일반적으로 필요할 때만 나타납니다. 서식 메뉴에 이러한 패널이 나열되므로 글꼴 패널 또는 텍스트 색상 패널에 대한 액세스 권한을 제공할 필요가 없습니다.
>




The Window menu typically contains the following top-level menu items, listed in the following order.
> 창 메뉴에는 일반적으로 다음과 같은 최상위 메뉴 항목이 포함됩니다.
>




| Menu item                             | Keyboard shortcut | Action                                                                                                                                                                                                                                                                                                          | Guidance                                                                                                                                                     |
|---------------------------------------|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimize                              | Command-M         | Minimizes the active window to the Dock. Pressing the Option key changes this item to Minimize All.                                                                                                                                                                                                             |                                                                                                                                                              |
| Zoom                                  |                   | Toggles between a predefined size appropriate to the window’s content and the window size people set. Pressing the Option key changes this item to Zoom All.                                                                                                                                                    | Avoid using Zoom to enter or exit full-screen mode. The View menuenables these functions.                                                                    |
| Show Previous Tab                     | Control-Shift-Tab | Shows the tab before the current tab in a tab-based window                                                                                                                                                                                                                                                      |                                                                                                                                                              |
| Show Next Tab                         | Control-Tab       | Shows the tab after the current tab in a tab-based window                                                                                                                                                                                                                                                       |                                                                                                                                                              |
| Move Tab to New Window                |                   | Opens the current tab in a new window                                                                                                                                                                                                                                                                           |                                                                                                                                                              |
| Merge All Windows                     |                   | Combines all open windows into a single tabbed window                                                                                                                                                                                                                                                           |                                                                                                                                                              |
| Enter/Exit Full Screen                | Control-Command-F | In an app that supports a full-screen experience, opens the window at full-screen size in a new space                                                                                                                                                                                                           | Include this item in the Window menu only if your app doesn't have a View menu. In this scenario, continue to provide separate Minimize and Zoom menu items. |
| Bring All to Front                    |                   | Brings all an app's open windows to the front, maintaining their onscreen location, size, and layering order. (Clicking the app icon in the Dock has the same effect.) Pressing the Option key changes this item to Arrange in Front, which brings an app's windows to the front in a neatly tiled arrangement. |                                                                                                                                                              |
| *Name of an open app-specific window* |                   | Brings the selected window to the front.                                                                                                                                                                                                                                                                        | List the currently open windows in alphabetical order for easy scanning. Avoid listing panels or other modal views.                                          |

# **Help menu**

The Help menu — located at the trailing end of the menu bar — provides access to an app’s help documentation. When you use the Help Book format for this documentation, macOS automatically includes a search field at the top of the Help menu.
> 메뉴 모음의 끝에 있는 도움말 메뉴는 앱의 도움말 설명서에 액세스할 수 있는 기능을 제공합니다. 이 설명서에 도움말 북 형식을 사용하면 MacOS에서 자동으로 도움말 메뉴 맨 위에 검색 필드를 포함합니다.
>




| Menu item | Keyboard shortcut | Action | Guidance |
| --- | --- | --- | --- |
| Send YourAppNameFeedback to Apple |  | Opens the Feedback Assistant, in which people can provide feedback. |  |
| YourAppNameHelp |  | When the content uses the Help Book format, opens the content in the built-in Help Viewer. |  |
| Additional Item |  |  | Use a separator between your primary help documentation and additional items, which might include registration information or release notes. Keep the total the number of items you list in the Help menu small to avoid overwhelming people with too many choices when they need help. Alternatively, consider linking to additional items from within your help documentation. |

For guidance, see [Offering help](../patterns/offering-help); for developer guidance, see [NSHelpManager](https://developer.apple.com/documentation/appkit/nshelpmanager).
> 자세한 내용은 도움말 제공을 참조하고, 개발자 지침은 NSHelpManager를 참조하십시오.
>




# **Dynamic menu items**

In rare cases, it can make sense to present a *dynamic menu item*, which is a menu item that changes its behavior when people choose it while pressing a modifier key (Control, Option, Shift, or Command). For example, the *Minimize*item in the Window menu changes to *Minimize All* when people press the Option key.
> 드물게 동적 메뉴 항목을 제시하는 것이 타당할 수 있는데, 이는 사람들이 수식자 키(Control, Option, Shift 또는 Command)를 누르면서 선택하면 동작이 바뀌는 메뉴 항목이다. 예를 들어 옵션 키를 누르면 창 메뉴의 최소화 항목이 모두 최소화로 변경됩니다.
>




**Avoid making a dynamic menu item the only way to accomplish a task.**Dynamic menu items are hidden by default, so they’re best suited to offer shortcuts to advanced actions that people can accomplish in other ways. For example, if someone hasn’t discovered the *Minimize All* dynamic menu item in the Window menu, they can still minimize each open window.
> 동적 메뉴 항목을 작업을 수행하는 유일한 방법으로 만들지 마십시오.동적 메뉴 항목은 기본적으로 숨겨져 있으므로 다른 방법으로 수행할 수 있는 고급 작업에 대한 바로 가기를 제공하는 데 가장 적합합니다. 예를 들어 다른 사용자가 창 메뉴에서 모든 동적 메뉴 최소화 항목을 검색하지 않은 경우에도 열린 각 창을 최소화할 수 있습니다.
>




**Use dynamic menu items primarily in menu bar menus.** Adding a dynamic menu item to contextual or Dock menus can make the item even harder for people to discover.
> 동적 메뉴 항목은 주로 메뉴 모음 메뉴에서 사용합니다. 동적 메뉴 항목을 상황에 맞는 메뉴 또는 도킹 메뉴에 추가하면 항목을 찾기가 훨씬 어려워질 수 있습니다.
>




**Require only a single modifier key to reveal a dynamic menu item.** It can be physically awkward to press more than one key while simultaneously opening a menu and choosing a menu item, in addition to reducing the discoverability of the dynamic behavior. For developer guidance, see the [isAlternate](https://developer.apple.com/documentation/appkit/nsmenuitem/1514823-isalternate) property of [NSMenuItem](https://developer.apple.com/documentation/appkit/nsmenuitem).
> 동적 메뉴 항목을 표시하려면 단일 수식 키만 필요하며, 동적 동작의 검색 가능성을 줄일 뿐만 아니라 메뉴를 열고 메뉴 항목을 선택하는 동시에 둘 이상의 키를 누르는 것은 물리적으로 어색할 수 있다. 개발자 지침은 NSMenuItem의 isAlternate 속성을 참조하십시오.
>




**TIP**macOS automatically sets the width of a menu to hold the widest item, including dynamic menu items.
> TIPmacOS는 동적 메뉴 항목을 포함하여 가장 넓은 항목을 담을 수 있도록 메뉴의 너비를 자동으로 설정합니다.
>




# **Menu bar extras**

A menu bar extra exposes app-specific functionality using an icon that appears in the menu bar when your app is running, even when it’s not the frontmost app. Menu bar extras are on the opposite side of the menu bar from your app's menus.
> 메뉴 모음은 앱이 가장 앞에 있는 앱이 아닌 경우에도 앱이 실행 중일 때 메뉴 모음에 나타나는 아이콘을 사용하여 앱별 기능을 추가로 표시합니다. 메뉴 모음 추가 기능은 앱 메뉴에서 메뉴 모음 반대쪽에 있습니다.
>




When necessary, the system hides menu bar extras to make room for app menus. Similarly, if there are too many menu bar extras, the system may hide some to avoid crowding app menus.
> 필요한 경우, 시스템은 앱 메뉴를 위한 공간을 확보하기 위해 메뉴 모음 추가 사항을 숨깁니다. 마찬가지로, 메뉴 모음 추가 항목이 너무 많으면 시스템이 앱 메뉴가 붐비지 않도록 일부 항목을 숨길 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/the-menu-bar/images/menu-bar-extras_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/the-menu-bar/images/menu-bar-extras_2x.png)

**Consider using a symbol to represent your menu bar extra.** You can create an [interface icon](../foundations/icons) or you can choose a [symbol](../foundations/sf-symbols) from the SF Symbols app, using it as-is or customizing it to suit your needs. Both interface icons and symbols use black and clear colors to define their shapes; the system can apply other colors to the black areas in each image so it looks good on both dark and light menu bars, and when your menu bar extra is selected.
> 기호를 사용하여 메뉴 모음을 추가로 나타낼 수 있습니다. 인터페이스 아이콘을 만들거나 SF 기호 앱에서 기호를 선택하여 그대로 사용하거나 필요에 따라 사용자 정의할 수 있습니다. 인터페이스 아이콘과 기호 모두 검은색과 선명한 색상을 사용하여 모양을 정의합니다. 시스템은 각 이미지의 검은색 영역에 다른 색상을 적용할 수 있기 때문에 어두운 메뉴 모음과 밝은 메뉴 모음 모두에서 보기 좋으며 추가 메뉴 모음을 선택할 때도 좋습니다.
>




**Display a menu — not a popover — when people click your menu bar extra.** Unless the app functionality you want to expose is too complex for a menu, avoid presenting it in a [popover](../components/presentation/popovers).
> 다른 사람이 메뉴 모음을 추가로 클릭할 때 팝업이 아닌 메뉴를 표시합니다. 표시할 앱 기능이 메뉴에 비해 너무 복잡하지 않은 경우 팝업에 표시하지 마십시오.
>




**Let people — not your app — decide whether to enable your menu bar extra.** Typically, people add a menu bar extra to the menu bar by changing a setting in an app’s settings window. To ensure discoverability, however, consider giving people the option of enabling the menu bar extra during setup.
> 일반적으로 사용자는 앱의 설정 창에서 설정을 변경하여 메뉴 모음에 메뉴 모음을 추가로 추가합니다. 그러나 검색 가능성을 보장하려면 설치 중에 추가로 메뉴 모음을 사용할 수 있는 옵션을 사용자에게 제공하는 것을 고려하십시오.
>




**Avoid relying on the presence of menu bar extras.** The system hides and shows menu bar extras regularly, and you can’t be sure which other menu bar extras people have chosen to display or predict the location of your menu bar extra.
> 시스템은 메뉴 모음 추가 정보를 숨기고 정기적으로 표시하며, 다른 사용자가 메뉴 모음 추가 정보를 표시하거나 예측하기 위해 선택한 다른 메뉴 모음 추가 정보를 확인할 수 없습니다.
>




**Consider exposing app-specific functionality in other ways, too.** For example, you can provide a [Dock menu](../components/menus-and-actions/dock-menus) that appears when people Control-click your app’s Dock icon. People can hide or choose not to use your menu bar extra, but a Dock menu is aways available when your app is running.
> 예를 들어, 사용자가 앱의 도킹 아이콘을 클릭할 때 나타나는 도킹 메뉴를 제공할 수 있습니다. 메뉴 모음을 숨기거나 추가로 사용하지 않도록 선택할 수 있지만 앱이 실행 중일 때 도킹 메뉴를 사용할 수 있습니다.
>




# **Platform considerations**

*Not supported in iOS, iPadOS, tvOS, or watchOS.*
> iOS, iPadOS, tvOS 또는 watch에서 지원되지 않음운영 체제
>



